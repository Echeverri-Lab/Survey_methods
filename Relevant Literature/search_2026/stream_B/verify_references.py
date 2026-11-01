"""
verify_references.py
====================

Checks every Stream B record (except placeholders and duplicates) against
Crossref, with OpenAlex as a fallback for records without a DOI.

For a record with a DOI: does the DOI resolve, and does the registered title
match the title in our citation?  For a record without a DOI: what is the best
bibliographic match, and how close is it?

Raw API responses are cached in `api_cache.json` so the check is reproducible
and the APIs are not re-queried on re-runs.

Usage:  python verify_references.py
Reads:  stream_b_log.csv, stream_b_manual_codes.csv
Writes: stream_b_verification.csv
"""
from __future__ import annotations

import csv
import difflib
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_stream_b import norm_title, title_guess  # noqa: E402

HERE = Path(__file__).resolve().parent
CACHE = HERE / "api_cache.json"
UA = {"User-Agent": "stream-b-reference-check/1.0"}


def get_json(url: str, cache: dict):
    if url in cache:
        return cache[url]
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            data = json.load(r)
    except Exception as e:  # 404 for unregistered DOIs, timeouts, etc.
        data = {"error": str(e)}
    cache[url] = data
    time.sleep(0.6)
    return data


def sim(a: str, b: str) -> float:
    a, b = norm_title(a), norm_title(b)
    if not a or not b:
        return 0.0
    # Our titles are sometimes truncated or carry a subtitle the registry lacks.
    if a in b or b in a:
        return 1.0
    return round(difflib.SequenceMatcher(None, a, b).ratio(), 2)


def crossref_doi(doi, cache):
    d = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi), cache)
    m = d.get("message") if isinstance(d, dict) else None
    if not m:
        return None
    return {"title": (m.get("title") or [""])[0], "doi": doi,
            "year": (m.get("issued", {}).get("date-parts") or [[""]])[0][0],
            "first_author": ((m.get("author") or [{}])[0]).get("family", ""),
            "source": "crossref-doi"}


def crossref_search(ref, cache):
    ref = re.sub(r"https?://\S+|[*_\[\]]", "", ref)
    q = urllib.parse.urlencode({"query.bibliographic": ref[:250], "rows": 1})
    d = get_json("https://api.crossref.org/works?" + q, cache)
    items = (d.get("message") or {}).get("items") if isinstance(d, dict) else None
    if not items:
        return None
    m = items[0]
    return {"title": (m.get("title") or [""])[0], "doi": m.get("DOI", ""),
            "year": (m.get("issued", {}).get("date-parts") or [[""]])[0][0],
            "first_author": ((m.get("author") or [{}])[0]).get("family", ""),
            "source": "crossref-search"}


def openalex_search(title, cache):
    if not title:
        return None
    q = urllib.parse.urlencode({"search": title[:200], "per-page": 1})
    d = get_json("https://api.openalex.org/works?" + q, cache)
    res = d.get("results") if isinstance(d, dict) else None
    if not res:
        return None
    m = res[0]
    auth = (m.get("authorships") or [{}])[0].get("author", {}).get("display_name", "")
    return {"title": m.get("title") or "", "doi": (m.get("doi") or "").replace("https://doi.org/", ""),
            "year": m.get("publication_year", ""), "first_author": auth.split()[-1] if auth else "",
            "source": "openalex-search"}


def main():
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    codes = {r["record_id"]: r for r in csv.DictReader(open(HERE / "stream_b_manual_codes.csv"))}
    out = []
    for r in csv.DictReader(open(HERE / "stream_b_log.csv")):
        c = codes[r["record_id"]]
        row = {"record_id": r["record_id"], "flag": c["flag"], "our_title": title_guess(r["reference"]),
               "our_doi": r["doi"], "match_title": "", "match_doi": "", "match_year": "",
               "match_first_author": "", "match_source": "", "title_similarity": "", "author_agrees": "", "year_agrees": "", "verdict": ""}
        if c["flag"] in ("placeholder", "duplicate"):
            row["verdict"] = "not_checked_" + c["flag"]
            out.append(row)
            continue
        hit = crossref_doi(r["doi"], cache) if r["doi"] else None
        if r["doi"] and not hit:
            row["verdict"] = "doi_not_registered"
        if not hit:
            hit = crossref_search(r["reference"], cache)
            if hit and sim(row["our_title"], hit["title"]) < 0.85:
                alt = openalex_search(row["our_title"], cache)
                if alt and sim(row["our_title"], alt["title"]) > sim(row["our_title"], hit["title"]):
                    hit = alt
        if hit:
            s = sim(row["our_title"], hit["title"])
            row.update(match_title=hit["title"], match_doi=hit["doi"], match_year=hit["year"],
                       match_first_author=hit["first_author"], match_source=hit["source"], title_similarity=s)
            ref_plain = norm_title(r["reference"].split(")")[0])
            fa = norm_title(str(hit["first_author"]))
            row["author_agrees"] = (not fa) or fa.split()[-1] in ref_plain
            try:
                row["year_agrees"] = abs(int(hit["year"]) - int(r["year"][:4])) <= 1
            except ValueError:
                row["year_agrees"] = ""
            if not row["verdict"]:
                if hit["source"] == "crossref-doi":
                    row["verdict"] = "verified" if s >= 0.85 else "doi_title_mismatch"
                else:
                    row["verdict"] = "matched_no_doi_in_citation" if s >= 0.85 else "no_confident_match"
        elif not row["verdict"]:
            row["verdict"] = "no_confident_match"
        out.append(row)
        CACHE.write_text(json.dumps(cache))
    with open(HERE / "stream_b_verification.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    from collections import Counter
    print(Counter(o["verdict"] for o in out))


if __name__ == "__main__":
    main()
