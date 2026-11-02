"""
assign_pairs.py
===============

Assigns every record awaiting title/abstract screening to two screeners.

Records are shuffled with a fixed seed and split into one block per pair of
screeners (all pairs: 4 screeners -> 6 blocks), so every record has two
independent screeners, workloads are equal, and agreement can be reported for
every pair. Writes `assignments.csv` (record_id, block, screener_a, screener_b).

    python assign_pairs.py AE KEL AB CAN          # first assignment
    python assign_pairs.py AE KEL AB CAN --add    # later: assign new, unassigned records
                                                  # (e.g., the Web of Science batch), continuing the pair rotation
"""
from __future__ import annotations

import csv
import itertools
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
OUT = HERE / "assignments.csv"
SEED = 2026
csv.field_size_limit(10**8)


def main(screeners: list[str], add: bool):
    if OUT.exists() and not add:
        sys.exit("assignments.csv exists; use --add to assign only new records.")
    with open(LOG, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        ta = next(c for c in reader.fieldnames if c.startswith("screen_ta_decision"))
        pending = [r["record_id"] for r in reader if not r[ta]]
    done = [r for r in csv.DictReader(open(OUT, encoding="utf-8"))] if OUT.exists() else []
    assigned = {r["record_id"] for r in done}
    new = [rid for rid in pending if rid not in assigned]
    random.Random(f"{SEED}-{len(done)}").shuffle(new)
    pairs = list(itertools.combinations(screeners, 2))
    start = len(done)
    rows = done + [{"record_id": rid, "block": f"P{(start + k) % len(pairs) + 1}",
                    "screener_a": pairs[(start + k) % len(pairs)][0], "screener_b": pairs[(start + k) % len(pairs)][1]}
                   for k, rid in enumerate(new)]
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["record_id", "block", "screener_a", "screener_b"])
        w.writeheader()
        w.writerows(rows)
    per = {s: sum(s in (r["screener_a"], r["screener_b"]) for r in rows) for s in screeners}
    print(f"Assigned {len(new)} new record(s); total {len(rows)}. Records per screener: {per}")
    for b in sorted({r['block'] for r in rows}, key=lambda x: int(x[1:])):
        rb = [r for r in rows if r["block"] == b]
        print(f"  {b}: {rb[0]['screener_a']}+{rb[0]['screener_b']} — {len(rb)} records")


if __name__ == "__main__":
    args = sys.argv[1:]
    main([a for a in args if not a.startswith("--")], "--add" in args)
