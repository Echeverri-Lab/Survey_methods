# Prompt for Claude in VS Code

## Before you paste: two setup steps

**1. Move the six files into your repo.** They currently live in this Cowork session's outputs folder:

```
~/Library/Application Support/Claude/local-agent-mode-sessions/346a2077-56bf-4268-aca7-279d69e17e20/8a7b39cf-be2e-451a-aace-c229c595241c/local_ff2c58f1-fa7f-41b7-804b-b33517333ac9/outputs/
```

Clone the repo and copy them in:

```bash
git clone https://github.com/Echeverri-Lab/Survey_methods.git ~/Survey_methods
cd ~/Survey_methods
mkdir -p submission/CSP2-26-0397

COWORK="$HOME/Library/Application Support/Claude/local-agent-mode-sessions/346a2077-56bf-4268-aca7-279d69e17e20/8a7b39cf-be2e-451a-aace-c229c595241c/local_ff2c58f1-fa7f-41b7-804b-b33517333ac9/outputs"

cp "$COWORK/01_Search_Protocol_RUN_THIS_FIRST.md" \
   "$COWORK/02_Methods_section_REPLACEMENT.md" \
   "$COWORK/03_make_fig2_prisma.py" \
   "$COWORK/04_Supplementary_Material_REPLACEMENT.md" \
   "$COWORK/05_Cover_letter_to_editor.md" \
   "$COWORK/06_PROMPT_for_VSCode_Claude.md" \
   "$COWORK/Fig2_PRISMA_flow.pdf" \
   submission/CSP2-26-0397/
```

**2. Also copy your five submitted manuscript files** (`Manuscript_CSP.docx`, `Title Page.docx`, `Fig1 (1).pdf`, `Fig2 (1).pdf`, `Supplementary_Material (1).pdf`) into `submission/CSP2-26-0397/`. The agent needs the .docx to edit it.

Then open `~/Survey_methods` in VS Code and paste everything below the line.

---

I'm revising a manuscript that was administratively returned by *Conservation Science and Practice* (ms. CSP2-26-0397) because it was missing documentation of the literature search methods and a PRISMA flow diagram. I've already drafted the replacement content; I need you to apply it to the files, restructure the repo to hold the search audit trail, and commit.

