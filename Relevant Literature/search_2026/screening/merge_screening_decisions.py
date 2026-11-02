"""
merge_screening_decisions.py
============================

Collects title/abstract decisions from one screener's workbook into
`ta_decisions.csv` (one row per record and screener). The screening log is
updated only by reconcile_screening.py, once both assigned screeners have decided.

- Rows with an empty DECISION are skipped (partial screening is fine).
- An "exclude" without a REASON is not collected; it is listed so it can be fixed.
- Re-merging the same workbook replaces that screener's earlier entries.

Usage:  python merge_screening_decisions.py screening_workbook_AE.xlsx
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from pathlib import Path

from openpyxl import load_workbook

HERE = Path(__file__).resolve().parent
OUT = HERE / "ta_decisions.csv"
COLS = ["record_id", "screener", "decision", "reason", "notes", "date"]


def main(xlsx):
    m = re.search(r"screening_workbook_(\w+)\.xlsx$", Path(xlsx).name)
    if not m:
        sys.exit("Workbook name must be screening_workbook_<INITIALS>.xlsx")
    screener = m.group(1)
    ws = load_workbook(xlsx, read_only=True)["Screen"]
    it = ws.iter_rows(values_only=True)
    head = [str(h) for h in next(it)]
    ix = {h: head.index(h) for h in ("record_id", "DECISION", "REASON (if exclude)", "screener notes")}
    new, missing_reason = [], []
    for row in it:
        rid, dec = row[ix["record_id"]], (row[ix["DECISION"]] or "").strip().lower()
        if not rid or not dec:
            continue
        why = (row[ix["REASON (if exclude)"]] or "").strip()
        if dec not in ("include", "exclude", "unsure"):
            missing_reason.append(f"{rid} (decision '{dec}')")
            continue
        if dec == "exclude" and not why:
            missing_reason.append(rid)
            continue
        new.append({"record_id": rid, "screener": screener, "decision": dec, "reason": why,
                    "notes": (row[ix["screener notes"]] or "").strip(), "date": dt.date.today().isoformat()})
    old = list(csv.DictReader(open(OUT, encoding="utf-8"))) if OUT.exists() else []
    keys = {(r["record_id"], r["screener"]) for r in new}
    rows = [r for r in old if (r["record_id"], r["screener"]) not in keys] + new
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["record_id"], r["screener"])))
    print(f"{screener}: {len(new)} decision(s) collected into {OUT.name}.")
    if missing_reason:
        print(f"Not collected ({len(missing_reason)}): " + ", ".join(missing_reason[:20]))


if __name__ == "__main__":
    main(sys.argv[1])
