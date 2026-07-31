# Literature Search Protocol — CSP2-26-0397
## Run this to generate the counts the editor is asking for

**Why this exists:** the editorial office returned the manuscript because the Methods paragraph names Web of Science and four search terms but gives no database coverage dates, no reproducible Boolean string, no screening counts, and no flow diagram. CSP explicitly permits *practice-focused* reviews built on "a clearly defined and carefully curated body of findings" — but it requires that the curation be explicit and documented with "a PRISMA flow diagram or equivalent." So the framing does not need to change. The audit trail does.

The repository (`Echeverri-Lab/Survey_methods`) currently holds 62 PDFs and two RIS exports totalling 23 unique records, but no search log. Reconstructing the numbers post hoc from those files would not be defensible. Re-run the search below, record the counts, and everything else in this folder fills in from them.

---

## Step A — Run the core database search

Search **Web of Science Core Collection** (and, recommended, **Scopus** — reviewers frequently ask why only one database was used; a second database is cheap insurance and lets you report duplicate removal honestly).

Log in through Berkeley's subscription, select **Topic (TS=)** as the field, and paste the string exactly.

### Core search string

```
TS=(
  (survey* OR questionnaire* OR "opinion poll*" OR psychometric*
   OR "scale development" OR "scale validation" OR "measurement invariance"
   OR "Likert")
  AND
  ("human dimensions" OR "conservation social science" OR "environmental psychology"
   OR "conservation psychology" OR "socio-ecological" OR "social-ecological"
   OR "socio-environmental" OR conservation OR biodiversity OR ecolog*)
  AND
  (method* OR design OR validity OR reliability OR "best practice*"
   OR guideline* OR review OR framework)
)
```

Apply these limits and **write down what you set**:

| Parameter | Value to record |
|---|---|
| Database(s) and edition(s) | e.g. Web of Science Core Collection (SCI-EXPANDED, SSCI, A&HCI) |
| Coverage / date range searched | e.g. 1970–2026 (or "all years") |
| Date search executed | the actual calendar date you run it |
| Language limit | e.g. English (state it — it is a real limitation) |
| Document types | e.g. Article, Review, Book Chapter |
| Records retrieved | **n = ?** ← record this |

Export all records as RIS or BibTeX to `Relevant Literature/search_2026/wos_core.ris` in the repo.

### Topic-specific supplementary searches

The 12 steps span domains the core string will under-sample. Run each of these separately and record retrieved counts individually — this is what makes a *curated* review auditable rather than arbitrary.

| # | Step(s) served | Search string (TS=) |
|---|---|---|
| S1 | 1 | `TS=(("semi-structured interview*" OR ethnograph* OR "focus group*" OR "qualitative method*") AND (conservation OR ecolog* OR biodiversity))` |
| S2 | 2 | `TS=(("value-belief-norm" OR "theory of planned behavior" OR "new ecological paradigm" OR "nature relatedness" OR "cultural ecosystem service*") AND (scale OR measure* OR construct*))` |
| S3 | 3 | `TS=(("wildlife attitude*" OR "attitudes toward wildlife" OR "nature connectedness" OR "environmental identity" OR "wildlife value orientation*") AND (validat* OR psychometric* OR reliability))` |
| S4 | 4, 9 | `TS=(("power analysis" OR "sample size" OR "pilot stud*" OR "cognitive pretesting" OR randomi?ation) AND (survey* OR questionnaire*) AND (conservation OR environment*))` |
| S5 | 5 | `TS=((preregistration OR pre-registration OR "open science" OR "registered report*") AND (ecolog* OR conservation OR psycholog*))` |
| S6 | 7 | `TS=(("attitude-behavior gap" OR "attitude-behaviour gap" OR "revealed preference*" OR "incentive compatible" OR "implicit association") AND (conservation OR environment* OR "pro-environmental"))` |
| S7 | 8 | `TS=(("institutional review board" OR "research ethics" OR "informed consent" OR "CARE principles" OR "Indigenous data sovereignty" OR decoloni*) AND (research OR data OR survey*))` |
| S8 | 10 | `TS=(("mixed-mode" OR "response rate*" OR "online panel*" OR Prolific OR "Mechanical Turk" OR "tailored design") AND (survey* OR questionnaire*))` |
| S9 | 11 | `TS=(("large language model*" OR "natural language processing" OR LLM OR "machine learning") AND ("qualitative analysis" OR "thematic analysis" OR "open-ended" OR "content analysis"))` |
| S10 | 11, 12 | `TS=(("structural equation model*" OR "confirmatory factor analysis" OR "ordinal regression") AND (conservation OR "human dimensions" OR environment*))` |
| S11 | 12 | `TS=((CHERRIES OR COREQ OR SRQR OR "JARS" OR "reporting standard*" OR "reporting guideline*") AND (survey* OR qualitative OR quantitative))` |

