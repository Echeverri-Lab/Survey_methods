# Step 12 — Writing Up a Survey Research Paper

> *"What undermines a study is not modest claims but oversold ones."*  
> — Survey Design curriculum, Step 12

Writing up survey research requires more than good prose — it requires adherence to established reporting standards so reviewers and replicators can evaluate and replicate the work. This step covers methods reporting, results presentation, discussion framing, reflexivity, and equitable communication of findings.

---

## Folder structure

```
Step_12_Writing_Survey_Research_Paper/
├── README.md                          ← this file
├── reporting_checklists.md            ← CHERRIES, SRQR, COREQ, JARS-Quant/Qual checklists
└── methods_section_template.md        ← Mad-libs style methods section template
```

---

## 1. Methods Reporting Standards

Use the appropriate reporting checklist for your study design. Reviewers increasingly expect these to be completed and submitted as supplementary materials.

| Standard | Scope | Citation |
|---|---|---|
| **CHERRIES** | Online/internet surveys | Eysenbach, 2004 |
| **SRQR** | Qualitative research (standards for reporting) | O'Brien et al., 2014 |
| **COREQ** | Qualitative interviews and focus groups | Tong et al., 2007 |
| **JARS-Quant** | Quantitative research (APA standard) | Levitt et al., 2018 |
| **JARS-Qual** | Qualitative research (APA standard) | Levitt et al., 2018 |
| **EQUATOR Network** | Umbrella resource for all health/social science reporting guidelines | equator-network.org |

See `reporting_checklists.md` for item-by-item checklists.

### Minimum Required Methods Documentation

Regardless of which standards apply, a survey paper methods section must report:

- [ ] Recruitment platform(s) and field dates
- [ ] Eligibility and screening criteria (verbatim)
- [ ] Full instrument items, or citation to published instrument with all modifications listed verbatim
- [ ] Language(s) used and full translation procedure (see Step 10)
- [ ] Sampling and experimental design (see Steps 4 and 9)
- [ ] Compensation type and amount (see Step 8)
- [ ] Ethics board name, approval date, and protocol number (see Step 8)
- [ ] Pre-registration link, or explicit rationale for its absence (see Step 5)
- [ ] Software and package versions used for analysis (see Step 11)
- [ ] Exclusion criteria and counts at each cleaning step (see Step 11)

**For qualitative coding additionally:**
- [ ] Coding orientation (inductive, deductive, or hybrid)
- [ ] Number of coders and their roles
- [ ] Software used (NVivo, MAXQDA, ATLAS.ti, etc.)
- [ ] How disagreements were resolved
- [ ] Inter-rater reliability statistic and value (Cohen's κ, Krippendorff's α)
- [ ] Final codebook (parent codes, child codes, definitions, exemplar quotes) as supplementary material

---

## 2. Results Reporting

### Quantitative Results
Results should be reported in this sequence:

1. **Response rate**: Use AAPOR standard definition (see Step 10). Report denominator clearly.
2. **Exclusion summary**: A brief table showing N removed at each cleaning step (see Step 11).
3. **Sample characteristics table**: Sociodemographic breakdown of the *analysis sample*, covering variables on which generalization claims rest. Compare to target population where known.
4. **Scale reliability**: Cronbach's α or McDonald's ω with 95% confidence intervals.
5. **Factor structure**: EFA/CFA results with fit indices (CFI, RMSEA, SRMR) and factor loadings.
6. **Inferential results**: Test statistics, degrees of freedom, *p*-values, **effect sizes with confidence intervals**. Do not report *p*-values alone (Sun et al., 2010).

### Qualitative Results
Choose one style and justify it:
- **Quantitative style**: Code frequencies, co-occurrence tables, inter-group comparisons of code frequency.
- **Interpretive style**: Narrative themes supported by illustrative quotes.

**Illustrative quotes**: Attribute by pseudonym with re-identifying details redacted, especially in small samples. Where feasible, member-check key interpretations with participants before publication.

---

## 3. Discussion, Limitations, and Reflexivity

### Discussion Structure
1. Briefly restate the research question and main finding (1 paragraph).
2. Interpret findings in relation to the theoretical framework and prior literature.
3. Address **plausible alternative explanations** — selection bias, social desirability, mode effects, unmeasured confounds — before settling on a preferred account.

