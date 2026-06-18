# Step 10 — Survey Distribution and Administration

> *"Pre-specify stopping rules and document how, when, where, by whom, and at what response rate the data were collected."*  
> — Survey Design curriculum, Step 10

The target audience is the primary driver of how a survey should be administered. This step covers survey distribution modes, field tools, language/cultural adaptation, and the operational logistics of running a survey in the field. A well-designed instrument can still produce biased or incomplete data if administration decisions are made carelessly or documented poorly.

---

## Folder structure

```
Step_10_Survey_Distribution/
├── README.md                          ← this file
├── mode_selection_guide.md            ← Decision guide for selecting distribution modes
├── platform_comparison_table.md       ← Feature/cost comparison of major survey platforms
├── field_operations_checklist.md      ← Pre-launch, during-field, and post-field checklists
└── translation_protocol.md            ← Step-by-step multilingual adaptation protocol
```

---

## 1. Distribution Modes

| Mode | Best suited for | Key advantages | Key limitations |
|---|---|---|---|
| **Online panel** (Prolific, Qualtrics Panels, Dynata) | National/international samples, WEIRD-reduced samples | Fast, scalable, randomization built in | Excludes internet-poor populations, bot risk on some platforms |
| **In-person / intercept** | Place-based, localized, or low-trust populations | High response rates, real-time clarification, builds rapport | Interviewer effects, logistically expensive, geographic constraints |
| **Mail / postcard** | Rural, remote, elderly, internet-excluded populations | High coverage, no device needed | Slow, costly, limits response format complexity |
| **Phone / SMS / WhatsApp** | Mobile-saturated, low-broadband regions | Reaches where internet is patchy | Short items only, no visual stimuli, time-intensive for voice |
| **Mixed-mode** | Maximizing coverage and response rate | Best of each mode, reduces non-response bias | Mode effects must be tested and documented |

**In-person administration** introduces **interviewer effects** — subtle cues that shape how participants respond. Control these by:
- Standardizing verbatim scripts for enumerators.
- Using structured training sessions (role play and practice), documented in the IRB/BREB protocol.
- Rotating interviewers across sites and demographics where possible.
- Recording interviewer ID as a covariate for later analysis.

For mail surveys, follow Dillman's **Tailored Design Method** (TDM; Dillman, 2011): initial mailing → 1-week postcard reminder → 3-week replacement survey → 7-week certified letter to non-responders.

---

## 2. Field Tools Comparison

| Tool | Best use case | Offline capable | Branching logic | Multimedia support | Cost |
|---|---|---|---|---|---|
| **Qualtrics** | Academic/commercial panels, complex instruments | ✓ (via offline app) | ✓ (advanced) | ✓ (audio, video, images) | Institutional license (extra fees for panel recruitment) |
| **QuestionPro** | Low priority surveys (e.g., screening, webinar follow-ups) | ✗ | ✓ (basic) | ✓ | Cheaper than Qualtrics |
| **KoBoToolbox** | Humanitarian, field-based, low-resource contexts | ✓ | ✓ | ✓ (images) | Free (humanitarian) |
| **ODK / ODK Collect** | Ecological/field surveys, GPS required | ✓ | ✓ | ✓ (images, audio) | Free |
| **Survey123 (Esri)** | Geospatially integrated studies | ✓ | ✓ | ✓ | Esri license |
| **REDCap** | Clinical/medical research, HIPAA compliance needed | Limited | ✓ | Limited | Free (many institutions) |
| **LimeSurvey** | Self-hosted, data sovereignty requirements | ✗ | ✓ | ✓ | Free (self-hosted) |
| **Google Forms** | Quick pilots, student projects | ✗ | Limited | ✓ (images) | Free |

> ⚠️ **Note on QR codes:** QR-code flyers bridge in-person presence with online completion. Expect substantial drop-off between scan and submission (~50% in some studies). Track each QR link separately to monitor completion funnels.

---

## 3. Language and Cultural Adaptation
Language and cultural adaptation are inseparable from administration. A culturally adapted instrument is not just translated — it is re-examined for idiom, register, taboo, and cultural-fit.

### The Standard Adaptation Pipeline:
1. **Forward translation:** Certified professional translator produces target-language version.
2. **Back-translation:** An independent second translator (blind to the original) translates back into the source language (Edunov et al., 2018). Discrepancies flag problematic items.
3. **Expert committee review:** Resolve discrepancies and ambiguities with bilingual subject-matter experts.
4. **Pre-testing / cognitive interviewing:** Test the adapted version with 8–15 native speakers from the target population (see Step 9).
5. **Final proofreading:** Native-speaker proofread before deployment.

> 💡 **Machine translation (DeepL, Qualtrics translation tab)** produces a useful first draft but is insufficient as a standalone approach for any scientific publication.

**Wherever possible, collaborate with local researchers and community organizations.** They identify idiom, register, taboo, and cultural-fit issues that no translator working in isolation can.

---

## 4. Operational Field Administration Checklist

### Pre-Launch
- [ ] IRB/BREB approval received and documented (see Step 8)
- [ ] Ensure your survey is only collecting identifiable data you have permission to collect. (Note: Qualtrics automatically collects IP addresses, which many IRBs count as identifiable, but you can turn this off).
- [ ] Survey programmed and tested across devices (desktop, tablet, mobile)
- [ ] Randomization and branching logic verified
- [ ] Attention checks confirmed active
- [ ] Exclusion criteria pre-registered
- [ ] Compensation payment method confirmed and tested
- [ ] Language versions back-translated and cognitively tested
- [ ] Enumerator training completed (if in-person)
- [ ] Timing conflicts checked (holidays, seasonal events, elections)
- [ ] Soft launch (~20 responses) reviewed before full deployment

### During Field Period
- [ ] Response rate tracked daily
- [ ] Reminder contacts sent at pre-scheduled intervals (Day 3, Day 7, Day 14)
- [ ] Attention check failure rates monitored
- [ ] Completion time distribution reviewed for outliers (bots or speeders)
- [ ] IP duplicate screening active
- [ ] Enumerator field notes collected (if in-person)

### Post-Field / Data Handoff
- [ ] Stopping rule reached or documented reason for deviation
- [ ] Final response rate recorded
- [ ] Date range, mode, enumerator IDs, platform version recorded
- [ ] Raw data exported, backed up, and access-controlled
- [ ] Exclusion log created (who was excluded, why, and when)

---

## 5. Response Rate Reporting
Response rate definitions matter for transparency and comparability. Use AAPOR standard definitions:

| Metric | Formula |
|---|---|
| **Response Rate (RR1)** | Complete surveys / (Complete + Partial + Refusals + Non-contacts + Others) |
| **Cooperation Rate** | Complete surveys / (Complete + Partial + Refusals + Others) |
| **Completion Rate** | Complete surveys / (Complete + Partial) |

> 💡 For online panels, vendors often report "incidence rate" (IR) and "completion rate," which are not the same as AAPOR response rates. Report both clearly in your methods.

---

## References
- Dillman, D. A., Smyth, J. D., & Christian, L. M. (2011). *Internet, phone, mail, and mixed-mode surveys: The tailored design method*. John Wiley & Sons.
- Douglas, B. D., Ewell, P. J., & Brauer, M. (2023). Data quality in online human-subjects research. *PLOS ONE*, 18(3), e0279720.
- Edunov, S., et al. (2018). (Reference for back-translation evaluation).
- American Association for Public Opinion Research (AAPOR). (2023). *Standard Definitions: Final Dispositions of Case Codes and Outcome Rates for Surveys*. https://aapor.org