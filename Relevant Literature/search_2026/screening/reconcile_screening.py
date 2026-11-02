"""
reconcile_screening.py
======================

Combines the two independent title/abstract decisions per record.

- "include" and "unsure" both send a record to full text, so the two screeners
  agree when both pass it (include/unsure) or both exclude it.
- Agreements are written to ../screening_log.csv: decision ("include" if either said
  include, else "unsure"; or "exclude"), reason (first screener's; both kept in notes
  if they differ), and screener_initials ("A+B").
- Disagreements go to `conflicts.csv`. The pair discusses each one and fills
  `resolved_decision` (include/unsure/exclude) and, for exclude, `resolved_reason`;
  the next run applies them.
- An existing different decision in the log is never overwritten; it is listed.
- Prints percent agreement and Cohen's kappa for each pair (pass vs exclude).

Usage:  python reconcile_screening.py
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
csv.field_size_limit(10**8)
PASS = {"include", "unsure"}


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def main():
    assign = {r["record_id"]: r for r in csv.DictReader(open(HERE / "assignments.csv", encoding="utf-8"))}
    decs = defaultdict(dict)
    for d in csv.DictReader(open(HERE / "ta_decisions.csv", encoding="utf-8")):
        decs[d["record_id"]][d["screener"]] = d
    cpath = HERE / "conflicts.csv"
    resolved = {r["record_id"]: r for r in csv.DictReader(open(cpath, encoding="utf-8"))} if cpath.exists() else {}

    final, conflicts, pair_data = {}, [], defaultdict(lambda: ([], []))
    for rid, a in assign.items():
        sa, sb = a["screener_a"], a["screener_b"]
        da, db = decs[rid].get(sa), decs[rid].get(sb)
        if not (da and db):
            continue
        pa, pb = da["decision"] in PASS, db["decision"] in PASS
        pair_data[f"{sa}+{sb}"][0].append(pa)
        pair_data[f"{sa}+{sb}"][1].append(pb)
        if pa == pb:
            dec = ("include" if "include" in (da["decision"], db["decision"]) else "unsure") if pa else "exclude"
            reason = "" if pa else da["reason"]
            note = "" if pa or da["reason"] == db["reason"] else f"TA reasons: {sa}={da['reason']}; {sb}={db['reason']}"
            final[rid] = (dec, reason, f"{sa}+{sb}", note)
            continue
        r = resolved.get(rid, {})
        if r.get("resolved_decision") in ("include", "unsure", "exclude") and (r["resolved_decision"] != "exclude" or r.get("resolved_reason")):
            final[rid] = (r["resolved_decision"], r.get("resolved_reason", ""), f"{sa}+{sb}", "resolved after discussion")
        else:
            conflicts.append({"record_id": rid, "pair": f"{sa}+{sb}",
                              f"decision_A": f"{sa}: {da['decision']} {da['reason']}".strip(),
                              f"decision_B": f"{sb}: {db['decision']} {db['reason']}".strip(),
                              "resolved_decision": r.get("resolved_decision", ""), "resolved_reason": r.get("resolved_reason", "")})

    with open(LOG, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        cols, rows = reader.fieldnames, list(reader)
    ta = next(c for c in cols if c.startswith("screen_ta_decision"))
    written, clashes = 0, []
    for r in rows:
        if r["record_id"] not in final:
            continue
        dec, reason, who, note = final[r["record_id"]]
        if r[ta] and r[ta] != dec:
            clashes.append(f"{r['record_id']}: log={r[ta]} reconciled={dec}")
            continue
        if r[ta] == dec:
            continue
        r[ta], r["screen_ta_reason"], r["screener_initials"] = dec, reason, who
        if note:
            r["notes"] = "; ".join(x for x in (r["notes"], note) if x)
        written += 1
    with open(LOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    with open(cpath, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["record_id", "pair", "decision_A", "decision_B", "resolved_decision", "resolved_reason"])
        w.writeheader()
        w.writerows(conflicts)

    both = sum(1 for rid, a in assign.items() if a["screener_a"] in decs[rid] and a["screener_b"] in decs[rid])
    print(f"Assigned: {len(assign)} | decided by both: {both} | written to log this run: {written} | open conflicts: {len(conflicts)}")
    print(f"{'pair':10} {'n':>5} {'agree':>7} {'kappa':>7}")
    for pair, (a, b) in sorted(pair_data.items()):
        print(f"{pair:10} {len(a):5} {sum(x == y for x, y in zip(a, b)) / len(a):7.0%} {kappa(a, b):7.2f}")
    if clashes:
        print("Log already had a different decision (left unchanged):", *clashes, sep="\n  ")


if __name__ == "__main__":
    main()
