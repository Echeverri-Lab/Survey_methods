# screening — title/abstract screening workbooks

> **Abstracts are not committed** (publisher copyright). Committed CSVs carry DOIs and OpenAlex IDs; full copies with abstracts are kept locally in `local_abstracts/` (gitignored; see `local_abstracts.py`).

`../screening_log.csv` is the master record. Workbooks are just a convenient place to type decisions.

**Double screening (from 2026-11-02):** every record is screened independently by two people. Screeners: AE, KEL, AB, CAN. Records are split into six blocks, one per pair (`assignments.csv`, seed 2026), so each person screens about 1,876 records and agreement can be reported for every pair.

| File | What it is |
|---|---|
| `assign_pairs.py` | Assigns records awaiting screening to pairs → `assignments.csv`. `--add` assigns new records later (e.g., the Web of Science batch) |
| `make_screening_workbook.py` | Builds a person's workbook: their assigned, not-yet-decided records |
| `screening_workbook_<INITIALS>.xlsx` | Personal workbooks (not committed) |
| `merge_screening_decisions.py` | Collects one person's decisions into `ta_decisions.csv` (one row per record and screener) |
| `reconcile_screening.py` | Compares the two decisions per record: agreements → `../screening_log.csv`; disagreements → `conflicts.csv`; prints agreement and Cohen's kappa per pair |
| `conflicts.csv` | Disagreements for each pair to discuss; fill `resolved_decision` (and `resolved_reason` for exclude), then re-run reconcile |

## Workflow
1. Each person screens their workbook **independently** (no discussing records with your pair partner until both have finished the block).
2. Save, then merge (any time, as often as you like):

   ```bash
   python merge_screening_decisions.py screening_workbook_AE.xlsx
   ```
3. Reconcile (after merges):

   ```bash
   python reconcile_screening.py
   ```
4. Each pair resolves its rows in `conflicts.csv` together, then reconcile is run again.
5. For a fresh workbook with only your undecided records: merge first, move the old workbook aside, then `python make_screening_workbook.py AE`.

"include" and "unsure" both send a record to full text; screeners agree when both pass a record or both exclude it.
