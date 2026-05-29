# Quality Control Checklist for Survey Instruments
## Step 6 — Instrument Construction

> This checklist should be completed in three passes: **(1)** after drafting the instrument, **(2)** after cognitive interviews, and **(3)** after the pilot study. Retain dated copies of all three passes in this folder.

---

## Stage 1 — Pre-Cognitive-Interview Review (Internal)

### 1A — Matrix completeness
- [ ] Every item has an entry in the Survey Design Matrix
- [ ] Every item maps to ≥ 1 research question
- [ ] Every item has a documented scale source OR construction rationale
- [ ] Items with no analytic justification have been removed or moved to a "cut list"
- [ ] The variable summary table lists every IV, DV, covariate, and random effect
- [ ] The respondent burden audit is complete and total time is within target range

### 1B — Item wording
- [ ] No double-barrelled items (asking two things at once)
- [ ] No leading questions (implying a preferred answer)
- [ ] No loaded language (emotionally charged phrasing)
- [ ] Technical jargon is defined or avoided
- [ ] Negatively worded items are flagged (for reverse-scoring in analysis)
- [ ] Reading level is appropriate for target population (aim for ≤ Grade 8 for general public)
- [ ] Items have been translated and back-translated if multilingual delivery is planned

### 1C — Response options
- [ ] All Likert scales have clearly labelled endpoints and a defined number of points (5 or 7 recommended)
- [ ] All response options are exhaustive (include "other" or "not applicable" where needed)
- [ ] All response options are mutually exclusive
- [ ] Sensitive demographic items include "prefer not to say" and inclusive categories
- [ ] No "double-negative" options (e.g., "Not unfamiliar")
- [ ] Skip logic / branching is documented and tested

### 1D — Order and structure
- [ ] Demographics are placed at the **end** of the survey
- [ ] Open-ended items appear **before** Likert items if measuring the same construct
- [ ] Within-block randomization is planned where appropriate
- [ ] Randomization plan is documented (for pre-registration)
- [ ] Survey begins with engaging, low-sensitivity items to reduce dropout
- [ ] Attention checks are included (≥ 2 for surveys > 10 min)
- [ ] Attention checks are appropriately framed for the research relationship (community vs. online panel)

### 1E — Platform / mode checks
- [ ] Survey renders correctly on mobile devices
- [ ] All media files (images, audio, video) load and play correctly
- [ ] Forced-response fields are used only where non-response is truly unacceptable
- [ ] Progress bar is enabled (reduces dropout)
- [ ] Consent page cannot be skipped
- [ ] Response data is stored securely (compliant with IRB / GDPR / PIPEDA as applicable)
- [ ] Participant ID assignment is automated and anonymized

---

## Stage 2 — Cognitive Interview Log

> Conduct cognitive interviews with **5–10 participants** from the target population (not colleagues). Use think-aloud protocol: ask participants to verbalize their thought process as they answer each item.

### Cognitive interview protocol
1. Introduce the session: *"I'm going to ask you to fill out this survey and talk out loud as you do. There are no right or wrong answers — I want to understand how you interpret each question."*
2. For each item, probe:
   - *"What does this question mean to you?"*
   - *"How did you decide on that answer?"*
   - *"Was anything confusing or unclear?"*
   - *"Did any of the answer options not fit your situation?"*
3. Record issues in the log below.

### Cognitive interview issue log

| Item ID | Participant # | Issue type | Verbatim quote (if available) | Resolution |
|---|---|---|---|---|
| | | ☐ Comprehension <br>☐ Recall <br>☐ Judgment <br>☐ Response mapping <br>☐ Sensitive / uncomfortable | | ☐ Reworded <br>☐ Response options changed <br>☐ Item cut <br>☐ No change — documented |
| | | | | |

### Post-cognitive-interview sign-off
- [ ] All comprehension failures addressed
- [ ] All response-mapping failures addressed
- [ ] Sensitive items reviewed with community liaison (if applicable)
- [ ] Revised instrument saved as `v0.3_post_cognitive_interview_YYYY-MM-DD`

---

## Stage 3 — Pilot Study Protocol

> Run a pilot with **30–50 participants** from the target population (or as many as power analysis allows) before full data collection. The pilot tests: comprehension at scale, timing, dropout, data quality, and preliminary psychometric properties.

