# Randomization Plan

Document the random assignment procedure here. This file should be completed **before** data collection begins and referenced in your pre-registration.

---

## Study Metadata

| Field | Entry |
|---|---|
| Study title | |
| Design type | ☐ RCT-BACI  ☐ Quasi-experimental BACI  ☐ ACI  ☐ Within-subjects  ☐ Other: |
| Number of arms / conditions | |
| Blocking / stratification variables (if any) | |
| Random seed | |
| Software used | ☐ R (`set.seed()`)  ☐ Python (`numpy.random.seed()`)  ☐ Qualtrics randomizer  ☐ Other: |
| Script file path | `code/randomization.R` or `code/randomization.py` |
| Person who generated assignment | |
| Date generated | |

---

## Condition Descriptions

| Condition label | Description | N allocated |
|---|---|---|
| Control | | |
| Treatment 1 | | |
| Treatment 2 (if any) | | |

---

## Allocation Ratio

- Planned ratio (e.g., 1:1, 2:1 treatment:control): ______________
- Justification for unequal allocation (if applicable): ______________

---

## Stratification / Blocking

- [ ] No blocking — simple randomization.
- [ ] Blocked randomization. Block size: _______ . Rationale: _______________
- [ ] Stratified randomization. Stratification variable(s): _______________
- [ ] Minimization / covariate-adaptive randomization. Variables minimized on: _______________

---

## Implementation

- [ ] Assignment sequence generated before any participant is enrolled.
- [ ] Assignment sequence stored in a locked file (not accessible to data collectors if blinding is required).
- [ ] Assignment delivered to participants via: ☐ Survey platform randomizer  ☐ Researcher  ☐ Automated system
- [ ] Blinding: ☐ Participants blind to condition  ☐ Data analysts blind until lock  ☐ Not blinded (document reason)

---

## Balance Check (complete after enrollment closes)

Run a balance table comparing treatment arms on key baseline covariates. Paste output or file reference here.

| Covariate | Control M (SD) | Treatment M (SD) | p-value |
|---|---|---|---|
| Age | | | |
| Gender | | | |
| Education | | | |
| Prior contact with focal species | | | |
| Baseline attitude score | | | |

- [ ] No statistically significant imbalances detected (p > .05 for all covariates).
- [ ] Imbalances detected on: _______________ → will be included as covariates in primary analysis.

---

## Deviations Log

Record any deviations from the pre-specified randomization plan.

| Date | Deviation | Reason | Impact on analysis |
|---|---|---|---|
| | | | |

---

*Cross-reference: `study_design_checklist.md` §5 · `../Step_05_PreRegistration/` · `../Step_09_Power_and_Sampling/`*
