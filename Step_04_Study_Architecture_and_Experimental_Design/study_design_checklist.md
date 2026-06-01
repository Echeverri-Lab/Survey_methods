# Study Design Checklist

Use this checklist when architecting a survey or behavioral intervention study. Work through each section before finalizing your design. Cross-reference with `design_decision_matrix.md` and `temporal_context_log.md` in this folder.

---

## 1. Construct Temporal Classification

Before choosing a design, classify the construct(s) you are measuring. This determines which designs are valid.

| Construct type | Examples | Typical stability | Compatible designs |
|---|---|---|---|
| **Trait-like / slow** | Values, worldviews, identity | Years–decades | Cross-sectional, pre-post (long-term) |
| **Attitude / mid-range** | Wildlife attitudes, policy support | Months–years | BACI, ACI, repeated measures |
| **State-like / fast** | Affect, mood, situation-specific emotions | Hours–days | Within-subjects, experience sampling |

- [ ] I have identified each construct and assigned it a stability class (trait / attitude / state).
- [ ] The chosen design is compatible with the temporal stability of **all** focal constructs.
- [ ] I am not using a one-shot post-test to measure state-like constructs expected to be ephemeral.
- [ ] I am not expecting to detect value change over weeks — genuine value change requires multi-year tracking (Manfredo et al., 2003; 2021).

---

## 2. Design Type Selection

### 2a. Observational / Cross-Sectional
- [ ] Constructs are trait-like or stable enough for a single snapshot (Boren & Echeverri, 2025; Echeverri et al., 2017; Kaczensky et al., 2004).
- [ ] No causal inference about intervention effects is claimed.
- [ ] Sampling strategy allows generalization to the target population.

### 2b. Before–After–Control–Impact (BACI) — Gold Standard for Interventions
- [ ] A control group exists that does not receive the stimulus.
- [ ] Baseline (pre) measurement is collected **before** any exposure (documentary, workshop, game, etc.).
- [ ] Post measurement timing is justified given the expected duration of the effect (durable vs. transient).
- [ ] The stimulus is clearly defined: type (documentary / workshop / game / other), dose, and delivery format are documented.
- [ ] Sensitization risk from pre-measurement is acknowledged and addressed (e.g., filler items, counterbalancing).

### 2c. After–Control–Impact (ACI) — Natural Experiments / Retrospective
- [ ] Pre-measurement was impossible or would itself sensitize respondents.
- [ ] The design is explicitly labeled as ACI / natural experiment; within-individual change is **not** estimated.
- [ ] Equivalence of control and impact groups at baseline is argued via auxiliary evidence or matching.
- [ ] Limitations relative to BACI are stated in the manuscript.

### 2d. Within-Subjects (Repeated Measures)
- [ ] Justification for within-subjects approach documented (power, ecological validity, etc.).
- [ ] Testing / carry-over effects are addressed: counterbalancing, washout periods, or order-randomization.
- [ ] Attrition plan: baseline oversampling ratio calculated and documented (see `../Step_09_Power_and_Sampling/`).
- [ ] Retention rates will be reported transparently in the manuscript.

### 2e. Between-Subjects
- [ ] Sample size accounts for the between-subjects design (larger N required than within-subjects equivalent; see power scripts).
- [ ] Random assignment procedure documented (see `design_docs/randomization_plan.md`).
- [ ] Balance across key covariates verified post-randomization.

---

## 3. Intervention Specification (if applicable)

- [ ] Stimulus type documented: ☐ Documentary  ☐ Workshop  ☐ Game  ☐ Message framing  ☐ Other: ___________
- [ ] Stimulus content archived or referenced (file path or DOI).
- [ ] Delivery format: ☐ In-person  ☐ Online  ☐ Hybrid
- [ ] Exposure dose (duration, number of sessions) specified.
- [ ] **Expected change type declared:** ☐ Durable (persists > 3 months)  ☐ Transient (dissipates within days/weeks)
- [ ] Post-measurement timing aligns with expected change duration.
- [ ] Control condition described (waitlist, active placebo, business-as-usual).

