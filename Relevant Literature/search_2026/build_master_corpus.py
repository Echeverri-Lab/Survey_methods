"""
build_master_corpus.py
=======================

Reproducible pipeline for CSP2-26-0397 revision, Step 2-3-5-6 of the work plan:

1. Load the 1,580-record corpus (`survey_corpus_v3_retained.csv`).
2. Draw a reproducible 25% random subsample (n=395, seed=42).
3. Load the papers already cited in the repository (from the two RIS exports
   in `Relevant Literature/`), and merge them with the 395-paper subsample
   into a single master database, de-duplicated by DOI (falling back to
   normalised title when DOI is missing).
4. Classify every record in the master database against the 12 Step folders
   using the same keyword logic as the S1-S11 topic searches documented in
   `search_strings.md`, so additions can be routed to the right Step.
5. Write outputs used to update Fig2_PRISMA_flow_data.md and to drive the
   step-by-step curation pass (Step 4 of the work plan).

Outputs (all under Relevant Literature/search_2026/exports/):
    master_corpus_395_plus_repo.csv   - full master database
    step_classification.csv           - one row per record x candidate step
    summary_counts.md                 - counts to paste into Fig2 data file
"""
from __future__ import annotations

import csv
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIT_ROOT = HERE.parent  # .../Relevant Literature
CORPUS_CSV = HERE / "exports" / "survey_corpus_v3_retained.csv"
RIS_FILES = [
    LIT_ROOT / "Survey methods paper.ris",
    LIT_ROOT / "Exported Items" / "Exported Items.ris",
]
OUT_DIR = HERE / "exports"
SEED = 42
SAMPLE_FRACTION = 0.25

STEP_KEYWORDS = {
    "Step_01_Epistemological_Alignment_and_Method_Selection": [
        "semi-structured interview", "ethnograph", "focus group",
        "qualitative method", "epistemolog", "mixed method", "mixed-method",
        "community-based participatory",
    ],
    "Step_02_Theory_Grounding_and_Construct_Conceptualization": [
        "value-belief-norm", "theory of planned behavior", "theory of planned behaviour",
        "new ecological paradigm", "nature relatedness", "cultural ecosystem service",
        "protection motivation theory", "norm activation",
    ],
    "Step_03_Psychometric_Scales_and_Construct_Validity": [
        "wildlife attitude", "attitudes toward wildlife", "nature connectedness",
        "environmental identity", "wildlife value orientation", "validat",
        "psychometric", "reliability", "measurement invariance", "scale development",
        "confirmatory factor analysis", "factorial validity",
    ],
    "Step_04_Study_Architecture_and_Experimental_Design": [
        "power analysis", "sample size", "pilot stud", "cognitive pretesting",
        "randomi", "study design", "experimental design", "choice experiment",
    ],
    "Step_05_Preregistration_and_Open_Science": [
        "preregist", "pre-registration", "open science", "registered report",
        "reproducib",
    ],
    "Step_06_Instrument_Construction": [
        "questionnaire design", "question wording", "survey instrument",
        "question types", "item development",
    ],
    "Step_07_Measuring_Behavior_Beyond_Self_Report": [
        "attitude-behavior gap", "attitude-behaviour gap", "revealed preference",
        "incentive compatible", "implicit association", "self-report", "actual behavior",
        "camera trap",
    ],
    "Step_08_Ethics_and_Participant_Compensation": [
        "institutional review board", "research ethics", "informed consent",
        "care principles", "indigenous data sovereignty", "decoloni", "irb",
        "covert research", "ethics board",
    ],
    "Step_09_Power_Analysis_Sampling_and_Pilots": [
        "power analysis", "sample size", "pilot stud",
    ],
    "Step_10_Survey_Distribution": [
        "mixed-mode", "response rate", "online panel", "prolific",
        "mechanical turk", "tailored design", "mode of data collection",
        "text-to-web",
    ],
    "Step_11_Data_Preparation_Analysis_and_Reporting": [
        "large language model", "natural language processing", " llm ",
        "machine learning", "qualitative analysis", "thematic analysis",
        "content analysis", "structural equation model", "confirmatory factor analysis",
        "ordinal regression", "data quality", "data cleaning",
    ],
    "Step_12_Writing_Survey_Research_Paper": [
        "cherries", "coreq", "srqr", "jars", "reporting standard",
        "reporting guideline", "prisma",
    ],
}


