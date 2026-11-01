"""
prescreen_b3.py
===============

Applies the automated B3 pre-screen fixed on 2026-11-01, before any human
screening (STREAM_B_PROTOCOL.md amendment log; option B in b3_report.md):

  1. Any B3 record whose OpenAlex document type cannot be screened as a source
     of guidance (errata, retractions, editorials, book reviews, peer-review
     reports, letters, conference abstracts, reference entries, paratext,
     "other") is excluded.
  2. A record reached ONLY as a forward citation of Boateng et al. 2018 is kept
     for screening if its type is review, book, or book chapter, or its title
     contains a guidance term (GUIDANCE_RE); otherwise it is excluded.

Writes the decision into `../screening_log.csv` (screen_ta_decision /
screen_ta_reason, prefixed "auto:"), touching only B3 rows with no decision
yet, so human decisions are never overwritten.

Usage:  python prescreen_b3.py
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
csv.field_size_limit(10**8)

NON_SCREENABLE = {"erratum", "retraction", "paratext", "peer-review", "book-review", "editorial", "letter",
                  "conference-abstract", "reference-entry", "other"}
KEEP_TYPES = {"review", "book", "book-chapter"}
GUIDANCE_RE = re.compile(r"guideline|guidance|best practi|primer|tutorial|recommendation|checklist|framework"
                         r"|review|how to|step-by-step|standard", re.I)
BOATENG_ONLY = "forward:boateng2018"


def main():
    types = {r["openalex_id"]: r["type"] for r in csv.DictReader(open(HERE / "b3_records.csv", encoding="utf-8"))}
    with open(LOG, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols, rows = reader.fieldnames, list(reader)
    dec = next(c for c in cols if c.startswith("screen_ta_decision"))
    why = "screen_ta_reason"
    tally = Counter()
    for r in rows:
        if not r["record_id"].startswith("B3-") or r[dec]:
            continue
        t = types.get(r["openalex_id"], "")
        if t in NON_SCREENABLE:
            r[dec], r[why] = "exclude", f"auto: document type not screenable ({t})"
            tally["excluded: non-screenable type"] += 1
        elif r["reached_by"] == BOATENG_ONLY and t not in KEEP_TYPES and not GUIDANCE_RE.search(r["title"]):
            r[dec], r[why] = "exclude", "auto: reached only via Boateng 2018 forward citation; failed guidance rule"
            tally["excluded: Boateng-only, failed guidance rule"] += 1
        else:
            tally["to screen"] += 1
    with open(LOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    for k, v in tally.items():
        print(f"{k}: {v}")
    left = [r for r in rows if r["record_id"].startswith("B3-") and not r[dec]]
    sys.path.insert(0, str(HERE.parent))
    from local_abstracts import lookup
    abstracts = lookup("screening_log.csv", "record_id")
    print("to screen, already in Stream A or legacy list:", sum(bool(r["duplicate_of"]) for r in left),
          "| no abstract:", sum(not abstracts.get(r["record_id"]) for r in left) if abstracts else "n/a (no local abstracts)")


if __name__ == "__main__":
    main()
