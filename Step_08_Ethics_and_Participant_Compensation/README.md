# Step 08 — Ethics, Protocols, and Participant Compensation

> *"Approval can take days to months depending on institution, population vulnerability, and topic sensitivity, so plan accordingly."*  
> — Survey Design curriculum, Step 8

Ethical oversight of human-dimensions work requires stringent protocols to protect research participants. Unlike IACUC (for animal research), human subjects research requires approval from an Institutional Review Board (IRB) in the U.S., a Behavioural Research Ethics Board (BREB) in Canada, or analog ethics committees worldwide. 

This folder contains resources for navigating the ethical review process, compensating participants fairly, and engaging with communities respectfully.

---

## Folder structure

```
Step_08_Ethics_and_Compensation/
├── README.md                              ← this file
├── ethics_checklist.md                    ← Checklist for ethical considerations and data sovereignty
├── compensation_guide.md                  ← Guide to participant compensation and ethical pay rates
│
├── Examples of approved IRB:BREB protocols and recruitment materials/
│   ├── Langhans_information_sheet.docx    ← Real-world example of an information sheet/consent form
│
└── policies/
    └── consent_template.md                ← Mad-libs style template for writing an informed consent form
```

---

## Core Ethical Considerations

### 1. The IRB/BREB Process
- **Submit early:** Submit your study justification, instrument (survey draft usually required), and all recruitment materials (emails, flyers, social media posts) before you begin recruitment.
- **Multi-jurisdictional studies:** Cross-border, Indigenous-community, or multi-site studies often need separate approvals from multiple boards (e.g., Tribal IRBs, host-country ethics boards).

### 2. Informed Consent & Data Sovereignty
- **Informed Consent:** Must clearly communicate potential risks, benefits, data handling procedures (e.g., storage methods), and details about data-sharing (e.g., FAIR principles).
- **CARE Principles:** For work with Indigenous communities (or historically marginalized/extracted-from communities), pair FAIR data principles with **CARE** principles (Collective benefit, Authority to control, Responsibility, Ethics) to ensure data sovereignty (Carroll et al., 2020).
- **Anonymity vs. Confidentiality:** Define this clearly.
  - *Anonymity* means absolutely no identifying information is collected (not even IP addresses).
  - *Confidentiality* means identities are known or identifiable but are stored securely and separately from responses. Beware of free-text responses combining with demographic profiles to inadvertently re-identify participants.

### 3. Fair Compensation
- **Respect Time but Avoid Coercion:** Pay well to respect participant effort, but avoid making compensation so high (relative to local incomes) that it becomes coercive for vulnerable populations.
- **Platform Guidelines:** Benchmark against online platforms. For instance, Prolific recommends ≥$8/hr USD (or equivalent legal minimums); MTurk often pays a fraction of that (Hara & Tanaka, 2022).
- **Lotteries vs. Direct Cash:** Per-completion payment is usually preferred over lotteries (Göritz, 2010), but lotteries or non-cash options (donations, universal gift cards, reciprocal community services) are suitable for resource-constrained or cross-cultural settings.

### 4. Deception and Debriefing
- **Deception:** Generally frowned upon but sometimes necessary (e.g., cover stories to reduce social desirability bias). 
- **Debriefing:** A thorough written debrief is required when deception is used. It must explain the true purpose, why deception was used, and explicitly offer participants the chance to withdraw their data (Sieber et al., 1995).

