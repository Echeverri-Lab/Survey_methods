"""
compare_charting.py
===================

Agreement between two charters on the sources both charted (pilot or dual sample).

    python compare_charting.py charting_log_pilot.csv AE XY

Reports, per field, the share of sources where both agree and Cohen's kappa
(for stages and criteria: per code, present/absent), then lists every
disagreement so the two can discuss and refine the definitions.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from charting_fields import CRITERIA, SINGLE, STAGES  # noqa: E402

CATEGORICAL = ["ft_decision", "ft_exclusion_reason"] + [n for n, vals, *_ in SINGLE if vals] + ["curation_decision"]


def kappa(a, b):
    n = len(a)
    if n == 0:
        return float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def main(path, x, y):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    a = {r["record_id"]: r for r in rows if r["charter"] == x}
    b = {r["record_id"]: r for r in rows if r["charter"] == y}
    ids = sorted(set(a) & set(b))
    print(f"Sources charted by both {x} and {y}: {len(ids)}\n")
    print(f"{'field':28} {'agree':>7} {'kappa':>7}")
    diffs = []
    for f in CATEGORICAL:
        va, vb = [a[i][f] for i in ids], [b[i][f] for i in ids]
        print(f"{f:28} {sum(p == q for p, q in zip(va, vb)) / max(len(ids), 1):7.0%} {kappa(va, vb):7.2f}")
        diffs += [(i, f, p, q) for i, p, q in zip(ids, va, vb) if p != q]
    for f, codes in (("stages", STAGES), ("criteria", CRITERIA)):
        for c in codes:
            va = [c in a[i][f].split(";") for i in ids]
            vb = [c in b[i][f].split(";") for i in ids]
            if any(va) or any(vb):
                print(f"{f + ' ' + c:28} {sum(p == q for p, q in zip(va, vb)) / max(len(ids), 1):7.0%} {kappa(va, vb):7.2f}")
        diffs += [(i, f, a[i][f], b[i][f]) for i in ids if a[i][f] != b[i][f]]
    print("\nDisagreements to discuss:")
    for d in diffs:
        print(f"  {d[0]}  {d[1]}: {x}='{d[2]}'  {y}='{d[3]}'")


if __name__ == "__main__":
    main(*sys.argv[1:4])