---

## 4. Temporal Context Controls

Wildlife attitude and behavior studies are sensitive to when data are collected. The following factors must be recorded as covariates or controlled by design.

- [ ] **Season / phenological period** at data collection documented (e.g., breeding, migration, hunting season, dormancy).
- [ ] **Local conflict or management events** occurring near data collection window noted (e.g., wolf depredation incidents, culls, rewilding announcements).
- [ ] **Weather conditions** recorded or referenced where mood effects are plausible.
- [ ] **News / media salience** of focal taxa assessed for the data collection window.
- [ ] Data collection window justified: generalizability limitations from a single temporal window stated.
- [ ] If multiple waves, temporal covariates recorded at each wave.

---

## 5. Sampling and Randomization

- [ ] Target population defined with explicit inclusion/exclusion criteria.
- [ ] Sampling frame documented.
- [ ] Sampling strategy: ☐ Simple random  ☐ Stratified  ☐ Cluster  ☐ Convenience  ☐ Quota  ☐ Snowball
- [ ] For interventions: random assignment sequence generated by code (seed documented in `design_docs/randomization_plan.md`).
- [ ] Stratification or blocking variables justified.
- [ ] Expected attrition rate estimated; baseline oversampling applied (see power scripts).

*(Detailed power and sample size planning: `../Step_09_Power_and_Sampling/`)*

---

## 6. Measurement Timing and Survey Flow

- [ ] Measurement occasions mapped: T0 (baseline), T1 (immediate post), T2 (follow-up), etc.
- [ ] Delay between stimulus and post-measurement justified given hypothesized mechanism.
- [ ] Survey flow diagram created and stored in `design_docs/`.
- [ ] Attention checks and manipulation checks included and placed appropriately in the flow.
- [ ] Sensitive items (e.g., hunting behavior, illegal activity) are placed later in the instrument to reduce drop-off.
- [ ] Pre-registration completed before data collection begins (`../Step_05_PreRegistration/`).

---

## 7. Internal Validity Threats

Review each threat and document how the design addresses it.

| Threat | Relevant designs | Mitigation |
|---|---|---|
| History effects | BACI, ACI | Record contemporaneous events; short inter-wave intervals |
| Maturation | Repeated measures | Control group; short study duration |
| Testing / sensitization | Within-subjects, BACI | Filler items; ACI alternative; counterbalancing |
| Selection bias | Between-subjects | Random assignment; covariate balance checks |
| Attrition / dropout | Longitudinal | Oversampling; incentives; intent-to-treat analysis |
| Demand characteristics | All | Indirect measures; behavioral outcomes; blind conditions |
| Temporal context confounds | All wildlife studies | Record season, events, weather as covariates |

- [ ] Each relevant threat identified and mitigation strategy documented.

---

## 8. External Validity and Generalizability

- [ ] Study site / population described with respect to national or regional benchmarks.
- [ ] Temporal window limitations acknowledged.
- [ ] Replication across seasons, sites, or populations planned or recommended.
- [ ] Effect size and practical significance discussed (not only statistical significance).

---

## 9. Pre-registration and Open Science

- [ ] Hypotheses, design, and analysis plan pre-registered (OSF, AsPredicted, or equivalent).
- [ ] Pre-registration link/ID stored in `../Step_05_PreRegistration/`.
- [ ] Deviations from pre-registration will be labeled as exploratory in manuscript.
- [ ] Data and materials availability statement drafted.

---

## Sign-off

| Role | Name | Date | Notes |
|---|---|---|---|
| Lead researcher | | | |
| Co-investigator | | | |
| Methods reviewer | | | |

---

*References: Manfredo et al. (2003); Manfredo et al. (2021); Keren (1993); Boren & Echeverri (2025); Echeverri et al. (2017); Kaczensky et al. (2004); Clayton et al. (2013); Clayton & Brook (2005); Williams et al. (2024); Schreck Reis et al. (2013); Callahan et al. (2019).*
