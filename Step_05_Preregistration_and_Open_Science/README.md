# Step 05 — Pre-registration and Open Science

## Why preregister?

Pre-registration means publicly documenting your **hypotheses, methods, and analysis plan** in a time-stamped repository *before* data collection begins. It is the primary structural defense against two threats to scientific credibility:

| Threat | Definition | How preregistration helps |
|---|---|---|
| **HARKing** | Hypothesizing After Results are Known — presenting post-hoc findings as if they were predicted a priori | Forces hypotheses to be written *before* results exist |
| **p-hacking** | Iterating over analysis choices until *p* < .05 | Locks in the confirmatory analysis plan in advance |

Pre-registration does **not** restrict intellectual freedom. It only requires that:
1. **Confirmatory tests** (pre-specified) be reported as such.
2. **Exploratory analyses** (unplanned or post-hoc) be clearly labeled as exploratory.

Exploratory work is not inferior — its inferential status simply differs, and transparent labeling lets readers and reviewers interpret findings appropriately (van den Akker et al., 2024).

Meta-research on psychology shows that preregistered studies more frequently include explicit power analyses, use larger samples, and yield more robust findings — with no penalty in publication time and often higher impact metrics (van den Akker et al., 2024). For socio-ecological research, preregistration signals to reviewers and policymakers that data are transparent and reproducible (Fidler et al., 2017; Gould et al., 2025).

---

## Recommended platforms

| Platform | URL | Format | Best for |
|---|---|---|---|
| **AsPredicted** (v2.00) | https://aspredicted.org/create.php | 11-question short form | Fast, citable registration; ideal for confirmatory survey studies |
| **OSF Prereg** | https://osf.io/prereg/ | Long-form (COS template or custom) | Full study registration; links data, materials, analysis scripts |
| **OSF Registered Reports** | https://cos.io/rr/ | Journal-integrated | Peer review *before* data collection; in-principle acceptance |
| **prereg-psych.org** | https://prereg-psych.org/ | Psychology-focused | ZPID platform; psychology-specific templates |

### Choosing between AsPredicted and OSF

| Factor | Use AsPredicted | Use OSF |
|---|---|---|
| Speed | ✅ ~15 min to complete | Slower; longer template |
| Complexity | Simple single-study surveys | Multi-study, linked materials/data |
| Exploratory items | Declared in Q8 | Dedicated section |
| Public visibility | Citable PDF URL | Full project page |
| Script/data hosting | ❌ | ✅ |

**Recommendation for this project:** Use **AsPredicted** for quick confirmatory pre-registration, then link it from an **OSF project page** that will later host data, codebook, and analysis scripts.

---

## OSF template library

