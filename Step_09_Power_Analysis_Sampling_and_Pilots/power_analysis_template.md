# Power Analysis Worksheet

Complete this worksheet for your primary (confirmatory) hypothesis, then attach it together with the output of your power-analysis script (R or Python) to your proposal or pre-registration. Example R scripts for common designs are in `scripts/` (see the Step 09 README).

> **Rule of thumb for this worksheet:** every number must have a source. If an effect size comes from a published study, give the citation and DOI and show how you converted it. If it is the smallest effect you care about, say why that size matters for your question.

---

## 1. Study design

| Field | Your entry |
|---|---|
| Study title | |
| Primary hypothesis (H1) | |
| Primary outcome and how it is measured | |
| Design | ☐ Two groups, between subjects  ☐ BACI (before/after × control/impact)  ☐ ACI (after only, control/impact)  ☐ Within subjects  ☐ Other: |
| Statistical test for H1 | |
| Unit of analysis (person, household, site…) | |
| Allocation ratio (e.g., 1:1) | |
| Software and script used | ☐ R  ☐ Python  ☐ G*Power  ☐ Other: |
| Script file name | |

---

## 2. Assumed effect size

| Field | Your entry |
|---|---|
| Effect size metric | ☐ Cohen's d  ☐ Cohen's f  ☐ Correlation r  ☐ Odds ratio / two proportions  ☐ Other: |
| Assumed value | |
| Source (author, year, journal) | |
| DOI | |
| Statistic reported in the source (e.g., means and SDs, t, F, r) | |
| How you converted it to your metric (formula) | |
| Smallest effect size of interest (SESOI) and why it matters | |
| Why you did not rely on a pilot-study estimate alone | |

*Tip: pilot studies are too small to estimate an effect size precisely. Use them to test procedures, completion time, and the reliability of your measures; base the effect size on published evidence or on your smallest effect size of interest.*

---

## 3. Error rates and inflation for attrition

| Field | Your entry |
|---|---|
| Alpha (Type I error rate) | |
| One- or two-sided test | ☐ Two-sided  ☐ One-sided (justify below) |
| Target power (1 − β) | |
| Required N from the power analysis (per group) | |
| Required N from the power analysis (total) | |
| Expected attrition between waves (%) and source | |
| Expected non-response / exclusions (%) and source | |
| Inflated N to recruit = N ÷ ((1 − attrition) × (1 − non-response)) | |

Justification for any non-default choice (e.g., one-sided test, alpha other than .05, power other than .80):

______________________________________________

---

## 4. Sensitivity analysis

Report the sample size your design needs across a plausible range of effect sizes, or the smallest effect your feasible N can detect.

| Assumed effect size | Required N per group | Required N total | Notes |
|---|---|---|---|
| | | | |

Smallest effect detectable with the N you can realistically recruit (at your alpha and power): _______________

---

## 5. Script output

Paste the key lines printed by your script (or attach the full output as a separate page).

*Paste the output here.*

---

## 6. Checklist before you attach this worksheet

- [ ] The effect size has a real, checkable source (citation and DOI), or a stated smallest effect size of interest.
- [ ] I showed how a reported statistic was converted to d, f, or r.
- [ ] Alpha, sidedness, and power are stated and justified.
- [ ] The recruited N is inflated for attrition and non-response.
- [ ] A sensitivity analysis shows how N changes across plausible effect sizes.
- [ ] The script and its output are attached, with the package versions printed by the script.

---

*Cross-reference: `README.md` · `scripts/` · `../Step_04_Study_Architecture_and_Experimental_Design/design_decision_matrix.md` · `../Step_05_Preregistration_and_Open_Science/preregistration_template.md`*
