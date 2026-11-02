"""
make_charting_workbook.py
=========================

Builds a full-text eligibility + data-charting workbook for one person.

    python make_charting_workbook.py AE                    # records that passed title/abstract screening
    python make_charting_workbook.py AE --pilot B3-01588,B3-00105,B3-00908

Default rows: screening-log records with screen_ta_decision include or unsure and no
full-text decision yet. --pilot takes explicit record_ids (for calibrating two people
on the same sources). The workbook never overwrites an existing file.
Decisions go back with merge_charting.py.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, str(Path(__file__).resolve().parent))
from charting_fields import (CRITERIA, CRITERIA_NAMES, CURATION, CURATION_NAMES, FT_DECISIONS,  # noqa: E402
                             FT_REASONS, SINGLE, STAGE_NAMES, STAGES)

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
FONT = "Arial"
HEAD = PatternFill("solid", fgColor="1F3A5F")
INPUT = PatternFill("solid", fgColor="FFF2CC")
csv.field_size_limit(10**8)


def columns():
    """(header, width, allowed values or None, is_input)."""
    cols = [("record_id", 11, None, False), ("citation", 60, None, False), ("doi", 18, None, False),
            ("FT_DECISION", 11, FT_DECISIONS, True), ("FT_EXCLUSION_REASON", 22, FT_REASONS, True),
            ("retrieval_notes", 24, None, True)]
    cols += [(s, 5, ["x"], True) for s in STAGES]
    cols += [(c, 5, ["x"], True) for c in CRITERIA]
    cols += [(name, w, vals, True) for name, vals, w, _ in SINGLE]
    cols += [(c, 5, ["x"], True) for c in CURATION]
    cols += [("charter_notes", 30, None, True)]
    return cols


def main(initials: str, pilot_ids: list[str] | None):
    out = HERE / (f"charting_PILOT_{initials}.xlsx" if pilot_ids else f"charting_workbook_{initials}.xlsx")
    if out.exists():
        sys.exit(f"{out.name} already exists; merge it first or move it before regenerating.")
    with open(LOG, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        ta = next(c for c in cols if c.startswith("screen_ta_decision"))
        ft = next(c for c in cols if c.startswith("fulltext_decision"))
        rows = list(reader)
    if pilot_ids:
        by_id = {r["record_id"]: r for r in rows}
        missing = [i for i in pilot_ids if i not in by_id]
        if missing:
            sys.exit(f"record_ids not in the log: {missing}")
        rows = [by_id[i] for i in pilot_ids]
    else:
        rows = [r for r in rows if r[ta] in ("include", "unsure") and not r[ft]]

    wb = Workbook()
    ws = wb.active
    ws.title = "Chart"
    spec = columns()
    for j, (h, w, vals, _) in enumerate(spec, 1):
        c = ws.cell(row=1, column=j, value=h)
        c.font = Font(name=FONT, bold=True, color="FFFFFF", size=10)
        c.fill = HEAD
        c.alignment = Alignment(wrap_text=True, vertical="center", text_rotation=90 if w <= 5 else 0)
        ws.column_dimensions[c.column_letter].width = w
    ws.row_dimensions[1].height = 70
    last = len(rows) + 1
    for i, r in enumerate(rows, 2):
        cite = f"{r['authors']} ({r['year']}). {r['title']}. {r['journal_or_publisher']}".strip()
        for j, (h, _, _, is_input) in enumerate(spec, 1):
            v = {"record_id": r["record_id"], "citation": cite, "doi": r["doi"]}.get(h)
            c = ws.cell(row=i, column=j, value=v or None)
            c.font = Font(name=FONT, size=10, **({"color": "0563C1", "underline": "single"} if h == "doi" and v else {}))
            c.alignment = Alignment(wrap_text=True, vertical="top")
            if h == "doi" and v:
                c.hyperlink = f"https://doi.org/{v}"
            if is_input:
                c.fill = INPUT
        ws.row_dimensions[i].height = 60
    for j, (h, _, vals, _) in enumerate(spec, 1):
        if vals and last > 1:
            col = ws.cell(row=1, column=j).column_letter
            dv = DataValidation(type="list", formula1='"' + ",".join(vals) + '"', allow_blank=True,
                                showErrorMessage=True, error=f"Choose from: {', '.join(vals)}")
            ws.add_data_validation(dv)
            dv.add(f"{col}2:{col}{last}")
    ws.freeze_panes = "D2"

    g = wb.create_sheet("Guide", 0)
    g.column_dimensions["A"].width = 26
    g.column_dimensions["B"].width = 110
    lines = [
        ("Full-text eligibility and data charting", ""),
        ("Charter", initials + (" (PILOT)" if pilot_ids else "")),
        ("Rows", f"{len(rows)} source(s)"),
        ("", ""),
        ("WHAT TO EDIT", "Yellow columns on the Chart sheet only. Read the full text before deciding."),
        ("1. FT_DECISION", "include = meets the eligibility criteria on full text; exclude = does not, or full text could not be obtained."),
        ("2. FT_EXCLUSION_REASON", "Required for exclude: " + ", ".join(FT_REASONS) + ". Use not_retrieved only after trying the library, interlibrary loan, and the authors; record attempts in retrieval_notes."),
        ("3. If include: charting", "Mark every stage the source informs (S1–S12, 'x'), every criterion it meets (I1–I5, 'x'), then the single-choice fields, a short key_guidance paraphrase, and curation (C1–C3, 'x'). Fill superseded_by only to set the source aside (C4)."),
        ("", ""),
        ("STAGES", "; ".join(f"{k} {v}" for k, v in STAGE_NAMES.items())),
        ("CRITERIA", "; ".join(f"{k} {v}" for k, v in CRITERIA_NAMES.items())),
        ("CURATION", "; ".join(f"{k} {v}" for k, v in CURATION_NAMES.items()) + "; retained if ≥1 of C1–C3 and no superseded_by."),
        ("", ""),
        ("FIELD DEFINITIONS", ""),
    ] + [(name, (", ".join(vals) + " — " if vals else "") + desc) for name, vals, _, desc in SINGLE] + [
        ("", ""),
        ("EXAMPLE ROW (format only)", "FT_DECISION include | S3 x, S11 x | I1 x, I2 x | document_type article | discipline psychometrics | "
                                      "environmental_context yes | evidence_basis empirical | paradigm_signal post_positivist | "
                                      "key_guidance: Recommends ≥3 indicators per construct and composite reliability when loadings differ. | C1 x, C2 x"),
        ("WHEN DONE (or partway)", "Save, then run: python merge_charting.py " + out.name + (" --pilot" if pilot_ids else "")),
    ]
    for i, (a, b) in enumerate(lines, 1):
        ca, cb = g.cell(row=i, column=1, value=a), g.cell(row=i, column=2, value=b)
        ca.font = Font(name=FONT, bold=True, size=14 if i == 1 else 10)
        cb.font = Font(name=FONT, size=10)
        for c in (ca, cb):
            c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.active = wb.sheetnames.index("Chart")
    wb.save(out)
    print(f"Wrote {out.name}: {len(rows)} row(s)")


if __name__ == "__main__":
    args = sys.argv[1:]
    pilot = None
    if "--pilot" in args:
        k = args.index("--pilot")
        pilot = [x.strip() for x in args[k + 1].split(",") if x.strip()]
        args = args[:k] + args[k + 2:]
    main(args[0] if args else "AE", pilot)
