"""
make_screening_workbook.py
==========================

Builds an Excel workbook for title/abstract screening from `../screening_log.csv`:
every row with no title/abstract decision yet, with dropdowns for the decision
and the reason. The CSV log stays the master record; decisions go back into it
with merge_screening_decisions.py.

Usage:  python make_screening_workbook.py [screener_initials]   (default AE)
Writes: screening_workbook_<initials>.xlsx (refuses to overwrite an existing one,
        so screening already done in a workbook is never lost)
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

HERE = Path(__file__).resolve().parent
LOG = HERE.parent / "screening_log.csv"
csv.field_size_limit(10**8)

DECISIONS = ["include", "exclude", "unsure"]
# Exclusion codes from the approved eligibility criteria (see ../stream_B/STREAM_B_PROTOCOL.md, amendment log).
REASONS = ["not_human_survey", "application_only", "instrument_out_of_domain", "not_english", "wrong_doc_type", "duplicate"]
FONT = "Arial"
HEAD_FILL = PatternFill("solid", fgColor="1F3A5F")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
THIN = Side(style="thin", color="BFBFBF")

# (header, log column or callable, width)
COLUMNS = [
    ("record_id", "record_id", 11),
    ("source", lambda r, c: r[c["src"]], 14),
    ("dual sample", lambda r, c: "Y" if "dual_screen_sample" in r["notes"] else "", 7),
    ("title", "title", 50),
    ("authors", "authors", 24),
    ("year", "year", 7),
    ("venue", "journal_or_publisher", 20),
    ("doi", "doi", 18),
    ("abstract", lambda r, c: c["abstracts"].get(r["record_id"], ""), 90),
    ("reached by", "reached_by", 16),
    ("already in", lambda r, c: r[c["dup"]], 14),
    ("DECISION", None, 12),
    ("REASON (if exclude)", None, 20),
    ("screener notes", None, 30),
]


def clean(v) -> str:
    return ILLEGAL_CHARACTERS_RE.sub("", str(v or ""))[:32000]


def main(initials="AE"):
    out = HERE / f"screening_workbook_{initials}.xlsx"
    if out.exists():
        sys.exit(f"{out.name} already exists; merge it first or move it before regenerating.")
    with open(LOG, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        names = {"src": cols[1], "dup": cols[7], "dec": next(c for c in cols if c.startswith("screen_ta_decision"))}
        rows = [r for r in reader if not r[names["dec"]]]
    sys.path.insert(0, str(HERE.parent))
    from local_abstracts import lookup
    names["abstracts"] = lookup("screening_log.csv", "record_id")  # local only; not committed
    if not names["abstracts"]:
        print("note: no local abstracts found; the abstract column will be empty")

    wb = Workbook()
    ws = wb.active
    ws.title = "Screen"
    for j, (h, _, w) in enumerate(COLUMNS, 1):
        c = ws.cell(row=1, column=j, value=h)
        c.font = Font(name=FONT, bold=True, color="FFFFFF")
        c.fill = HEAD_FILL
        c.alignment = Alignment(vertical="center", wrap_text=True)
        ws.column_dimensions[c.column_letter].width = w
    ws.row_dimensions[1].height = 30
    body = Font(name=FONT, size=10)
    top_wrap = Alignment(vertical="top", wrap_text=True)
    for i, r in enumerate(rows, 2):
        for j, (h, src, _) in enumerate(COLUMNS, 1):
            v = "" if src is None else (src(r, names) if callable(src) else r[src])
            c = ws.cell(row=i, column=j, value=clean(v) or None)
            c.font = body
            c.alignment = top_wrap
            c.border = Border(bottom=THIN)
            if h == "doi" and v:
                c.hyperlink = f"https://doi.org/{v}"
                c.font = Font(name=FONT, size=10, color="0563C1", underline="single")
            if src is None:
                c.fill = INPUT_FILL
        ws.row_dimensions[i].height = 90
    last = len(rows) + 1
    dv_dec = DataValidation(type="list", formula1='"' + ",".join(DECISIONS) + '"', allow_blank=True,
                            showErrorMessage=True, errorTitle="Decision", error="Choose include, exclude, or unsure.")
    dv_why = DataValidation(type="list", formula1='"' + ",".join(REASONS) + '"', allow_blank=True,
                            showErrorMessage=True, errorTitle="Reason", error="Choose an exclusion code from the list.")
    ws.add_data_validation(dv_dec)
    ws.add_data_validation(dv_why)
    dv_dec.add(f"L2:L{last}")
    dv_why.add(f"M2:M{last}")
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = f"A1:N{last}"

    g = wb.create_sheet("Guide", 0)
    g.column_dimensions["A"].width = 26
    g.column_dimensions["B"].width = 110
    guide = [
        ("Title/abstract screening workbook", ""),
        ("Screener", initials),
        ("Records", f"{len(rows)} awaiting a title/abstract decision when generated"),
        ("", ""),
        ("WHAT TO EDIT", "Only the yellow columns on the Screen sheet: DECISION, REASON (if exclude), screener notes."),
        ("DECISION", "include = meets at least one of I1–I5 on title/abstract (go to full text); exclude = clearly meets an "
                     "exclusion code; unsure = cannot tell from title/abstract (goes to full text)."),
        ("REASON", "Required for exclude, one code: " + ", ".join(REASONS) + ". See the codes below."),
        ("dual sample = Y", "Pre-drawn 20% sample (seed 2026) that a second screener will also screen. Screen it like any other row."),
        ("already in", "Record also found in Stream A (A:...) or already cited in the repository (legacy:...). Screen it anyway; "
                       "duplicates are resolved when the streams are merged."),
        ("No abstract", "Screen on title; mark unsure if the title is ambiguous."),
        ("", ""),
        ("ELIGIBILITY", "Approved 2026-11-01. Eligible if about questionnaire-based surveys of people AND at least one of:"),
        ("I1 Guidance", "Methodological guidance, recommendations, or best practice for any of the twelve workflow stages."),
        ("I2 Methodological evidence", "Research about survey methods (mode effects, incentives, question order, data quality, "
                                       "bot detection, LLM coding accuracy, ...)."),
        ("I3 Instrument", "Development, validation, adaptation, or invariance testing of a multi-item instrument for an attitude, "
                          "value, belief, norm, identity, emotion, or self-reported behavior about nature, wildlife, biodiversity, "
                          "or the environment."),
        ("I4 Standard", "Reporting, ethical, or data-governance standard applicable to such surveys."),
        ("I5 Paradigm and limits", "Examines the assumptions, limits, or alternatives to survey-based measurement of "
                                   "people's relationships with nature."),
        ("Context", "Any discipline. Only I3 is limited to the environmental domain."),
        ("Language and type", "English. Peer-reviewed articles, scholarly books/chapters, professional or standards-body documents; "
                              "preprints only if no peer-reviewed version exists."),
        ("", ""),
        ("EXCLUSION CODES", ""),
        ("not_human_survey", "Not about surveying people, including ecological/biodiversity field surveys."),
        ("application_only", "Applies a method to a substantive question with no guidance, evaluation, or validation of the method. "
                             "Expected to be the most common reason."),
        ("instrument_out_of_domain", "Instrument development/validation for a construct not about nature, wildlife, "
                                     "biodiversity, or the environment."),
        ("not_english", "Not in English."),
        ("wrong_doc_type", "Thesis/dissertation, conference abstract, editorial or commentary without methodological content, "
                           "erratum, book review."),
        ("duplicate", "Same work as another record (including a later version of a preprint)."),
        ("", ""),
        ("WHEN DONE (or partway)", "Save, then run: python merge_screening_decisions.py screening_workbook_" + initials + ".xlsx"),
        ("", ""),
        ("EXAMPLE ROW (format only)", "record_id B3-00042 | DECISION exclude | REASON application_only | "
                                     "screener notes: Empirical TPB study; no guidance on method"),
    ]
    for i, (a, b) in enumerate(guide, 1):
        ca, cb = g.cell(row=i, column=1, value=a), g.cell(row=i, column=2, value=b)
        ca.font = Font(name=FONT, bold=True, size=14 if i == 1 else 10)
        cb.font = Font(name=FONT, size=10)
        cb.alignment = Alignment(wrap_text=True, vertical="top")
        ca.alignment = Alignment(vertical="top", wrap_text=True)

    p = wb.create_sheet("Progress", 1)
    p.column_dimensions["A"].width = 28
    p.column_dimensions["B"].width = 12
    rng = f"Screen!$L$2:$L${last}"
    stats = [
        ("Total records", f"=COUNTA(Screen!$A$2:$A${last})"),
        ("Screened", f"=COUNTA({rng})"),
        ("Include", f'=COUNTIF({rng},"include")'),
        ("Exclude", f'=COUNTIF({rng},"exclude")'),
        ("Unsure", f'=COUNTIF({rng},"unsure")'),
        ("Remaining", "=B2-B3"),
        ("Percent screened", "=IF(B2=0,0,B3/B2)"),
        ("Dual-sample rows screened", f'=COUNTIFS(Screen!$C$2:$C${last},"Y",{rng},"<>")'),
        ("Excludes missing a reason", f'=COUNTIFS({rng},"exclude",Screen!$M$2:$M${last},"")'),
    ]
    p.cell(row=1, column=1, value="Measure").font = Font(name=FONT, bold=True)
    p.cell(row=1, column=2, value="Count").font = Font(name=FONT, bold=True)
    for i, (a, f) in enumerate(stats, 2):
        p.cell(row=i, column=1, value=a).font = Font(name=FONT, size=10)
        c = p.cell(row=i, column=2, value=f)
        c.font = Font(name=FONT, size=10)
        if a == "Percent screened":
            c.number_format = "0.0%"
    wb.active = wb.sheetnames.index("Screen")
    wb.save(out)
    print(f"Wrote {out.name}: {len(rows)} rows")


if __name__ == "__main__":
    main(*sys.argv[1:2])
