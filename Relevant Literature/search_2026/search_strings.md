# Search strings — CSP2-26-0397

Verbatim Boolean strings extracted from `01_Search_Protocol_RUN_THIS_FIRST.md`
(Step A). Fill in the blank fields as each search is executed. Export the
corresponding RIS/BibTeX file to `exports/` and reference its filename here.

Field of search for all strings below: **Topic (TS=)**.

---

## Core search

Paste into **Web of Science → Advanced Search**, database set to **Web of Science Core Collection**.

```
TS=(
  ("questionnaire*" OR psychometric* OR Likert OR "opinion poll*"
   OR "scale development" OR "scale validation" OR "measurement invariance"
   OR "self-report*" OR "survey instrument*" OR "survey design"
   OR "questionnaire design" OR "survey research" OR "survey methodolog*")
  AND
  ("human dimensions" OR "conservation social science" OR "environmental psychology"
   OR "conservation psychology" OR "socio-ecological" OR "social-ecological"
   OR "socio-environmental" OR "pro-environmental" OR stakeholder*
   OR ((conservation OR biodiversity OR wildlife OR ecolog* OR "ecosystem service*")
       AND (attitude* OR perception* OR value* OR behavio?r* OR preference* OR willingness)))
)
AND DT=(Article OR Review)
AND PY=(2021-2026)
AND WC=("Environmental Sciences" OR "Ecology" OR "Biodiversity & Conservation"
  OR "Environmental Studies" OR "Marine & Freshwater Biology"
  OR "Multidisciplinary Sciences" OR "Green & Sustainable Science & Technology"
  OR "Public, Environmental & Occupational Health" OR "Psychology, Multidisciplinary"
  OR "Zoology" OR "Forestry" OR "Plant Sciences" OR "Oceanography"
  OR "Water Resources" OR "Fisheries" OR "Geosciences, Multidisciplinary"
  OR "Geography, Physical" OR "Psychiatry" OR "Entomology"
  OR "Social Sciences, Interdisciplinary" OR "Geography" OR "Ornithology"
  OR "Economics" OR "Limnology")
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | Web of Science Core Collection (note editions) |
| Coverage / date range searched | |
| Date search executed | |
| Language limit | |
| Document types | Article, Review |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

---

## Topic-specific supplementary searches (S1–S11)

Run each as a separate Advanced Search. Record the headline count and export separately.

### Two deliberate departures from the core search

**1. `PY=(2021-2026)` is wrong for some of these.** Restricting to the last five years makes sense for the core search — you want current practice. It is actively harmful for the searches whose purpose is to find *foundational* sources. A five-year window would miss:

- COREQ (2007), CHERRIES (2004), SRQR (2014) — all of S11's targets
- Value-Belief-Norm (1999), Theory of Planned Behaviour (1991), New Ecological Paradigm (2000) — all of S2's targets
- The original validation papers for most established scales — much of S3

So: **S2, S3, and S11 run with no year limit.** The rest keep `PY=(2021-2026)`. This is a defensible and easily explained asymmetry — recent application literature, foundational methodological literature — but you must state it in Table S1 rather than let a reviewer discover an inconsistency.

**2. `WC=` is dropped from most of these.** The category filter is what was hiding *Behavior Research Methods*, *Public Opinion Quarterly*, and *IJQM* from you. These supplementary searches exist precisely to reach outside the ecological categories, so constraining them by ecology categories would defeat their purpose. `WC=` is retained only on S1 and S6, where the ecological context is the point and the terms are otherwise broad.

Add to every search: `NOT DT=("Retracted Publication")`.

### S1 — Qualitative and inductive methods (Step 1)

```
TI=("semi-structured interview*" OR ethnograph* OR "focus group*"
    OR "qualitative method*" OR "mixed method*" OR "participatory method*")
AND TS=(conservation OR biodiversity OR wildlife OR ecolog* OR "natural resource*"
    OR "protected area*")
AND DT=(Article OR Review) AND PY=(2021-2026)
AND WC=("Environmental Sciences" OR "Ecology" OR "Biodiversity & Conservation"
    OR "Environmental Studies" OR "Social Sciences, Interdisciplinary")
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S2 — Social-science theory and construct conceptualization (Step 2) · no year limit

```
TI=("value-belief-norm" OR "theory of planned behavior" OR "theory of planned behaviour"
    OR "new ecological paradigm" OR "nature relatedness" OR "cultural ecosystem service*"
    OR "wildlife value orientation*" OR "environmental identity"
    OR "norm activation" OR "protection motivation")
AND DT=(Article OR Review)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S3 — Validated scales and construct validity (Step 3) · no year limit

```
TI=(scale* OR psychometric* OR validat* OR "measurement invariance" OR reliability
    OR "factor structure")
AND TS=("wildlife attitude*" OR "attitudes toward wildlife" OR "nature connectedness"
    OR "connectedness to nature" OR "environmental identity"
    OR "wildlife value orientation*" OR "nature relatedness"
    OR "environmental attitude*" OR "place attachment")
AND DT=(Article OR Review)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S4 — Power analysis, sampling, pilots (Steps 4, 9)