The [`crsh/prereg`](https://github.com/crsh/prereg) R package collects peer-reviewed pre-registration templates as R Markdown documents. Relevant templates include:

| Template | Citation | Best suited for |
|---|---|---|
| **COS Prereg Challenge** | Center for Open Science | General psychology/social science |
| **AsPredicted** | Forsell et al. | Short-form confirmatory studies |
| **van 't Veer & Giner-Sorolla (2016)** | [doi:10.1016/j.jesp.2016.03.004](https://doi.org/10.1016/j.jesp.2016.03.004) | Social psychology experiments |
| **Joint Psychological Societies (2021)** | Bosnjak et al., *American Psychologist* | Quantitative psychology research |
| **Replication Recipe** | Brandt et al. (2014) | Replication studies |

Browse all available templates and examples at the **OSF Pre-registration Resource Library**: https://osf.io/zab38/

Install the R package if you want PDF output:
```r
install.packages("prereg")
```

---

## Folder contents

| File | Purpose |
|---|---|
| `aspredicted_template.md` | Fillable template matching AsPredicted v2.00 (11 questions), with cross-references to the full template |
| `preregistration_template.md` | Comprehensive long-form template (OSF-style); covers all sections including contingency analyses and amendments log |
| `confirmatory_vs_exploratory_guide.md` | Decision guide for classifying each analysis as confirmatory or exploratory |
| `preregistration_checklist.md` | Go/no-go checklist to complete before submitting the preregistration |

---

## Workflow

```
Step 04 (Study Design locked)
        ↓
Fill preregistration_template.md
        ↓
Apply preregistration_checklist.md
        ↓
Submit to OSF or AsPredicted (time-stamp obtained)
        ↓
Begin data collection
        ↓
During analysis: classify each test with confirmatory_vs_exploratory_guide.md
        ↓
Manuscript: report confirmatory and exploratory results in separate sections
```

---

## Key references

- van den Akker, O. R., van Assen, M. A. L. M., Bakker, M., Elsherif, M., Wong, T. K., & Wicherts, J. M. (2024). Preregistration in practice: A comparison of preregistered and non-preregistered studies in psychology. Behavior Research Methods, 56(6), 5424–5433. https://doi.org/10.3758/s13428-023-02277-0
- Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLOS Medicine, 2*(8), e124.
- Fidler, F., et al. (2017). Metaresearch for evaluating reproducibility in ecology and evolution. *BioScience, 67*(3), 282–289.
- Gould, E., et al. (2025). Preregistration in ecology and conservation. [cite full reference]
- Ferguson, J., Littman, R., Christensen, G., Paluck, E. L., Swanson, N., Wang, Z. A., Miguel, E., Birke, D., & Pezzuto, J. H. (2023). Survey of open science practices and attitudes in the social sciences. *Nature Communications, 14*, 5401. https://doi.org/10.1038/s41467-023-41111-1
- Spitzer, L., & Mueller, S. (2023). Registered report: Survey on attitudes and experiences regarding preregistration in psychological research. *PLOS ONE, 18*(3), e0281086.
- Willroth, E. C., & Atherton, O. E. (2024). Best laid plans: A guide to reporting preregistration deviations. *Advances in Methods and Practices in Psychological Science, 7*(1). https://doi.org/10.1177/25152459231213802
- Ghai, S., Theriault, R., Forscher, P., Shoda, Y., Syed, M., Puthillam, A., Peng, H. C., Basnight-Brown, D., Majid, A., Azevedo, F., & Singh, L. (2025). A manifesto for a globally diverse, equitable, and inclusive open science. *Communications Psychology, 3*, 1. https://doi.org/10.1038/s44271-024-00179-1
- Mundinger, C., Schulz, N. K. E., Singh, P., Janz, S., Schurig, M., Seidemann, J., Kurtz, J., Müller, C., Schielzeth, H., von Kortzfleisch, V. T., & Richter, S. H. (2025). Testing the reproducibility of ecological studies on insect behavior in a multi-laboratory setting identifies opportunities for improving experimental rigor. *PLOS Biology, 23*(x), e3003019.

---

## Fillable PDF versions of the templates

Every template in this folder also comes as a fillable PDF next to the Markdown file. You do not need GitHub or Markdown to use them: open the PDF link below, click the download button, fill it in with the free Adobe Acrobat Reader (macOS Preview and web browsers also work), save, and attach it to your assignment.

| Template | Markdown source | Fillable PDF |
|---|---|---|
| AsPredicted Pre-registration Template (v2.00) | [`aspredicted_template.md`](aspredicted_template.md) | [`aspredicted_template.pdf`](aspredicted_template.pdf) |
| Confirmatory vs. Exploratory Analysis — Decision Guide | [`confirmatory_vs_exploratory_guide.md`](confirmatory_vs_exploratory_guide.md) | [`confirmatory_vs_exploratory_guide.pdf`](confirmatory_vs_exploratory_guide.pdf) |
| Pre-registration Go / No-Go Checklist | [`preregistration_checklist.md`](preregistration_checklist.md) | [`preregistration_checklist.pdf`](preregistration_checklist.pdf) |
| Pre-registration Template | [`preregistration_template.md`](preregistration_template.md) | [`preregistration_template.pdf`](preregistration_template.pdf) |

*The PDFs are generated from the Markdown with [`tools/make_fillable_pdfs.py`](../tools/make_fillable_pdfs.py); edit the Markdown, then rebuild the PDFs.*
