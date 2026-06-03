# Step 06 — Instrument Construction and Quality Control

> *"Items that cannot be justified can be cut before piloting."*  
> — Survey Design curriculum, Step 6

This folder contains everything needed to assemble a rigorous survey instrument: design matrices, flow diagrams, reusable templates, and multi-stage quality control checklists.

---

## Folder structure

```
Step_06_Instrument_Construction/
├── README.md                              ← this file
├── question_types_reference.md            ← Compendium of survey response formats & data types
│
├── examples/
│   ├── survey_matrix_echeverri2019.md             ← Worked example: full item matrix for Echeverri et al. (2019)
│   ├── survey_flow_diagram_echeverri2019.md        ← Mermaid flowchart, colour-coded by variable role
│   └── survey_matrix_FFCP_premonitoring.md         ← Real-world example: FFCP pre-monitoring survey matrix (Kelley, unpublished)
│
├── templates/
│   ├── survey_template.md                 ← Minimal survey assembly template
│   └── survey_matrix_template.md          ← Blank design matrix for any socio-ecological study
│
└── quality_control/
    ├── README.md
    └── qc_checklist.md                    ← Five-stage QC checklist (draft → cog. interview → pilot → field → cleaning)
```

---

## What the Step 6 manuscript says

Key principles for instrument construction:

| Principle | Why it matters |
|---|---|
| **Survey matrix first** | Forces every item to be justified by a research question before piloting. Items that cannot be justified are cut. |
| **Question order / priming** | Blocks prime each other; place open-ended items before Likert; demographics last |
| **Respondent burden audit** | Every item adds burden; map each to a specific analytic need before keeping it |
| **Demographics at the end** | Placing gender, ethnicity, or income at the start can trigger social identity threat (Steele & Aronson, 1995; Danaher & Crandall, 2008) |
| **Inclusive categories** | Ill-fitting options produce frustration and disengagement (Miller, 2025) |
| **Attention checks** | Non-negotiable for online surveys; frame as comprehension aids with community partners (Abbey & Meloy, 2017) |
| **Interactive / multimedia elements** | Mitigate fatigue and improve ecological validity (e.g., species photos + audio in Echeverri et al. 2019) |

---

---

## 💡 Lab practice: survey question justification matrix

> *Taught and used in the Echeverri Lab; first demonstrated in the FFCP pre-monitoring survey (Kelley, unpublished).*

Before piloting any instrument, build a **question justification matrix** — a table with one row per survey item that documents:

| Column | What to fill in |
|---|---|
| **Question** | Exact wording of the item as it will appear to respondents |
| **Purpose / research justification** | Which research question or objective this item addresses; what you will *do* with the data |
| **Construction source** | Existing validated scale (cite it), adapted item (note changes), or custom item (explain how it was constructed) |

**Why this works:**

- **Reduces survey bloat** — any item that cannot be justified against a research question is a candidate for removal before piloting.
- **Improves item rigor** — forces you to think about whether a custom item is necessary or whether a validated scale already exists.
- **Speeds up IRB/ethics review** — reviewers can immediately see why each question is included and that nothing extraneous is being collected.
- **Enables post-hoc transparency** — the matrix becomes a methods appendix or supplementary material in the final paper.

**See it in action:** `examples/survey_matrix_FFCP_premonitoring.md` — a real-world example from the FFCP wildlife monitoring add-on study, covering 8 items across consent, repeated-measures constructs, a benchmarking item (NWOS), and open-ended close.

---

## How to use this folder

### Starting a new instrument
1. Open `templates/survey_matrix_template.md` — fill in the **Study Overview** and add one row per item.
2. Review `question_types_reference.md` to ensure you are selecting the best response formats for your specific analytical and data needs.
3. Complete the **Variable Summary Table** — every IV, DV, and covariate must appear here.
4. Run the **Respondent Burden Audit** and verify total time is within target range.
5. Work through the **Item-level QC Checklist** (Part 5 of the template) before any cognitive testing.

### Learning from a worked example
- `examples/survey_matrix_echeverri2019.md` — complete item-by-item breakdown of a 12-species, 19-page socio-ecological survey.
- `examples/survey_flow_diagram_echeverri2019.md` — Mermaid flowchart of the same study (paste code into [mermaid.live](https://mermaid.live) to render and export).

### Running quality control
- Follow `quality_control/qc_checklist.md` in three dated passes: after drafting, after cognitive interviews, and after piloting.

---

## Key references

- Abbey, J. D., & Meloy, M. G. (2017). Attention by design. *Journal of Operations Management*, 53–56, 63–70.
- Echeverri, A., et al. (2019). Avian cultural ecosystem services. *People and Nature*, 1(1), 102–115.
- Miller, J. (2025). Inclusive survey design. *Survey Practice*.
- Danaher, K., & Crandall, C. S. (2008). Stereotype threat in applied settings re-examined. *Journal of Applied Social Psychology*, 38(6), 1639–1655.
- Steele, C. M., & Aronson, J. (1995). Stereotype threat and the intellectual test performance of African Americans. *Journal of Personality and Social Psychology*, 69(5), 797–811.
- Tourangeau, R., Rips, L. J., & Rasinski, K. (2000). *The Psychology of Survey Response*. Cambridge University Press.
- Willis, G. B. (2005). *Cognitive Interviewing*. SAGE.