```
TI=("power analysis" OR "sample size" OR "pilot stud*" OR "cognitive pretest*"
    OR "cognitive interview*" OR "sampling design" OR "nonresponse bias"
    OR "non-response bias")
AND TS=(survey* OR questionnaire* OR respondent*)
AND TS=(conservation OR environment* OR ecolog* OR "social science*")
AND DT=(Article OR Review) AND PY=(2021-2026)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S5 — Preregistration and open science (Step 5)

```
TI=(preregistration OR "pre-registration" OR preregistered OR "registered report*"
    OR "open science" OR "questionable research practice*" OR "research transparency"
    OR reproducib*)
AND TS=(ecolog* OR conservation OR environment* OR psycholog* OR "social science*")
AND DT=(Article OR Review) AND PY=(2021-2026)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S6 — Measuring behaviour beyond self-report (Step 7)

```
TI=("attitude-behavior gap" OR "attitude-behaviour gap" OR "revealed preference*"
    OR "stated preference*" OR "incentive compatible" OR "implicit association"
    OR "behavioral intention*" OR "behavioural intention*" OR "eye-tracking"
    OR "discrete choice experiment*")
AND TS=(conservation OR environment* OR "pro-environmental" OR biodiversity OR wildlife)
AND DT=(Article OR Review) AND PY=(2021-2026)
AND WC=("Environmental Sciences" OR "Ecology" OR "Biodiversity & Conservation"
    OR "Environmental Studies" OR "Psychology, Multidisciplinary" OR "Economics")
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S7 — Research ethics and data sovereignty (Step 8)

```
TI=("research ethics" OR "informed consent" OR "institutional review board"
    OR "data sovereignty" OR decoloni* OR "CARE principles" OR "Indigenous data"
    OR "ethical review" OR "community-based participatory")
AND TS=(research OR survey* OR questionnaire* OR data OR conservation OR environment*)
AND DT=(Article OR Review) AND PY=(2021-2026)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S8 — Survey mode, administration, data quality (Step 10)

```
TI=("response rate*" OR "mixed-mode" OR "mixed mode" OR "online panel*" OR Prolific
    OR "Mechanical Turk" OR MTurk OR "web survey*" OR "mail survey*"
    OR "tailored design" OR "data quality" OR "survey mode*" OR "bot detection")
AND TS=(survey* OR questionnaire* OR respondent*)
AND DT=(Article OR Review) AND PY=(2021-2026)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S9 — LLM- and NLP-assisted qualitative analysis (Step 11)

```
TI=("large language model*" OR LLM OR LLMs OR "natural language processing"
    OR "machine learning" OR "artificial intelligence" OR GPT OR ChatGPT
    OR "generative AI")
AND TS=("qualitative analysis" OR "thematic analysis" OR "content analysis"
    OR "open-ended" OR "qualitative research" OR "qualitative coding"
    OR "inductive coding")
AND DT=(Article OR Review) AND PY=(2021-2026)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S10 — Latent-variable and ordinal modelling (Steps 11, 12)

```
TI=("structural equation model*" OR "confirmatory factor analysis"
    OR "ordinal regression" OR "latent variable*" OR "path analysis"
    OR "measurement model" OR "Likert")
AND TS=(conservation OR "human dimensions" OR environment* OR ecolog*
    OR "socio-ecological" OR "social-ecological")
AND DT=(Article OR Review) AND PY=(2021-2026)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

### S11 — Reporting standards (Step 12) · no year limit

```
TI=(CHERRIES OR COREQ OR SRQR OR JARS OR "reporting standard*"
    OR "reporting guideline*" OR "reporting checklist*" OR "reporting quality")
AND TS=(survey* OR questionnaire* OR qualitative OR quantitative OR research)
AND DT=(Article OR Review)
```

| Field | Value |
|---|---|
| Database(s) and edition(s) | |
| Date search executed | |
| Limits | |
| Records retrieved (n) | |
| Export filename (in `exports/`) | |

---

## Recording sheet

Fill as you go; this populates Table S1 and the `db_topic` total.

| ID | Steps | Year limit | `WC=` applied | Date run | Records | Query # |
|---|---|---|---|---|---|---|
| Core | all | 2021–2026 | yes | | **1,612** | |
| S1 | 1 | 2021–2026 | yes | | | |
| S2 | 2 | none | no | | | |
| S3 | 3 | none | no | | | |
| S4 | 4, 9 | 2021–2026 | no | | | |
| S5 | 5 | 2021–2026 | no | | | |
| S6 | 7 | 2021–2026 | yes | | | |
| S7 | 8 | 2021–2026 | no | | | |
| S8 | 10 | 2021–2026 | no | | | |
| S9 | 11 | 2021–2026 | no | | | |
| S10 | 11, 12 | 2021–2026 | no | | | |
| S11 | 12 | none | no | | | |
| | | | | | **`db_topic` = sum of S1–S11** | |

## A sanity check worth doing

Before you screen anything, check whether the combined retrieval actually finds the papers you already know are central — Whitehouse-Tedd et al. (2021), Kay (2025), van den Akker et al. (2024), Hayes (2025), Putnick & Bornstein (2016), Baker et al. (2010). Search your merged Zotero library for each.

Any that are missing tell you something useful, and either outcome is reportable. If a search finds them, say so — it is evidence of sensitivity. If it doesn't, that source moves into the citation-chasing or standard-texts stream in Table S1, which is exactly what those streams are for. What you should not do is quietly cite a source the documented search could never have found.
