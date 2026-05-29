# Design Decision Matrix

Use this matrix to select the appropriate study design given your construct type, research goal, and practical constraints. Circle or highlight the row that matches your situation and carry that design code into `study_design_checklist.md`.

---

## Part 1: Construct × Design Compatibility

| Construct stability | Research goal | Intervention present? | Recommended design | Notes |
|---|---|---|---|---|
| Trait-like (values, worldviews) | Describe population distribution | No | **Cross-sectional** | Single snapshot is sufficient |
| Trait-like (values, worldviews) | Detect change over time | No | **Longitudinal panel (multi-year)** | Weeks are insufficient; plan for years |
| Attitude (policy support, wildlife attitudes) | Describe and predict | No | **Cross-sectional** | Add covariates for temporal context |
| Attitude | Test causal effect of stimulus | Yes — pre-measurement feasible | **BACI** | Gold standard; randomize if possible |
| Attitude | Test causal effect — pre-measurement impossible or sensitizing | Yes | **ACI / natural experiment** | Cannot estimate within-individual change |
| State (affect, mood, situational emotion) | Capture real-time fluctuation | No | **Experience sampling / diary** | Single survey misses variation |
| State | Test immediate effect of stimulus | Yes | **Within-subjects BACI** | Control order effects; short inter-trial interval |
| Mixed (attitude + affect) | Test stimulus effect | Yes | **BACI with immediate + delayed post** | Separate timing for state vs. attitude outcomes |

---

## Part 2: Intervention Design Decision Tree

```
Is there a stimulus / treatment?
│
├─ NO → Cross-sectional or longitudinal panel
│         └─ Is the construct stable (trait-like)?
│               ├─ YES → Single wave cross-sectional is valid
│               └─ NO  → Repeated measures panel required
│
└─ YES
      │
      ├─ Is pre-measurement feasible?
      │     │
      │     ├─ YES → BACI
      │     │         ├─ Can participants be randomly assigned? → RCT-BACI (strongest)
      │     │         └─ No random assignment possible?       → Quasi-experimental BACI
      │     │
      │     └─ NO (pre-measurement impossible OR would sensitize)
      │               └─ ACI / Natural experiment
      │                   └─ Argue baseline equivalence via matching or auxiliary data
      │
      └─ Is the expected change DURABLE or TRANSIENT?
              ├─ Durable  → Include delayed follow-up (T2 at ≥ 3 months)
              └─ Transient → Immediate post only; note decay expected
```

---

## Part 3: Within-Subjects vs. Between-Subjects Trade-offs

| Criterion | Within-subjects | Between-subjects |
|---|---|---|
| Statistical power | Higher (participant = own control) | Lower (requires larger N) |
| Testing / carry-over effects | **Vulnerable** — must counterbalance or use washout | Not applicable |
| Attrition risk | Higher (multiple contacts required) | Lower |
| Demand characteristics | Higher (purpose more transparent) | Lower |
| Suitable for | State constructs, short studies | Trait/attitude constructs, sensitive topics |
| Recommended mitigation | Counterbalancing; filler tasks; long washout | Random assignment; covariate balance check |

---

## Part 4: Temporal Context Risk Assessment

Rate each factor Low / Medium / High for your data collection window.

| Factor | Risk level | Action if Medium/High |
|---|---|---|
| Data collection during hunting / culling season | | Record as covariate; consider delaying or stratifying by season |
| Active depredation conflict or rewilding event nearby | | Document events; add event-proximity covariate |
| National or regional media spike on focal species | | Record Google Trends or media index; add as covariate |
| Extreme weather affecting outdoor activity | | Record daily weather; assess mood confounds |
| Major policy announcement (listing, delisting, quota change) | | Flag wave; consider ACI framing |

---

## Part 5: Selected Design Summary (fill in)

| Field | Your entry |
|---|---|
| Focal constructs | |
| Stability classification | Trait / Attitude / State |
| Intervention present | Yes / No |
| Pre-measurement feasible | Yes / No / Partially |
| Design type selected | Cross-sectional / BACI / ACI / Within-subjects / Between-subjects / Mixed |
| Expected change type | Durable / Transient / N/A |
| Post-measurement occasions | T1: ___ T2: ___ |
| Temporal context risks | Low / Medium / High |
| Pre-registration platform | OSF / AsPredicted / Other: ___ |

---

*Cross-reference: `study_design_checklist.md` · `design_docs/randomization_plan.md` · `../Step_05_PreRegistration/` · `../Step_09_Power_and_Sampling/`*
