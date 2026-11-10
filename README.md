# Survey Design Companion Repository

A peer-reviewed, open-access companion repository for the manuscript:

> **"From Opinion Polls to Psychometrics: A Review and Practical Guide to Survey Design in Socio-Ecological Research"**

This repository provides structured guidance, templates, annotated code, and reference materials for each of the 12 stages described in the manuscript. It is intended for students and researchers who are new to psychometrics and survey design in conservation, ecology, and environmental social science.

---

## Contents

- [Step 00 Key Terminology](Step_00_Key_Terminology/)
- [Step 01 Epistemological Alignment and Method Selection](Step_01_Epistemological_Alignment_and_Method_Selection/)
- [Step 02 Theory Grounding and Construct Conceptualization](Step_02_Theory_Grounding_and_Construct_Conceptualization/)
- [Step 03 Psychometric Scales and Construct Validity](Step_03_Psychometric_Scales_and_Construct_Validity/)
- [Step 04 Study Architecture and Experimental Design](Step_04_Study_Architecture_and_Experimental_Design/)
- [Step 05 Preregistration and Open Science](Step_05_Preregistration_and_Open_Science/)
- [Step 06 Instrument Construction](Step_06_Instrument_Construction/)
- [Step 07 Measuring Behavior Beyond Self Report](Step_07_Measuring_Behavior_Beyond_Self_Report/)
- [Step 08 Ethics and Participant Compensation](Step_08_Ethics_and_Participant_Compensation/)
- [Step 09 Power Analysis Sampling and Pilots](Step_09_Power_Analysis_Sampling_and_Pilots/)
- [Step 10 Survey Distribution](Step_10_Survey_Distribution/)
- [Step 11 Data Preparation Analysis and Reporting](Step_11_Data_Preparation_Analysis_and_Reporting/)
- [Step 12 Writing Survey Research Paper](Step_12_Writing_Survey_Research_Paper/)
- [Review methods and audit trail](review_methods/) · [Search and screening records](Relevant%20Literature/search_2026/) · [PRISMA flow](PRISMA/)

> On the anonymized review mirror, the file tree on the left may truncate long folder names; use these links instead.

---

## How to use this repository

Each `Step_XX` folder corresponds to one section of the manuscript and contains:
- A `README.md` that summarises the key concepts, decisions, and best practices for that stage
- Templates, checklists, and/or worked examples (where applicable)
- R and/or Python code snippets (where applicable)
- A `papers/` sub-folder with PDFs and `.bib` files for the primary literature cited in that step

Work through the steps in order for a new study, or jump directly to the step most relevant to your current task.

### Using the templates without GitHub or Markdown

- **Fillable PDFs.** Every template in the step folders (design matrices, randomization plan, survey matrix, power-analysis worksheet, checklists, and others) has a fillable PDF next to its Markdown file, linked from each step's README. Download the PDF, type into the boxes with the free Adobe Acrobat Reader (macOS Preview and web browsers also work), save, and attach it. To download from GitHub, open the PDF and click the download button above the preview.
- **R power-analysis examples.** [`Step_09_Power_Analysis_Sampling_and_Pilots/scripts/`](Step_09_Power_Analysis_Sampling_and_Pilots/scripts/) has commented R scripts for two-group, BACI, and ACI designs and a 2×2 experiment with mediation.
- **Maintainers:** the PDFs are generated from the Markdown by [`tools/make_fillable_pdfs.py`](tools/make_fillable_pdfs.py). After editing a template, run `venv/bin/python tools/make_fillable_pdfs.py` (or `python tools/make_fillable_pdfs.py Step_04` for one step) and commit the Markdown and PDF together.

---

## Repository structure

### Workflow steps

