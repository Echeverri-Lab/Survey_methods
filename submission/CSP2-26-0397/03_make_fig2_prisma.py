#!/usr/bin/env python3
"""
Figure 2 for CSP2-26-0397: PRISMA-2020-style flow diagram for a
practice-focused review.

HOW TO USE
----------
1. Run the searches in 01_Search_Protocol_RUN_THIS_FIRST.md.
2. Edit the N dictionary below. Replace every None with your real count.
3. python3 03_make_fig2_prisma.py

While any value is None the script draws the diagram with visible "XX"
placeholders so you can check the layout before you have the numbers.
Once all values are filled it checks the arithmetic and refuses to draw
an internally inconsistent diagram -- unbalanced flow diagrams are one
of the most common things reviewers catch.

Outputs Fig2_PRISMA_flow.pdf (vector, for submission) and
Fig2_PRISMA_flow.png (for quick viewing).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ----------------------------------------------------------------------
# EDIT THIS BLOCK
# ----------------------------------------------------------------------
N = {
    # --- Identification: database searches ---
    "db_core":            None,  # records from the core Boolean search
    "db_topic":           None,  # records from the 11 topic-specific searches (combined)

    # --- Identification: other sources (counted separately) ---
    "oth_texts":          None,  # standard texts / handbooks
    "oth_citation":       None,  # backward + forward citation chasing
    "oth_standards":      None,  # reporting standards, guidelines, institutional docs
    "oth_team":           None,  # author-team corpus used as worked examples

    # --- Screening ---
    "duplicates":         None,  # duplicate records removed
    "screened":           None,  # records screened on title/abstract
    "excl_screen":        None,  # excluded at title/abstract
    "fulltext":           None,  # full texts assessed
    "excl_ft_notmethod":  None,  # excluded: not methodologically informative
    "excl_ft_nottransf":  None,  # excluded: no transferable guidance for ecology
    "excl_ft_superseded": None,  # excluded: superseded by newer/more authoritative source
    "excl_ft_unavail":    None,  # excluded: full text unavailable

    # --- Curation (the practice-focused layer) ---
    "eligible":           None,  # eligible after full-text assessment
    "not_prioritised":    None,  # eligible but not meeting any curation criterion

    # --- Included ---
    "included":           None,  # total sources included in the synthesis
    "cited_main":         None,  # of which cited in the main text
    "in_repo_tables":     None,  # of which catalogued in the repository living tables
}

# Set to your real screening tool / agreement stats, or leave as-is.
SCREENERS_NOTE = "Screened independently by two authors (20% subsample; κ = X.XX)"
# ----------------------------------------------------------------------


def v(key):
    """Return the count as a string, or 'XX' if not yet filled in."""
    val = N.get(key)
    return "XX" if val is None else f"{val:,}"


def check_arithmetic():
    """Validate internal consistency once all numbers are present."""
    if any(x is None for x in N.values()):
        missing = [k for k, x in N.items() if x is None]
        print(f"[draft mode] {len(missing)} placeholder(s) remaining: "
              f"{', '.join(missing)}")
        print("             Diagram drawn with 'XX'. Arithmetic not checked yet.\n")
        return

    problems = []

    identified = (N["db_core"] + N["db_topic"] + N["oth_texts"]
                  + N["oth_citation"] + N["oth_standards"] + N["oth_team"])

    if identified - N["duplicates"] != N["screened"]:
        problems.append(
            f"identified ({identified}) - duplicates ({N['duplicates']}) "
            f"= {identified - N['duplicates']}, but screened = {N['screened']}")

    if N["screened"] - N["excl_screen"] != N["fulltext"]:
        problems.append(
            f"screened ({N['screened']}) - excluded at screening "
            f"({N['excl_screen']}) = {N['screened'] - N['excl_screen']}, "
            f"but full texts assessed = {N['fulltext']}")

    ft_excl = (N["excl_ft_notmethod"] + N["excl_ft_nottransf"]
               + N["excl_ft_superseded"] + N["excl_ft_unavail"])
    if N["fulltext"] - ft_excl != N["eligible"]:
        problems.append(
            f"full texts ({N['fulltext']}) - full-text exclusions ({ft_excl}) "
            f"= {N['fulltext'] - ft_excl}, but eligible = {N['eligible']}")

    if N["eligible"] - N["not_prioritised"] != N["included"]:
        problems.append(
            f"eligible ({N['eligible']}) - not prioritised "
            f"({N['not_prioritised']}) = {N['eligible'] - N['not_prioritised']}, "
            f"but included = {N['included']}")

    if N["cited_main"] > N["included"]:
        problems.append(
            f"cited in main text ({N['cited_main']}) exceeds included "
            f"({N['included']})")

    if problems:
        raise SystemExit(
            "\nFLOW DIAGRAM DOES NOT BALANCE -- fix before submitting:\n  - "
            + "\n  - ".join(problems)
            + "\n\nReviewers check these sums. So does the editorial office.\n")

    print(f"[ok] Arithmetic balances. {identified:,} identified -> "
          f"{N['included']:,} included.\n")


# --- styling: greyscale-safe, CSP-friendly ---------------------------------
INK      = "#1a1a1a"
BOX_ID   = "#e8eef3"   # identification
BOX_SCR  = "#f2f0e8"   # screening
BOX_CUR  = "#e6efe8"   # curation
BOX_INC  = "#d9e4ec"   # included
BOX_EXCL = "#f7f7f7"   # exclusions (side boxes)
EDGE     = "#5a6b78"

FS_BOX   = 7.4
FS_STAGE = 8.6


def box(ax, x, y, w, h, text, fc, fontsize=FS_BOX, weight="normal",
        style="round,pad=0.012,rounding_size=0.012", ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style,
                                linewidth=0.9, edgecolor=EDGE,
                                facecolor=fc, linestyle=ls, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color=INK, zorder=3, linespacing=1.45,
            fontweight=weight)


def arrow(ax, xy_from, xy_to, style="-|>"):
    ax.add_patch(FancyArrowPatch(xy_from, xy_to, arrowstyle=style,
                                 mutation_scale=9, linewidth=0.9,
                                 color=EDGE, shrinkA=0, shrinkB=0, zorder=1))


def stage_label(ax, y, text, color):
    """Vertical stage band down the left-hand side."""
    ax.add_patch(FancyBboxPatch((0.012, y[0]), 0.052, y[1] - y[0],
                                boxstyle="round,pad=0.004,rounding_size=0.010",
                                linewidth=0.9, edgecolor=EDGE,
                                facecolor=color, zorder=2))
    ax.text(0.038, (y[0] + y[1]) / 2, text, ha="center", va="center",
            fontsize=FS_STAGE, color=INK, rotation=90, fontweight="bold",
            zorder=3)


def build():
    check_arithmetic()

    fig, ax = plt.subplots(figsize=(7.4, 9.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    LX, LW = 0.095, 0.50       # main column x / width
    RX, RW = 0.635, 0.352      # right-hand (exclusions) column

    # ---------------- IDENTIFICATION ----------------
    stage_label(ax, (0.782, 0.978), "Identification", BOX_ID)

    box(ax, LX, 0.885, LW, 0.088,
        f"Records identified from databases\n"
        f"Core Boolean search  (n = {v('db_core')})\n"
        f"11 topic-specific searches  (n = {v('db_topic')})",
        BOX_ID)

    box(ax, RX, 0.885, RW, 0.088,
        f"Records identified from other sources\n"
        f"Standard texts & handbooks  (n = {v('oth_texts')})\n"
        f"Citation chasing  (n = {v('oth_citation')})\n"
        f"Reporting standards & guidelines  (n = {v('oth_standards')})\n"
        f"Author-team corpus  (n = {v('oth_team')})",
        BOX_ID, fontsize=6.5)

    box(ax, LX, 0.790, LW, 0.048,
        f"Duplicate records removed\n(n = {v('duplicates')})",
        BOX_EXCL, ls="--")

    arrow(ax, (LX + LW / 2, 0.885), (LX + LW / 2, 0.838))
    arrow(ax, (RX + RW / 2, 0.885), (RX + RW / 2, 0.706))

    # ---------------- SCREENING ----------------
    stage_label(ax, (0.442, 0.772), "Screening", BOX_SCR)

    box(ax, LX, 0.658, LW, 0.048,
        f"Records screened on title and abstract\n(n = {v('screened')})",
        BOX_SCR)
    arrow(ax, (LX + LW / 2, 0.790), (LX + LW / 2, 0.706))

    box(ax, RX, 0.658, RW, 0.048,
        f"Excluded at title/abstract\n(n = {v('excl_screen')})",
        BOX_EXCL, ls="--")
    arrow(ax, (LX + LW, 0.682), (RX, 0.682))

    box(ax, LX, 0.556, LW, 0.048,
        f"Full-text records assessed for eligibility\n(n = {v('fulltext')})",
        BOX_SCR)
    arrow(ax, (LX + LW / 2, 0.658), (LX + LW / 2, 0.604))

    box(ax, RX, 0.522, RW, 0.116,
        f"Excluded at full text, with reasons\n"
        f"Not methodologically informative  (n = {v('excl_ft_notmethod')})\n"
        f"No transferable guidance for ecological\ncontexts  (n = {v('excl_ft_nottransf')})\n"
        f"Superseded by newer/more authoritative\nsource  (n = {v('excl_ft_superseded')})\n"
        f"Full text unavailable  (n = {v('excl_ft_unavail')})",
        BOX_EXCL, fontsize=6.7, ls="--")
    arrow(ax, (LX + LW, 0.580), (RX, 0.580))

    box(ax, LX, 0.452, LW, 0.048,
        f"Records eligible for synthesis\n(n = {v('eligible')})",
        BOX_SCR)
    arrow(ax, (LX + LW / 2, 0.556), (LX + LW / 2, 0.500))

    # ---------------- CURATION ----------------
    stage_label(ax, (0.322, 0.432), "Curation", BOX_CUR)

    box(ax, LX, 0.330, LW, 0.098,
        "Curation against prespecified criteria\n"
        "(retained if ≥ 1 criterion met)\n\n"
        "C1  Methodological influence\n"
        "C2  Direct transferability to ecological contexts\n"
        "C3  Illustration of a specific technique",
        BOX_CUR, fontsize=6.9)
    arrow(ax, (LX + LW / 2, 0.452), (LX + LW / 2, 0.428))

    box(ax, RX, 0.338, RW, 0.082,
        f"Eligible but not prioritised\n(n = {v('not_prioritised')})\n\n"
        f"Met no curation criterion;\nlisted in Supplementary Table S2",
        BOX_EXCL, fontsize=6.7, ls="--")
    arrow(ax, (LX + LW, 0.379), (RX, 0.379))

    # ---------------- INCLUDED ----------------
    stage_label(ax, (0.062, 0.216), "Included", BOX_INC)

    box(ax, LX, 0.148, LW, 0.058,
        f"Sources included in the synthesis\n(n = {v('included')})",
        BOX_INC, weight="bold", fontsize=8.0)
    arrow(ax, (LX + LW / 2, 0.330), (LX + LW / 2, 0.206))

    box(ax, LX, 0.070, 0.235, 0.058,
        f"Cited in main text\n(n = {v('cited_main')})", BOX_INC)
    box(ax, LX + 0.265, 0.070, 0.235, 0.058,
        f"Catalogued in repository\nliving tables (n = {v('in_repo_tables')})",
        BOX_INC)
    arrow(ax, (LX + 0.117, 0.148), (LX + 0.117, 0.128))
    arrow(ax, (LX + 0.382, 0.148), (LX + 0.382, 0.128))

    box(ax, RX, 0.148, RW, 0.058,
        "Mapped to the 12 workflow steps\n(per-step counts in\nSupplementary Table S3)",
        BOX_INC, fontsize=6.9)
    arrow(ax, (LX + LW, 0.177), (RX, 0.177))

    # footer note
    ax.text(0.5, 0.040, SCREENERS_NOTE, ha="center", va="bottom",
            fontsize=6.4, color="#666666", style="italic")

    fig.savefig("Fig2_PRISMA_flow.pdf", bbox_inches="tight",
                pad_inches=0.06)
    fig.savefig("Fig2_PRISMA_flow.png", dpi=400, bbox_inches="tight",
                pad_inches=0.06, facecolor="white")
    print("Wrote Fig2_PRISMA_flow.pdf and Fig2_PRISMA_flow.png")


if __name__ == "__main__":
    build()
