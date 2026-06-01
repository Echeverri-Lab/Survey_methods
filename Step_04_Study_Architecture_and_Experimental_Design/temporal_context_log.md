# Temporal Context Log

Record temporal and environmental covariates for **every data collection wave**. These factors can confound wildlife attitude and behavior measures and must be available for analysis and reporting (see `study_design_checklist.md` §4).

---

## Study Metadata

| Field | Entry |
|---|---|
| Study title | |
| Principal investigator | |
| Study site(s) | |
| Focal taxon / taxa | |
| Pre-registration ID | |

---

## Wave Log

Copy the block below for each data collection wave (T0, T1, T2, …).

---

### Wave: __________ (e.g., T0 — Baseline)

**Dates of data collection:** ______________ to ______________

#### 1. Phenological / Seasonal Context

| Variable | Entry |
|---|---|
| Season (N. Hemisphere) | ☐ Winter  ☐ Spring  ☐ Summer  ☐ Autumn |
| Relevant phenological event (tick ✓ all that apply) | ☐ Hunting / trapping season open  ☐ Hunting season closed  ☐ Breeding / nesting season  ☐ Migration peak  ☐ Post-harvest / livestock gathering  ☐ None notable |
| Notes on phenological context | |

#### 2. Local Conflict or Management Events

| Variable | Entry |
|---|---|
| Any depredation incidents reported in study area during this wave? | ☐ Yes  ☐ No  ☐ Unknown |
| If yes: number of incidents, date range, species involved | |
| Any management actions (cull, translocation, relisting, quota change)? | ☐ Yes  ☐ No  ☐ Unknown |
| If yes: describe | |
| Any rewilding, reintroduction, or conservation program launch? | ☐ Yes  ☐ No |
| Notes | |

#### 3. Media Salience

| Variable | Entry |
|---|---|
| Major news stories involving focal taxon during wave? | ☐ Yes  ☐ No |
| If yes: headline summary and date | |
| Google Trends index for focal taxon (optional, 0–100) | |
| Social media spike observed? | ☐ Yes  ☐ No |
| Notes | |

#### 4. Weather (aggregate over data collection window)

| Variable | Entry |
|---|---|
| Mean temperature (°C or °F, specify) | |
| Precipitation (mm or qualitative: dry / normal / wet) | |
| Extreme weather events? (heat wave, drought, flooding) | ☐ Yes  ☐ No — describe if yes: |
| Data source (e.g., NOAA, local station, ECMWF) | |

#### 5. Socio-political Context

| Variable | Entry |
|---|---|
| Recent election or major policy vote? | ☐ Yes  ☐ No — describe if yes: |
| Active social movement relevant to study topic? | ☐ Yes  ☐ No |
| Notes | |

#### 6. Sample Characteristics This Wave

| Variable | Entry |
|---|---|
| N invited | |
| N completed | |
| Response rate (%) | |
| Known differences from prior wave (if applicable) | |
| Attrition characteristics (if repeated measures) | |

#### 7. Analyst Notes

> Free text — any additional contextual observations that may be relevant during analysis.

---

## Covariate Coding Guide (for analysis)

When these variables enter regression models or are used as covariates:

| Variable | Suggested coding |
|---|---|
| Season | Dummy (ref = winter) or cyclical (sine/cosine of day-of-year) |
| Hunting season open | Binary 0/1 |
| Recent depredation | Binary 0/1, or count of incidents within 30-day window |
| Media salience | Google Trends index (continuous) or binary spike |
| Wave | Numeric or dummy |
| Days since stimulus | Continuous (for decay modeling) |

---

*See also: `study_design_checklist.md` §4 · `design_decision_matrix.md` Part 4 · `../Step_10_Analysis/`*
