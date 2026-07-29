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
- `templates/` — consent forms, debrief sheets

---

## Cross-references

- Construct stability → `../Step_02_Theory_Grounding/theory_summary.md`
- Scale selection → `../Step_03_Psychometric_Scales/`
- Pre-registration → `../Step_05_PreRegistration/`

---

## 2026 revision — literature curation pass

Reviewed against 37 candidate papers (Step 4 topic match) from the 25%
random subsample described in
`Relevant Literature/search_2026/exports/suggested_new_citations.md`.

- **Added** a new "Discrete Choice Experiments (DCE)" subsection to
  `design_decision_matrix.md` (Part 4b). This was a genuine gap: ~12 of the
  37 candidates used DCEs for socio-ecological valuation (payments for
  ecosystem services, protected-area trade-offs, farmer preferences), a
  stated-preference design family not previously covered alongside
  BACI/ACI/within-subjects designs. Cited Notaro et al. (2022) as a worked
  example addressing attribute non-attendance (C3), and Cop & Njavro (2022)
  as a review of DCE applications for benchmarking attribute design (C1).
- **Not added:** most other candidates were pilot studies in unrelated
  domains (VR labs, EEG, physics education) or additional survey-incentive
  studies, which are better suited to Step 9 (piloting) and Step 10
  (response rates) respectively — see those steps' curation notes.
- Power and sampling → `../Step_09_Power_and_Sampling/`
- Ethics and consent → `../Step_08_Ethics_and_Compensation/`