### 5. Decolonizing Consent and Inclusive Disclosure Practices
- **Beyond a one-time signature:** Standard IRB/BREB consent processes were designed around a Western, individualist, one-time-disclosure model. Lahman, Landram, Teman, & Kincaid (2022) argue that conventional human-subjects review can "ethically recolonize" communities by imposing U.S.-centric understandings of consent and privacy, and recommend cultural humility and ongoing, relational, community-negotiated consent rather than a single signed form.
- **Communicative accessibility:** Standard written/verbal consent procedures assume typical communication channels. Wittich, Boie, & Jaiswal (2023) document adapted consent methodologies (e.g., tactile signing, extended time, trusted intermediaries) for participants with deafblindness — a template for any survey involving communicatively vulnerable populations.
- **Calibrating disclosure length and content:** The "reasonable person" standard for how much risk/procedure detail to disclose can systematically underserve some populations. Khatiwada, Howard, Krempley, Walton, Williams, & Graber (2026) show that autistic self-advocates often need more concrete, literal, and structured consent information than neurotypical-designed forms typically provide — a mismatch worth checking against your target population before finalizing a consent form.
- **High-risk field contexts:** Where fieldwork occurs in conflict zones, standard consent/anonymity procedures may be insufficient protection; Roberts (2026) proposes context-specific "do no harm" protocols covering data storage, participant identification risk, and researcher safety as a joint concern.

---

## References

- Betancort Cabrera, N., et al. (2020). (General Reference for FAIR data principles in human research).
- Carroll, S. R., Garba, I., Figueroa-Rodríguez, O. L., Holbrook, J., Lovett, R., Materechera, S., ... & Hudson, M. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal*, 19, 43.
- Garrison, N. A. (2013). Genomic justice for Native Americans: impact of the Havasupai case on genetic research. *Science, Technology, & Human Values*, 38(2), 201-223.
- Göritz, A. S. (2010). Incentive effects on variance in intention to participate in a panel survey. *International Journal of Market Research*, 52(6), 727-735.
- Hara, K., & Tanaka, A. (2022). (General Reference for platform compensation rates, e.g., MTurk vs Prolific).
- Khatiwada, M., Howard, D., Krempley, T., Walton, K., Williams, C. S., & Graber, A. (2026). Reasonable to whom? Rethinking informed consent disclosures in light of the research-related concerns of the autistic community. *American Journal of Bioethics*. https://doi.org/10.1080/15265161.2026.2632012
- Lahman, M. K. E., Landram, S. V., Teman, E. D., & Kincaid, T. (2022). Cultural humility, human research ethics review, and informed consent. *Cultural Studies <-> Critical Methodologies*, 23(2), 133-144. https://doi.org/10.1177/15327086221138983
- Roberts, K. (2026). Research ethics in conflict zones: Reflections on 'do no harm' ethics for the research network. *Asia Pacific Viewpoint*. https://doi.org/10.1111/apv.70053
- Sieber, J. E., Iannuzzo, R., & Rodriguez, B. (1995). Deception methods in psychology: Have they changed in 23 years?. *Ethics & Behavior*, 5(1), 67-85.
- Wagner, R. (2003). (General Reference for co-developing work with communities).
- Wittich, W., Boie, N. R., & Jaiswal, A. (2023). Methodological approaches to obtaining informed consent when conducting research with individuals with deafblindness. *International Journal of Qualitative Methods*, 22. https://doi.org/10.1177/16094069231205176

---

## 2026 revision — literature curation pass

Of 17 Step 8 candidates reviewed by abstract, four were added as a new
Section 5 addressing gaps in the existing ethics guidance: decolonizing
consent practices (Lahman et al., 2022), communicative accessibility for
consent (Wittich et al., 2023), calibrating consent disclosures for autistic
participants (Khatiwada et al., 2026), and conflict-zone "do no harm"
protocols (Roberts, 2026). Several strong Indigenous-data-sovereignty
candidates (e.g., "Trust in Scholarly Communications and Infrastructure,"
"Indigenous data sovereignty in intangible cultural heritage governance")
were reviewed but not added because this README already cites Carroll et al.
(2020) CARE Principles directly on this topic; adding redundant citations was
avoided in favor of genuinely new gaps. General research-ethics-training and
REB-process papers (e.g., "Evaluating the Impacts of a Research Ethics
Training Course," "Surrogate Practices in Research in the Absence of a
Research Ethics Committee") were judged tangential to this repo's survey
design focus and were not added.
