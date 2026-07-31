# search_2026 — search and screening audit trail

This folder is the archive location cited in the manuscript Methods for the
literature search underlying Figure 2 (PRISMA-style flow diagram) and the
practice-focused curation described there. It exists because a search cannot
be judged reproducible if its only trace is a paragraph of prose — everything
here is the primary record the paragraph summarizes.

See `01_Search_Protocol_RUN_THIS_FIRST.md` (in `submission/CSP2-26-0397/`) for
the full protocol this folder implements.

## Contents

- **`search_strings.md`** — every Boolean search string used (the core
  Web of Science search and the eleven topic-specific searches S1–S11),
  verbatim, with fields for the database, coverage dates, limits, execution
  date, and records retrieved for each. Fill these in as each search is run.

- **`screening_log_TEMPLATE.csv`** — one row per record identified from any
  source (database searches, standard texts, citation chasing, reporting
  standards, or the author-team corpus). Tracks each record from
  identification through deduplication, title/abstract screening, full-text
  assessment, and curation, ending in whether it was included in the
  synthesis. Copy this to `screening_log.csv` in this same folder and fill it
  in as screening proceeds — do not edit the template in place.

- **`exports/`** — raw RIS/BibTeX export files from each database search
  (e.g. `wos_core.ris`, `wos_S1.ris`, ...). One file per search string, named
  to match the row it corresponds to in `search_strings.md`.

- **`count_from_log.py`** — reads `screening_log.csv` and computes every
  value in the `N` dictionary at the top of `03_make_fig2_prisma.py` directly
  from the log, so the flow-diagram counts are derived rather than tallied by
  hand and re-typed. Run it after the log is complete (or partially complete)
  and paste its output into `N`.

## Why this matters

CSP permits practice-focused reviews built on "a clearly defined and
carefully curated body of findings," but requires that curation be explicit
and documented — "a PRISMA flow diagram or equivalent." The flow diagram is
only as trustworthy as the log it's drawn from. Keeping the log in the repo,
alongside the raw exports, means the counts in Figure 2 and the Methods text
are checkable against a primary record rather than taken on faith.

## Workflow

1. Run each search in `search_strings.md`, export results to `exports/`, and
   fill in the blank fields (database, dates, limits, n retrieved).
2. Copy `screening_log_TEMPLATE.csv` to `screening_log.csv` and populate it
   as records move through deduplication, screening, full-text assessment,
   and curation.
3. Run `python3 count_from_log.py` and paste the printed dict into the `N`
   block at the top of `../../submission/CSP2-26-0397/03_make_fig2_prisma.py`
   (or wherever that script currently lives).
4. Regenerate the figure and copy the resulting counts into the Methods
   section.
