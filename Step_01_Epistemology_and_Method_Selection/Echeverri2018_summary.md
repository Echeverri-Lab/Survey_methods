# Summary: Echeverri et al. (2018, Biological Conservation)

This note summarizes epistemological framing, methodological choices, and common methods discussed or exemplified in Echeverri et al. (2018). It also provides a simple decision tree to help choose an appropriate approach for a given research question.

## Epistemologies (high-level takeaways)
- Positivist / Post-positivist: assumes an objective reality that can be measured. Supports deductive research and quantitative measurement (surveys, experiments) when constructs are well-defined and the goal is generalization.
- Constructivist / Interpretivist: assumes meaning is constructed by participants. Supports inductive, exploratory research (ethnography, semi-structured interviews, focus groups) when context, local meanings, and power relations matter.
- Pragmatist: chooses methods that best answer the research question; often supports mixed-methods designs when both breadth and depth are needed.

### Addendum — paradigms and their mapping to methods (table/image summary)
- Positivism / Post-positivism: ontology = single objective reality; epistemology = measurable knowledge via reliable tools; methodology = experiments, surveys; methods = questionnaires, structured observation, statistical analysis.
- Constructivist / Interpretivist: ontology = multiple socially constructed realities; epistemology = subjective knowledge that must be interpreted; methodology = ethnography, grounded theory; methods = interviews, participant observation, thematic analysis.
- Pragmatism: prioritizes problem-solving; mixes methods pragmatically (e.g., qualitative to develop constructs, quantitative to estimate prevalence).
- Subjectivism & Critical paradigms: emphasize perspective, power, and critique. Methods lean to qualitative, participatory, and action-research approaches.

## When NOT to choose a questionnaire/survey (practical checklist)
Before committing to a questionnaire-based approach, consider the following conditions that suggest surveys may be a poor fit:

- Constructs are not well-defined or likely differ across contexts (you need formative qualitative work first).
- The research question aims to uncover deep meanings, power relations, or local frames rather than prevalence.
- The population is very small, hard-to-sample, or not representative (surveys won’t yield generalizable estimates).
- The phenomenon is primarily behavioral and poorly captured by self-report (consider observational, behavioral tasks, or administrative linkage).
- Ethical or cultural constraints make standardized questioning intrusive or inappropriate (use participatory or qualitative methods).
- High risk of social desirability or measurement reactivity that would bias answers; consider behavioral measures or triangulation.

If any of the above applies, prefer one of:
- Formative qualitative work: interviews, FGDs, cognitive interviewing to develop items and understand local meaning.
- Ethnography / participant observation for rich contextual understanding.
- Case studies, participatory mapping, and action research when co-production and community engagement are central.
- Mixed-methods: do qualitative work first, then build a tailored survey and pilot.

## Practical decision checklist (short)
1. What is the main goal? (estimate prevalence/test hypothesis vs explore meaning)
2. Are constructs measurable? (existing validated scales or clear operationalizations)
3. Is the population accessible/large enough for sampling? (power & design)
4. Are behavioral/objective measures available or preferred? (link or collect them if possible)
5. Are there ethical or cultural constraints? (adapt methods accordingly)

If 1=prevalence/hypotheses AND 2=yes AND 3=yes → Survey pathway (select/validate scales, pilot, sampling, preregister).
If 1=exploratory OR 2=no OR 5=yes → Qualitative or mixed-methods pathway.

---

I added a visual decision tree (`decision_tree.svg`) to this folder. Consider adding a Mermaid or Graphviz source if you want an editable flowchart in the repo.

## Methodologies and when they fit
- Quantitative survey research
  - Aim: measure prevalence, strength, and distribution of attitudes/behaviors; test hypothesized relationships.
  - Suitable when constructs are clearly defined and can be operationalized with psychometric scales.
  - Strengths: generalizability (with appropriate sampling), statistical tests, effect estimation.
  - Limitations: limited depth on meanings, potential measurement bias.

- Qualitative methods (interviews, focus groups, ethnography)
  - Aim: explore meanings, local frames, and processes; generate new constructs or refine theory.
  - Suitable for exploratory stages, contested or novel contexts, and when power/meaning are central.
  - Strengths: rich, contextualized understanding; flexible and iterative.
  - Limitations: limited generalizability, labor-intensive.

- Mixed methods
  - Aim: combine strengths of both approaches (e.g., qualitative to develop items and quantitative to measure prevalence; or surveys plus behavioral tasks).
  - Use when both representativeness and contextual understanding are required.

## Typical Methods mentioned or implied
- Questionnaire-based psychometric scales (Likert-style items, validated instruments)
- Semi-structured interviews and focus groups for elicitation and cognitive interviews
- Behavioral measures (choice tasks, field observations) to move beyond self-report
- Sampling approaches: probability sampling for generalization; purposive/snowball sampling for qualitative depth
- Quality control: attention checks, pilot testing, cognitive interviews, and data validation

## Short example decision tree (text/flow)
1. Start: What is the main research goal?
   - If the goal is to estimate prevalence or test hypotheses about relationships across a population -> go to (2).
   - If the goal is to explore meaning, generate theory, or investigate a local/contested context -> choose qualitative methods (interviews, focus groups, ethnography).
   - If you need both depth and breadth -> choose mixed methods (qual -> quant or concurrent designs).

2. Are the constructs well-defined and measurable with existing scales?
   - Yes: Use quantitative survey methods. Steps: select/validate scales, run pilot, plan sampling and power analysis, pre-register analysis.
   - No: Conduct formative qualitative work (cognitive interviews, focus groups) to develop/adapt items; then pilot and scale up to a survey if generalization is needed.

3. Are behavioral outcomes available or important (beyond self-report)?
   - Yes: incorporate behavioral measures or objective data (tasks, linked records); consider experimental or quasi-experimental designs.
   - No: proceed with validated self-report measures but include quality control and consider validation via triangulation where possible.

## Decision tree (ASCII flow)

[Research goal]
    |
    |-- Exploratory / local meaning / contested -> Qualitative methods (interviews, ethnography, focus groups)
    |
    |-- Hypothesis testing / prevalence -> Are constructs well-defined?
           |
           |-- Yes -> Quantitative survey (select scales, pilot, power/sample design, preregister)
           |
           |-- No -> Qualitative formative work -> develop items -> pilot -> Survey (if generalization required)

At any node, consider Mixed Methods if you need both depth and breadth.

## Recommended files to add to this folder
- `papers/Echeverri_2018_BiolCons.pdf` (original paper; add if copyright allows)
- `notes.md` (this file)
- `decision_tree.png` or `decision_tree.svg` (visual version of the ASCII flow above)

---

### Short citations (add full BibTeX in `papers/` if desired)
- Echeverri, et al. (2018). Biological Conservation. [PDF to be added]

