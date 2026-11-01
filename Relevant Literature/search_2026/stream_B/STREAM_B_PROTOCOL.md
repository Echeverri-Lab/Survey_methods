# Stream B protocol (supplementary search, 2026 rebuild)

**Status: APPROVED as drafted, 2026-11-01.**

## Amendment and run log

| Date | Entry |
|---|---|
| 2026-11-01 | Protocol approved as drafted. Decisions 1 (seed set) and 4 (theory sources outside count) accepted as proposed. Decisions 2 (syllabi) and 3 (second screener) still open. |
| 2026-11-01 | B3 run. Seed DOIs verified in OpenAlex: Kyle et al. 2020 = 10.1111/cobi.13625; Eyster et al. 2025 = 10.1111/cobi.14461, titled "Use of theories of human action in recent conservation research" (the repository cites a wrong DOI). OpenAlex now requires an API key for cursor paging, so page-based paging was used (no effect on results). 9,117 unique records; see `b3_report.md`. |
| 2026-11-01 | `../screening_log.csv` created with B1 (18), B2 externally nominated (8), B3 (9,117), and B4 (10) rows. Screening not started. |
| 2026-11-01 | Eligibility and curation criteria approved (I1–I5; exclusion codes not_human_survey, application_only, instrument_out_of_domain, not_english, wrong_doc_type, duplicate; curation C1–C4). This replaces §2.1 of the submitted manuscript for all screening. Screening workbook regenerated with these codes. |
| 2026-11-01 | Screening starts with one screener (AE). The 20% dual-screening sample is drawn now (`flag_dual_sample.py`, seed 2026) and flagged in the log, so a second screener added later checks a sample fixed in advance. If no second screener is added, report single screening as a limitation. |
| 2026-11-01 | **Pre-screen rule fixed before any human screening (option B in `b3_report.md`):** (1) records of unscreenable OpenAlex document types are excluded; (2) records reached *only* as forward citations of Boateng et al. 2018 are screened only if they are a review, book, or book chapter, or their title contains a guidance term. Applied by `prescreen_b3.py`, decisions marked "auto:" in the log. Result: 207 + 5,193 excluded automatically; **3,717 to human screening** (769 without abstract; 33 already in Stream A or the legacy list). |

## Why a rebuild

The original Stream B was "every reference cited in the repository" (n=242). As `stream_b_summary.md` shows, that list:
- has no record of *how* sources were identified;
- mixes methodological guidance with theory primary sources (90 entries) and worked examples (33);
- contains duplicates, placeholders, and entries whose details conflict with the real publication.

The Table S2 breakdown (45 / 112 / 62 / 23) cannot be reproduced from any file. A documented Stream B should surface the standard sources (AAPOR, ESOMAR/WAPOR, Brown's CFA text, parent-discipline handbooks) and follow ROSES-style transparency.

The rebuilt Stream B is a **supplementary search**, run and logged prospectively. It sits alongside the re-run database search (Stream A) and goes through the **same eligibility and curation criteria and the same screening log**.



## Components

Each component writes rows to `../screening_log.csv`, with `source` set to the component code below.

### B1 — Reporting standards and institutional guidance (`standards`)
A fixed list of named sources, each checked once, logging the version and the date accessed:

- **Survey / opinion research:** AAPOR *Standard Definitions* (current edition); AAPOR *Code of Professional Ethics and Practices* and Transparency Initiative disclosure elements; ESOMAR/WAPOR *Guideline on Opinion Polls and Published Surveys*.
- **Reporting:** EQUATOR Network library (surveys, qualitative research); APA JARS-Quant and JARS-Qual; CHERRIES; COREQ; SRQR.
- **Evidence synthesis:** PRISMA 2020; PRISMA-ScR; ROSES; Collaboration for Environmental Evidence guidelines.
- **Ethics and data:** CARE; FAIR; TCPS 2 (Canada); the Belmont Report / Common Rule (US).
- Anything else the authors nominate, with a one-line justification.

### B2 — Standard texts and handbooks (`texts`)
Built from three logged sources:

1. **Graduate syllabi.** Name each syllabus used (course, institution, year), including the authors' own courses. Record every survey-methods or psychometrics text assigned.
2. **Externally nominated texts:**
   - Vaske 2019
   - Fink 2003
   - Johnson & Morgan 2016
   - Ford & Scandura 2023
   - Lam & Green 2023
   - Irwing et al. 2018
   - Dillman, Smyth & Christian 2014
   - Brown 2015 (*Confirmatory Factor Analysis for Applied Research*)
3. **Expert nomination.** Each author nominates texts independently, before seeing the others' lists. Log the nominator and the rationale. Reporting the overlap between nominators gives a simple check on selection bias.

### B3 — Citation chasing (`citation_chasing`)
- **Seed set (proposed; authors to confirm):** Kyle et al. 2020; Whitehouse-Tedd et al. 2021; Wardropper et al. 2021; Moon & Blackman 2014; Moon et al. 2018; Boateng et al. 2018; Ghasemi et al. 2026; Bennett et al. 2017; Teel & Manfredo 2010; Eyster et al. 2025.
- **One round** of backward chasing (the seeds' reference lists) and forward chasing (works citing the seeds), retrieved via the OpenAlex API. Log the query date and the OpenAlex work IDs so it can be reproduced.
- Each retrieved record is screened on title and abstract against the same eligibility criteria as Stream A.

### B4 — Author-team worked examples (`team_corpus`)
The team's own studies, used as illustrations (e.g., Figure 3, Table 1). Logged and **labelled as worked examples, not as evidence** for guidance, so the synthesis counts are not inflated by self-citation.

### Outside the synthesis count: theory primary sources (`theory_background`)
Primary sources for the theories listed in `Step_02/theory_summary.md` (e.g., Ajzen 1991; Schwartz 1992) are cited to define theories, not as survey-methods guidance. Log them, but report them in a separate box of the flow diagram ("sources cited for context") rather than in the synthesis set.

## Screening and curation

- Same eligibility criteria (§2.3 of the revised Methods) and curation criteria (§2.4) as Stream A.
- **Dual screening:** a second author independently screens a random 20% of Stream B records at title/abstract stage. Report agreement (Cohen's κ), and resolve disagreements by discussion.
- Every decision goes in `screening_log.csv`. Flow-diagram counts are computed by `count_from_log.py`, never typed by hand.

## Carried over from the old list

The 238 unique works in `stream_b_reconciled.csv` are a candidate pool, not an included set. Each enters the new log under whichever component actually describes how it was found, then goes through screening like any other record. Before that:

- **suspect** entries (11) are checked against the source. They are corrected if the work exists, or removed from the repository if it does not.
- **placeholders** (28) get a full citation or are removed.
- **duplicates** (4) are merged.
- **fix_metadata** entries (13) are corrected.

## Decisions needed from the authors

1. Approve or edit the B3 seed set.
2. Which syllabi go into B2?
3. Who is the second screener?
4. Should theory primary sources be kept outside the synthesis count (recommended)?
