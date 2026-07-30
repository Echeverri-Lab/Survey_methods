"""
Recomputes the manuscript-citation / synthesis-corpus overlap count used in
Figure 2 (make_prisma_fig2.py), replacing the stale "12 of 73" figure that was
computed against an earlier 418-record corpus (back when Stream B held only
23 records).

Method:
  1. Reproduce Stream A's 395-record subsample from survey_corpus_v3_retained.csv
     using the same seed (42) and method as build_master_corpus.py.
  2. Parse Stream B's 242-record list from master_reference_list_all_steps.md.
  3. Match the manuscript's reference list (manuscript_refs.py) against the
     union, by normalized first-author-surname + year, falling back to a
     normalized-title substring match.

Run: python citation_overlap_check.py
"""

import csv
import random
import re
import unicodedata
from pathlib import Path

from manuscript_refs import MANUSCRIPT_REFS

HERE = Path(__file__).parent
CORPUS_CSV = HERE / "exports" / "survey_corpus_v3_retained.csv"
MASTER_REF_MD = HERE / "exports" / "master_reference_list_all_steps.md"

SEED = 42
SAMPLE_FRACTION = 0.25


def strip_diacritics(s):
    return "".join(
        c for c in unicodedata.normalize("NFKD", s)
        if not unicodedata.combining(c)
    )


def norm_title(t):
    t = strip_diacritics(t).lower()
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def norm_author(a):
    a = strip_diacritics(a).lower()
    a = re.sub(r"\bet al\.?\b", "", a)
    a = re.sub(r"[^a-z ]", "", a)
    return a.strip()


def main():
    with open(CORPUS_CSV, newline="", encoding="utf-8") as f:
        corpus = list(csv.DictReader(f))
    assert len(corpus) == 1580, len(corpus)

    random.seed(SEED)
    n_sample = round(len(corpus) * SAMPLE_FRACTION)
    indices = list(range(len(corpus)))
    random.shuffle(indices)
    sample_idx = sorted(indices[:n_sample])
    stream_a_sample = [corpus[i] for i in sample_idx]
    assert len(stream_a_sample) == 395, len(stream_a_sample)

    stream_b_records = []
    with open(MASTER_REF_MD, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("| "):
                continue
            parts = [p.strip() for p in line.strip().strip("|").split("|")]
            if len(parts) < 4:
                continue
            idx_str, ref_text = parts[0], parts[1]
            if not idx_str.isdigit():
                continue
            stream_b_records.append(ref_text)
    assert len(stream_b_records) == 242, len(stream_b_records)

    corpus_titles = set()
    corpus_author_years = set()

    for rec in stream_a_sample:
        title = norm_title(rec.get("title", ""))
        if title:
            corpus_titles.add(title)
        authors = rec.get("authors", "")
        year = rec.get("year", "")
        first_author = authors.split(";")[0].split(",")[0].strip() if authors else ""
        if first_author and year:
            corpus_author_years.add((norm_author(first_author), year.strip()))

    year_re = re.compile(r"\((\d{4})\)")
    for ref_text in stream_b_records:
        m = year_re.search(ref_text)
        year = m.group(1) if m else ""
        author_part = ref_text.split("(")[0]
        author_part = re.split(r"[,&]| and ", author_part)[0]
        first_author = author_part.strip().rstrip(".")
        if first_author and year:
            corpus_author_years.add((norm_author(first_author), year))
        title_match = re.search(r'"([^"]+)"', ref_text)
        if title_match:
            corpus_titles.add(norm_title(title_match.group(1)))

    matched, unmatched = [], []
    for author, year, title in MANUSCRIPT_REFS:
        key_ay = (norm_author(author), str(year))
        title_n = norm_title(title)
        hit_ay = key_ay in corpus_author_years
        hit_title = any(
            title_n[:40] in ct or ct[:40] in title_n
            for ct in corpus_titles if len(ct) > 10
        )
        if hit_ay or hit_title:
            matched.append((author, year, title, "author+year" if hit_ay else "title"))
        else:
            unmatched.append((author, year, title))

    print(f"Stream A subsample: {len(stream_a_sample)} records")
    print(f"Stream B records: {len(stream_b_records)} records")
    print(f"Manuscript refs: {len(MANUSCRIPT_REFS)}")
    print(f"\nMatched ({len(matched)}):")
    for a, y, t, how in matched:
        print(f"  [{how:12s}] {a} ({y}) - {t[:70]}")
    print(f"\nUnmatched ({len(unmatched)}):")
    for a, y, t in unmatched:
        print(f"  {a} ({y}) - {t[:70]}")
    print(f"\n=== RESULT: {len(matched)} of {len(MANUSCRIPT_REFS)} manuscript "
          f"citations overlap with the 605-record synthesis corpus ===")


if __name__ == "__main__":
    main()
