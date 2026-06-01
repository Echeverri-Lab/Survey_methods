# Methods Section Template for Survey Research Papers

This is a fill-in-the-blank ("mad-libs") template for writing a rigorous methods section in a survey research paper. Replace all `[BRACKETED]` placeholders with your study-specific information. Delete any sections that do not apply to your design.

---

## Participants and Recruitment

We recruited `[N target]` participants through `[platform or method: e.g., Prolific Academic, in-person intercept at X location, partner organization mailing list]` between `[start date]` and `[end date]`. Participants were eligible if they `[eligibility criteria, e.g., were residents of X country, were ≥18 years old, had visited Y area in the past 5 years]`. `[Any exclusion criteria at recruitment stage]`. The study was approved by the `[IRB/BREB name]` (Protocol No. `[XXXX]`, approved `[date]`) and pre-registered on `[OSF/AsPredicted/ClinicalTrials.gov]` (`[link]`). All participants provided informed `[electronic/written]` consent prior to participation and received `[compensation type and amount, e.g., £X.XX via Prolific, equivalent to ≥£X/hr]`.

---

## Survey Instrument

The survey was administered in `[language(s)]` using `[platform, e.g., Qualtrics, KoBoToolbox]`. `[If translated: The instrument was translated from [source language] to [target language] following a forward–back-translation protocol (Edunov et al., 2018) and cognitively pre-tested with [N] native speakers (Willis, 2018); see Supplementary Materials S1 for the translation log.]`

The survey comprised the following sections, administered in this order:
1. `[Section 1 name and purpose, e.g., Consent and eligibility screener]`
2. `[Section 2 name and purpose, e.g., Wildlife tolerance scale (X items; Browne-Nuñez et al., 2015)]`
3. `[Section 3 name and purpose, e.g., Value orientation scale (X items; Manfredo et al., 2009)]`
4. `[Section 4 name and purpose, e.g., Open-ended word association task]`
5. `[Section 5 name and purpose, e.g., Sociodemographic questions (placed last to minimize stereotype threat; Steele & Aronson, 1995)]`

`[If items were randomized: Item order within [section name] was randomized across respondents to control for order effects.]` The full instrument is provided in Supplementary Materials `[SX]`.

---

## Sampling and Design

`[Choose and complete the applicable paragraph(s).]`

**Probability / quota sample:** We used a `[stratified / quota / random]` sampling design targeting a sample representative of `[population]` with respect to `[demographic variables, e.g., age, gender, region]`. Quotas were set based on `[census year and source]`.

**Non-probability / convenience sample:** We used a `[convenience / snowball / purposive]` sampling approach. Given the `[exploratory / theory-generating / interpretive]` aim of this study (see Step 1), a probability sample was not feasible `[or: was not required to answer the research question]`. We document this limitation candidly in the Discussion.

**Experimental design:** `[If applicable: Participants were randomly assigned to one of [N] conditions: [condition 1 description] vs. [condition 2 description]. Randomization was implemented via [Qualtrics randomizer / coin flip / block randomization]. Condition assignment was `[single-blind / double-blind]`.]`

---

## Data Collection Quality Controls

To ensure data quality, we applied the following controls, pre-specified in our pre-registration: `[list only those that apply]`

- Qualtrics bot detection and reCAPTCHA (score threshold: `[X]`)
- Duplicate IP and device fingerprint screening
- Embedded HTML link-engagement check for `[external content]`
- Minimum completion time threshold of `[X]` seconds, derived from `[pilot median completion time / 3]`
- `[N]` attention check items (e.g., "`[item wording]`"); participants failing `[≥1 / ≥2]` check(s) were excluded

---

## Data Cleaning and Exclusions

Raw data were exported from `[platform]` and processed in `[R version X.X / Python X.X]`. Exclusions were applied in the following sequence:

| Step | Criterion | N excluded | N remaining |
|---|---|---|---|
| 0 | Raw export | — | `[N]` |
| 1 | Non-consent / ineligibility | `[N]` | `[N]` |
| 2 | Bot / fraud flags | `[N]` | `[N]` |
| 3 | Speeders / attention failures / straightliners | `[N]` | `[N]` |
| 4 | `[Any additional criterion]` | `[N]` | `[N]` |
| **Final** | **Analysis sample** | — | **`[N]`** |

`[Missing data: Missing responses on [scale/outcome] were handled by [listwise deletion / multiple imputation using the mice package (van Buuren & Groothuis-Oudshoorn, 2011)]; the missing-completely-at-random assumption was [tested using / not tested; rationale].]`

---

## Measures

### `[Scale 1 Name]`
`[Construct]` was measured using the `[scale name]` (`[citation]`), a `[N]`-item scale employing a `[X]`-point Likert response format ranging from 1 (*Strongly Disagree*) to `[X]` (*Strongly Agree*). `[Describe any modifications verbatim.]` In our sample, the scale showed `[good / acceptable]` internal consistency (Cronbach's α = `[X]`, 95% CI `[X–X]`; McDonald's ω = `[X]`).

### `[Scale 2 Name]`
`[Repeat as above.]`

### `[Open-ended / qualitative item]`
Participants responded to the following open-ended prompt: "`[exact wording]`". Responses were coded `[inductively / deductively / using a hybrid approach]` by `[N]` coders `[independently / with consensus discussion]`. The final codebook (Supplementary Materials S`[X]`) contains `[N]` parent codes and `[N]` child codes. Inter-rater reliability was assessed on a `[X]%` subset using `[Cohen's κ / Krippendorff's α]` (`[statistic]` = `[value]`; `[Lombard et al., 2002]`), indicating `[excellent / good / fair]` agreement. Disagreements were resolved `[by discussion / by a third coder]`.

---

## Statistical Analysis

All analyses were conducted in `[R version X.X (R Core Team, YEAR) / Python X.X]` using the following packages: `[list packages and versions]`. The analysis plan was pre-registered at `[link]`; deviations from the pre-registered plan are noted in the Results.

`[Describe each analysis in 1–2 sentences, e.g.:]`

Scale reliability was assessed using Cronbach's α and McDonald's ω via the `psych` package (Revelle, `[YEAR]`). Confirmatory factor analysis (CFA) was conducted in `lavaan` (`[Rosseel, 2012]`); model fit was evaluated using CFI (≥0.95), RMSEA (≤0.06), and SRMR (≤0.08). `[Group comparisons / regression / SEM ...]` Effect sizes are reported as `[partial η² / Cohen's d / odds ratios / standardized β]` with 95% confidence intervals throughout; *p*-values are reported as supplementary information.

---

## References *(for methods section citations)*
- Lombard, M., Snyder-Duch, J., & Campanella Bracken, C. (2002). Content analysis in mass communication. *Human Communication Research*, 28(4), 587-604.
- Rosseel, Y. (2012). lavaan: An R package for structural equation modeling. *Journal of Statistical Software*, 48(2), 1–36.
- Steele, C. M., & Aronson, J. (1995). Stereotype threat and the intellectual test performance of African Americans. *Journal of Personality and Social Psychology*, 69(5), 797–811.
- van Buuren, S., & Groothuis-Oudshoorn, K. (2011). mice: Multivariate Imputation by Chained Equations in R. *Journal of Statistical Software*, 45(3).
- Willis, G. B. (2018). *Cognitive Interviewing: A Tool for Improving Questionnaire Design*. SAGE.