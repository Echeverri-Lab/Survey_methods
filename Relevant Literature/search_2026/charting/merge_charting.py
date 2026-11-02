"""
merge_charting.py
=================

Copies full-text decisions and charted data from a charting workbook into the records.

    python merge_charting.py charting_workbook_AE.xlsx          # writes ../screening_log.csv + charting_log.csv
    python merge_charting.py charting_PILOT_AE.xlsx --pilot     # writes charting_log_pilot.csv only

- screening log: fulltext_decision, fulltext_exclusion_reason, curation_C1-C3,
  curation_decision (retain if >=1 of C1-C3 and no superseded_by; set_aside otherwise),
  mapped_step. An existing different decision is never overwritten; it is listed.
- charting log: one row per (record_id, charter), replaced if charted again by the same person.
- Rows that fail a check are not merged and are listed (exclude without reason; include
  without a stage, criterion, evidence basis, or key_guidance).
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from pathlib import Path

from openpyxl import load_workbook

sys.path.insert(0, str(Path(__file__).resolve().parent))
from charting_fields import CRITERIA, CURATION, FT_REASONS, SINGLE, STAGES  # noqa: E402

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
csv.field_size_limit(10**8)
CHART_COLS = (["record_id", "charter", "date", "ft_decision", "ft_exclusion_reason", "retrieval_notes",
               "stages", "criteria"] + [n for n, *_ in SINGLE] + ["curation", "curation_decision", "charter_notes"])


def read_workbook(path):
    ws = load_workbook(path, read_only=True)["Chart"]
    it = ws.iter_rows(values_only=True)
    head = [str(h) for h in next(it)]
    for row in it:
        r = {h: ("" if v is None else str(v).strip()) for h, v in zip(head, row)}
        if r.get("record_id") and r.get("FT_DECISION"):
            yield r


def check(r):
    dec = r["FT_DECISION"].lower()
    if dec not in ("include", "exclude"):
        return f"FT_DECISION '{r['FT_DECISION']}'"
    if dec == "exclude":
        return "" if r["FT_EXCLUSION_REASON"] in FT_REASONS else "exclude without a valid reason"
    missing = [n for n, ok in (("a stage", any(r[s] for s in STAGES)), ("a criterion", any(r[c] for c in CRITERIA)),
                               ("evidence_basis", r["evidence_basis"]), ("key_guidance", r["key_guidance"])) if not ok]
    return ("include missing " + ", ".join(missing)) if missing else ""


def to_chart_row(r, charter):
    dec = r["FT_DECISION"].lower()
    cur = [c for c in CURATION if r[c]]
    decision = "" if dec != "include" else ("set_aside" if r["superseded_by"] or not cur else "retain")
    out = {"record_id": r["record_id"], "charter": charter, "date": dt.date.today().isoformat(),
           "ft_decision": dec, "ft_exclusion_reason": r["FT_EXCLUSION_REASON"], "retrieval_notes": r["retrieval_notes"],
           "stages": ";".join(s for s in STAGES if r[s]), "criteria": ";".join(c for c in CRITERIA if r[c]),
           "curation": ";".join(cur), "curation_decision": decision, "charter_notes": r["charter_notes"]}
    out.update({n: r[n] for n, *_ in SINGLE})
    return out


def upsert(path, new_rows):
    rows = list(csv.DictReader(open(path, encoding="utf-8"))) if path.exists() else []
    keys = {(r["record_id"], r["charter"]) for r in new_rows}
    rows = [r for r in rows if (r["record_id"], r["charter"]) not in keys] + new_rows
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CHART_COLS)
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["record_id"], r["charter"])))


def main(xlsx, pilot=False):
    m = re.search(r"charting_(?:PILOT_|workbook_)(\w+)\.xlsx$", Path(xlsx).name)
    charter = m.group(1) if m else ""
    good, problems = [], []
    for r in read_workbook(xlsx):
        p = check(r)
        (problems.append(f"{r['record_id']}: {p}") if p else good.append(to_chart_row(r, charter)))
    upsert(HERE / ("charting_log_pilot.csv" if pilot else "charting_log.csv"), good)
    print(f"Charting log: {len(good)} row(s) written.")
    if not pilot:
        with open(LOG, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            cols, rows = reader.fieldnames, list(reader)
        col = {k: next(c for c in cols if c.startswith(k)) for k in
               ("fulltext_decision", "fulltext_exclusion_reason", "curation_C1", "curation_C2", "curation_C3",
                "curation_decision") if any(c.startswith(k) for c in cols)}
        step_col = next((c for c in cols if c.startswith("mapped_step")), None)
        by_id = {g["record_id"]: g for g in good}
        conflicts, merged = [], 0
        for r in rows:
            g = by_id.get(r["record_id"])
            if not g:
                continue
            if r[col["fulltext_decision"]] and r[col["fulltext_decision"]] != g["ft_decision"]:
                conflicts.append(f"{r['record_id']}: log={r[col['fulltext_decision']]} workbook={g['ft_decision']}")
                continue
            r[col["fulltext_decision"]] = g["ft_decision"]
            r[col["fulltext_exclusion_reason"]] = g["ft_exclusion_reason"]
            for c in CURATION:
                r[col[f"curation_{c}"]] = "TRUE" if c in g["curation"].split(";") else ""
            r[col["curation_decision"]] = g["curation_decision"]
            if step_col:
                r[step_col] = ";".join(s[1:] for s in g["stages"].split(";") if s)
            merged += 1
        with open(LOG, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
        print(f"Screening log: {merged} record(s) updated.")
        if conflicts:
            print("Conflicts left unchanged:", *conflicts, sep="\n  ")
    if problems:
        print("Not merged (fix in the workbook and re-run):", *problems, sep="\n  ")


if __name__ == "__main__":
    main(sys.argv[1], "--pilot" in sys.argv[2:])