### 3A — Pilot data collection checks
- [ ] Pilot sample matches target population demographics
- [ ] Pilot was conducted in the same mode as the main study
- [ ] Consent was re-obtained for pilot participants (they cannot participate again in the main study)
- [ ] Pilot data is stored separately and clearly labelled

### 3B — Timing and dropout
- [ ] Median completion time matches estimated burden (within ±25%)
- [ ] Page-level drop-off rates have been reviewed
- [ ] Items / pages with high drop-off have been revised or removed

### 3C — Attention check performance
- [ ] Proportion passing all attention checks: _____%  (flag if < 80%)
- [ ] Speeders (completion time < [expected × 0.4]): _____% (flag if > 5%)
- [ ] Straight-liners (same response to ≥ 90% of Likert items): _____% (flag if > 3%)
- [ ] Decision rule for exclusion is documented and pre-registered

### 3D — Data quality flags
| Flag type | Threshold | Observed rate | Action |
|---|---|---|---|
| Failed ≥ 1 attention check | Flag for review | ___% | |
| Completion time < threshold | Flag/exclude | ___% | |
| Straight-lining (Likert) | Flag for review | ___% | |
| Item non-response rate > 10% | Review item | List items: | |
| Open-ended = gibberish / copy-paste | Exclude | ___% | |

### 3E — Preliminary psychometrics (for scale items)
- [ ] Internal consistency (Cronbach's α or McDonald's ω) computed for each subscale
- [ ] Acceptable threshold: α / ω ≥ 0.70 for exploratory; ≥ 0.80 for confirmatory
- [ ] Items with item-total correlation < 0.30 flagged for review
- [ ] Confirmatory factor analysis (CFA) fit indices reviewed (if using established scale):
  - CFI ≥ 0.95
  - RMSEA ≤ 0.06
  - SRMR ≤ 0.08
- [ ] Any items revised based on psychometric pilot results are documented

### 3F — Open-ended content check
- [ ] Random sample of 20% of open-ended responses reviewed for:
  - Relevance to the question
  - Range of responses (not all identical)
  - Absence of offensive / harmful content
  - Absence of identifying information (PII)
- [ ] Thematic coding scheme drafted from pilot responses

### 3G — Post-pilot sign-off
- [ ] All Stage 3 issues documented with resolutions
- [ ] Final instrument saved as `v1.0_final_pre-registration_YYYY-MM-DD`
- [ ] Instrument version locked and linked to pre-registration
- [ ] Data dictionary completed and archived

---

## Stage 4 — During Data Collection (Ongoing QC)

- [ ] Weekly spot-checks of incoming data for data quality flags
- [ ] Alert thresholds set in survey platform (e.g., flag if completion time drops sharply)
- [ ] Community liaison or field enumerators trained on flagging unusual respondent behaviour
- [ ] Any mid-study changes to instrument are documented with date, rationale, and effect on data comparability

---

## Stage 5 — Post-Collection Data Cleaning Checklist

- [ ] Exclusion criteria applied consistently per pre-registered decision rule
- [ ] All exclusions documented in a separate log with reason codes
- [ ] Missing data pattern examined (MCAR / MAR / MNAR assessment)
- [ ] Reverse-scored items recoded before analysis
- [ ] Composite scale scores computed per pre-registered formula
- [ ] Data dictionary shared with all analysts
- [ ] Raw data and cleaned data stored separately (raw data never overwritten)
- [ ] Data cleaning script version-controlled (Git)

---

## References

- Abbey, J. D., & Meloy, M. G. (2017). Attention by design: Using attention checks to detect inattentive respondents and improve data quality. *Journal of Operations Management*, 53–56, 63–70.
- Beatty, P. C., & Willis, G. B. (2007). Research synthesis: The practice of cognitive interviewing. *Public Opinion Quarterly*, 71(2), 287–311.
- Galesic, M., & Bosnjak, M. (2009). Effects of questionnaire length on participation and indicators of response quality. *Public Opinion Quarterly*, 73(2), 349–360.
- Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis. *Structural Equation Modeling*, 6(1), 1–55.
- Miller, J. (2025). Inclusive survey design. *Survey Practice*.
- Tourangeau, R., Rips, L. J., & Rasinski, K. (2000). *The Psychology of Survey Response*. Cambridge University Press.
- Willis, G. B. (2005). *Cognitive Interviewing: A Tool for Improving Questionnaire Design*. SAGE.
