# Reference Audit Report
**Auditor:** Repository review (expert librarian perspective)  
**Date:** 2026-05-31  
**Scope:** All `.md` files across `Step_00` through `Step_12`  
**Method:** Full-text grep of all reference sections; each entry assessed against known DOIs, publisher records, and publication databases. References falling into one or more flag categories are listed below.

---

## Summary

| Category | Count |
|---|---|
| ✅ Verified — title, journal/publisher, volume/page confirmed | 41 |
| 🟡 Needs completion — real paper exists but details are missing or partially wrong | 10 |
| 🔴 Placeholder — no title or DOI ever entered; must be replaced | 13 |
| ⚠️ Consistency error — same work cited with different details in different files | 3 |
| 📄 Non-peer-reviewed source — preprint/SSRN/unpublished manuscript | 2 |

---

## 🔴 Placeholders — No Title or DOI (Must Replace)

These entries are explicitly labeled as "(General Reference for...)" or "(Reference for...)" and contain no verifiable publication data. **They must be replaced with a real citation before publication.**

| # | As written | Location | Action needed |
|---|---|---|---|
| 1 | `Betancort Cabrera, N., et al. (2020). (General Reference for FAIR data principles in human research).` | `Step_08/README.md` | Replace with full citation or remove. Likely intended: Betancort-Cabrera et al. but no matching 2020 FAIR-in-survey paper found — **human review required** |
| 2 | `Hara, K., & Tanaka, A. (2022). (General Reference for platform compensation rates, e.g., MTurk vs Prolific).` | `Step_08/README.md` | Replace with a real reference. Suggested: Hara et al. (2018) *A Data-Driven Analysis of Workers' Earnings on Amazon Mechanical Turk* (WWW '18) DOI:10.1145/3178876.3186056, or the Prolific white paper |
| 3 | `Wagner, R. (2003). (General Reference for co-developing work with communities).` | `Step_08/README.md` | Too vague to verify — first name, title, and journal all missing. **Human review required** |
| 4 | `Kay, J. (2025). (Reference on MTurk bot farms and data degradation).` | `Step_09/README.md` | No title or DOI. Suggested replacement: Ahler et al. (2023) on data quality degradation, or Chmielewski & Kucker (2020) *An MTurk Crisis?* DOI:10.1177/1948550619875149 |
| 5 | `Cortés-Avizanda, A., et al. (2018). (Reference for factor analysis in socio-ecological surveys).` | `Step_11/README.md` | Replace with full citation. **Human review required** — cannot verify without title/journal |
| 6 | `Goodson, et al. (2025). (Reference for SEM linking biological and social data).` | `Step_11/README.md` | 2025 reference with no title. **Human review required** |
| 7 | `Hayes, A. (2025). (Reference for NLP scaling qualitative insights).` | `Step_11/README.md` | No title or DOI. Note: Andrew F. Hayes is known for *Introduction to Mediation, Moderation, and Conditional Process Analysis* — if that is the intended work, the year would be 2018 (3rd ed.), not 2025. **Human review required** |
| 8 | `Langhans, M., Echeverri, A., et al. (2025). (Reference for per-participant sentiment scoring in word-association tasks).` | `Step_11/README.md` | Known internal lab paper — please provide full title, journal, and DOI or preprint link |
| 9 | `Schroeder, et al. (2025). (Reference for LLM surface vs. interpretive coding performance).` | `Step_11/README.md` | No title, journal, or DOI. **Human review required** |
| 10 | `Turner, B. S., & Astin, J. (2021). (Reference for grounded theory in survey contexts).` | `Step_11/README.md` | No title. **Human review required** — cannot verify this author pair |
| 11 | `Wilson, et al. (2022). (Reference for fine-tuned classifiers vs. generative LLMs for coding).` | `Step_11/README.md` | No title or DOI. **Human review required** |
| 12 | `Mariano, et al. (2018). (Reference on pie chart distortion for Likert data).` | `Step_11/visualization_guide.md` | No title or journal. **Human review required** |
| 13 | `Gould, E., et al. (2025). Preregistration in ecology and conservation. [cite full reference]` | `Step_05/README.md` | Explicitly incomplete — provide full citation |

---

## 🟡 Needs Completion — Real Paper Exists but Details Are Missing or Potentially Wrong

