# Stream A search strings, version 2 — DRAFT for author approval

**Status:** APPROVED by the authors as drafted, 2026-11-01. Decisions: 2020–2026 on every string; Web of Science Core Collection only (single database stated as a limitation); variant (b) threshold 3,000 records. **Next:** peer review by an information specialist (PRESS 2015) before running; the reviewed version is saved as `search_strings_v2.md`. Not yet run.
**Database:** Web of Science Core Collection (Advanced Search). The editions searched must be recorded at run time.
**Replaces:** every earlier version. There are three conflicting copies, none tied to the counts reported in SI Table S1.
**Eligibility:** `submission/ConBio-26-785/01_ELIGIBILITY_CRITERIA_DRAFT.md` (approved). Each string below names the criterion (I1–I5) it targets.
**Citations marked [verify]** have not been read yet.

## Conventions (R1: "formatting… S11 inconsistently formatted")

- **One field throughout:** `TS=` (title, abstract, author keywords, Keywords Plus). The only exception is the prespecified narrowing variant (b) below.
- **Quoting:** multi-word phrases go in double quotes; single words stay unquoted.
- **Wildcards:** every noun that can be plural gets `*`. `$` stands for zero or one character (`behavio$r` matches behavior and behaviour).
- **The same limits on every string:**
  `AND PY=(2020-2026) AND LA=(English) AND DT=(Article OR Review OR "Book Chapter" OR Book) NOT DT=("Retracted Publication")`
  These are written once as **[LIMITS]** below, and `[LIMITS]` must be replaced with that full text before pasting.
- **No Web of Science category (`WC=`) filters.** They hid *Public Opinion Quarterly*, *Behavior Research Methods*, and similar journals, and they contradict the approved eligibility rule that guidance from any discipline is eligible.
- **Prespecified volume rule.** If a string returns more than **3,000** records, run its variant (b), which moves the method block from `TS=` to `TI=`. Record both counts and use (b). The rule is fixed now so the choice is not made after seeing results.

## What changed and why

| Reviewer point (R1-19 unless noted) | Change |
|---|---|
| "conservation social science" lacks a wildcard; missing "environmental / marine / natural resource social science\*" | The context block now has all four, wildcarded, plus "human dimension\*", "conservation psycholog\*", and "environmental psycholog\*" |
| Item response theory missing | Added "item response theory" and Rasch to the core search and to S3 and S10 |
| S4 lacks poll terms | Added `poll OR polls OR polling OR "opinion poll*" OR "public opinion"` to the core search and S4 |
| S11 inconsistent quotes | All strings now follow the conventions above |
| Search may introduce bias; benchmark protocols | Benchmark sensitivity test (below) |
| External expert review (ROSES / Environmental Evidence) | Information-specialist peer review using PRESS 2015 (below) |
| Eligibility now covers guidance from any discipline (R1-22, R1-3) | Step-specific strings (S4, S5, S8, S9, S11) no longer require an environmental term; the core search, S1, S2, S3, S6, and S10 keep one because their targets are environment-specific |
| Paradigm and limits (R2-1, HE-3; criterion I5) | New S12 |
| Single database (R1, positionality section) | See decision 2 |

## Strings

### Core — survey measurement in environmental contexts (I1–I3)
```
TS=(
  (survey* OR questionnaire* OR poll OR polls OR polling OR "opinion poll*" OR "public opinion"
   OR psychometric* OR "scale development" OR "scale validation" OR "measurement invariance"
   OR "item response theory" OR Rasch OR Likert OR "self-report*")
  AND
  ("human dimension*" OR "conservation social science*" OR "environmental social science*"
   OR "marine social science*" OR "natural resource* social science*"
   OR "conservation psycholog*" OR "environmental psycholog*"
   OR "socio-ecological" OR "social-ecological" OR "socio-environmental"
   OR "human-wildlife" OR "human-nature" OR "people and nature"
   OR ((conservation OR biodiversity OR wildlife OR "ecosystem service*" OR "protected area*"
        OR "natural resource*" OR environment*)
       NEAR/5 (attitude* OR value* OR belief* OR norm* OR perception* OR identit* OR behavio$r*)))
  AND
  (method* OR design* OR validity OR validat* OR reliab* OR "best practice*" OR guideline*
   OR guidance OR recommendation* OR framework* OR review*)
) [LIMITS]
```
(b): the third block becomes `AND TI=(method* OR design* OR validity OR validat* OR reliab* OR "best practice*" OR guideline* OR guidance OR recommendation* OR framework* OR review*)`.

