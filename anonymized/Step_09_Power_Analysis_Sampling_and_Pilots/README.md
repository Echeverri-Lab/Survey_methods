# Step 09 — Power Analysis, Sampling Design, and Pilot Studies

> *"A provocation-oriented study contributes when its scope is named clearly; what undermines a study is not modest claims but oversold ones."*  
> — Survey Design curriculum, Step 9

This folder covers the quantitative foundations of your survey rollout: defining your target population, justifying your sample size through power analysis, selecting an appropriate sampling frame, and running pilot studies to ensure your instruments work as intended.

---

## Folder structure

```
Step_09_Power_and_Sampling/
├── README.md                              ← this file
│
└── scripts/
    └── power_example.py                   ← Example scripts to calculate sample sizes and run power simulations
```

---

## 1. Power Analysis
Researchers should conduct a power analysis *before* data collection. While simple regressions may require relatively small samples, Structural Equation Modeling (SEM) and other complex models demand more robust datasets. Common rules of thumb recommend 10–20 observations per estimated parameter, or a minimum $N \geq 200$ for SEM (Bonett & Wright, 2000).

A power analysis is only as good as its assumed effect size. Derive effect sizes from prior studies in the same system, or ideally from a pilot study. When no estimate exists, run **sensitivity analyses** across a plausible range to understand how capable your design is at detecting different magnitudes of effect.

### Recommended Computational Tools:
- **R Packages**: 
  - [`pwr`](https://cran.r-project.org/web/packages/pwr/index.html) for standard tests (t-tests, ANOVA, linear models).
  - [`simr`](https://cran.r-project.org/web/packages/simr/index.html) for power analysis in Generalized Linear Mixed Models (GLMMs) via simulation.
  - [`simsem`](https://cran.r-project.org/web/packages/simsem/index.html) for simulating data and assessing power in complex Structural Equation Models (SEM).
- **Python Packages**:
  - [`statsmodels.stats.power`](https://www.statsmodels.org/stable/stats.html#power-and-sample-size-calculations) for standard analytical power solving.
  - [`pingouin.power`](https://pingouin-stats.org/build/html/api.html#power-analysis) for an extremely user-friendly API for classic experimental designs.
- **Standalone/GUI**:
  - **G*Power**: A classic, visual tool bridging ecological and psychometric power calculations (Kang, 2021).
  - **[DeclareDesign](https://declaredesign.org/)**: A fantastic R framework for diagnosing the statistical properties of your research design (power, bias, coverage) before implementation.

## 2. Sampling Design
Sampling design starts with being explicit about what population you want to speak to, and being honest when you cannot draw a clean circle around it. 

- **Probability vs. Non-Probability:** Probability sampling supports generalizable inference, which is where formal power and frame logic apply most cleanly. However, many human-dimension studies are exploratory, theory-generating, or interpretive. In these cases, it is valid to use **non-probability schemes** (convenience, quota, snowball, intercept).
- **Key Requirements for Non-probability:** 
  1. State the inferential goal honestly (Description vs. Hypothesis Generation vs. Group Comparison—see Step 1).
  2. Document the non-probability scheme definitively.
  3. Discuss bias candidly in the limitations. 
- **Online Platforms & Representation:** Much existing literature relies on "WEIRD" (Western, Educated, Industrialized, Rich, Democratic) populations (Schulz et al., 2018). While online panels reduce geographic bias, platforms like MTurk are increasingly compromised by bots and scammer farms targeting compensated surveys (Kay, 2025). Vetted platforms like Prolific are currently more reliable (Douglas et al., 2023). 
- **Quality Control:** Regardless of your platform, build in attention checks, eligibility re-confirmation, timing thresholds, and IP screening using **pre-registered exclusion criteria**.
- **Place-based Studies:** For hard-to-reach or place-based communities, online panels fail. Use in-person intercepts, partner organizations, trusted gatekeepers, or snowball referrals.

## 3. Pilot Studies
Pilot studies bridge instrument design and credible inference, functioning as a necessary rehearsal rather than simply a precursor. The **pilot → revise → re-pilot** loop is a core phase of the study itself.

1. **Cognitive Interviewing (~8–15 participants):** Identify wording, translation, and cultural-fit problems by having a small, representative group "think aloud" as they take the survey (Willis et al., 2018).
2. **Psychometric & Logistics Check (~50–100 participants):**
   - Yields realistic completion-time and dropout estimates. 
   - Allows psychometric validation: evaluate item-total correlations, scale reliability (Cronbach's $\alpha$ or McDonald's $\omega$), and factor structure. *Tip: Use the [`psych`](https://cran.r-project.org/web/packages/psych/index.html) or `lavaan` package in R, or `pingouin` and `factor_analyzer` in Python to automate these checks.*
   - Generates local effect-size estimates feeding back into your power analysis (far more defensible than using a generic Cohen's $d = 0.5$).
3. **Contingency Planning:** Pilots routinely surface problems requiring action—scales that fail to load, manipulations that produce negligible effects, attention-check failure rates that flag sampling problems, or fatigue-indicating completion times. Plan for these failures, report pilot decisions transparently, and refine your instrument.

---

## References
- Bonett, D. G., & Wright, T. A. (2000). Sample size requirements for estimating Pearson, Kendall and Spearman correlations. *Psychometrika*, 65(1), 23-28.
- Douglas, B. D., Ewell, P. J., & Brauer, M. (2023). Data quality in online human-subjects research: Comparisons between MTurk, Prolific, CloudResearch, Qualtrics, and SONA. *PLOS One*, 18(3), e0279720.
- Kang, H. (2021). Sample size determination and power analysis using the G*Power software. *Journal of Educational Evaluation for Health Professions*, 18.
- Kay, J. (2025). (Reference on MTurk bot farms and data degradation).
- Schulz, J. F., Bahrami-Rad, D., Beauchamp, J. P., & Henrich, J. (2018). The origins of WEIRD psychology. *Science*.
- Willis, G. B. (2018). *Cognitive Interviewing: A Tool for Improving Questionnaire Design*. SAGE.