| Folder | Contents |
|---|---|
| `Step_00_Key_Terminology/` | Glossary of 19 core terms: latent constructs, attitudes, values, Likert scales, CFA, SEM, and more. Full peer-reviewed references for each definition. |
| `Step_01_Epistemological_Alignment_and_Method_Selection/` | Positivist vs. interpretivist frameworks; axiology checklist; method-selection decision tree; mixed-methods guidance. Includes paper summaries for Brown & Dueñas (2020) and Echeverri (2018). |
| `Step_02_Theory_Grounding_and_Construct_Conceptualization/` | How to anchor constructs in theory before writing a single item. Theory summary template; annotated `.bib` for key frameworks (VBN, TPB, NEP, NRS, CES). |
| `Step_03_Psychometric_Scales_and_Construct_Validity/` | Curated reference table of validated scales for socio-ecological research (wildlife attitudes, nature relatedness, ecosystem services, wellbeing). Scale documentation template; PDFs of primary scale papers. |
| `Step_04_Study_Architecture_and_Experimental_Design/` | Between- vs. within-subjects design; randomisation plan template; survey flow diagram; temporal context log; design decision matrix. |
| `Step_05_Preregistration_and_Open_Science/` | Why and how to preregister; AsPredicted and OSF templates; confirmatory vs. exploratory analysis guide; preregistration checklist. |
| `Step_06_Instrument_Construction/` | 11-type question reference table (word association, Likert, slider, 3-D visualisation, etc.); survey matrix template; survey template; QC checklist; worked example from Echeverri (2019). |
| `Step_07_Measuring_Behavior_Beyond_Self_Report/` | Eye-tracking, mouse-tracking, implicit association, incentivised choice, field behavioural observation. Worked examples with citations; code stub folder. |
| `Step_08_Ethics_and_Participant_Compensation/` | IRB/BREB process; informed consent template; CARE and FAIR data principles; compensation guidelines for Prolific, MTurk, and community panels; deception and debriefing protocols. (Approved protocol examples are not included in the public repository for privacy reasons.) |
| `Step_09_Power_Analysis_Sampling_and_Pilots/` | Effect-size estimation; power analysis in R (`pwr`, `lavaan`) and Python (`pingouin`); probability and non-probability sampling schemes; pilot study guidance; speeder-threshold derivation. |
| `Step_10_Survey_Distribution/` | Mode selection guide (online panel vs. in-person vs. field tablet); AAPOR response-rate definitions; translation and back-translation protocol; platform comparison table (Qualtrics, REDCap, KoBoToolbox, SurveyCTO). |
| `Step_11_Data_Preparation_Analysis_and_Reporting/` | Full cleaning pipeline with ordered exclusion log template; annotated R and Python code for eligibility filtering, bot detection, speeder removal, AI-text flagging, and missing data imputation (`mice`); CFA/SEM workflow; qualitative coding guidance; LLM-assisted coding considerations; visualization guide with working R/Python code for Likert, word clouds, Sankey diagrams, ordination, and path models. |
| `Step_12_Writing_Survey_Research_Paper/` | Methods-section fill-in-the-blank template; results and discussion structure; reflexivity guidance; reporting checklists for CHERRIES, SRQR, COREQ, JARS-Quant, and JARS-Qual; equitable authorship and communication notes. |

### Other top-level folders

| Folder | Purpose |
|---|---|
| `review_methods/` | Documentation of how the review behind the manuscript was conducted, kept separate from the step-by-step resources. Includes the superseded 2026 curation-pass records moved out of the step folders. |
| `PRISMA/` | Flow-diagram data and scripts for the manuscript's literature search. |
| `Relevant Literature/` | Collected PDFs, RIS export files, and reference libraries not yet assigned to a specific step. `search_2026/` holds the search strings, exports, screening log, and supplementary-search (Stream B) records. |

---

## Quick start

```
# Clone the repository
git clone https://github.com/Echeverri-Lab/Survey_methods.git
cd Survey_methods

# Install Python dependencies
pip install -r requirements.txt
```

1. Read `Step_00_Key_Terminology/README.md` to orient yourself to the vocabulary used throughout.
2. Work through each `Step_XX` README in order, completing the templates and checklists as you go.
3. Add your own PDFs to the relevant `papers/` sub-folders and update the `.bib` files.
4. Place your survey instrument files under `Step_06_Instrument_Construction/`.
5. Run your cleaning and analysis scripts from `Step_11_Data_Preparation_Analysis_and_Reporting/`.
6. Before submitting your manuscript, check that every reference exists and supports the sentence it is cited for.

---

## Contributing

See `CONTRIBUTING.md` for guidance on adding content, fixing references, or suggesting new steps.

## License

See `LICENSE`.