### S1 — Choosing methods: qualitative, mixed, and participatory (Step 1; I1)
```
TS=(
  ("semi-structured interview*" OR ethnograph* OR "focus group*" OR "qualitative method*"
   OR "mixed method*" OR "mixed-method*" OR "participatory research" OR "participatory method*")
  AND (conservation OR biodiversity OR wildlife OR "natural resource*" OR "protected area*"
       OR "social-ecological" OR "socio-ecological")
  AND (method* OR guideline* OR guidance OR "best practice*" OR review* OR framework* OR choos* OR select*)
) [LIMITS]
```

### S2 — Theory and construct definition (Step 2; I1, I3)
```
TS=(
  ("value-belief-norm" OR "theory of planned behavio$r" OR "reasoned action"
   OR "new ecological paradigm" OR "nature relatedness" OR "connectedness to nature"
   OR "wildlife value orientation*" OR "environmental identit*" OR "norm activation"
   OR "protection motivation" OR "relational value*" OR "place attachment")
  AND (construct* OR measur* OR operationali* OR conceptuali* OR scale* OR review*)
) [LIMITS]
```

### S3 — Instruments and construct validity (Step 3; I3)
```
TS=(
  (psychometric* OR "scale development" OR "scale validation" OR validat* OR reliab*
   OR "factor structure" OR "factorial validity" OR "measurement invariance"
   OR "item response theory" OR Rasch OR "short form*")
  AND (attitude* OR value* OR identit* OR connectedness OR relatedness OR "place attachment"
       OR tolerance OR "eco-anxiety" OR "climate anxiety" OR worldview*)
  AND (wildlife OR nature OR environment* OR biodiversity OR conservation OR species OR climate)
) [LIMITS]
```

### S4 — Study design, sampling, power, and pretesting (Steps 4, 9; I1, I2)
```
TS=(
  ("power analys*" OR "sample size*" OR "sampling design*" OR "probability sampl*"
   OR "nonprobability sampl*" OR "non-probability sampl*" OR "pilot stud*" OR pretest*
   OR "pre-test*" OR "cognitive interview*" OR "think-aloud" OR "nonresponse bias"
   OR "non-response bias" OR "between-subject*" OR "within-subject*")
  AND (survey* OR questionnaire* OR poll OR polls OR "opinion poll*" OR "public opinion")
  AND (guideline* OR guidance OR "best practice*" OR recommendation* OR tutorial* OR primer*
       OR review* OR method*)
) [LIMITS]
```

### S5 — Preregistration and open science (Step 5; I1, I2)
```
TS=(
  (preregistration OR "pre-registration" OR preregistered OR "registered report*"
   OR "open science" OR "questionable research practice*" OR "research transparency")
  AND (survey* OR questionnaire* OR psycholog* OR "social science*" OR ecolog* OR conservation)
) [LIMITS]
```

### S6 — Measuring behavior beyond self-report (Step 7; I1, I2)
```
TS=(
  ("attitude-behavio$r gap" OR "intention-behavio$r gap" OR "revealed preference*"
   OR "incentive-compatible" OR "incentive compatible" OR "implicit association"
   OR "eye-tracking" OR "eye tracking" OR "mouse-tracking" OR "behavio$ral task*"
   OR "observed behavio$r*" OR "self-report* bias")
  AND (conservation OR "pro-environmental" OR environment* OR biodiversity OR wildlife OR nature)
) [LIMITS]
```

