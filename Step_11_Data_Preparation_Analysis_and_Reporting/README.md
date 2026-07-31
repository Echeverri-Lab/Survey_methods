# Step 11 — Data Preparation, Analysis, and Reporting

> *"Document every cleaning decision in a script and readme, preserve raw data unaltered, and version-control both."*  
> — Survey Design curriculum, Step 11

This step covers the full analytical pipeline from raw survey export to reported results: data cleaning and exclusion, psychometric validation, inferential analysis, qualitative coding, visualization, and reproducibility. All code, cleaning decisions, and analysis scripts should be version-controlled and deposited alongside a de-identified dataset (where IRB/BREB permits).

---

## Folder structure

```
Step_11_Data_Preparation_Analysis_and_Reporting/
├── README.md                          ← this file
├── data_cleaning_checklist.md         ← Step-by-step data cleaning decisions with R/Python code
├── analysis_reference_table.md        ← Research question → method → package → GitHub repo crosswalk
├── visualization_guide.md             ← Recommended visualizations by data type
│
└── notebooks/
    └── example_analysis.py            ← Example Python analysis notebook
```

---

## 1. Data Cleaning

Data cleaning is not a preliminary task — it is an analytic decision with direct implications for inference. Every exclusion must be pre-specified, documented, and reproducible. Always preserve the unaltered raw data file; all cleaning should happen in a versioned script.

**Cleaning order matters.** Apply exclusions in this sequence to avoid post-hoc rationalization:

1. **Ineligibility:** Non-consenters → failed eligibility screeners → metadata contradictions (e.g., IP geolocation inconsistent with eligibility country).
2. **Bot and fraud detection:** Platform controls (Qualtrics bot detection, reCAPTCHA), duplicate IP/device fingerprint flags, embedded HTML link-engagement checks.
3. **Low-quality responses:** Speeders (below pilot-derived threshold), attention-check failures, straightliners (same response to all Likert items).
4. **AI-generated text:** Flag open-ended responses exhibiting generic phrasing, near-identical structure across respondents, or inconsistency with closed items (Naito et al., n.d.). Tools such as `GPTZero` or perplexity/burstiness metrics can assist, but human review is necessary.
5. **Missing data:** After exclusions, decide in advance how missingness will be handled — listwise deletion, pairwise deletion, or multiple imputation (Vaske, 2019).

See `data_cleaning_checklist.md` for annotated R and Python code.

### 1b. Data Quality Diagnostics — 2026 Evidence Update

- **Response-format choices affect data quality directly.** Experimental work on memes/emoji response scales in web surveys found measurable effects on multimodal cognitive effort and data quality relative to standard Likert formats — a caution against novel visual response formats without piloting ("Using Memes and Emoji-Scales in a Web Survey," 2024).
- **Scale direction (ascending vs. descending) is not a neutral design choice.** A dedicated study on scale direction found it measurably affects response data quality, reinforcing the general survey-design principle of testing item/scale formatting choices rather than assuming they are interchangeable ("The Impact of Scale Direction on Data Quality," 2025).
- **Interviewer-respondent rapport and demographic match matter for data quality.** In the NESDA study, interviewer and respondent sociodemographic characteristics and interpersonal rapport jointly predicted data quality in interviewer-administered surveys — relevant for any in-person or phone administration in this repository's Step 10 guidance (Interviewer and Respondent Sociodemographic Characteristics, Rapport, and Their Joint Impact on Data Quality in the NESDA Study, 2025).
- **Incentive structure affects data quality, not just response rate.** A field experiment on guaranteed incentives vs. prize drawings in a web survey of college students on sensitive topics found effects on both participation *and* data quality/cost — a reminder that incentive-design decisions (see Step 10) have downstream implications for the analysis stage covered here (Guaranteed Incentives and Prize Drawings, 2023).
- **Group-level data-quality disparities should be checked, not assumed absent.** A study explicitly testing for racial differences in survey data quality is a useful methodological check to replicate in any survey with diverse respondent demographics before pooling data across groups ("Do Racial Differences Exist in Survey Data Quality?", 2025).

---

