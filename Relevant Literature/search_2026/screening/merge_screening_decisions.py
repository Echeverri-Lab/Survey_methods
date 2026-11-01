"""
merge_screening_decisions.py
============================

Copies title/abstract decisions from a screening workbook back into the master
log `../screening_log.csv`.

- Rows with an empty DECISION are skipped (partial screening is fine).
- An "exclude" without a REASON is not merged and is listed, so it can be fixed.
- A row whose log entry already has a different decision is not overwritten;
  it is listed as a conflict.
- Screener notes are appended to the log's notes column.

Usage:  python merge_screening_decisions.py screening_workbook_AE.xlsx
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

from openpyxl import load_workbook

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
csv.field_size_limit(10**8)


def main(xlsx):
    initials = re.search(r"screening_workbook_(\w+)\.xlsx$", Path(xlsx).name)
    initials = initials.group(1) if initials else ""
    ws = load_workbook(xlsx, read_only=True)["Screen"]
    it = ws.iter_rows(values_only=True)
    head = [str(h) for h in next(it)]
    ix = {h: head.index(h) for h in ("record_id", "DECISION", "REASON (if exclude)", "screener notes")}
    decisions = {}
    missing_reason = []
    for row in it:
        rid, dec = row[ix["record_id"]], (row[ix["DECISION"]] or "").strip().lower()
        if not rid or not dec:
            continue
        why = (row[ix["REASON (if exclude)"]] or "").strip()
        if dec == "exclude" and not why:
            missing_reason.append(rid)
            continue
        decisions[rid] = (dec, why, (row[ix["screener notes"]] or "").strip())

    with open(LOG, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols, rows = reader.fieldnames, list(reader)
    dec_col = next(c for c in cols if c.startswith("screen_ta_decision"))
    merged, conflicts = 0, []
    for r in rows:
        d = decisions.get(r["record_id"])
        if not d:
            continue
        if r[dec_col] and r[dec_col] != d[0]:
            conflicts.append(f"{r['record_id']}: log={r[dec_col]} workbook={d[0]}")
            continue
        if r[dec_col] == d[0]:
            continue
        r[dec_col], r["screen_ta_reason"], r["screener_initials"] = d[0], d[1], initials
        if d[2]:
            r["notes"] = "; ".join(x for x in (r["notes"], d[2]) if x)
        merged += 1
    with open(LOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"Merged {merged} decisions into {LOG.name}.")
    if missing_reason:
        print(f"Not merged, exclude without a reason ({len(missing_reason)}): {', '.join(missing_reason[:20])}")
    if conflicts:
        print(f"Conflicts left unchanged ({len(conflicts)}):", *conflicts[:20], sep="\n  ")


if __name__ == "__main__":
    main(sys.argv[1])