### S7 — Ethics, consent, and data sovereignty (Step 8; I1, I4)
```
TS=(
  ("research ethic*" OR "informed consent" OR "institutional review board*" OR "ethics review"
   OR "ethical review" OR "data sovereignty" OR "Indigenous data" OR "CARE principles"
   OR decoloni* OR "participant compensation" OR incentive* OR deception OR debrief*)
  AND (survey* OR questionnaire* OR "human subject*" OR "social science*" OR conservation)
  AND (guideline* OR guidance OR "best practice*" OR recommendation* OR framework* OR review*
       OR principle*)
) [LIMITS]
```

### S8 — Administration, mode, and data quality (Steps 10, 11; I2)
```
TS=(
  ("response rate*" OR "mixed-mode" OR "mixed mode" OR "survey mode*" OR "mode effect*"
   OR "online panel*" OR Prolific OR "Mechanical Turk" OR MTurk OR crowdsourc*
   OR "web survey*" OR "mail survey*" OR "tailored design" OR "data quality"
   OR "attention check*" OR "careless respon*" OR "inattentive respon*" OR straightlin*
   OR "bot detection" OR bots OR "fraudulent respon*" OR translat* OR "back-translat*")
  AND (survey* OR questionnaire* OR poll OR polls OR respondent*)
  AND (guideline* OR guidance OR "best practice*" OR recommendation* OR review* OR experiment*
       OR comparison* OR method*)
) [LIMITS]
```

### S9 — LLM and NLP analysis of open-ended responses (Step 11; I1, I2)
```
TS=(
  ("large language model*" OR LLM OR LLMs OR "natural language processing" OR "generative AI"
   OR "generative artificial intelligence" OR GPT* OR ChatGPT OR "machine learning"
   OR "text classification")
  AND ("qualitative analys*" OR "thematic analys*" OR "content analys*" OR "open-ended"
       OR "qualitative research" OR "qualitative coding" OR "qualitative data")
) [LIMITS]
```

### S10 — Latent-variable and ordinal analysis (Steps 11, 12; I1, I2)
```
TS=(
  ("structural equation model*" OR "confirmatory factor analys*" OR "exploratory factor analys*"
   OR "latent variable*" OR "measurement model*" OR "ordinal regression" OR "ordinal model*"
   OR "item response theory" OR Rasch OR "Cronbach* alpha" OR "McDonald* omega")
  AND ("human dimension*" OR conservation OR environment* OR ecolog* OR wildlife
       OR "social-ecological" OR "socio-ecological")
  AND (guideline* OR guidance OR "best practice*" OR recommendation* OR tutorial* OR primer*
       OR review* OR misuse OR pitfall*)
) [LIMITS]
```

### S11 — Reporting standards (Step 12; I4)
```
TS=(
  (CHERRIES OR COREQ OR SRQR OR JARS OR "reporting standard*" OR "reporting guideline*"
   OR "reporting checklist*" OR "reporting quality" OR (transparen* NEAR/3 report*))
  AND (survey* OR questionnaire* OR qualitative OR "social science*")
) [LIMITS]
```

### S12 — Paradigm, assumptions, and limits of survey measurement (Step 1, Box 1; I5) — new
```
TS=(
  (epistemolog* OR ontolog* OR paradigm* OR positivis* OR "post-positivis*" OR constructivis*
   OR interpretivis* OR "critical realis*" OR relational* OR "Indigenous methodolog*"
   OR "Indigenous knowledge" OR pluralis* OR reflexiv* OR positionality)
  AND (survey* OR questionnaire* OR psychometric* OR quantitative OR measurement)
  AND (conservation OR environment* OR nature OR wildlife OR "social-ecological"
       OR "socio-ecological" OR "natural scien*")
) [LIMITS]
```

**Syntax to confirm in the live interface (and in the PRESS review):** `NEAR/5` with a parenthesized OR group on each side (core); `$` inside a quoted phrase (`"theory of planned behavio$r"`, S2, S6); and whether `LA=` and `DT=` combine with `NOT DT=` as written. Web of Science accepts these as far as I know, but I couldn't test them without access.

## Benchmark sensitivity test (R1: "benchmark article protocols")

