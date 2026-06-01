# Mode Selection Guide: How to Choose Your Distribution Method

Use this guide to systematically select the most appropriate distribution mode(s) for your study. Answer each question in sequence.

---

## Decision Tree

```
1. Do you need a nationally/internationally representative sample?
   ├── YES → Use an online panel (Prolific, Qualtrics Panels)
   │         └── Is internet access unreliable for your target population?
   │             ├── YES → Add a mixed-mode follow-up (phone/SMS/mail)
   │             └── NO  → Online panel is sufficient
   └── NO → Is your study place-based or community-specific?
            ├── YES → Is your population digitally excluded (elderly, rural, remote)?
            │         ├── YES → Mail/TDM or in-person intercept
            │         └── NO  → In-person, QR-code, or mixed-mode
            └── NO → Exploratory/convenience sample OK?
                     ├── YES → Online (Qualtrics self-distribution, social media)
                     └── NO  → Revisit Step 1 and Step 4 (sampling frame)
```

---

## Key Considerations by Mode

### Online Panels (Prolific, Qualtrics, Dynata, Lucid)
- **Prolific**: Best for vetting participants; demographic pre-screening, transparent pay, lower bot rates. Use Prolific Academic for academic research rates (≥$8/hr USD).
- **Qualtrics Panels / Lucid**: Good for quota-filling fast, but scrutinize data quality. Include attention checks and timing exclusions.
- **MTurk**: Data quality has degraded significantly (bot farms, scammer accounts). Use only with very robust quality controls and document your approach.

### In-Person Intercept
- Randomize starting locations and interviewers.
- Use a structured approach: fixed script, no ad-libbing.
- Record refusal rate per site for non-response analysis.

### Mail (Dillman TDM)
- Contact 1 (Day 0): Full survey packet + cover letter
- Contact 2 (Day 3–5): Thank-you / reminder postcard
- Contact 3 (Day 2–3 weeks): Replacement survey to non-responders
- Contact 4 (Day 6–7 weeks): Certified letter with final replacement survey

### Mixed-Mode
- Clearly document which participants used which mode.
- Test for mode effects: run a small subset across both modes and check for significant differences in means or distributions before pooling data.

---

## Red Flags: When to Reconsider Your Mode
- Completion time < 1/3 of estimated time → likely speeders or bots
- Attention check failure rate > 15% → sampling or platform problem
- Dropout rate > 40% → survey too long, too sensitive, or poorly structured
- Duplicate IP rate > 5% → platform bot problem; consider moving to Prolific