**Repo:** this one — `Echeverri-Lab/Survey_methods` (the paper's companion repository).

## Read these first, in this order

All in `submission/CSP2-26-0397/`:

1. `01_Search_Protocol_RUN_THIS_FIRST.md` — the search strings and screening procedure I have to execute manually, plus a list of fixes at the end (Step D). Read Step D carefully; several items are your job.
2. `02_Methods_section_REPLACEMENT.md` — the new Methods section text, with `[n = XX]` placeholders.
3. `04_Supplementary_Material_REPLACEMENT.md` — replacement Supplementary Material with Tables S1–S4.
4. `03_make_fig2_prisma.py` — generates the flow diagram. Has an `N` dict of counts, currently all `None`.
5. `05_Cover_letter_to_editor.md` — for reference; don't edit.

Also read `Manuscript_CSP.docx` in that folder to understand the current structure before editing it.

## What I need you to do

### 1. Scaffold the search audit trail

Create `Relevant Literature/search_2026/` with:
- a `README.md` explaining what goes in this folder and why (it is cited in the manuscript Methods as the archive location for search exports and the screening log)
- `screening_log_TEMPLATE.csv` — columns: `record_id, source (core/S1–S11/texts/citation_chasing/standards/team_corpus), authors, year, title, journal_or_publisher, doi, duplicate_of, screen_ta_decision (include/exclude), screen_ta_reason, fulltext_decision (include/exclude), fulltext_exclusion_reason (not_methodological / not_transferable / superseded / unavailable), curation_C1, curation_C2, curation_C3 (each TRUE/FALSE), curation_decision (retain/set_aside), mapped_step (0–12, semicolon-separated if multiple), cited_in_main_text (TRUE/FALSE), in_repo_living_table (TRUE/FALSE), screener_initials, notes`
- `search_strings.md` — extract every Boolean string verbatim from `01_Search_Protocol_RUN_THIS_FIRST.md` (the core search and all eleven S1–S11 strings) into a clean reference file with blank fields for date executed, database, limits, and records retrieved
- `.gitkeep` inside a `exports/` subfolder for the RIS files I'll add

Then write `Relevant Literature/search_2026/count_from_log.py`: reads `screening_log.csv` (if present) and prints every value needed for the `N` dict in `03_make_fig2_prisma.py`, computed from the log rather than tallied by hand. Print it as a copy-pasteable Python dict literal. This is the whole point — the diagram numbers should be derived from the log, not typed twice.

### 2. Revise the manuscript

Work on a copy: `submission/CSP2-26-0397/Manuscript_CSP_revised.docx`. Use `python-docx`. Preserve existing styles, fonts, and paragraph formatting — do not restyle the document.

- Replace the single paragraph under the heading **"Methods (Scope and approach)"** with the full new section from `02_Methods_section_REPLACEMENT.md`. Retitle the heading to **"Methods: literature search, screening, and curation"**. Keep the `[n = XX]` and bracketed placeholders intact — I fill those in after running the search. Match the subheading formatting to how the manuscript already handles the "Step N:" headings.
- Fix the typo in that section: `"identified through Web of Science,]"` → remove the stray `]`.
- **Renumber figures.** The PRISMA diagram becomes Figure 2; the existing Figure 2 (question types and visualizations) becomes Figure 3. Insert the new Figure 2 caption from `02_Methods_section_REPLACEMENT.md` into the Figure Captions section between the Figure 1 and (now) Figure 3 captions. Grep the whole document for `Figure 2`, `Fig. 2`, `Fig 2` and report every hit you changed and every hit you deliberately left alone.
- Add the two new references (Page et al. 2021; Pullin & Stewart 2006) to the reference list in correct alphabetical position, matching the existing APA formatting exactly.

### 3. Repo housekeeping (from Step D of the protocol)

- The repo has an `anonymized/` directory that duplicates every `Step_XX` folder. Check whether it is a true duplicate (diff it against the main tree). If so, propose removing it or moving it to `_archive/` — **ask me before deleting anything.**
- Read `Flag_for_Review/reference_audit_report.md` and give me a prioritised summary of what still needs resolving. Don't try to fix citations yourself; I need to make those calls.
- Check whether the repo's `README.md` manuscript title matches the actual submitted title. The README says "A Step-by-Step Guide to Survey Design for Socio-Ecological Research"; the manuscript is titled "From Opinion Polls to Psychometrics: A Review and Practical Guide to Survey Design in Socio-Ecological Research". Flag the mismatch and fix the README.
- Note in your summary whether the anonymised `anonymous.4open.science` link should still be used — I need to check CSP's policy myself, so just flag where it appears.

### 4. Verify

- Run `python3 submission/CSP2-26-0397/03_make_fig2_prisma.py` and confirm it regenerates the PDF cleanly in draft mode (all placeholders → prints a "[draft mode]" notice, no exception).
- Test `count_from_log.py` against a small fake `screening_log.csv` you generate with ~20 dummy rows, confirm the printed dict is internally consistent, then paste those numbers into a scratch copy of the figure script to confirm the arithmetic validator passes. **Delete the fake log and scratch copy afterwards** — do not commit dummy data.
- Open `Manuscript_CSP_revised.docx` programmatically and print the Methods section plus all figure captions so I can eyeball the result.
- Confirm the revised .docx still opens without repair warnings.

### 5. Commit

Small, reviewable commits on a new branch `revision/prisma-search-methods` — not on `main`. Suggested split: (a) search audit scaffolding, (b) revised manuscript + figure, (c) repo housekeeping. Conventional-style messages. Push the branch and give me the compare URL, but **do not open a PR or merge.**

## Boundaries — important

- **You cannot run the literature search.** Web of Science and Scopus need authenticated institutional access through a browser. Do not attempt to scrape them, do not use any API workaround, and above all **do not invent, estimate, or back-fill any record counts.** Every number stays a placeholder until I run the search myself. If you find yourself tempted to fill in a plausible number, stop and flag it instead.
- Don't modify the original submitted files — only the `_revised` copies.
- Don't touch `Step_00`–`Step_12` content. Out of scope.
- If a manuscript edit is ambiguous (e.g. you can't cleanly locate the Methods paragraph, or the figure caption formatting is inconsistent), stop and ask rather than guessing.

When you're done, give me a short summary of what changed, what you flagged for my decision, and exactly which placeholders I still need to fill.
