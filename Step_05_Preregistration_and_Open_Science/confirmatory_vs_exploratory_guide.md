# Confirmatory vs. Exploratory Analysis — Decision Guide

> Use this guide when writing the preregistration and again during analysis to classify every test or pattern you report. Mislabeling is the mechanism of HARKing: transparent labeling is the fix.

---

## The core distinction

| | Confirmatory | Exploratory |
|---|---|---|
| **Hypothesis written** | Before data collection | After seeing data (or not at all) |
| **Analysis plan specified** | Before data collection | During or after analysis |
| **Inferential weight** | High — justifies causal/directional claims | Low — hypothesis-generating only |
| **Reported as** | "We predicted… and found…" | "We observed… which may suggest…" |
| **Requires replication?** | Less urgently | Yes, before strong claims |

---

## Decision flowchart

```
Was this analysis written in the preregistration document
before data collection began?
        │
       YES ──────────────────────────────────► CONFIRMATORY ✓
        │
        NO
        │
        ▼
Was it a pre-specified contingency
(triggered by a pre-defined condition in the preregistration)?
        │
       YES ──────────────────────────────────► CONFIRMATORY ✓
        │
        NO
        │
        ▼
                                        EXPLORATORY ⚠
                        (must be labeled as such in manuscript)
```

---

## Frequently asked cases

| Scenario | Classification | Rationale |
|---|---|---|
| Hypothesis H1 tested exactly as written in preregistration | **Confirmatory** | Pre-specified |
| Same H1 but you switched from OLS to a robust regression after seeing residuals | **Exploratory** | Analysis deviation — note as amendment |
| Subgroup analysis not mentioned in preregistration | **Exploratory** | Post-hoc |
| Subgroup analysis listed as contingency in Section 8.4 of preregistration | **Confirmatory** | Pre-specified contingency |
| You notice an unexpected correlation in the data and test it | **Exploratory** | Classic HARKing risk — must be labeled |
| Qualitative coding of open-ended items, planned in Section 8 | **Confirmatory** | Pre-specified |
| Qualitative theme that emerged unexpectedly during coding | **Exploratory** | Post-hoc |
| Reliability check (Cronbach's α) run as an assumption check | **Confirmatory** | Pre-specified in Section 8.3 |

---

## How to report in the manuscript

### Confirmatory results section
> "We pre-registered the hypothesis that [X → Y]. Consistent with this prediction, [result, statistic, CI]."
> "We pre-registered the hypothesis that [X → Y]. Contrary to this prediction, [result, statistic, CI]."

**Do not omit null confirmatory results.** A null result on a pre-specified test is informative and must be reported.

### Exploratory results section
> "In exploratory analyses, we observed [result]. This pattern was not pre-specified and should be interpreted with caution pending replication."

---

## Common HARKing warning signs (self-audit)

- [ ] Did you run any analyses *before* finalizing which ones to call "confirmatory"?
- [ ] Did the hypothesis wording change after you saw the direction of results?
- [ ] Did you add or remove covariates after inspecting the outcome variable?
- [ ] Did you change the operationalization of a variable after seeing correlations?
- [ ] Did you drop a hypothesis because it was not significant, without reporting it?

If you checked any box above, those analyses **must** be labeled exploratory.

---

## Amendment procedure

If you need to deviate from the preregistration *during* analysis (e.g., a measure has inadequate reliability):

1. **Stop analysis** before examining the outcome variable.
2. Write a timestamped amendment in Section 11 of `preregistration_template.md`.
3. Upload the amendment to OSF/AsPredicted.
4. Proceed. The amended analysis retains exploratory status unless it was a pre-specified contingency.