## 2. Reliability, Dimensionality, and Assumption Checking

### Scale Reliability
- **Cronbach's α**: Appropriate when tau-equivalence holds (i.e., all items contribute equally to the construct).
- **McDonald's ω**: Preferred when tau-equivalence is violated — a more defensible default for most socio-ecological scales (Tavakol & Dennick, 2011).
- **R**: `psych::alpha()`, `psych::omega()`, `MBESS::ci.reliability()`
- **Python**: `pingouin.cronbach_alpha()`, `factor_analyzer`

### Factor Analysis
- **EFA** (Exploratory): Use when scale structure is uncertain. Extract using parallel analysis; rotate obliquely (oblimin or promax) unless factors are theoretically orthogonal.
- **CFA** (Confirmatory): Use to test a pre-specified model. Report CFI (≥0.95), RMSEA (≤0.06), SRMR (≤0.08).
- **Measurement invariance**: Configural → metric → scalar invariance testing must precede multi-group comparisons (Putnick & Bornstein, 2016).
- **R**: `lavaan`, `semTools`, `psych`
- **Python**: `semopy`, `factor_analyzer`

### Assumption Checks
Before modeling: normality (Q-Q plots, Shapiro–Wilk), homogeneity of variance (Levene's test, residual plots), independence. Decide in advance how violations will be handled (transformation, robust SE, non-parametric equivalent).

---

## 3. Inferential Analysis

| Research question | Recommended method | Key considerations | R packages | Python packages |
|---|---|---|---|---|
| Group difference (2 groups, continuous) | t-test, Wilcoxon rank-sum | Check normality; Wilcoxon for ordinal/non-normal | `stats`, `coin` | `scipy.stats`, `pingouin` |
| Group difference (3+ groups, continuous) | ANOVA, Kruskal-Wallis | Post-hoc correction (Tukey, Bonferroni) | `stats`, `emmeans` | `pingouin`, `statsmodels` |
| Group difference (categorical associations) | Chi-squared test, Fisher's exact test | Expected frequencies > 5 for Chi-squared; use Fisher's otherwise | `stats` | `scipy.stats` |
| Association between variables | Pearson/Spearman correlation | Ordinal data → Spearman or polychoric | `psych`, `Hmisc` | `pingouin`, `scipy.stats` |
| Prediction (continuous outcome) | OLS regression | Check residuals, VIF for multicollinearity | `lm()`, `car`, `performance` | `statsmodels`, `sklearn` |
| Prediction (binary outcome) | Logistic regression | Report odds ratios + 95% CI | `glm()`, `MASS` | `statsmodels`, `sklearn` |
| Prediction (ordinal outcome) | Ordinal logistic regression | Proportional odds assumption | `MASS::polr`, `ordinal` | `statsmodels` |
| Complex causal pathways | SEM / path analysis | Fit indices (CFI, RMSEA, SRMR); bootstrapped indirect effects | `lavaan`, `semPlot` | `semopy` |
| Multilevel / nested data | Mixed-effects models | Random intercepts and/or slopes | `lme4`, `lmerTest` | `statsmodels`, `pymer4` |

**Always report effect sizes** (partial η², Cohen's *d*, odds ratios, standardized β) and confidence intervals alongside *p*-values (Sun et al., 2010). Statistical significance alone does not convey practical relevance.

See `inferential_analysis_table.md` for an expanded set of inferential analyses, their assumptions, and compatible R packages.

---

## 4. Qualitative and Mixed-Methods Analysis

**Inductive vs. Deductive Coding:**
- **Inductive (bottom-up):** Codes and themes are derived directly from the data without trying to fit them into a pre-existing coding frame or researcher's preconceptions.
- **Deductive (top-down):** driven by the researcher's theoretical or analytic interest, where data is coded to fit into a pre-existing coding framework.

| Approach | Orientation | Software | Key use case |
|---|---|---|---|
| Reflexive Thematic Analysis | Inductive/hybrid | NVivo, MAXQDA, ATLAS.ti | Flexible; most common in socio-ecological surveys |
| Content Analysis | Deductive | Any + codebook | Quantifying code frequencies; comparing across groups |
| Grounded Theory | Fully inductive | NVivo, MAXQDA | Theory generation from data |
| Sentiment Analysis | Computational | R (`tidytext`, `sentimentr`), Python (`VADER`, `TextBlob`, `transformers`) | Word-association tasks; large open-text corpora |

**Inter-rater reliability (IRR):** Use multiple coders wherever possible. Report Cohen's κ for two coders with nominal categories, or Krippendorff's α for interval scales, multiple coders, or missing data (Lombard et al., 2002).
- **R**: `irr::kappa2()`, `kripp.alpha()`
- **Python**: `sklearn.metrics.cohen_kappa_score`, `krippendorff` package

**NLP and LLMs:** NLP and Large Language Models increasingly scale qualitative insights (Hayes, 2025), but proceed with care:
- Confirm IRB/BREB clearance before sending participant text to external APIs (e.g., OpenAI, Anthropic).
- Consider fine-tuned classifiers (Wilson et al., 2022) over generative LLMs for well-defined coding tasks.
- LLMs perform better on surface coding than deep interpretive themes (Schroeder et al., 2025).
- Double-code a random subset and report agreement before relying on model codes.
- Document model name, version, parameters, and full prompts in supplementary materials.
- Consider privacy-preserving alternatives: local models (Ollama + Llama 3), institutional LLM sandboxes.

### 4b. LLM-Assisted Qualitative Coding — 2026 Evidence Update

A 2025–2026 wave of methodological papers directly tests where LLM-assisted
coding is (and is not) trustworthy for survey/qualitative data:

- **LLMs can approach human-level performance on latent content coding.** Across sentiment, political leaning, emotional intensity, and sarcasm, one large benchmarking study found LLM annotations frequently converge with trained human coders, though performance varies substantially by construct and text type — sarcasm and political leaning remain harder than sentiment ("Comparing Large Language Models and Human Annotators in Latent Content Analysis of Sentiment, Political Leaning, Emotional Intensity and Sarcasm," *Scientific Reports*, 2025).
- **Structured, step-by-step LLM workflows outperform ad hoc prompting.** A step-by-step thematic-analysis protocol using ChatGPT (mirroring Braun & Clarke's phases) improved transparency and reproducibility of LLM-assisted coding relative to unstructured prompting ("Thematic Analysis and Artificial Intelligence: A Step-by-Step Process for Using ChatGPT in Thematic Analysis," 2025).
- **LLMs can scale open-ended survey coding, including non-English text.** A case study coding German open-ended survey responses on survey motivation with LLMs demonstrates multilingual applicability of the same LLM-coding template used for English text — useful for the cross-national survey work in this repository ("Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation," 2025).
- **Qualitative researchers remain skeptical of "knowledge production" claims.** A qualitative interview study of researchers who use generative AI found consistent concern that LLMs can produce plausible-sounding text without genuine interpretive insight, reinforcing this README's guidance to treat LLM output as a coding *aid* requiring human validation, not an autonomous analyst ("It Might Be Able to Produce a Text, but It's Not Able to Produce Knowledge," 2025).
- **LLMs can support, not replace, large-scale qualitative data collection.** A case study using LLMs to collect and structure qualitative data at scale illustrates both the throughput gains and the need for validation loops when LLMs are used earlier in the pipeline (data collection/structuring) rather than only for post hoc coding ("Collecting Qualitative Data at Scale with Large Language Models: A Case Study," 2025).

---

## 5. Visualization

See `visualization_guide.md` for annotated examples and code. Quick reference:

| Data type | Recommended plot | Avoid | R package | Python package |
|---|---|---|---|---|
| Likert distributions | Diverging stacked bar | Pie chart | `likert`, `ggplot2` | `plotnine`, `matplotlib` |
| Word associations | Word cloud + stacked bar | Word cloud alone | `wordcloud2`, `ggplot2` | `wordcloud`, `plotnine` |
| Qualitative code transitions | Sankey diagram | Table alone | `ggsankey`, `ggalluvial` | `plotly`, `pySankey` |
| Multivariate constructs | Ordination biplot (PCA/NMDS) | — | `vegan`, `ggplot2` | `scikit-learn`, `plotnine` |
| Group comparisons | Boxplot with jitter + effect size | Bar chart of means | `ggplot2`, `ggdist` | `seaborn`, `plotnine` |
| SEM path diagram | Path diagram | — | `semPlot`, `lavaanPlot` | `semopy` |

---

## 6. Reproducibility

- Store **raw data unaltered**; all modifications happen in versioned scripts.
- Use **R Projects** or **Python virtual environments** with `renv` / `requirements.txt` to lock package versions.
- Write a **data dictionary / codebook** documenting every variable: name, label, type, response options, coding, and notes.
- Deposit cleaning and analysis code, codebook, and (where permitted) de-identified data in a public GitHub repository, linked to your pre-registration (see Step 5).

---

## Relevant External GitHub Repositories

| Repository | Description | Language |
|---|---|---|
| [easystats/easystats](https://github.com/easystats/easystats) | Meta-package suite for effect sizes, model checks, and reporting in R | R |
| [cran/lavaan](https://github.com/yrosseel/lavaan) | SEM, CFA, path analysis | R |
| [sinhrks/factor_analyzer](https://github.com/EducationalTestingService/factor_analyzer) | EFA and CFA in Python | Python |
| [raphaelvallat/pingouin](https://github.com/raphaelvallat/pingouin) | Statistical tests, reliability, correlations in Python | Python |
| [tidyverse/ggplot2](https://github.com/tidyverse/ggplot2) | The grammar of graphics for R | R |
| [mwsohn/likert](https://github.com/jbryer/likert) | Diverging stacked bar charts for Likert data | R |
| [davidsjoberg/ggsankey](https://github.com/davidsjoberg/ggsankey) | Sankey and Alluvial diagrams for R | R |
| [ropensci/tidytext](https://github.com/juliasilge/tidytext) | Text mining and sentiment analysis in R | R |
| [cjhutto/vaderSentiment](https://github.com/cjhutto/vaderSentiment) | VADER sentiment analysis (validated for short social text) | Python |
| [facebookresearch/flores](https://github.com/facebookresearch/flores) | Multilingual translation evaluation benchmarks | Python |
| [statsmodels/statsmodels](https://github.com/statsmodels/statsmodels) | Regression, time series, mixed models in Python | Python |
| [alexanderlerch/pyACA](https://github.com/irr-package) | Krippendorff alpha inter-rater reliability | Python |
| [pawjast/krippendorff](https://github.com/pbn4/krippendorff-alpha) | Krippendorff's alpha in Python | Python |

---

## References

- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77-101.
- Browne-Nuñez, C., et al. (2015). Toward an integrated understanding of the human dimensions of human-wildlife conflict. *Biological Conservation*, 184, 258-266.
- Cortés-Avizanda, A., et al. (2018). (Reference for factor analysis in socio-ecological surveys).
- "Collecting Qualitative Data at Scale with Large Language Models: A Case Study" (2025). https://doi.org/10.1145/3710947
- "Comparing Large Language Models and Human Annotators in Latent Content Analysis of Sentiment, Political Leaning, Emotional Intensity and Sarcasm" (2025). *Scientific Reports*. https://doi.org/10.1038/s41598-025-96508-3
- "Do Racial Differences Exist in Survey Data Quality?" (2025). https://doi.org/10.1007/s41996-025-00181-7
- Goodson, et al. (2025). (Reference for SEM linking biological and social data).
- "Guaranteed Incentives and Prize Drawings: Effects on Participation, Data Quality, and Costs in a Web Survey of College Students on Sensitive Topics" (2023). https://doi.org/10.1177/08944393231189853
- Hayes, A. (2025). (Reference for NLP scaling qualitative insights).
- "Interviewer and Respondent Sociodemographic Characteristics, Rapport, and Their Joint Impact on Data Quality in the NESDA Study" (2025). https://doi.org/10.1002/mpr.70090
- "It Might Be Able to Produce a Text, but It's Not Able to Produce Knowledge: Qualitative Researchers' Perspectives on the Use of Generative AI in Research" (2025). https://doi.org/10.1080/14780887.2025.2602816
- Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, 1(9), 389-399.
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). SAGE.
- Langhans, M., Echeverri, A., et al. (2025). (Reference for per-participant sentiment scoring in word-association tasks).
- Levitt, H. M., et al. (2018). Qualitative and quantitative reporting standards: APA JARS. *American Psychologist*, 73(1), 1.
- Lombard, M., Snyder-Duch, J., & Campanella Bracken, C. (2002). Content analysis in mass communication. *Human Communication Research*, 28(4), 587-604.
- Naito, R., Zhao, J., Naidoo, R., & Chan, K. M. (2023). Private and civic actions as distinct types of individual engagement for transforming the exotic pet trade. *People and Nature*, 5(5), 1526-1538.
- Norman, G. (2010). Likert scales, levels of measurement and the "laws" of statistics. *Advances in Health Sciences Education*, 15(5), 625-632.
- Putnick, D. L., & Bornstein, M. H. (2016). Measurement invariance conventions and reporting. *Developmental Review*, 41, 71-90.
- Schroeder, et al. (2025). (Reference for LLM surface vs. interpretive coding performance).
- Sun, S., Pan, W., & Wang, L. L. (2010). A comprehensive review of effect size reporting. *Psychological Methods*, 15(4), 424-428.
- Tavakol, M., & Dennick, R. (2011). Making sense of Cronbach's alpha. *International Journal of Medical Education*, 2, 53-55.
- Teel, T. L., & Manfredo, M. J. (2010). Understanding the diversity of public interests. *Environment and Behavior*, 42(4), 549-570.
- "The Impact of Scale Direction on Data Quality" (2025). https://doi.org/10.18148/srm/2025.v19i2.8384
- "Thematic Analysis and Artificial Intelligence: A Step-by-Step Process for Using ChatGPT in Thematic Analysis" (2025). https://doi.org/10.1177/16094069251333886
- Turner, B. S., & Astin, J. (2021). (Reference for grounded theory in survey contexts).
- "Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation" (2025). https://doi.org/10.18148/srm/2025.v19i3.8568
- "Using Memes and Emoji-Scales in a Web Survey: Experimental Assessment of Consequences for Multimodal Cognitive Effort and Data Quality" (2024). https://doi.org/10.1080/13645579.2024.2359474
- Vaske, J. J. (2019). *Survey Research and Analysis* (2nd ed.). Venture Publishing.
- Wilson, et al. (2022). (Reference for fine-tuned classifiers vs. generative LLMs for coding).

---

## 2026 revision — literature curation pass

Of 87 Step 11 candidates reviewed by abstract — by far the largest candidate
set of any Step — the great majority (~65) were rejected as off-topic
Structural Equation Modeling *application* papers (Theory of Planned
Behavior, protection motivation, ecosystem services, TAM/UTAUT, forestry,
tourism, entrepreneurship, etc.) that use SEM as an analytic tool in
unrelated substantive domains, offering no new *methodological* guidance
beyond what Section 3's existing SEM row already documents. Instead, this
pass focused on two clusters of genuinely new methodological evidence: (1)
five 2025 papers on LLM-assisted qualitative coding, added to a new Section
4b, directly extending this README's existing (but citation-sparse) LLM
guidance in Section 4 with concrete benchmarking and workflow evidence; and
(2) five 2023–2025 papers on survey data-quality diagnostics (response
format, scale direction, interviewer rapport, incentive structure, racial
data-quality disparities), added to a new Section 1b, extending the existing
data-cleaning checklist with evidence on *why* these specific design choices
matter for downstream data quality. Ecological data-quality papers
("Evaluating effects of data quality and variable weighting on habitat
suitability modelling," "Data quality issues in data used in species
distribution models") were reviewed but judged out of scope — they concern
species distribution modeling data pipelines, not human-subjects survey data
cleaning, and are more relevant to a conservation-biology methods repository
than this survey-design one. Several references above are cited by title
rather than full author lists because author metadata was not available in
the corpus records reviewed during this pass; author names should be
verified against source PDFs before final manuscript submission.