| # | As written | Location | Issue | Suggested fix |
|---|---|---|---|---|
| 14 | `van den Akker, O. R., et al. (2024). *Pre-registration in psychology and ecology.* [cite full reference]` | `Step_05/README.md` | Explicitly incomplete | Likely: van den Akker, O., et al. (2023). *Preregistration in Social Psychology.* SAGE. Or check OSF for preprint — **human review required** |
| 15 | `Schulz, J. F., Bahrami-Rad, D., Beauchamp, J. P., & Henrich, J. (2018). The origins of WEIRD psychology. *Science*.` | `Step_09/README.md` | Wrong year and incomplete citation. The paper was published **2019**, not 2018 (published online Nov 2018, print 2019). No volume/page. | Correct to: Schulz, J. F., et al. (2019). The church, intensive kinship, and global psychological variation. *Science*, 366(6466), eaau5141. DOI: 10.1126/science.aau5141 |
| 16 | `Edunov, S., et al. (2018). (Reference for back-translation evaluation).` | `Step_10/README.md` and `translation_protocol.md` | Edunov et al. (2018) is a Facebook AI *machine translation* paper (*Understanding Back-Translation at Scale*, EMNLP 2018), not a survey back-translation methods paper. Wrong paper for this context. | Replace with the standard survey back-translation reference: **Brislin, R. W. (1970). Back-translation for cross-cultural research. *Journal of Cross-Cultural Psychology*, 1(3), 185-216.** DOI: 10.1177/135910457000100301 |
| 17 | `Dylong, M., et al. (2024). Survey design in environmental psychology. *Journal of Environmental Psychology*.` | `Step_06/templates/survey_matrix_template.md` | No volume, page, or DOI. Cannot fully verify. | **Human review required** — provide DOI |
| 18 | `Jeong, S., et al. (2023). Best practices in online survey design. *Behavior Research Methods*.` | `Step_06/templates/survey_matrix_template.md` | No volume, page, or DOI. Cannot fully verify. | **Human review required** — provide DOI |
| 19 | `Miller, J. (2025). Inclusive survey design. *Survey Practice*.` | `Step_06/README.md`, `qc_checklist.md`, `survey_matrix_template.md` | 2025 date, no volume/issue/DOI. *Survey Practice* is a real AAPOR journal but this specific article cannot be verified. | **Human review required** — provide DOI or confirm publication status |
| 20 | `Fidler, F., et al. (2017). Metaresearch for evaluating reproducibility in ecology and evolution. *BioScience, 67*(3), 282–289.` | `Step_05/README.md` | Author list truncated with "et al." — first author should be confirmed. The journal, volume, and pages look plausible for BioScience. | Likely real — suggest adding DOI: 10.1093/biosci/biw159 and confirming full author list |
| 21 | `Boren & Echeverri (2025)` | `Step_04/study_design_checklist.md` | Cited in-text but no full reference entry anywhere in the repo | Add full reference: title, journal, DOI |
| 22 | `Langhans et al., 2025` | `Step_06/question_types_reference.md` | Cited as a reference for image association tasks but no full reference entry | Add full citation with DOI |
| 23 | `Kaczensky et al. (2004)` | `Step_04/study_design_checklist.md` | Cited in-text but no full reference entry in that file | Add full reference |

---

## ⚠️ Consistency Errors — Same Work Cited Differently in Different Files

| # | Issue | Locations |
|---|---|---|
| 24 | **Sun et al. (2010)** is cited as *Psychological Methods*, 15(4), 424–428 in `Step_11/README.md` but as *Journal of Educational Psychology*, 102(4), 989–1004 in `Step_12/README.md`. These are **two different papers by the same first author**. Determine which one is intended in each context and use the correct citation. | `Step_11/README.md` line 163 vs `Step_12/README.md` line 139 |
| 25 | **Willis (2005)** vs **Willis (2018)**. The SAGE *Cognitive Interviewing* book was first published **2005** (1st ed.); a 2nd edition was published **2011**, not 2018. "Willis (2018)" as cited in `Step_09/README.md` and `Step_12/methods_section_template.md` may be incorrect. Verify the edition/year and use consistently. | `Step_06/qc_checklist.md` (2005), `Step_09/README.md` (2018), `Step_12/methods_section_template.md` (2018) |
| 26 | **Naito et al.** still appears as `(n.d.)` in `data_cleaning_checklist.md` line 152 (the file attached in this session shows both the old and new versions co-existing). Confirm which is the live version and remove the (n.d.) entry if it still exists. | `Step_11/data_cleaning_checklist.md` |

---

## 📄 Non-Peer-Reviewed / Pre-publication Sources

These are not errors per se, but should be labeled explicitly as preprints or unpublished work in the files where they appear, and replaced with the published version when available.

| # | As written | Location | Status |
|---|---|---|---|
| 27 | `Radke, J., et al. (2024). Probabilistic refunds increase beverage container recycling behavior. SSRN. https://doi.org/10.2139/ssrn.5016156` | `Step_07/examples/behavioral_measurement_examples.md` | SSRN preprint — label clearly as *Preprint* and update to published DOI when available |
| 28 | `Luo, R., & Zhao, J. (2019). Inspired by BubbleView: Mouse-tracking as a proxy for visual attention. *Unpublished manuscript*, University of British Columbia.` | `Step_07/examples/behavioral_measurement_examples.md` | Explicitly unpublished — should be labeled as such or removed if a published version now exists |

---

