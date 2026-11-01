"""
build_stream_b.py
=================

Rebuilds the Stream B (bottom-up / expert-knowledge) record log for ConBio 26-785.

Stream B was originally defined as "every unique reference cited across the
repository's Step folders" (master_reference_list_all_steps.md, n=242). This
script turns that list into a structured, auditable log and recomputes its
overlap with the Stream A database corpus, instead of relying on hand-typed
counts.

Usage:
    python build_stream_b.py <master_reference_list_all_steps.md> \
        <survey_corpus_v3_retained.csv> <master_corpus_395_plus_repo.csv> \
        <suggested_new_citations.md>

Outputs (next to this script):
    stream_b_log.csv        one row per Stream B record
    stream_b_summary.md     counts by document type and provenance
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
TEAM_SURNAMES = ("Echeverri", "Boren", "Niesner", "Langhans")
DOI_RE = re.compile(r"10\.\d{4,9}/(?:[^\s|()<>\]]|\([^\s()]*\))+", re.I)

csv.field_size_limit(10**8)


def norm_title(s: str) -> str:
    s = re.sub(r"[*_\"“”‘’'`]", "", s.lower())
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def clean_doi(s: str) -> str:
    return s.lower().rstrip(".,;").replace("https://doi.org/", "")


def parse_master(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|(.*)\|(.*)\|(.*)\|\s*$", line)
        if not m:
            continue
        num, ref, stream, files = (x.strip() for x in m.groups())
        dois = DOI_RE.findall(ref)
        year = re.search(r"\((\d{4}[a-z]?|n\.d\.)", ref)
        rows.append({
            "record_id": f"B{int(num):03d}",
            "reference": ref,
            "doi": clean_doi(dois[0]) if dois else "",
            "year": year.group(1) if year else "",
            "orig_stream_label": "A+B" if stream.startswith("A+B") else "B",
            "cited_in_files": files,
        })
    return rows


def title_guess(ref: str) -> str:
    """Best-effort title: quoted title, else text after '(year).' up to next period."""
    m = re.match(r'^"(.+?)"', ref)
    if m:
        return m.group(1)
    m = re.match(r"^([^(]{15,}?)\s*\(\d{4}\)", ref)
    if m and not re.search(r"\b[A-Z]\.|&|et al", m.group(1)):
        return m.group(1).strip("* ")  # title-first entries, e.g. "Against All Odds… (2025)"
    m = re.search(r"\(\d{4}[a-z]?\)\.?\s*\*?(.+?)(?:\.\s|\*|$)", ref)
    return m.group(1).strip("* ") if m else ""


def load_corpus(path: Path, source: str | None = None) -> tuple[set, set]:
    """DOIs and normalised titles; `source` keeps only rows with that value in the 'source' column."""
    dois, titles = set(), set()
    with path.open(encoding="utf-8", errors="replace") as f:
        for r in csv.DictReader(f):
            if source and r.get("source") != source:
                continue
            if r.get("doi"):
                dois.add(clean_doi(r["doi"]))
            if r.get("title"):
                titles.add(norm_title(r["title"]))
    return dois, titles


def match(row, dois, titles) -> bool:
    if row["doi"] and row["doi"] in dois:
        return True
    t = norm_title(title_guess(row["reference"]))
    return len(t) > 25 and t in titles


def main(master, full_corpus, sub_corpus, suggested):
    rows = parse_master(Path(master))
    full = load_corpus(Path(full_corpus))
    sub = load_corpus(Path(sub_corpus), source="random_sample_395")
    sugg_dois = {clean_doi(d) for d in DOI_RE.findall(Path(suggested).read_text(encoding="utf-8"))}

    for r in rows:
        ref = r["reference"]
        r["in_streamA_1580"] = match(r, *full)
        r["in_streamA_395"] = match(r, *sub)
        r["in_suggested_from_streamA"] = bool(r["doi"]) and r["doi"] in sugg_dois
        authors = ref.split("(")[0]
        r["team_authored"] = any(s in authors for s in TEAM_SURNAMES)
        r["incomplete_citation"] = (len(ref) < 45 or not re.search(r"\.\s", ref.split(")", 1)[-1]))
        files = [f.strip() for f in r["cited_in_files"].split(";") if f.strip()]
        r["cited_files_missing"] = ";".join(f for f in files if not (REPO / f.lstrip("/")).exists())

    fields = list(rows[0].keys()) + ["doc_type", "provenance", "notes"]
    out = HERE / "stream_b_log.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({**r, "doc_type": "", "provenance": "", "notes": ""})
    c = Counter
    print("records", len(rows))
    print("orig label", c(r["orig_stream_label"] for r in rows))
    print("in 395", sum(r["in_streamA_395"] for r in rows), "in 1580", sum(r["in_streamA_1580"] for r in rows))
    print("in suggested list", sum(r["in_suggested_from_streamA"] for r in rows))
    print("team", sum(r["team_authored"] for r in rows), "incomplete", sum(r["incomplete_citation"] for r in rows))
    print("missing cited files", sum(bool(r["cited_files_missing"]) for r in rows))


if __name__ == "__main__":
    main(*sys.argv[1:5])