Before screening, check that the combined retrieval contains each benchmark: eligible records already known, indexed in Web of Science, and published 2020–2026. Report sensitivity as found/total.

If any benchmark is missed, identify the string that should have caught it, revise that string **once**, rerun it, and report the revision. Benchmarks the strings still miss stay in the review only through Stream B, and Table S1 says so.

| # | Benchmark | Expected string(s) |
|---|---|---|
| 1 | Kyle et al. 2020, *Conserv Biol* (10.1111/cobi.13625) | Core, S3, S10 |
| 2 | Whitehouse-Tedd et al. 2021, *Conserv Biol* (10.1111/cobi.13599) | Core, S3 |
| 3 | Wardropper et al. 2021, *Conserv Biol* (10.1111/cobi.13747) | Core, S8 |
| 4 | Ghasemi et al. 2026, *Conserv Biol* (10.1111/cobi.70326) | Core, S3 |
| 5 | Eyster et al. 2025, *Conserv Biol* (10.1111/cobi.14461) | S2 |
| 6 | Moon et al. 2019, *Methods Ecol Evol* (10.1111/2041-210x.13126) | S12 |
| 7 | Clayton et al. 2021, *Sustainability* (10.3390/su13042387) | S3 |
| 8 | Pérez et al. 2021, *Animals* (BAtSS) | S3 |
| 9 | Kay 2025, *Behav Res Methods* | S8 |
| 10 | Douglas et al. 2023, *PLOS ONE* (data quality across online platforms) | S8 |
| 11 | van den Akker et al. 2024, *Behav Res Methods* | S5 |
| 12 | Willroth & Atherton 2024, *AMPPS* | S5 |
| 13 | Hayes 2025, *Int J Qual Methods* | S9 |
| 14 | Jowsey et al. 2025, *Qual Inquiry* (10.1177/10778004251401851) | S9 |
| 15 | Lengieza et al. 2025 (five-culture validation) | S3 |

## Information-specialist peer review (R1: "external expert review")

- **Reviewer:** a librarian or information specialist outside the author team, e.g., a UC Berkeley subject librarian for environmental science or the social sciences. Name and affiliation go in the Acknowledgments, with their permission.
- **Instrument:** the PRESS 2015 Guideline Evidence-Based Checklist (McGowan et al. 2016, *J Clin Epidemiol* [verify]). It covers translation of the question, Boolean and proximity operators, subject headings, text words, spelling/syntax, and limits.
- **Record:** the reviewer's comments, each change made, and the date. Store these as `search_peer_review.md` in this folder. The version that is actually run becomes `search_strings_v2.md` (no DRAFT), and every count goes in its recording sheet.

## Recording sheet (filled at run time)

| ID | Variant used | Date run | Editions | Records | Export file(s) |
|---|---|---|---|---|---|
| Core | a / b | | | | |
| S1 | | | | | |
| S2 | | | | | |
| S3 | | | | | |
| S4 | | | | | |
| S5 | | | | | |
| S6 | | | | | |
| S7 | | | | | |
| S8 | | | | | |
| S9 | | | | | |
| S10 | | | | | |
| S11 | | | | | |
| S12 | | | | | |

**Export:** full record plus cited references, plain text or RIS, in batches of 1,000 (the Web of Science limit). Name files `wos_<ID>_<batch>.txt` in `exports/`.

## Decisions for you

1. **Date window.** As drafted, 2020–2026 for every string, matching what the manuscript reported. Foundational and older work enters through Stream B (texts, standards, citation chasing), which has no date limit. A wider window (e.g., 2015–2026) would be more complete, but would roughly double screening for one screener before 30 January 2027.
2. **Add Scopus?** It answers the single-database limitation that R1 and our own positionality section raise, and much of it will overlap Web of Science and drop out at deduplication. If yes, I translate the approved strings to Scopus syntax (`TITLE-ABS-KEY`, `W/n` for proximity) after the information-specialist review.
3. **The 3,000-record threshold** for variant (b).
4. **Who will do the information-specialist review?**
