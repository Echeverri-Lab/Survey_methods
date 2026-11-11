# Step 09 — Power Analysis, Sampling Design, and Pilot Studies

> *"A provocation-oriented study contributes when its scope is named clearly; what undermines a study is not modest claims but oversold ones."*  
> — Survey Design curriculum, Step 9

This folder covers the quantitative foundations of your survey rollout: defining your target population, justifying your sample size through power analysis, selecting an appropriate sampling frame, and running pilot studies to ensure your instruments work as intended.

---

## Folder structure

```
Step_09_Power_Analysis_Sampling_and_Pilots/
├── README.md                              ← this file
├── power_analysis_template.md / .pdf      ← worksheet to attach to your proposal (fillable PDF)
│
└── scripts/
    ├── power_example_a_two_groups.R       ← (a) two conditions, between subjects (pwr)
    ├── power_example_b_baci.R             ← (b) BACI: before/after × control/impact (pwr + lme4 simulation)
    ├── power_example_c_aci.R              ← (c) ACI: after-only control/impact, clustered sites (pwr)
    ├── power_example_d_2x2_between_mediation.R ← (d) 2×2 message experiment: behaviour outcomes + mediation
    ├── power_example_e_sample_size_calculator_traits.R ← (e) sample size calculator: predicting an outcome from traits (no intervention)
    └── power_example.py                   ← Python placeholder
```

---

## 1. Power Analysis
Researchers should conduct a power analysis *before* data collection. While simple regressions may require relatively small samples, Structural Equation Modeling (SEM) and other complex models demand more robust datasets. Common rules of thumb recommend 10–20 observations per estimated parameter, or a minimum $N \geq 200$ for SEM (Bonett & Wright, 2000).

A power analysis is only as good as its assumed effect size. Derive effect sizes from prior studies in the same system, or ideally from a pilot study. When no estimate exists, run **sensitivity analyses** across a plausible range to understand how capable your design is at detecting different magnitudes of effect.

> **Worked ecological example.** Starcevich, Burgess, & Uhrin (2025) illustrate this trade-off directly for environmental monitoring: they show how sample size, revisit frequency, and Type I error rate ("test size") jointly determine the power of a long-term marine debris monitoring survey, and how optimizing one dimension (e.g., minimizing sites visited) can silently erode power to detect a real trend. This is a useful worked template for any repeated-measures or longitudinal environmental survey design in this repository.

### Worked examples in R (start here)

The `scripts/` folder has one commented R script per design. Each script explains, step by step, how to choose and justify the effect size (meta-analyses, converting reported statistics to *d* or *f*, the smallest effect size of interest, and why pilot effect sizes are unreliable), how to set alpha and power, and how to inflate the sample for attrition and non-response. Each one ends with a sensitivity table and a sentence you can adapt for your proposal.

