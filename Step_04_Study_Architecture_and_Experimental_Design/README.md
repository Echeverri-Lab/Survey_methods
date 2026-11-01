# Step 04 — Study Architecture and Experimental Design

This folder covers the architecture of survey and behavioral intervention studies: construct-design matching, design type selection, randomization, temporal context controls, and survey flow.

---

## Key Documents

| File | Purpose |
|---|---|
| `study_design_checklist.md` | Master checklist — work through this before finalizing any design |
| `design_decision_matrix.md` | Construct × design compatibility table and decision tree |
| `temporal_context_log.md` | Per-wave log of season, conflict events, media salience, and weather covariates |
| `design_docs/randomization_plan.md` | Random assignment procedure, seed, balance checks |
| `design_docs/survey_flow_diagram.md` | Mermaid flow diagram template for survey administration |

---

## Core Concepts (from manuscript §2.4)

- **Construct temporal stability** drives design choice: trait-like constructs (values, worldviews, identity) suit cross-sectional designs; state-like constructs (affect, mood) require repeated or experience-sampling designs.
- **BACI** (Before–After–Control–Impact) is the gold standard for intervention studies.
- **ACI** (After–Control–Impact) is appropriate when pre-measurement is impossible or would sensitize respondents; within-individual change cannot be estimated.
- **Within-subjects** designs gain power but are vulnerable to testing effects and attrition — oversample at baseline.
- **Temporal context** (season, phenology, conflict events, media salience) can confound wildlife attitude measures and must be recorded as covariates.

---

## Subfolders

- `design_docs/` — randomization plan, flow diagrams, pretest specs
- Consent forms and debrief templates are in `../Step_08_Ethics_and_Participant_Compensation/`

---

## Cross-references

- Construct stability → [`../Step_02_Theory_Grounding_and_Construct_Conceptualization/theory_summary.md`](../Step_02_Theory_Grounding_and_Construct_Conceptualization/theory_summary.md)
- Scale selection → [`../Step_03_Psychometric_Scales_and_Construct_Validity/`](../Step_03_Psychometric_Scales_and_Construct_Validity/)
- Pre-registration → [`../Step_05_Preregistration_and_Open_Science/`](../Step_05_Preregistration_and_Open_Science/)

