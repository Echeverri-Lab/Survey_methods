#!/usr/bin/env python3
"""
Figure 2 for CSP2-26-0397: two-stream PRISMA-style flow diagram for a
practice-focused review.

DESIGN
------
This review used two independent search strategies, merged only at the end:

  Stream A (top-down)  — database keyword search -> dedup -> automated
                          keyword pre-screening -> human-coder screening ->
                          retained working corpus -> random 25% subsample.
  Stream B (bottom-up) — backward/forward citation chasing + author-team
                          expert domain knowledge -> records already
                          catalogued in the repository's living tables.

The two streams are drawn as parallel columns and merge into a single
"Included" box. See Fig2_PRISMA_flow_data.md for the full numbers, the
correction note, and interpretation.

HOW TO USE
----------
Edit the N dictionary below if any counts change, then:
    python3 03_make_fig2_prisma.py
The script checks that each stream's arithmetic balances and refuses to draw
an internally inconsistent diagram.

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
    # --- Stream A: top-down database search ---
    "db_core":            1612,
    "db_topic":           15761,
    "duplicates":         6102,
    "excl_ft_unavail":    34,
    "excl_auto":          2961,   # excluded at title/abstract, automated keyword pre-screen
    "excl_human":         6696,   # excluded at title/abstract, human coder
    "retained_corpus":    1580,   # survey_corpus_v3_retained.csv
    "sample_a":           395,    # random 25% subsample drawn for synthesis

    # --- Stream B: bottom-up snowball / expert-knowledge search ---
    # All unique references cited across the repository's Step 00-12 living
    # documents, extracted programmatically from every "## References" /
    # "## Full Reference List" / inline "*References:*" section repo-wide
    # (see Relevant Literature/search_2026/exports/master_reference_list_all_steps.md).
    "stream_b":           242,    # citation chasing + author-team domain expertise

    # --- Merge ---
    "overlap_ab":         32,     # records present in both streams (matched by DOI
                                   # against the Stream A 395-record subsample)
    "included":           605,    # sample_a + stream_b - overlap_ab

    # --- Included breakdown ---
    # Recomputed via Relevant Literature/search_2026/citation_overlap_check.py:
    # matches the manuscript's actual reference list (75 entries, not the
    # previously assumed 73) against the reproduced Stream A subsample
    # (seed=42) unioned with the 242-record Stream B list, by normalized
    # first-author-surname + year (title-substring fallback). This replaces
    # the stale "12 of 73" figure computed against the old 418-record corpus.
    "cited_main":         75,     # unique sources cited in Manuscript_CSP_revised.docx
    "cited_and_in_corpus": 56,    # of those, also present in the 605-record synthesis corpus
    "in_repo_tables":     242,    # catalogued in repository living tables (= Stream B)
}

SCREENERS_NOTE = ("Stream A screened by automated keyword pre-screening (Claude Sonnet 5) "
                   "then a single human coder (A. Echeverri); Stream B compiled by the author "
                   "team via citation chasing and domain expertise.")
# ----------------------------------------------------------------------


def v(key):
    val = N.get(key)
    return "XX" if val is None else f"{val:,}"


def check_arithmetic():
    if any(x is None for x in N.values()):
        missing = [k for k, x in N.items() if x is None]
        print(f"[draft mode] {len(missing)} placeholder(s) remaining: {', '.join(missing)}")
        print("             Diagram drawn with 'XX'. Arithmetic not checked yet.\n")
        return

    problems = []

    identified_a = N["db_core"] + N["db_topic"]
    after_dedup = identified_a - N["duplicates"]
    if after_dedup != 11271:
        problems.append(f"Stream A after dedup = {after_dedup}, expected 11,271")

    screened = after_dedup - N["excl_ft_unavail"]
    after_auto = screened - N["excl_auto"]
    retained = after_auto - N["excl_human"]
    if retained != N["retained_corpus"]:
        problems.append(
            f"Stream A: {after_auto} remaining after auto pre-screen − "
            f"{N['excl_human']} excluded by human coder = {retained}, "
            f"but retained_corpus = {N['retained_corpus']}")

    merged = N["sample_a"] + N["stream_b"] - N["overlap_ab"]
    if merged != N["included"]:
        problems.append(
            f"sample_a ({N['sample_a']}) + stream_b ({N['stream_b']}) − "
            f"overlap ({N['overlap_ab']}) = {merged}, but included = {N['included']}")

    if N["in_repo_tables"] > N["included"]:
        problems.append("in_repo_tables exceeds included")

    if N["cited_and_in_corpus"] > N["cited_main"]:
        problems.append("cited_and_in_corpus exceeds cited_main")

    if problems:
        raise SystemExit(
            "\nFLOW DIAGRAM DOES NOT BALANCE -- fix before submitting:\n  - "
            + "\n  - ".join(problems) + "\n")

    print(f"[ok] Both streams balance. Stream A retained {N['retained_corpus']:,} -> "
          f"sampled {N['sample_a']:,}. Stream B = {N['stream_b']:,}. "
          f"Merged included = {N['included']:,}.\n")


# --- styling ---------------------------------------------------------------
INK      = "#1a1a1a"
BOX_A    = "#e8eef3"   # Stream A identification/screening
BOX_B    = "#f3ece3"   # Stream B identification
BOX_INC  = "#d9e4ec"   # Included / merge
BOX_EXCL = "#f7f7f7"   # exclusions (side boxes)
EDGE     = "#5a6b78"

FS_BOX   = 7.0
FS_STAGE = 8.2


def box(ax, x, y, w, h, text, fc, fontsize=FS_BOX, weight="normal",
        style="round,pad=0.010,rounding_size=0.010", ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style,
                                linewidth=0.9, edgecolor=EDGE,
                                facecolor=fc, linestyle=ls, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color=INK, zorder=3, linespacing=1.4,
            fontweight=weight)


def arrow(ax, xy_from, xy_to, style="-|>"):
    ax.add_patch(FancyArrowPatch(xy_from, xy_to, arrowstyle=style,
                                 mutation_scale=8.5, linewidth=0.9,
                                 color=EDGE, shrinkA=0, shrinkB=0, zorder=1))


def col_label(ax, x, w, y, text, color, fontsize=FS_STAGE):
    n_lines = text.count("\n") + 1
    h = 0.030 if n_lines == 1 else 0.030 + 0.024 * (n_lines - 1)
    ax.add_patch(FancyBboxPatch((x, y - (h - 0.030)), w, h,
                                boxstyle="round,pad=0.004,rounding_size=0.008",
                                linewidth=0.9, edgecolor=EDGE,
                                facecolor=color, zorder=2))
    ax.text(x + w / 2, y - (h - 0.030) + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color=INK, fontweight="bold", zorder=3, linespacing=1.3)


def build():
    check_arithmetic()

    fig, ax = plt.subplots(figsize=(8.2, 10.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Two columns: A (left, wide, multi-stage) and B (right, narrow, simple)
    AX, AW = 0.045, 0.560
    BX, BW = 0.650, 0.320

    col_label(ax, AX, AW, 0.960, "Stream A — top-down database (keyword) search", BOX_A, fontsize=7.2)
    col_label(ax, BX, BW, 0.960, "Stream B — bottom-up\nsnowball / expert search", BOX_B, fontsize=6.6)

    # ---------------- Stream A ----------------
    box(ax, AX, 0.888, AW, 0.058,
        f"Records identified from databases\n"
        f"Core Boolean search (n = {v('db_core')})  +  "
        f"11 topic searches (n = {v('db_topic')})",
        BOX_A)
    arrow(ax, (AX + AW / 2, 0.888), (AX + AW / 2, 0.850))

    box(ax, AX, 0.812, AW * 0.62, 0.036,
        f"Records after dedup (n = 11,271)", BOX_A)
    box(ax, AX + AW * 0.68, 0.812, AW * 0.32, 0.036,
        f"Duplicates removed\n(n = {v('duplicates')})", BOX_EXCL, ls="--", fontsize=6.4)
    arrow(ax, (AX + AW * 0.31, 0.850), (AX + AW * 0.31, 0.848))

    box(ax, AX, 0.750, AW * 0.62, 0.036,
        f"Screened title/abstract\n(minus {v('excl_ft_unavail')} unavailable) (n = 11,237)",
        BOX_A, fontsize=6.6)
    arrow(ax, (AX + AW * 0.31, 0.812), (AX + AW * 0.31, 0.786))

    box(ax, AX, 0.688, AW * 0.62, 0.036,
        f"Remaining after automated\nkeyword pre-screen (n = 8,276)",
        BOX_A, fontsize=6.6)
    box(ax, AX + AW * 0.68, 0.688, AW * 0.32, 0.036,
        f"Excluded — automated\npre-screen (n = {v('excl_auto')})",
        BOX_EXCL, ls="--", fontsize=6.2)
    arrow(ax, (AX + AW * 0.31, 0.750), (AX + AW * 0.31, 0.724))

    box(ax, AX, 0.610, AW * 0.62, 0.052,
        f"Retained by human coder\n(working corpus, "
        f"survey_corpus_v3_retained.csv)\n(n = {v('retained_corpus')})",
        BOX_A, fontsize=6.6, weight="bold")
    box(ax, AX + AW * 0.68, 0.610, AW * 0.32, 0.052,
        f"Excluded — human coder\n(A. Echeverri)\n(n = {v('excl_human')})",
        BOX_EXCL, ls="--", fontsize=6.2)
    arrow(ax, (AX + AW * 0.31, 0.688), (AX + AW * 0.31, 0.662))

    box(ax, AX, 0.534, AW * 0.62, 0.052,
        f"Random 25% subsample drawn\nfor full-text synthesis\n(seed = 42)\n(n = {v('sample_a')})",
        BOX_A, fontsize=6.6, weight="bold")
    arrow(ax, (AX + AW * 0.31, 0.610), (AX + AW * 0.31, 0.586))

    # ---------------- Stream B ----------------
    box(ax, BX, 0.888, BW, 0.058,
        "Records identified via\nbackward/forward citation chasing\n"
        "and author-team domain expertise",
        BOX_B, fontsize=6.6)
    arrow(ax, (BX + BW / 2, 0.888), (BX + BW / 2, 0.586))

    box(ax, BX, 0.534, BW, 0.052,
        f"Retained\n(catalogued in repository\nliving tables)\n(n = {v('stream_b')})",
        BOX_B, fontsize=6.6, weight="bold")

    # ---------------- Merge ----------------
    arrow(ax, (AX + AW * 0.31, 0.534), (0.42, 0.454))
    arrow(ax, (BX + BW / 2, 0.534), (0.46, 0.454))

    box(ax, 0.245, 0.396, 0.470, 0.052,
        f"Merge (de-duplicate by DOI/title)\n"
        f"{v('sample_a')} + {v('stream_b')} − {v('overlap_ab')} overlap",
        BOX_INC, fontsize=6.8)
    arrow(ax, (0.480, 0.396), (0.480, 0.334))

    box(ax, 0.245, 0.270, 0.470, 0.058,
        f"Sources included in the synthesis\n(n = {v('included')})",
        BOX_INC, weight="bold", fontsize=8.4)
    arrow(ax, (0.480, 0.270), (0.480, 0.220))

    box(ax, 0.145, 0.150, 0.685, 0.070,
        f"Unique sources currently cited in Manuscript_CSP_revised.docx (n = {v('cited_main')})\n"
        f"Of those {v('cited_main')}, also present in the {v('included')}-record synthesis corpus (n = {v('cited_and_in_corpus')})\n"
        f"Candidate new sources from Stream A's subsample not yet cited (shortlist, unvetted) (n = 348)",
        BOX_EXCL, fontsize=6.6)

    # footer note
    ax.text(0.5, 0.055, SCREENERS_NOTE, ha="center", va="bottom",
            fontsize=6.2, color="#666666", style="italic", wrap=True)
    ax.text(0.5, 0.025,
            "Stream A and Stream B were searched independently; 32 records were "
            "identified independently by both streams (matched by DOI) and are "
            "counted once in the merged Included total.",
            ha="center", va="bottom", fontsize=6.2, color="#666666", style="italic")

    fig.savefig("Fig2_PRISMA_flow.pdf", bbox_inches="tight", pad_inches=0.06)
    fig.savefig("Fig2_PRISMA_flow.png", dpi=400, bbox_inches="tight",
                pad_inches=0.06, facecolor="white")
    print("Wrote Fig2_PRISMA_flow.pdf and Fig2_PRISMA_flow.png")


if __name__ == "__main__":
    build()