Record: **n retrieved per string**, and the **combined total**.

### Non-database sources (essential for a practice-focused review)

These are legitimate and expected in CSP's practice-focused modality — but they must be counted separately, not folded into the database total.

| Source type | What to count |
|---|---|
| Standard texts / handbooks | Survey-methodology and conservation-social-science books identified from graduate syllabi and expert knowledge (Dillman, Vaske, Stern, Groves, etc.) — **n = ?** |
| Backward/forward citation chasing | Records found by snowballing reference lists of included studies — **n = ?** |
| Reporting standards & institutional documents | CHERRIES, COREQ, SRQR, JARS, PRISMA, CARE/FAIR, BES Better Science Guides, IRB/BREB materials — **n = ?** |
| Author-team corpus | Studies from the team's own decade of socio-ecological survey practice used as worked examples — **n = ?** |

---

## Step B — Screen and record the drop-offs

Do this in Zotero or Rayyan so the counts fall out automatically.

1. **Deduplicate.** Record duplicates removed (`n = ?`). If you used two databases, this number is expected to be large — say so.
2. **Title/abstract screen** against the eligibility criteria below. Record screened (`n = ?`) and excluded (`n = ?`).
3. **Full-text assessment.** Record assessed (`n = ?`) and excluded with reasons — keep reasons in these buckets so they map onto the diagram:
   - not methodologically informative for survey design
   - no transferable guidance for socio-ecological / ecological contexts
   - superseded by a more recent or more authoritative source
   - full text unavailable
4. **Curation pass** (this is the practice-focused layer, and the part most reviews get dinged for leaving implicit). Of the eligible records, retain those meeting **at least one** of:
   - **C1 — Methodological influence:** foundational or widely adopted (e.g. textbooks used in courses teaching social theory and survey design; standards adopted by journals or professional bodies)
   - **C2 — Direct transferability:** guidance applicable without modification to ecological or conservation research contexts
   - **C3 — Technique illustration:** provides a concrete worked example of a specific method, scale, or analysis step
   Record how many were retained (`n = ?`) and how many eligible-but-not-prioritised records were set aside (`n = ?`). Reporting that second number is what converts "we curated" into "here is our curation, audited."
5. **Final synthesis set.** Record total included (`n = ?`), how many are cited in the main text, and how many are catalogued in the repository's living tables.

**Two screeners, please.** Have a second author independently screen a random ~20% subsample and report percentage agreement or Cohen's κ. It is one afternoon of work and it is the single most common reviewer request for reviews at this journal. If you genuinely cannot, state that screening was performed by one author and name it as a limitation.

---

## Step C — Fill in the numbers and rebuild the figure

Open `03_make_fig2_prisma.py`, edit the `N` dictionary at the top, and run:

```bash
python3 03_make_fig2_prisma.py
```

It writes `Fig2_PRISMA_flow.pdf` (vector, 300 dpi-safe, CSP-compliant single-column-scalable) and `Fig2_PRISMA_flow.png`. The script validates internal arithmetic and will refuse to run if the boxes don't balance — that catches the most common error reviewers spot in flow diagrams.

Then paste the counts into `02_Methods_section_REPLACEMENT.md`, which has the same placeholders.

---

## Step D — Also fix these while you're in the file

1. **Typo, Methods paragraph:** `"identified through Web of Science,]"` — stray bracket after "Web of Science". This is in the submitted version.
2. **Figure renumbering:** the PRISMA diagram becomes **Figure 2**; the current Figure 2 (question types and visualizations) becomes **Figure 3**. In-text mentions to update: the Figure Captions section, and the caption text itself. The manuscript body refers to question types via "(Table 1)" rather than "Figure 2", so body-text edits are minimal — but search for `Fig. 2` and `Figure 2` to be sure.
3. **Supplementary Material is currently one page containing only an anonymised URL.** Replace it with the search documentation (see `04_Supplementary_S1_S2_template.md`). A one-line link is very likely part of why this was flagged: from the editor's side there was no methods documentation anywhere in the submission package.
4. **De-anonymise the repository link.** The Supplementary PDF points at `anonymous.4open.science`; the live repo is `github.com/Echeverri-Lab/Survey_methods`. Check CSP's policy on whether they want the anonymised link retained through review. Also delete or clearly archive the `anonymized/` duplicate directory in the repo — it currently duplicates every step folder and will confuse readers.
5. **Repo housekeeping:** `Flag_for_Review/reference_audit_report.md` lists citations flagged as placeholders or non-peer-reviewed. Your own README says resolve these before submission. Worth doing now, since a returned manuscript gets a fresh look.
6. **Archive the search.** Save the RIS exports and the screening spreadsheet in the repo under `Relevant Literature/search_2026/` and cite that path in the Methods. Documented and retrievable beats described.