| Script | Design | Packages | What it prints |
|---|---|---|---|
| [`power_example_a_two_groups.R`](scripts/power_example_a_two_groups.R) | Two conditions (control vs. treatment), between subjects | `pwr` | N per group, N to recruit, sensitivity table, simulation check |
| [`power_example_b_baci.R`](scripts/power_example_b_baci.R) | BACI: everyone measured before and after; control vs. impact groups | `pwr`, `lme4` | N of completers and recruits, sensitivity to the pre–post correlation, mixed-model simulation |
| [`power_example_c_aci.R`](scripts/power_example_c_aci.R) | ACI: after-only, control vs. impact, respondents clustered in sites | `pwr` | N for 2 and 3 groups (*d* and *f*), design effect, sites needed, sensitivity table |
| [`power_example_d_2x2_between_mediation.R`](scripts/power_example_d_2x2_between_mediation.R) | Hypothetical 2×2 between-subjects message experiment (narrative vs. fact sheet × scientist vs. farmer messenger), with behavioural outcomes and mediation | `pwr` (+ base-R simulation) | Minimum detectable *d* with a fixed N, the same effect as *f*/partial η², why the interaction is exploratory, detectable petition-signing increases, Monte Carlo mediation power |
| [`power_example_e_sample_size_calculator_traits.R`](scripts/power_example_e_sample_size_calculator_traits.R) | **Sample size calculator** for an observational study with several predictors and no intervention (hypothetical: willingness to host a bird nest, predicted from the bird's plumage colour, pattern, and diet). Three versions: one rating per person; a fixed set of real species; designed trait profiles (conjoint) | `pwr`, `lme4` | N for one predictor's unique effect (Δ*R*², *f*²) vs. the overall test; why the number of SPECIES, not people, limits power when traits belong to species; respondents × profiles needed in a conjoint design |

To run a script, install [R](https://cran.r-project.org) (and optionally RStudio), open the file, edit the "YOUR ASSUMPTIONS" section, and click **Source** (or run `Rscript scripts/power_example_a_two_groups.R`). The scripts install `pwr` and `lme4` if they are missing. Record the numbers in [`power_analysis_template.pdf`](power_analysis_template.pdf) and attach the script output.

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

## Fillable PDF versions of the templates

Every template in this folder also comes as a fillable PDF next to the Markdown file. You do not need GitHub or Markdown to use them: open the PDF link below, click the download button, fill it in with the free Adobe Acrobat Reader (macOS Preview and web browsers also work), save, and attach it to your assignment.

| Template | Markdown source | Fillable PDF |
|---|---|---|
| Power Analysis Worksheet | [`power_analysis_template.md`](power_analysis_template.md) | [`power_analysis_template.pdf`](power_analysis_template.pdf) |

*The PDFs are generated from the Markdown with [`tools/make_fillable_pdfs.py`](../tools/make_fillable_pdfs.py); edit the Markdown, then rebuild the PDFs.*

---

## References
- Albers, C., & Lakens, D. (2018). When power analyses based on pilot data are biased: Inaccurate effect size estimators and follow-up bias. *Journal of Experimental Social Psychology*, 74, 187–195. https://doi.org/10.1016/j.jesp.2017.09.004
- Bergquist, M., Thiel, M., Goldberg, M. H., & van der Linden, S. (2023). Field interventions for climate change mitigation behaviors: A second-order meta-analysis. *Proceedings of the National Academy of Sciences*, 120(13), e2214851120. https://doi.org/10.1073/pnas.2214851120
- Bonett, D. G., & Wright, T. A. (2000). Sample size requirements for estimating Pearson, Kendall and Spearman correlations. *Psychometrika*, 65(1), 23-28.
- Braddock, K., & Dillard, J. P. (2016). Meta-analytic evidence for the persuasive effect of narratives on beliefs, attitudes, intentions, and behaviors. *Communication Monographs*, 83(4), 446–467. https://doi.org/10.1080/03637751.2015.1128555
- Douglas, B. D., Ewell, P. J., & Brauer, M. (2023). Data quality in online human-subjects research: Comparisons between MTurk, Prolific, CloudResearch, Qualtrics, and SONA. *PLOS One*, 18(3), e0279720.
- Fritz, M. S., & MacKinnon, D. P. (2007). Required sample size to detect the mediated effect. *Psychological Science*, 18(3), 233–239. https://doi.org/10.1111/j.1467-9280.2007.01882.x
- Kang, H. (2021). Sample size determination and power analysis using the G*Power software. *Journal of Educational Evaluation for Health Professions*, 18.
- Kay, C. S. (2025). Why you shouldn’t trust data collected on MTurk. Behavior Research Methods, 57(12), 340. https://doi.org/10.3758/s13428-025-02852-7
- Kraemer, H. C., Mintz, J., Noda, A., Tinklenberg, J., & Yesavage, J. A. (2006). Caution regarding the use of pilot studies to guide power calculations for study proposals. *Archives of General Psychiatry*, 63(5), 484. https://doi.org/10.1001/archpsyc.63.5.484
- Lakens, D. (2013). Calculating and reporting effect sizes to facilitate cumulative science: A practical primer for t-tests and ANOVAs. *Frontiers in Psychology*, 4, 863. https://doi.org/10.3389/fpsyg.2013.00863
- Lakens, D. (2022). Sample size justification. *Collabra: Psychology*, 8(1), 33267. https://doi.org/10.1525/collabra.33267
- Lakens, D., Scheel, A. M., & Isager, P. M. (2018). Equivalence testing for psychological research: A tutorial. *Advances in Methods and Practices in Psychological Science*, 1(2), 259–269. https://doi.org/10.1177/2515245918770963
- Nisa, C. F., Bélanger, J. J., Schumpe, B. M., & Faller, D. G. (2019). Meta-analysis of randomised controlled trials testing behavioural interventions to promote household action on climate change. *Nature Communications*, 10, 4545. https://doi.org/10.1038/s41467-019-12457-2
- Osbaldiston, R., & Schott, J. P. (2012). Environmental sustainability and behavioral science: Meta-analysis of proenvironmental behavior experiments. *Environment and Behavior*, 44(2), 257–299. https://doi.org/10.1177/0013916511402673
- Richard, F. D., Bond, C. F., & Stokes-Zoota, J. J. (2003). One hundred years of social psychology quantitatively described. *Review of General Psychology*, 7(4), 331–363. https://doi.org/10.1037/1089-2680.7.4.331
- Schulz, J. F., Bahrami-Rad, D., Beauchamp, J. P., & Henrich, J. (2018). The origins of WEIRD psychology. *Science*.
- Starcevich, L. A., Burgess, H., & Uhrin, A. V. (2025). Optimizing marine debris monitoring: Balancing statistical power and test size in survey design. *Ecological Indicators*. https://doi.org/10.1016/j.ecolind.2025.113807
- Willis, G. B. (2018). *Cognitive Interviewing: A Tool for Improving Questionnaire Design*. SAGE.

