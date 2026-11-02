# charting — full-text eligibility and data charting

PRISMA-ScR items 10–11. One workbook per person; the CSV logs are the record.

| File | What it is |
|---|---|
| `charting_fields.py` | The data dictionary: stages S1–S12, criteria I1–I5, curation C1–C3 (+ C4 via `superseded_by`), full-text exclusion codes, and every single-choice field with its allowed values and definition |
| `make_charting_workbook.py` | Builds a workbook (Guide + Chart sheets, dropdowns) for records that passed title/abstract screening, or for a `--pilot` list |
| `merge_charting.py` | Writes decisions back: full-text decision, reason, curation, and stage mapping into `../screening_log.csv`; charted fields into `charting_log.csv` (`--pilot`: `charting_log_pilot.csv` only) |
| `compare_charting.py` | Agreement (percent and Cohen's kappa) between two people on the same sources, and a list of disagreements |

## Pilot (before charting starts)
Two people chart the same three sources, compare, and refine the definitions:

```bash
python make_charting_workbook.py AE --pilot B3-01588,B3-00105,B3-00908   # Kyle et al. 2020; Moon & Blackman 2014; Moon et al. 2019
python make_charting_workbook.py XY --pilot B3-01588,B3-00105,B3-00908   # second person's initials
python merge_charting.py charting_PILOT_AE.xlsx --pilot
python merge_charting.py charting_PILOT_XY.xlsx --pilot
python compare_charting.py charting_log_pilot.csv AE XY
```

Record any change to the definitions (in `charting_fields.py`) and the date in the protocol's amendment log.

## Charting
```bash
python make_charting_workbook.py AE        # sources with title/abstract decision include or unsure
python merge_charting.py charting_workbook_AE.xlsx
```
`../count_from_log.py` then gives the flow-diagram counts, including "reports not retrieved".
