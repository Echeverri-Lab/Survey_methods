"""
OBSOLETE (2026-11-02): all records are now double-screened; see ../screening/assign_pairs.py.

flag_dual_sample.py
===================

Draws the 20% dual-screening sample (STREAM_B_PROTOCOL.md, "Screening and
curation") from Stream B records awaiting human title/abstract screening, with
a fixed seed, and marks them in `../screening_log.csv` by adding
"dual_screen_sample" to the notes column. Drawing the sample before screening
means the second screener checks a sample nobody chose after seeing decisions.

Idempotent: if any row is already flagged, it reports the existing sample and
changes nothing.

Usage:  python flag_dual_sample.py
"""
from __future__ import annotations

import csv
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
SEED, FRACTION, FLAG = 2026, 0.20, "dual_screen_sample"
csv.field_size_limit(10**8)


def main():
    with open(LOG, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols, rows = reader.fieldnames, list(reader)
    dec = next(c for c in cols if c.startswith("screen_ta_decision"))
    flagged = [r for r in rows if FLAG in r["notes"]]
    if flagged:
        print(f"Sample already drawn: {len(flagged)} rows flagged; nothing changed.")
        return
    pool = [r for r in rows if r["record_id"].startswith(("B1-", "B2-", "B3-", "B4-")) and not r[dec]]
    sample = random.Random(SEED).sample(pool, round(len(pool) * FRACTION))
    for r in sample:
        r["notes"] = "; ".join(x for x in (r["notes"], FLAG) if x)
    with open(LOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"Pool awaiting screening: {len(pool)}; flagged for dual screening: {len(sample)} (seed {SEED})")


if __name__ == "__main__":
    main()
