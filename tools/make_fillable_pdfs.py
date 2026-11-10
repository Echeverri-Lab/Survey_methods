#!/usr/bin/env python3
"""Build fillable PDF versions of the student-facing Markdown templates.

Each template listed in TEMPLATES is converted to a PDF that sits next to the
Markdown source (same name, .pdf extension). The PDF keeps every instruction
from the Markdown and turns the places where students write into AcroForm
fields:

* empty table cells and placeholder cells ("...", "YYYY-MM-DD")  -> text boxes
* "- [ ]" checklist items and "☐ option" choices                 -> check boxes
* "______" blanks and list items that end in a colon ("- RQ1:")  -> text boxes
* italic prompts with nothing below them ("*Describe ... here*") -> large boxes
* "Trait / Attitude / State" choices in an "Entry" column       -> check boxes

Rebuild every PDF after editing a template:

    venv/bin/python tools/make_fillable_pdfs.py

or rebuild only some of them:

    venv/bin/python tools/make_fillable_pdfs.py Step_04 Step_09

Requirements: reportlab (see requirements.txt) and the DejaVu fonts that ship
with matplotlib (already in requirements.txt). DejaVu is used because it has
the ☐, ≥, ≤, →, and box-drawing characters the templates use.
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

REPO = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Templates to convert, with per-file options.
#   landscape        : lay the page out sideways (wide tables)
#   min_rows         : minimum body rows for repeatable (log-style) tables
#   checkbox_answers : add an answer box under every "- [ ]" question
#   bullets_as_fields: every plain bullet is a label with an answer box
#   prompt_boxes     : every italic-only paragraph gets an answer box
#   madlib           : paragraphs with `[PLACEHOLDER]`s get a box to rewrite them
# --------------------------------------------------------------------------
TEMPLATES: dict[str, dict] = {
    "Step_01_Epistemological_Alignment_and_Method_Selection/axiology_checklist.md": {"checkbox_answers": True},
    "Step_01_Epistemological_Alignment_and_Method_Selection/epistemological_stance_memo.md": {"prompt_boxes": True, "box_lines": 14},
    "Step_01_Epistemological_Alignment_and_Method_Selection/method_selection_form.md": {},
    "Step_01_Epistemological_Alignment_and_Method_Selection/method_selection_log.md": {"min_rows": 10},
    "Step_02_Theory_Grounding_and_Construct_Conceptualization/notes.md": {"prompt_boxes": True, "box_lines": 30},
    "Step_03_Psychometric_Scales_and_Construct_Validity/templates/scale_documentation_template.md": {"bullets_as_fields": True},
    "Step_04_Study_Architecture_and_Experimental_Design/design_decision_matrix.md": {},
    "Step_04_Study_Architecture_and_Experimental_Design/design_docs/randomization_plan.md": {"min_rows": 4},
    "Step_04_Study_Architecture_and_Experimental_Design/design_docs/survey_flow_diagram.md": {},
    "Step_04_Study_Architecture_and_Experimental_Design/study_design_checklist.md": {},
    "Step_04_Study_Architecture_and_Experimental_Design/temporal_context_log.md": {"min_rows": 6},
    "Step_05_Preregistration_and_Open_Science/aspredicted_template.md": {"prompt_boxes": True},
    "Step_05_Preregistration_and_Open_Science/confirmatory_vs_exploratory_guide.md": {},
    "Step_05_Preregistration_and_Open_Science/preregistration_checklist.md": {},
    "Step_05_Preregistration_and_Open_Science/preregistration_template.md": {"prompt_boxes": True, "min_rows": 4},
    "Step_06_Instrument_Construction/templates/survey_matrix_template.md": {"landscape": True, "min_rows": 8},
    "Step_06_Instrument_Construction/templates/survey_template.md": {"bullets_as_fields": True},
    "Step_06_Instrument_Construction/quality_control/qc_checklist.md": {},
    "Step_08_Ethics_and_Participant_Compensation/policies/consent_template.md": {"bullets_as_fields": True},
    "Step_09_Power_Analysis_Sampling_and_Pilots/power_analysis_template.md": {"min_rows": 5},
    "Step_10_Survey_Distribution/translation_protocol.md": {"landscape": True, "min_rows": 10},
    "Step_11_Data_Preparation_Analysis_and_Reporting/data_cleaning_checklist.md": {"min_rows": 4},
    "Step_12_Writing_Survey_Research_Paper/methods_section_template.md": {"madlib": True},
    "Step_12_Writing_Survey_Research_Paper/reporting_checklists.md": {},
}

# --------------------------------------------------------------------------
# Fonts and styles
# --------------------------------------------------------------------------


def _find_dejavu() -> Path:
    candidates = []
    try:
        import matplotlib  # noqa: F401

        candidates.append(Path(matplotlib.__file__).parent / "mpl-data" / "fonts" / "ttf")
    except ImportError:
        pass
    candidates += [Path("/usr/share/fonts/truetype/dejavu"), Path("/usr/share/fonts/dejavu")]
    for c in candidates:
        if (c / "DejaVuSans.ttf").exists():
            return c
    sys.exit("DejaVu fonts not found: install matplotlib (pip install -r requirements.txt).")


def register_fonts() -> None:
    d = _find_dejavu()
    pdfmetrics.registerFont(TTFont("DV", str(d / "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("DV-B", str(d / "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("DV-I", str(d / "DejaVuSans-Oblique.ttf")))
    pdfmetrics.registerFont(TTFont("DV-BI", str(d / "DejaVuSans-BoldOblique.ttf")))
    pdfmetrics.registerFont(TTFont("DVM", str(d / "DejaVuSansMono.ttf")))
    pdfmetrics.registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV-I", boldItalic="DV-BI")


INK = colors.HexColor("#1f2933")
MUTED = colors.HexColor("#5b6770")
ACCENT = colors.HexColor("#1d4e89")
FIELD_BG = colors.HexColor("#eef4fb")
FIELD_BORDER = colors.HexColor("#7b9cc4")
RULE = colors.HexColor("#c8d1da")
HEAD_BG = colors.HexColor("#e3e9ef")

BODY_SIZE = 9.5
CELL_SIZE = 8

STYLES = {
    "body": ParagraphStyle("body", fontName="DV", fontSize=BODY_SIZE, leading=BODY_SIZE * 1.35, textColor=INK, spaceAfter=4, alignment=TA_LEFT),
    "h1": ParagraphStyle("h1", fontName="DV-B", fontSize=16, leading=20, textColor=ACCENT, spaceBefore=4, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName="DV-B", fontSize=12.5, leading=16, textColor=ACCENT, spaceBefore=10, spaceAfter=5),
    "h3": ParagraphStyle("h3", fontName="DV-B", fontSize=10.5, leading=14, textColor=INK, spaceBefore=8, spaceAfter=4),
    "h4": ParagraphStyle("h4", fontName="DV-B", fontSize=9.5, leading=13, textColor=INK, spaceBefore=6, spaceAfter=3),
    "quote": ParagraphStyle("quote", fontName="DV", fontSize=9, leading=12.5, textColor=MUTED, leftIndent=10, spaceAfter=3),
    "cell": ParagraphStyle("cell", fontName="DV", fontSize=CELL_SIZE, leading=CELL_SIZE * 1.3, textColor=INK),
    "cellhead": ParagraphStyle("cellhead", fontName="DV-B", fontSize=CELL_SIZE, leading=CELL_SIZE * 1.3, textColor=INK),
    "hint": ParagraphStyle("hint", fontName="DV-I", fontSize=7, leading=8.5, textColor=MUTED),
    "banner": ParagraphStyle("banner", fontName="DV", fontSize=8, leading=10.5, textColor=INK),
    "code": ParagraphStyle("code", fontName="DVM", fontSize=7.2, leading=8.8, textColor=INK),
}

# --------------------------------------------------------------------------
# Inline Markdown
# --------------------------------------------------------------------------

LATEX = {r"\geq": "≥", r"\leq": "≤", r"\alpha": "α", r"\omega": "ω", r"\times": "×", r"\beta": "β", r"\eta": "η", r"\chi": "χ"}


def _clean_math(s: str) -> str:
    def repl(m):
        t = m.group(1)
        for k, v in LATEX.items():
            t = t.replace(k, v)
        return t.replace("^2", "²").replace("_", "")

    return re.sub(r"\$([^$]+)\$", repl, s)


def md_inline(s: str) -> str:
    """Markdown inline syntax -> reportlab paragraph markup."""
    s = _clean_math(s)
    s = s.replace("&", "&amp;").replace("<br>", "\x00").replace("<br/>", "\x00").replace("<br />", "\x00")
    s = s.replace("<", "&lt;").replace(">", "&gt;").replace("\x00", "<br/>")
    s = re.sub(r"`([^`]+)`", r'<font face="DVM" size="8">\1</font>', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="#1d4e89">\1</link>', s)
    s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"(?<![\w_])_(?!_)(?!\s)(.+?)(?<!\s)_(?![\w_])", r"<i>\1</i>", s)
    return s


def plain(s: str) -> str:
    """Markdown inline -> plain text (for tooltips and labels)."""
    s = _clean_math(s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    s = re.sub(r"[*`]", "", s)
    s = s.replace("<br>", " ")
    return re.sub(r"\s+", " ", s).strip()


def runs(s: str) -> list[tuple[str, str]]:
    """Split inline Markdown into (text, font) runs for the inline form layout."""
    s = _clean_math(s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    out: list[tuple[str, str]] = []
    pos = 0
    for m in re.finditer(r"\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])|`([^`]+)`", s):
        if m.start() > pos:
            out.append((s[pos : m.start()], "DV"))
        if m.group(1):
            out.append((m.group(1), "DV-BI"))
        elif m.group(2):
            out.append((m.group(2), "DV-B"))
        elif m.group(3):
            out.append((m.group(3), "DV-I"))
        else:
            out.append((m.group(4), "DVM"))
        pos = m.end()
    if pos < len(s):
        out.append((s[pos:], "DV"))
    return out


# --------------------------------------------------------------------------
# Form flowables
# --------------------------------------------------------------------------


class FieldNamer:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.n = 0

    def __call__(self, hint: str) -> str:
        self.n += 1
        slug = re.sub(r"[^A-Za-z0-9]+", "_", hint)[:40].strip("_") or "field"
        return f"{self.prefix}.{self.n:03d}_{slug}"


def _textfield(canv, name, tooltip, x, y, w, h, multiline, font_size=9):
    canv.acroForm.textfield(
        name=name,
        tooltip=(tooltip or name)[:250],
        x=x,
        y=y,
        width=w,
        height=h,
        fontName="Helvetica",
        fontSize=font_size,  # fixed size: auto-size (0) is ignored by browser PDF viewers
        borderColor=FIELD_BORDER,
        fillColor=FIELD_BG,
        textColor=colors.black,
        borderWidth=0.6,
        fieldFlags="multiline" if multiline else "",
        annotationFlags="print",
        relative=True,
    )


def _checkbox(canv, name, tooltip, x, y, size):
    canv.acroForm.checkbox(
        name=name,
        tooltip=(tooltip or name)[:250],
        x=x,
        y=y,
        size=size,
        buttonStyle="check",
        borderColor=FIELD_BORDER,
        fillColor=colors.white,
        textColor=colors.black,
        borderWidth=0.6,
        fieldFlags="",
        annotationFlags="print",
        relative=True,
    )


class TextBox(Flowable):
    """A text field that fills the available width."""

    def __init__(self, namer, tooltip, height=16, multiline=True, label=None, width=None, font_size=9.5):
        super().__init__()
        self.namer, self.tooltip, self.h, self.multiline, self.label, self.fixed_w = namer, tooltip, height, multiline, label, width
        self.font_size = font_size

    def wrap(self, aw, ah):
        self.w = self.fixed_w or aw
        return self.w, self.h + (11 if self.label else 0)

    def draw(self):
        y = 0
        if self.label:
            self.canv.setFont("DV-I", 7)
            self.canv.setFillColor(MUTED)
            self.canv.drawString(0, self.h + 3, self.label)
        _textfield(self.canv, self.namer(self.tooltip), self.tooltip, 0, y, self.w, self.h, self.multiline, self.font_size)


@dataclass
class Tok:
    kind: str  # "text" | "check" | "field" | "br"
    text: str = ""
    font: str = "DV"
    width: float = 0  # field width; 0 = fill rest of line
    tip: str = ""


class InlineForm(Flowable):
    """Text with check boxes and short text fields laid out in flowing lines."""

    def __init__(self, toks: list[Tok], namer, size=BODY_SIZE, indent=0, color=INK):
        super().__init__()
        self.toks, self.namer, self.size, self.indent, self.color = toks, namer, size, indent, color

    def _layout(self, aw):
        size = self.size
        fh = size + 5  # field height
        box = size + 0.5
        lines: list[list] = [[]]
        x = self.indent
        avail = aw

        def newline():
            nonlocal x
            lines.append([])
            x = self.indent

        for k, t in enumerate(self.toks):
            if t.kind == "br":
                newline()
            elif t.kind == "check":
                if x > self.indent + 4:
                    x += 4  # gap after the previous option's label
                nxt_word = ""
                if k + 1 < len(self.toks) and self.toks[k + 1].kind == "text":
                    nxt_word = (self.toks[k + 1].text.split() or [""])[0]
                    nxt_w = stringWidth(nxt_word, self.toks[k + 1].font, size)
                else:
                    nxt_w = 0
                if x + box + 3 + nxt_w > avail and x > self.indent:
                    newline()
                lines[-1].append(("check", x, box, t.tip))
                x += box + 3
            elif t.kind == "field":
                w = t.width
                if w == 0:  # fill the rest of the line
                    if avail - x < 110:
                        newline()
                    w = avail - x
                elif x + w > avail:
                    newline()
                    w = min(w, avail - x)
                lines[-1].append(("field", x, w, t.tip))
                x += w + 3
            else:
                for word in re.split(r"(\s+)", t.text):
                    if not word:
                        continue
                    ww = stringWidth(word, t.font, size)
                    if word.isspace():
                        if x > self.indent:
                            x += stringWidth(" ", t.font, size)
                        continue
                    if x + ww > avail and x > self.indent:
                        newline()
                    lines[-1].append(("text", x, word, t.font))
                    x += ww
        heights = []
        for ln in lines:
            has_field = any(item[0] == "field" for item in ln)
            heights.append((fh + 3) if has_field else size * 1.35)
        return lines, heights, fh, box

    def wrap(self, aw, ah):
        self.aw = aw
        self.lines, self.heights, self.fh, self.box = self._layout(aw)
        self.height = sum(self.heights) + 2
        return aw, self.height

    def draw(self):
        c = self.canv
        y = self.height
        for ln, h in zip(self.lines, self.heights):
            y -= h
            base = y + (h - self.size) / 2 + 1
            for item in ln:
                if item[0] == "text":
                    c.setFont(item[3], self.size)
                    c.setFillColor(self.color)
                    c.drawString(item[1], base, item[2])
                elif item[0] == "check":
                    _checkbox(c, self.namer(item[3]), item[3], item[1], base - 1.5, self.box)
                else:
                    _textfield(c, self.namer(item[3]), item[3], item[1], y + 1.5, item[2], self.fh, False, min(9, self.size))


# --------------------------------------------------------------------------
# Markdown -> tokens for inline forms
# --------------------------------------------------------------------------

BLANK = re.compile(r"_{3,}")


def text_toks(s: str) -> list[Tok]:
    return [Tok("text", t, f) for t, f in runs(s)]


def form_toks(s: str, tip: str, end_field: bool = False) -> list[Tok]:
    """Turn a line with ☐ choices and ____ blanks into tokens."""
    toks: list[Tok] = []
    parts = re.split(r"(☐|☑|_{3,})", s)
    label = ""
    for i, p in enumerate(parts):
        if p in ("☐", "☑"):
            nxt = parts[i + 1] if i + 1 < len(parts) else ""
            opt = plain(re.split(r"☐|_{3,}", nxt)[0]).strip(" :")
            toks.append(Tok("check", tip=f"{tip}: {opt}" if opt else tip))
        elif BLANK.fullmatch(p):
            after = parts[i + 1] if i + 1 < len(parts) else ""
            at_end = not plain(after).strip(" .")
            width = 0 if at_end else max(60, min(160, len(p) * 9))
            toks.append(Tok("field", width=width, tip=f"{tip}: {plain(label)}".strip(": ")))
        elif p:
            toks += text_toks(p)
            label = p
    if end_field and not any(t.kind == "field" for t in toks[-1:]):
        toks.append(Tok("text", " "))
        toks.append(Tok("field", width=0, tip=f"{tip}: {plain(s)}".strip(": ")))
    return toks


def has_form(s: str) -> bool:
    return "☐" in s or bool(BLANK.search(s))


# --------------------------------------------------------------------------
# Block parser
# --------------------------------------------------------------------------


@dataclass
class Block:
    kind: str
    lines: list[str] = field(default_factory=list)
    level: int = 0
    lang: str = ""


def parse_blocks(md: str) -> list[Block]:
    lines = md.splitlines()
    blocks: list[Block] = []
    i = 0
    para: list[str] = []

    def flush():
        nonlocal para
        if para:
            blocks.append(Block("para", para))
            para = []

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("```"):
            flush()
            lang = s[3:].strip()
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            blocks.append(Block("code", body, lang=lang))
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", s)
        if m:
            flush()
            blocks.append(Block("heading", [m.group(2)], level=len(m.group(1))))
        elif re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", s):
            flush()
            blocks.append(Block("hr"))
        elif s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-{2,}", lines[i + 1].strip()):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            blocks.append(Block("table", rows))
            continue
        elif s.startswith(">"):
            flush()
            q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append(Block("quote", q))
            continue
        elif re.match(r"^\s*([-*+]|\d+[.)])\s+", ln):
            flush()
            blocks.append(Block("item", [ln]))
            # absorb lazy continuation lines
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"^\s*([-*+]|\d+[.)])\s+|^\s*[|>#`]", lines[i + 1]):
                if re.fullmatch(r"(-{3,}|\*{3,})", lines[i + 1].strip()):
                    break
                blocks[-1].lines[0] += " " + lines[i + 1].strip()
                i += 1
        elif not s:
            flush()
        else:
            para.append(ln)
        i += 1
    flush()
    return blocks


def split_row(row: str) -> list[str]:
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|") and not row.endswith("\\|"):
        row = row[:-1]
    cells, cur, in_code = [], "", False
    k = 0
    while k < len(row):
        ch = row[k]
        if ch == "\\" and k + 1 < len(row) and row[k + 1] == "|":
            cur += "|"
            k += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
        k += 1
    cells.append(cur.strip())
    return cells


# --------------------------------------------------------------------------
# Builder
# --------------------------------------------------------------------------

PLACEHOLDER = re.compile(r"^(\.\.\.|…|x{2,}|yyyy-mm-dd|min|yes/no|_+|-|—)?$", re.I)
FILL_HEADER = re.compile(r"entry|your choice|your answer|risk level|response|^value|^answer|^result|^status|^n\b|^date$", re.I)
LONG_HEADER = re.compile(r"rationale|justif|descri|notes?|deviation|reason|impact|change|output|text|comment|action|decision|explan|detail", re.I)
LONG_ROW = re.compile(r"justif|why|how |describe|descri|hypothes|question|outcome|statistic|source|convert|rationale|explain|criteria|procedure|plan\b|notes", re.I)
ID_CELL = re.compile(r"^[A-Za-z]{0,3}\d+[-_.]?\d*$")


class Builder:
    def __init__(self, rel: str, opts: dict, page_w: float):
        self.rel = rel
        self.opts = opts
        self.page_w = page_w
        self.namer = FieldNamer(Path(rel).stem)
        self.story: list = []
        self.section = ""

    # ---- helpers ---------------------------------------------------------
    def box(self, tip, lines=None):
        n = lines or self.opts.get("box_lines", 5)
        self.story.append(TextBox(self.namer, tip, height=12 * n + 6))
        self.story.append(Spacer(1, 5))

    def para(self, text, style="body"):
        self.story.append(Paragraph(md_inline(text), STYLES[style]))

    # ---- main --------------------------------------------------------------
    def build(self, blocks: list[Block]):
        for idx, b in enumerate(blocks):
            nxt = blocks[idx + 1] if idx + 1 < len(blocks) else None
            getattr(self, f"do_{b.kind}")(b, nxt)
        return self.story

    def do_heading(self, b, nxt):
        lvl = min(b.level, 4)
        self.section = plain(BLANK.sub("", b.lines[0]))
        if BLANK.search(b.lines[0]):  # e.g. "### Wave: _______ (e.g., T0)"
            self.story.append(Spacer(1, 6))
            self.story.append(InlineForm(form_toks(f"**{b.lines[0]}**", self.section), self.namer, size=10.5))
            return
        self.story.append(Paragraph(md_inline(b.lines[0]), STYLES[f"h{lvl}"]))

    def do_hr(self, b, nxt):
        self.story.append(HR())

    def do_code(self, b, nxt):
        rows = [l.strip() for l in b.lines if l.strip()]
        if len(rows) >= 3 and all(r.startswith("|") for r in rows) and re.match(r"^\|?\s*:?-{2,}", rows[1]):
            return self.do_table(Block("table", rows), nxt)
        text = "\n".join(b.lines)
        self.story.append(Preformatted(text, STYLES["code"], maxLineLength=150))
        self.story.append(Spacer(1, 4))
        if b.lang == "mermaid":
            self.para("<i>Your version of this flow (list each step and arrow, or sketch it and attach the image):</i>".replace("<i>", "*").replace("</i>", "*"))
            self.box(f"{self.section}: your flow", lines=12)

    def do_quote(self, b, nxt):
        for ln in self._hard_lines(b.lines):
            if not ln.strip():
                continue
            self.story.append(Paragraph(md_inline(ln), STYLES["quote"]))
        self.story.append(Spacer(1, 3))

    def _hard_lines(self, lines):
        """Join soft-wrapped lines; keep lines ending in two spaces or a backslash separate."""
        out, cur = [], ""
        for ln in lines:
            hard = ln.endswith("  ") or ln.endswith("\\")
            cur = (cur + " " + ln.strip().rstrip("\\")).strip() if cur else ln.strip().rstrip("\\")
            if hard or not ln.strip():
                out.append(cur)
                cur = ""
        if cur:
            out.append(cur)
        return out

    def do_para(self, b, nxt):
        lines = self._hard_lines(b.lines)
        text = " ".join(lines)
        is_prompt = bool(re.fullmatch(r"\*[^*].*\*|_[^_].*_", text.strip()))
        if any(has_form(l) for l in lines):
            for ln in lines:
                if has_form(ln):
                    self.story.append(InlineForm(form_toks(ln, self.section), self.namer))
                else:
                    self.para(ln)
            self.story.append(Spacer(1, 3))
            return
        self.para("<br>".join(lines) if len(lines) > 1 else text)
        if self.opts.get("madlib") and [ph for ph in re.findall(r"`\[[^\]]+\]`", text) if ph != "`[BRACKETED]`"]:
            n = max(3, min(12, len(text) // 110 + 2))
            self.box(f"{self.section}: your text", lines=n)
            return
        follows_nothing = nxt is None or nxt.kind in ("heading", "hr")
        if plain(text).endswith(":") and follows_nothing:
            self.box(f"{self.section}: {plain(text)[:80]}", lines=self.opts.get("box_lines", 6))
            return
        if is_prompt and (self.opts.get("prompt_boxes") or text.strip().startswith("*(")) and follows_nothing:
            self.box(f"{self.section}: {plain(text)[:80]}")

    def do_item(self, b, nxt):
        ln = b.lines[0]
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(\[( |x|X)\]\s+)?(.*)", ln)
        indent_spaces, marker, check, _, text = m.groups()
        depth = len(indent_spaces.expandtabs(4)) // 2
        indent = 12 * depth
        tip = f"{self.section}: {plain(text)[:90]}"
        child_follows = nxt is not None and nxt.kind == "item" and len(re.match(r"^(\s*)", nxt.lines[0]).group(1)) > len(indent_spaces)
        ends_colon = plain(text).endswith(":") and not child_follows
        madlib_item = self.opts.get("madlib") and re.search(r"`\[[^\]]+\]`", text)

        toks: list[Tok] = []
        if check is not None:
            toks.append(Tok("check", tip=tip))
        elif marker[0].isdigit():
            toks.append(Tok("text", marker + " "))
        else:
            toks.append(Tok("text", "•  ", "DV"))
        bullet_field = self.opts.get("bullets_as_fields") and check is None and not marker[0].isdigit()
        if has_form(text) or ends_colon:
            toks += form_toks(text, self.section, end_field=ends_colon)
        else:
            toks += text_toks(text)
        self.story.append(InlineForm(toks, self.namer, indent=0))
        if indent:
            self.story[-1] = Indented(self.story[-1], indent)
        if bullet_field and not ends_colon:
            self.story.append(Indented(TextBox(self.namer, tip, height=12 * 3 + 6), indent + 14))
            self.story.append(Spacer(1, 3))
        elif self.opts.get("checkbox_answers") and check is not None:
            self.story.append(Indented(TextBox(self.namer, tip + " (answer)", height=12 * 3 + 6), indent + 14))
            self.story.append(Spacer(1, 4))
        elif madlib_item:
            self.story.append(Indented(TextBox(self.namer, tip, height=18), indent + 14))
            self.story.append(Spacer(1, 2))
        if nxt is None or nxt.kind != "item":
            self.story.append(Spacer(1, 4))

    # ---- tables ------------------------------------------------------------
    def do_table(self, b, nxt):
        rows = [split_row(r) for r in b.lines]
        header, body = rows[0], rows[2:]
        ncol = len(header)
        body = [(r + [""] * ncol)[:ncol] for r in body]
        wide = ncol >= 5
        fill_cols = {j for j, h in enumerate(header) if FILL_HEADER.search(plain(h))}
        long_cols = {j for j, h in enumerate(header) if LONG_HEADER.search(plain(h))}

        def is_blank(c):
            return bool(PLACEHOLDER.match(plain(c)))

        def is_example(r):
            rest = [c for c in r[1:] if c]
            return bool(rest) and all(re.fullmatch(r"\*[^*].*\*", c) for c in rest)

        # Repeatable (log-style) tables get extra blank rows.
        last = body[-1] if body else []
        repeatable = bool(body) and all(is_blank(c) for c in last[1:]) and (is_blank(last[0]) or ID_CELL.match(plain(last[0]))) and not any(
            plain(c) for c in last[1:]
        )
        repeatable = repeatable or (bool(body) and all(is_example(r) for r in body))
        n_rows_added = 0
        if repeatable:
            target = self.opts.get("min_rows", 4)
            while len(body) < target:
                body.append([""] * ncol)
                n_rows_added += 1

        avail = self.page_w
        widths = self._col_widths(header, body, fill_cols, avail)
        data = [[Paragraph(md_inline(h), STYLES["cellhead"]) for h in header]]
        for r in body:
            row_label = plain(r[0]) if r and r[0] and not is_blank(r[0]) else ""
            cells = []
            for j, c in enumerate(r):
                tip = f"{self.section} | {row_label} | {plain(header[j])}".replace("|  |", "|")
                cells.append(self._cell(c, j, tip, fill_cols, long_cols, wide, is_example(r), widths[j]))
            data.append(cells)
        t = Table(data, colWidths=widths, repeatRows=1)
        t.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.4, RULE),
                    ("BACKGROUND", (0, 0), (-1, 0), HEAD_BG),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 3),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]
            )
        )
        self.story.append(t)
        if n_rows_added:
            self.story.append(Paragraph("<i>Need more rows? Add a continuation page or attach a spreadsheet with the same columns.</i>", STYLES["hint"]))
        self.story.append(Spacer(1, 8))

    def _col_widths(self, header, body, fill_cols, avail):
        weights = []
        for j, h in enumerate(header):
            texts = [plain(r[j]) for r in body if j < len(r)]
            longest_word = max([len(w) for t in texts + [plain(h)] for w in t.split()] or [4])
            avg = sum(len(t) for t in texts) / max(1, len(texts))
            w = max(avg, len(plain(h)) * 0.8, longest_word * 1.1, 6)
            if j in fill_cols or not any(texts):
                w = max(w, 28)
            weights.append(min(w, 90))
        # Minimum width: the longest word in the header or a body cell must fit.
        mins = []
        for j, h in enumerate(header):
            m = max([stringWidth(w, "DV-B", CELL_SIZE) for w in plain(h).split()] or [20])
            for r in body:
                for w in plain(re.sub(r"<br\s*/?>", " ", r[j])).replace("☐", " ").split():
                    m = max(m, stringWidth(w, "DV", CELL_SIZE) + (CELL_SIZE + 6 if "☐" in r[j] else 0))
            if any(not plain(r[j]) or PLACEHOLDER.match(plain(r[j])) for r in body):
                m = max(m, 34)
            mins.append(min(m + 8, avail / len(header) * 1.6))
        if sum(mins) >= avail:
            return [avail * m / sum(mins) for m in mins]
        spare = avail - sum(mins)
        tot = sum(weights)
        return [m + spare * w / tot for m, w in zip(mins, weights)]

    def _cell(self, c, j, tip, fill_cols, long_cols, wide, example, width):
        txt = plain(c)
        row_label = tip.split(" | ")[1] if tip.count(" | ") >= 2 else ""
        tall = 34 if (wide or j in long_cols or LONG_ROW.search(row_label)) else 16
        if example:
            return Paragraph(md_inline(c), STYLES["hint"])
        if not txt or PLACEHOLDER.match(txt):
            return TextBox(self.namer, tip + (f" ({txt})" if txt else ""), height=tall, multiline=True, font_size=8)
        parts = re.split(r"<br\s*/?>", c)
        if "☐" in c or (j in fill_cols and (BLANK.search(c) or re.search(r"\S\s/\s\S", c) or txt.endswith(":"))):
            flows = []
            for p in parts:
                if not p.strip():
                    continue
                if "☐" not in p and j in fill_cols and re.search(r"\S\s/\s\S", p):
                    opts = [o.strip() for o in p.split(" / ")]
                    toks = []
                    for o in opts:
                        if BLANK.search(o) or o.rstrip().endswith(":"):
                            o = BLANK.sub("", o).strip()
                            toks += [Tok("check", tip=f"{tip}: {plain(o)}")] + text_toks(o + " ") + [Tok("field", width=0, tip=f"{tip}: {plain(o)}")]
                        else:
                            toks += [Tok("check", tip=f"{tip}: {plain(o)}")] + text_toks(o + "   ")
                    flows.append(InlineForm(toks, self.namer, size=CELL_SIZE))
                else:
                    end_field = plain(p).endswith(":")
                    flows.append(InlineForm(form_toks(p, tip, end_field=end_field), self.namer, size=CELL_SIZE))
            return flows
        if j in fill_cols and re.fullmatch(r"\(.*\)", txt):
            return [Paragraph(md_inline(c), STYLES["hint"]), TextBox(self.namer, f"{tip} {txt}", height=tall, font_size=8)]
        if BLANK.search(c):
            return [InlineForm(form_toks(p, tip), self.namer, size=CELL_SIZE) for p in parts if p.strip()]
        return Paragraph(md_inline(c), STYLES["cell"])


class HR(Flowable):
    def wrap(self, aw, ah):
        self.w = aw
        return aw, 10

    def draw(self):
        self.canv.setStrokeColor(RULE)
        self.canv.setLineWidth(0.6)
        self.canv.line(0, 5, self.w, 5)


class Indented(Flowable):
    def __init__(self, inner, indent):
        super().__init__()
        self.inner, self.indent = inner, indent

    def wrap(self, aw, ah):
        w, h = self.inner.wrap(aw - self.indent, ah)
        return aw, h

    def draw(self):
        self.inner.drawOn(self.canv, self.indent, 0)


# --------------------------------------------------------------------------
# Document
# --------------------------------------------------------------------------


def build_pdf(rel: str, opts: dict) -> Path:
    src = REPO / rel
    out = src.with_suffix(".pdf")
    pagesize = landscape(letter) if opts.get("landscape") else letter
    margin = 0.55 * inch
    doc = SimpleDocTemplate(
        str(out),
        pagesize=pagesize,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=margin,
        bottomMargin=margin,
        title=plain(_title(src)),
        author="Survey_methods repository",
        subject=f"Fillable version of {rel}",
        creator="tools/make_fillable_pdfs.py",
    )
    page_w = pagesize[0] - 2 * margin - 1
    md = src.read_text(encoding="utf-8")
    builder = Builder(rel, opts, page_w)
    banner = Table(
        [[Paragraph(
            "<b>Fillable PDF.</b> Click a blue box to type; tick the small squares. Save with <b>File › Save</b> "
            "and attach the saved PDF to your assignment. Works best in the free Adobe Acrobat Reader; "
            "macOS Preview and web browsers also work. If an answer does not fit its box, continue it on an extra page. "
            f"Source: <font face=\"DVM\" size=\"7\">{rel}</font> (rebuild with <font face=\"DVM\" size=\"7\">tools/make_fillable_pdfs.py</font>).",
            STYLES["banner"],
        )]],
        colWidths=[page_w],
    )
    banner.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f4f7fa")), ("BOX", (0, 0), (-1, -1), 0.5, RULE), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    story = builder.build(parse_blocks(md))
    # put the banner right after the H1 title
    if story and isinstance(story[0], Paragraph):
        story = [story[0], banner, Spacer(1, 6)] + story[1:]
    else:
        story = [banner, Spacer(1, 6)] + story

    def footer(canv, d):
        canv.saveState()
        canv.setFont("DV", 7)
        canv.setFillColor(MUTED)
        canv.drawString(margin, 0.32 * inch, rel)
        canv.drawRightString(pagesize[0] - margin, 0.32 * inch, f"Page {d.page}")
        canv.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return out


def _title(src: Path) -> str:
    for ln in src.read_text(encoding="utf-8").splitlines():
        if ln.startswith("# "):
            return ln[2:]
    return src.stem


def main(argv: list[str]) -> None:
    register_fonts()
    selected = [r for r in TEMPLATES if not argv or any(a in r for a in argv)]
    if not selected:
        sys.exit(f"No template matches {argv}")
    for rel in selected:
        if not (REPO / rel).exists():
            print(f"MISSING  {rel}")
            continue
        out = build_pdf(rel, TEMPLATES[rel])
        print(f"wrote    {out.relative_to(REPO)}")


if __name__ == "__main__":
    main(sys.argv[1:])
