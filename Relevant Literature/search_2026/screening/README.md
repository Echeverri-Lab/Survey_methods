# screening — title/abstract screening workbooks

> **Abstracts are not committed** (publisher copyright). Committed CSVs carry DOIs and OpenAlex IDs; full copies with abstracts are kept locally in `local_abstracts/` (gitignored; see `local_abstracts.py`).

`../screening_log.csv` is the master record. Workbooks are just a convenient place to type decisions.

| File | What it is |
|---|---|
| `screening_workbook_AE.xlsx` | Records awaiting a title/abstract decision, with dropdowns. Sheets: Guide, Progress, Screen |
| `make_screening_workbook.py` | Builds a workbook for one screener from the undecided rows in the log |
| `merge_screening_decisions.py` | Copies decisions from a workbook back into the log |

## Workflow

1. Screen in the workbook: fill the yellow columns only, and save.
2. Merge, as often as you like (partial screening is fine):

   ```bash
   python merge_screening_decisions.py screening_workbook_AE.xlsx
   ```

   Excludes without a reason are not merged; they are listed so you can fix them. A decision that conflicts with one already in the log is never overwritten.
3. For a fresh workbook with only the still-undecided rows, merge first, move the old workbook aside, then run `python make_screening_workbook.py AE`.

A second screener gets their own workbook (`make_screening_workbook.py <initials>`). That workbook will need its own columns in the log for agreement statistics; set this up when the second screener joins.