### Limitations Paragraph
Name **specific threats** rather than generic boilerplate caveats. Build on the inferential-goal framing from Step 9. Examples of specific, non-boilerplate limitations:
- "The Prolific sample overrepresents urban, college-educated respondents relative to [target population]; effects on [construct] may be attenuated in rural subgroups."
- "Completion on mobile devices was XX%, which may have reduced engagement with image-based stimuli."
- "Social desirability cannot be ruled out on the pro-conservation items; alpha scores for [scale] were in the acceptable range but the distribution was left-skewed."

### Reflexivity
Reflexivity applies across the methods spectrum. A **positionality statement** should:
- Name how researcher identity, disciplinary training, and institutional context shaped construct choices, instrument design, and interpretation.
- For community-engaged or cross-cultural work, address how power asymmetries were attended to throughout the study (Secules et al., 2021).

---

## 4. Returning Findings and Equitable Communication

The published manuscript is rarely the only output. For community or place-based populations, plan accompanying outputs:

| Output type | Audience | Notes |
|---|---|---|
| Plain-language summary (1 page) | General public / community participants | Avoid jargon; include key findings and their implications |
| Community presentation | Partner organizations / study participants | Co-present with community partners where possible |
| Policy brief | Practitioners / managers / government | Action-oriented; specific recommendations |
| Co-authored products | Community researchers / translators / partner analysts | Follow ICMJE authorship criteria; contribution > acknowledgments |

**Authorship:** Translators, co-researchers, and partner analysts who shaped instrument design, interpretation, or analysis should be considered for authorship, not relegated to acknowledgments (ICMJE, 2023).

---

## Relevant External Repositories and Resources

| Resource | Description |
|---|---|
| [EQUATOR Network](https://www.equator-network.org/) | Comprehensive library of reporting guidelines for health and social science research |
| [APA JARS](https://apastyle.apa.org/jars) | APA Journal Article Reporting Standards for quantitative and qualitative research |
| [OSF Preprints](https://osf.io/preprints/) | Open Science Framework — pre-registration, data, and code deposit |
| [Zenodo](https://zenodo.org/) | CERN's open data/code repository; integrates with GitHub for DOI minting |
| [papaja (R)](https://github.com/crsh/papaja) | R package for writing APA-style reproducible manuscripts in R Markdown |
| [quarto](https://quarto.org/) | Next-generation reproducible document system (R + Python); renders to PDF, HTML, Word |
| [rticles (R)](https://github.com/rstudio/rticles) | R Markdown templates for dozens of journal formats |
| [tenzing](https://github.com/marton-balazs-kovacs/tenzing) | CRediT taxonomy authorship contribution documentation tool |

---

## References

- Eysenbach, G. (2004). Improving the quality of web surveys: the Checklist for Reporting Results of Internet E-Surveys (CHERRIES). *Journal of Medical Internet Research*, 6(3), e34.
- ICMJE. (2023). *Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals*. http://www.icmje.org
- Levitt, H. M., Bamberg, M., Creswell, J. W., Frost, D. M., Josselson, R., & Suárez-Orozco, C. (2018). Journal article reporting standards for qualitative primary, qualitative meta-analytic, and mixed methods research in psychology. *American Psychologist*, 73(1), 26–46.
- O'Brien, B. C., Harris, I. B., Beckman, T. J., Reed, D. A., & Cook, D. A. (2014). Standards for reporting qualitative research: a synthesis of recommendations. *Academic Medicine*, 89(9), 1245-1251.
- Secules, S., McCall, C., Mejia, J. A., Beebe, C., Masters, A. S., L. Sánchez‐Peña, M., & Svyantek, M. (2021). Positionality practices and dimensions of impact on equity research. *Journal of Engineering Education*, 110(1), 19-43.
- Sun, S., Pan, W., & Wang, L. L. (2010). A comprehensive review of effect size reporting and interpreting practices in academic journals in education and psychology. *Journal of Educational Psychology*, 102(4), 989-1004.
- Tong, A., Sainsbury, P., & Craig, J. (2007). Consolidated criteria for reporting qualitative research (COREQ). *International Journal for Quality in Health Care*, 19(6), 349-357.
