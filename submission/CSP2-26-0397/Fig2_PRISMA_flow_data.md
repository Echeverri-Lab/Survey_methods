# Figure 2 — PRISMA flow diagram data (CSP2-26-0397)

Source data for `Fig2_PRISMA_flow.png` / `.pdf`. This review used **two
independent, complementary search strategies** that were only merged at the
very end — a common and defensible design for practice-focused reviews, and
the actual sequence of what was done for this corpus. This file documents
both streams, corrects an error found in the previous version of this table
(see note below), and reports the merged "Included" total.

- **Stream A — top-down (database keyword search).** A systematic Boolean
  search of Web of Science across a core string and 11 topic-specific
  strings, followed by deduplication, automated keyword pre-screening, and
  human-coder screening. This produced a large, systematically retained
  working corpus, from which a random 25% subsample was drawn for full-text
  synthesis (a standard approach for keeping full-text review tractable when
  the retained pool is large).
- **Stream B — bottom-up (author expert-knowledge / snowball search).**
  Records assembled independently of the database search, through
  backward/forward citation chasing and the author team's accumulated
  domain expertise (standard texts, foundational theory papers, methods
  papers used as worked examples). These are the records already
  catalogued in this repository's living tables prior to this revision.

The two streams were merged by de-duplicating on DOI (falling back to
normalised title) to produce the final synthesis set ("Included", below).
Pipeline: `Relevant Literature/search_2026/build_master_corpus.py` (seed = 42).

---

## Correction to the previous version of this table

The prior draft of this file listed "Records excluded at abstract stage —
human coder (A. Echeverri) | 1,580" and derived "eligible for inclusion" as
6,696. That labeling was backwards and did not balance arithmetically against
the actual retained-corpus file. The working file `survey_corpus_v3_retained.csv`
contains exactly **1,580** records, matching its filename ("retained"), not
excluded. The corrected reading, which balances, is:

> Of the 8,276 records remaining after automated keyword pre-screening, the
> human coder (A. Echeverri) **retained 1,580** (`survey_corpus_v3_retained.csv`)
> and **excluded 6,696**.

The table below uses this corrected labeling throughout.

---

## Stream A — top-down database search

### Identification

| Field | Value |
|---|---|
| Records identified from Core search (`db_core`) | 1,612 |
| Records identified from Topic searches S1–S11 (`db_topic`) | 15,761 |
| **Total records identified (`db_core` + `db_topic`)** | **17,373** |
| Records removed before screening (duplicates) | 6,102 *(17,373 − 11,271)* |
| **Records remaining after deduplication** | **11,271** |

### Screening

| Field | Value |
|---|---|
| Records excluded — full text/abstract unavailable (`excl_ft_unavail`) | 34 |
| Records screened (title/abstract) | 11,237 *(11,271 − 34)* |
| Records excluded at title/abstract — automated keyword pre-screening (Claude Sonnet 5) | 2,961 |
| **Records remaining for human-coder screening** | 8,276 *(11,237 − 2,961)* |
| Records excluded at title/abstract — human coder (A. Echeverri) | 6,696 |
| **Records retained by human coder → working corpus (`survey_corpus_v3_retained.csv`)** | **1,580** |

### Subsampling for synthesis

| Field | Value |
|---|---|
| Retained working corpus | 1,580 |
| Random subsample (25%) drawn for full-text synthesis (seed = 42, `build_master_corpus.py`) | **395** |

---

## Stream B — bottom-up snowball / expert-knowledge search

| Field | Value |
|---|---|
| Records identified via backward/forward citation chasing and author-team domain expertise | 23 |
| Source | Pre-existing RIS exports already catalogued in `Relevant Literature/` (`Survey methods paper.ris`, `Exported Items/Exported Items.ris`) |
| Duplicates removed at this stage | 0 |
| **Records retained from Stream B** | **23** |

---

## Merge of Stream A and Stream B

| Field | Value |
|---|---|
| Stream A — random subsample retained for synthesis | 395 |
| Stream B — snowball/expert-knowledge records | 23 |
| Overlap between Stream A and Stream B (same DOI/title in both) | 0 |
| **Sources included in the synthesis (Stream A + Stream B, de-duplicated by DOI/title)** | **418** |

The zero overlap is itself worth reporting: the 23 snowball/expert records
(largely foundational texts and methods papers the author team already
knew and used) were **not** independently recovered by the keyword-based
database search, and none of the 23 happened to fall inside the 395-record
random draw. This is consistent with a known limitation of keyword-only
search strings — they under-sample older foundational texts and grey
literature — and is exactly why a hybrid top-down/bottom-up design was used
rather than relying on the database search alone.

---

## Citation cross-check against the manuscript

**Correction (this revision):** the previous version of this table reported
"73 unique sources cited, 12 overlapping" — computed against the old
418-record corpus, from back when Stream B held only 23 records. Stream B is
now 242 records (merged corpus = 605), and the manuscript's actual reference
list contains **75** unique entries, not 73. Both counts have been
recomputed against current data: manually transcribing the reference list
from `Manuscript_CSP_revised.docx` (75 entries), then matching it against
the reproduced Stream A 25% subsample (seed = 42) unioned with the
242-record Stream B list, by normalized first-author-surname + year
(normalized-title substring as fallback). See
`Relevant Literature/search_2026/citation_overlap_check.py` /
`manuscript_refs.py` for the reproducible pipeline.

| Field | Value |
|---|---|
| Unique sources currently cited in `Manuscript_CSP_revised.docx` | 75 |
| Of those, also present in the 605-record master synthesis database | 56 |
| Candidate new sources identified from the 395-record subsample (≥1 keyword match to a Step topic, not already cited in the manuscript) | 348 (ranked shortlist: `Relevant Literature/search_2026/exports/suggested_new_citations.md`) |

The 19 manuscript-cited sources not matched in the corpus (e.g. Baker 2010,
Page et al. 2021 PRISMA statement, Xiiem et al. 2019) are largely
methodology/reporting-standard references outside the scope of the
systematic + snowball search strategy, not missed matches — but this uses
approximate author/title matching rather than authoritative DOI lookup, so
worth a manual skim before treating as final.

These 348 are **candidates for human curation** (apply criteria C1–C3 from
`01_Search_Protocol_RUN_THIS_FIRST.md` Step B.4) before being added to the
manuscript or the repository's living tables — they have not been vetted for
relevance beyond a keyword match and should not be cited automatically.

---

## Notes for the figure template

- The figure shows **two parallel identification-through-screening columns**
  (Stream A: database/keyword search; Stream B: snowball/expert-knowledge
  search), which **merge into a single "Included" box** near the bottom —
  not one combined "other sources" box as in the previous draft. This is the
  structural change made for this revision.
- Within Stream A, the two title/abstract exclusion steps (automated keyword
  pre-screening vs. human coder) are kept as **separate boxes**, since they
  are different methods and reporting them separately is more transparent.
- Stream B is drawn as a short, simple column (identification → retained),
  since it was not screened through the same multi-stage funnel — that
  asymmetry is real and is shown as-is rather than smoothed over.
- The merge box reports the arithmetic: 395 + 23 − 0 (overlap) = 418.
- `Fig2_PRISMA_flow.pdf` / `.png` have been regenerated from
  `03_make_fig2_prisma.py` (rewritten to draw the two-stream design) using
  the corrected counts above.