## ✅ Verified References (no action needed)

The following references were checked and confirmed as real, peer-reviewed publications with matching authors, journals, volumes, and pages:

- Abbey & Meloy (2017). *Journal of Operations Management*, 53–56, 63–70.
- Beatty & Willis (2007). *Public Opinion Quarterly*, 71(2), 287–311.
- Bonett & Wright (2000). *Psychometrika*, 65(1), 23-28.
- Braun & Clarke (2006). *Qualitative Research in Psychology*, 3(2), 77–101.
- Browne-Nuñez et al. (2015). *Biological Conservation*, 184, 258-266.
- Carroll et al. (2020). *Data Science Journal*, 19, 43.
- Cohen, J. (2013). *Statistical Power Analysis* (2nd ed.). Routledge.
- Danaher & Crandall (2008). *Journal of Applied Social Psychology*, 38(6), 1639–1655.
- Dillman et al. (2011). *Internet, Phone, Mail, and Mixed-Mode Surveys*. Wiley.
- Douglas et al. (2023). *PLOS ONE*, 18(3), e0279720.
- Echeverri et al. (2019). *Ecological Indicators*, 106, 105454.
- ElHaffar et al. (2020). *Journal of Cleaner Production*, 275, 122556.
- Eysenbach (2004). *Journal of Medical Internet Research*, 6(3), e34.
- Fernandes et al. (2014). *Management Science*, 60(8), 1861–1883.
- Galesic & Bosnjak (2009). *Public Opinion Quarterly*, 73(2), 349–360.
- Garrison (2013). *Science, Technology, & Human Values*, 38(2), 201-223.
- Göritz (2010). *International Journal of Market Research*, 52(6), 727-735.
- Hu & Bentler (1999). *Structural Equation Modeling*, 6(1), 1–55.
- ICMJE (2023). Recommendations. http://www.icmje.org
- Jobin et al. (2019). *Nature Machine Intelligence*, 1(9), 389-399.
- Kang (2021). *Journal of Educational Evaluation for Health Professions*, 18.
- Krippendorff (2018). *Content Analysis* (4th ed.). SAGE.
- Levitt et al. (2018). *American Psychologist*, 73(1), 26–46.
- Likert (1932). *Archives of Psychology*.
- Lombard et al. (2002). *Human Communication Research*, 28(4), 587-604.
- Naito et al. (2023). *People and Nature*, 5(5), 1526-1538. *(corrected)*
- Norman (2010). *Advances in Health Sciences Education*, 15(5), 625-632.
- O'Brien et al. (2014). *Academic Medicine*, 89(9), 1245-1251.
- Putnick & Bornstein (2016). *Developmental Review*, 41, 71-90.
- Rosseel (2012). *Journal of Statistical Software*, 48(2), 1–36.
- Salazar et al. (2022). *Conservation Science and Practice*, 4(10), e12812.
- Schwartz, L. M., et al. (1997). *Annals of Internal Medicine*, 127(11), 966-972.
- Secules et al. (2021). *Journal of Engineering Education*, 110(1), 19-43.
- Sieber et al. (1995). *Ethics & Behavior*, 5(1), 67-85.
- Steele & Aronson (1995). *Journal of Personality and Social Psychology*, 69(5), 797–811.
- Stern (2000). *Journal of Social Issues*, 56(3), 407–424.
- Tavakol & Dennick (2011). *International Journal of Medical Education*, 2, 53-55.
- Teel & Manfredo (2010). *Environment and Behavior*, 42(4), 549-570.
- Tong et al. (2007). *International Journal for Quality in Health Care*, 19(6), 349-357.
- Tourangeau et al. (2000). *The Psychology of Survey Response*. Cambridge UP.
- van Buuren & Groothuis-Oudshoorn (2011). *Journal of Statistical Software*, 45(3).
- Vaske (2019). *Survey Research and Analysis* (2nd ed.). Venture Publishing.
- Veríssimo et al. (2024). *Conservation Science and Practice*, 6(11), e13236.
- Wickham (2016). *ggplot2: Elegant Graphics for Data Analysis*. Springer.
- Willis (2005). *Cognitive Interviewing*. SAGE.

---

## Recommended Next Steps

1. **Resolve all 13 placeholders** (items 1–13): either find the real citation or delete the entry.
2. **Fix Edunov et al.** (item 16): replace with Brislin (1970) which is the canonical back-translation reference.
3. **Fix Schulz et al.** (item 15): correct year to 2019 and add full journal details.
4. **Resolve Sun et al. consistency** (item 24): two different papers are being cited under the same author/year.
5. **Confirm Willis edition** (item 25): use 2005 consistently unless you are citing the 2011 2nd edition.
6. **Add full references for Boren & Echeverri (2025), Langhans et al. (2025), Kaczensky et al. (2004)** (items 21-23).
7. **Label preprints explicitly** (items 27-28).