def normalise_title(title: str) -> str:
    t = title.lower()
    t = re.sub(r"[^a-z0-9 ]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def load_corpus(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_ris_records(path: Path) -> list[dict]:
    """Very small RIS parser: returns list of dicts with title/doi keys."""
    if not path.exists():
        return []
    records = []
    current: dict[str, str] = {}
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("TY  -"):
                current = {}
            elif line.startswith("ER  -"):
                if current:
                    records.append(current)
                current = {}
            elif "  - " in line[:8]:
                tag = line[:2]
                value = line.split("  - ", 1)[1].strip() if "  - " in line else ""
                if tag in ("TI", "T1"):
                    current["title"] = value
                elif tag == "DO":
                    current["doi"] = value
                elif tag in ("PY", "Y1"):
                    current["year"] = value[:4]
    return records


def main():
    random.seed(SEED)
    corpus = load_corpus(CORPUS_CSV)
    assert len(corpus) == 1580, f"Expected 1580 records, found {len(corpus)}"

    n_sample = round(len(corpus) * SAMPLE_FRACTION)
    indices = list(range(len(corpus)))
    random.shuffle(indices)
    sample_idx = sorted(indices[:n_sample])
    sample = [corpus[i] for i in sample_idx]

    # Load already-cited repo records
    repo_records = []
    for ris in RIS_FILES:
        repo_records.extend(load_ris_records(ris))

    # De-duplicate master set by DOI (fallback: normalised title)
    seen_doi = set()
    seen_title = set()
    master = []
    source_flags = []

    def add_record(rec, source):
        doi = (rec.get("doi") or "").strip().lower()
        title_norm = normalise_title(rec.get("title", ""))
        key_doi = doi if doi else None
        if key_doi and key_doi in seen_doi:
            return False
        if title_norm and title_norm in seen_title:
            return False
        if key_doi:
            seen_doi.add(key_doi)
        if title_norm:
            seen_title.add(title_norm)
        rec = dict(rec)
        rec["source"] = source
        master.append(rec)
        return True

    for rec in sample:
        add_record(rec, "random_sample_395")

    n_repo_new = 0
    n_repo_overlap = 0
    for rec in repo_records:
        rec.setdefault("abstract", "")
        rec.setdefault("journal", "")
        rec.setdefault("authors", "")
        added = add_record(rec, "repo_already_cited")
        if added:
            n_repo_new += 1
        else:
            n_repo_overlap += 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    master_path = OUT_DIR / "master_corpus_395_plus_repo.csv"
    fieldnames = ["title", "year", "authors", "journal", "doi", "wos_accession", "abstract", "source"]
    with open(master_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for rec in master:
            w.writerow(rec)

    # Step classification (keyword match on title+abstract), sample-only records
    class_path = OUT_DIR / "step_classification.csv"
    with open(class_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["title", "year", "doi", "matched_steps"])
        for rec in sample:
            text = (rec.get("title", "") + " " + rec.get("abstract", "")).lower()
            matched = [
                step for step, kws in STEP_KEYWORDS.items()
                if any(kw in text for kw in kws)
            ]
            w.writerow([rec.get("title"), rec.get("year"), rec.get("doi"), "; ".join(matched)])

    unmatched = sum(
        1 for rec in sample
        if not any(
            any(kw in (rec.get("title", "") + " " + rec.get("abstract", "")).lower() for kw in kws)
            for kws in STEP_KEYWORDS.values()
        )
    )

    summary_path = OUT_DIR / "summary_counts.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("# Master corpus build — summary counts\n\n")
        f.write(f"- Full corpus (`survey_corpus_v3_retained.csv`): **{len(corpus)}**\n")
        f.write(f"- Random subsample drawn (seed={SEED}, fraction={SAMPLE_FRACTION}): **{len(sample)}**\n")
        f.write(f"- Records parsed from repo RIS exports (already cited): **{len(repo_records)}**\n")
        f.write(f"  - Overlapping with the 395 random subsample (already in pool): **{n_repo_overlap}**\n")
        f.write(f"  - Net new repo-only records added to master: **{n_repo_new}**\n")
        f.write(f"- **Master database size (395 + repo, de-duplicated): {len(master)}**\n\n")
        f.write(f"- Of the 395, records with >=1 keyword match to a Step: **{len(sample) - unmatched}**\n")
        f.write(f"- Of the 395, records with no Step keyword match (general/background only): **{unmatched}**\n")

    print(f"Master database: {len(master)} records -> {master_path}")
    print(f"Summary written -> {summary_path}")


if __name__ == "__main__":
    main()
