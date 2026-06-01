# Supporting Information — Step 07: Measuring Behavior
## Examples of Behavioral Measurement Tasks in Conservation Survey Research

> **How to use this document.**
> This file accompanies §2.7 of the methods manuscript. Each entry documents a real-world behavioral measurement paradigm drawn from peer-reviewed conservation and psychology research. For each example, the table records: the behavioral proxy used, the study context, the measurement instrument, the key analytic approach, and the connection to self-reported psychometric constructs. Use these as templates when designing the behavioral component of your own survey.

---

## Overview: Why Behavioral Measures?

Self-reported attitudes and intentions systematically overestimate pro-environmental behavior — a well-documented phenomenon known as the **attitude–behavior gap** (ElHaffar et al., 2020). Incorporating observed or incentive-compatible behavioral tasks into survey protocols addresses three core threats to construct validity:

1. **Social desirability bias** — respondents inflate reported intentions when they perceive a "correct" answer.
2. **Hypothetical bias** — stated willingness-to-pay or willingness-to-act overestimates real commitment when no actual cost is incurred.
3. **Temporal inconsistency** — stated future intentions decay before the behavior actually occurs.

The examples below span a spectrum from *low-cost behavioral proxies* (petition signatures, pledges) to *costly signals* (monetary donations, physical effort), and *passive behavioral traces* (mouse-tracking, dwell time). Ecologists can select the appropriate level of cost and observability for their study context.

---

## Example Matrix

| Example ID | Study | Behavioral Measure | Measurement Unit | Instrument | Analytic Approach |
|---|---|---|---|---|---|
| B-01 | Salazar et al. (2022) | Physical donation (money in box) | $ donated per visitor per day | In-person donation box | One-tailed independent *t*-test |
| B-02 | Salazar et al. (2022) | Virtual pledge (behavioral intention proxy) | Pledges per visitor per day | QR code → Padlet.com | One-tailed Welch's *t*-test |
| B-03 | Veríssimo et al. (2024) | Monetary donation (portion of incentive) | $ donated (0–$70 NZD) | End-of-survey choice | Between-group comparison; 6-week retention follow-up |
| B-04 | Veríssimo et al. (2024) | Behavioral intention (donate, volunteer, policy support) | 5-point Likert | Survey (Qualtrics) | Descriptive; group comparison |
| B-05 | Veríssimo et al. (2024) | Cat owner behavior (restriction measures) | Categorical choice (3 options) | Conditional branching survey item | Descriptive |
| B-06 | Radke et al. (2024) | Physical container recycling | Count of accepted containers brought to lab | In-person lab task | Between-group comparison (probabilistic vs. certain reward) |
| B-07 | Shi (2023) | Mouse-tracking visual attention (BubbleView) | Proportional dwell time; fixation count per AOI | Browser-based task (Qualtrics-compatible) | Pre-registered; mixed-effects regression |
| B-08 | Shi (2023) | Decision choice | Binary (better card = 1, worse card = 0) | Browser-based task | Logistic regression |

---

## Detailed Examples

---

### B-01 & B-02 — Physical Donations and Virtual Pledges
**Source:** Salazar, G., Monroe, M. C., Ennes, M., Jones, J. A., & Veríssimo, D. (2022). Testing the influence of visual framing on engagement and pro-environmental action. *Conservation Science and Practice*, 4(10), e12812. https://doi.org/10.1111/csp2.12812

#### Study Context
A field experiment at a natural history museum tested whether *positive* vs. *negative* visual framing of a conservation exhibit altered visitor pro-environmental behavior. Two behavioral outcomes were tracked simultaneously: physical donations (costly signal) and virtual pledges (low-cost behavioral intention proxy).

#### B-01 — Donations (Observed Behavior)

| Field | Detail |
|---|---|
| **Behavioral proxy** | Dollar amount deposited in a physical donation box |
| **Measurement unit** | Mean number of donations per visitor per day |
| **Seeding protocol** | Three $1 bills placed in box each morning to normalize the social norm of giving |
| **Variable role** | Dependent variable (observed behavior) |
| **Data structure** | Continuous, non-negative; non-normally distributed (Shapiro–Wilk *p* < .001); seven outliers retained (robust to *t*-test) |
| **Statistical test** | One-tailed independent *t*-test; Levene's test confirmed equal variances (*p* = .98) |
| **Design note** | Compared negative-framing vs. positive-framing exhibit conditions |

> **Ecological application.** A donation box placed at the exit of a visitor center, wildlife survey station, or community meeting can serve as a low-cost, unobtrusive behavioral outcome variable. Seeding the box removes the zero-norm signal that discourages first donations.

#### B-02 — Pledges (Behavioral Intention Proxy)

| Field | Detail |
|---|---|
| **Behavioral proxy** | Publicly posted virtual pledge via QR code → Padlet.com |
| **Measurement unit** | Mean number of pledges per visitor per day |
| **Pledge categories** | Private sphere (e.g., personal plastic use), non-activist public sphere (e.g., voting), activist behaviors (e.g., community action) — categories adapted from Stern (2000) |
| **Variable role** | Dependent variable (behavioral *intention*, not observed behavior) |
| **Data structure** | Non-normally distributed (Shapiro–Wilk *p* < .001); two outliers retained |
| **Statistical test** | One-tailed Welch's *t*-test; Levene's test showed unequal variances (*p* = .03), justifying Welch over Student's *t* |
| **Limitation** | Pledges are low-cost and public, so they may overestimate commitment relative to private costly behaviors (cf. B-01) |

> **Methodological note for ecologists.** When both a pledge and a donation measure are collected in the same study, the *difference* between the two (pledge rate minus donation rate) can serve as a direct operationalization of the attitude–behavior gap at the aggregate level.

---

### B-03, B-04 & B-05 — Incentive-Compatible Donation, Stated Intentions, and Cat Owner Behavior
**Source:** Veríssimo, D., Fiennes, S., & Dunn, M. (2024). Using digital mobile games to increase the support for nature conservation. *Conservation Science and Practice*, 6(11), e13236. https://doi.org/10.1111/csp2.13236

#### Study Context
A two-survey longitudinal experiment tested whether playing a mobile game featuring the Kākāpō (*Strigops habroptilus*) — a critically endangered New Zealand parrot — increased conservation support relative to a control game. Behavioral measurement was embedded directly into the survey instrument.

#### B-03 — End-of-Survey Donation (Incentive-Compatible; Costly Signal)

| Field | Detail |
|---|---|
| **Behavioral proxy** | Dollar amount donated from incentive payment |
| **Endowment** | $70 NZD (≈ $42 USD) incentive payment for survey completion |
| **Choice structure** | Participants privately allocated any portion (0–100%) to one of two Kākāpō conservation charities |
| **Variable role** | Dependent variable (observed costly behavior); continuous-ratio scale (0–$70) |
| **Retention measure** | Donation behavior re-assessed at 6-week follow-up survey |
| **Design note** | Real financial consequence: the donation was processed immediately. This distinguishes it from hypothetical willingness-to-donate measures. |
| **Power analysis** | *a priori* in R (`pwr` package): α = 0.05, power = 0.80, effect size *d* = 0.2 (Cohen, 2013); minimum *n* = 99 per group; final *N* = 200 (100 per group) |

> **Ecological application.** This design is directly replicable in conservation surveys. Upon completing a paid online survey (e.g., via Prolific, MTurk, or a grant-funded field stipend), participants are told a portion of their payment can be redirected to a named local conservation fund. Donation amount then becomes a continuous behavioral outcome that can be regressed against attitude, identity, and knowledge scales collected earlier in the same survey.

#### B-04 — Behavioral Intentions (Likert; Lower-Cost)

| Field | Detail |
|---|---|
| **Items** | (1) Donate to a Kākāpō conservation NGO; (2) Volunteer for a Kākāpō conservation NGO; (3) Support a policy to remove non-native mammalian predators from New Zealand |
| **Response format** | 5-point Likert scale: "Highly likely" to "Highly unlikely" |
| **Variable role** | Dependent variable (behavioral intention) |
| **Limitation** | Hypothetical; not incentive-compatible. Provides upper-bound estimate of behavioral commitment. |

#### B-05 — Conditional Behavior: Cat Owner Restriction Measures

| Field | Detail |
|---|---|
| **Branching logic** | Only shown to participants who answered "yes" to both (a) owning a cat and (b) allowing outdoor roaming |
| **Items** | Would you consider: (1) keeping cat indoors; (2) putting a bell on the cat; (3) limiting outdoor hours? |
| **Response format** | Categorical (Yes / No per option) |
| **Variable role** | Behavioral intention / feasibility measure; segment-specific |
| **Ecological rationale** | Cat predation on native wildlife is a direct conservation threat; conditional branching targets only the relevant sub-population |

> **Design note for ecologists.** Conditional branching allows survey instruments to embed *targeted behavioral items* for specific stakeholder groups without increasing burden for irrelevant respondents. Parallels in conservation surveys include: asking only farmers about pesticide reduction behaviors, or only fishers about bycatch reporting.

---

### B-06 — Physical Recycling Behavior Under Probabilistic vs. Certain Incentives
**Source:** Radke, J., Argentopoulos, S., Dunn, E. W., & Zhao, J. (2024). Probabilistic refunds increase beverage container recycling behavior. SSRN. https://doi.org/10.2139/ssrn.5016156

#### Study Context
A lab experiment recruited participants who were told — 24 hours before arrival — that they could bring recyclable beverage containers to the session and receive payment (either a certain $0.10/bottle or a probabilistic $1,000 at 0.01% chance per bottle). The number of containers physically brought to the lab served as the behavioral outcome.

| Field | Detail |
|---|---|
| **Behavioral proxy** | Count of accepted recyclable containers brought to the lab |
| **Measurement unit** | Count (integer, 0–24 bottles; maximum capped at 24) |
| **Conditions** | Certain reward ($0.10/bottle, 100%) vs. Probabilistic reward ($1,000/bottle, 0.01%) |
| **Variable role** | Dependent variable (observed, effortful behavior) |
| **Inclusion rule** | Participants who did not read the pre-study email were excluded; participants who read the email but brought no bottles were *included* (true zero behavior retained) |
| **Quality control** | Research assistant verified each container met BC ReturnIt acceptance criteria; non-accepted containers recorded separately for exploratory analysis |
| **Survey component** | Qualtrics survey administered after behavior; included affect ratings (0–100 happiness scale) pre- and post-task, recycling habit questions, and demographics |

> **Ecological application.** Physical effort tasks can be adapted for conservation contexts: e.g., asking participants to bring invasive plant cuttings, to sign up for a community cleanup day (with attendance tracked), or to return a prepaid biodiversity monitoring card. The key feature is that behavior precedes or accompanies the survey, making post-hoc justification impossible.

> **Methodological note.** Because participants knew about the opportunity in advance (email), the study captures *planned* effortful behavior — a higher bar than spontaneous in-survey choices. This distinction (planned vs. spontaneous costly behavior) should be matched to the research question.

---

### B-07 & B-08 — Mouse-Tracking Visual Attention and Decision Choice (BubbleView)
**Source:** Shi, C. (2023). *How does choice architecture influence attention and decision making?* (MA Thesis in Psychology, University of British Columbia).

#### Study Context
A lab experiment used a browser-based mouse-tracking paradigm (BubbleView; adapted from Luo & Zhao, 2019) to measure where participants visually attended when choosing between two credit card offers. A black opaque mask covered the stimulus; only a small circular region around the mouse cursor was revealed, forcing deliberate navigation of the visual field. Mouse position was logged continuously as a proxy for visual attention.

#### B-07 — Visual Attention via Mouse-Tracking

| Field | Detail |
|---|---|
| **Behavioral proxy** | Mouse position as proxy for visual fixation |
| **Measurement unit** | Proportional dwell time per AOI (total dwell on AOI ÷ total dwell on mask); proportional fixation count per AOI |
| **Areas of Interest (AOIs)** | 7 features per card × 2 cards = 14 AOIs total |
| **Instrument** | BubbleView task embedded in Qualtrics (browser-based; no eye-tracker hardware required) |
| **Starting position** | Mouse forced to center of screen at trial onset to equalize starting attention |
| **Pre-registration** | Yes — proportional dwell time and proportional fixation count were pre-registered primary attention measures |
| **Variable role** | Mediating/explanatory variable (attention allocation) |

> **Ecological application.** BubbleView requires no specialized hardware and runs in a standard browser, making it compatible with online surveys (Qualtrics, jsPsych). In a conservation context, it can quantify *which features of a species photograph or conservation message* attract visual attention, providing a behavioral complement to stated salience ratings. This is a lower-cost alternative to laboratory eye-tracking (SR Research EyeLink, Tobii) that is feasible for large online samples.

#### B-08 — Binary Choice Decision

| Field | Detail |
|---|---|
| **Behavioral proxy** | Card selection (better vs. worse card given participant's financial situation) |
| **Coding** | Binary: 1 = chose objectively better card; 0 = chose worse card |
| **Variable role** | Dependent variable (decision quality) |
| **Follow-up measures** | Surprise memory test (accuracy score); financial literacy (Fernandes et al., 2014); numeracy (Schwartz et al., 1997) |

---

## Selecting the Right Behavioral Measure: A Decision Guide

| Research Goal | Recommended Measure | Cost to Participant | Ecological Feasibility |
|---|---|---|---|
| Measure costly pro-environmental commitment | Incentive-compatible donation (B-03) | Moderate (real money) | High — deployable in Qualtrics/Prolific |
| Capture spontaneous in-situ behavior | Physical donation box (B-01) | Low (voluntary) | High — field surveys, visitor centers |
| Document behavioral intentions cheaply | Pledge / petition signature (B-02) | Very low | High — QR code, online form |
| Assess effortful planned behavior | Physical task before survey (B-06) | High (time + effort) | Moderate — lab or community event |
| Measure visual salience of stimuli | Mouse-tracking BubbleView (B-07) | Low | High — browser-based, online compatible |
| Target behavior-relevant subgroups | Conditional branching items (B-05) | Very low | High — standard survey logic |
| Track longitudinal behavior change | Multi-wave donation / pledge retention (B-03 6-wk) | Moderate | Moderate — requires follow-up contact |

---

## Integration with Psychometric Scales: Connecting Behavior to Survey Constructs

The value of behavioral measures is realized when they are regressed against psychometric constructs measured earlier in the same survey instrument. The following table illustrates example regression models that directly address the attitude–behavior gap:

| Outcome (Behavioral DV) | Psychometric Predictor(s) | Model Type | Expected Finding |
|---|---|---|---|
| Donation amount (B-03) | Wildlife attitude scale score | OLS / Tobit regression | Positive β — but gap expected for low-salience species |
| Recycling bottle count (B-06) | Pro-environmental self-identity (PESI) | Negative binomial / Poisson | Positive β — probabilistic reward may moderate |
| Mouse dwell time on species (B-07) | Species familiarity (SP-02 from Echeverri 2019) | Mixed-effects regression | Familiar species → longer dwell on identity-relevant features |
| Pledge signature (B-02) | Conservation knowledge score | Logistic regression | Positive β — but weaker than donation commitment |
| Cat restriction adoption (B-05) | Nature connectedness scale | Logistic regression | Positive β — especially for indoor-restriction option |

> **Note on Tobit regression.** Donation outcomes are typically left-censored at zero (many participants donate nothing). Ordinary least squares underestimates effects at the censoring boundary. A Tobit model explicitly accounts for the censoring mechanism and is preferred when the proportion of zero-donors exceeds ~20% of the sample (see `Step_10_Analysis/` for worked examples).

---

## References

- Cohen, J. (2013). *Statistical power analysis for the behavioral sciences* (2nd ed.). Routledge.
- ElHaffar, G., Durif, F., & Dubé, L. (2020). Towards closing the attitude-intention-behavior gap in green consumption: A narrative review of the literature and an overview of future research directions. *Journal of Cleaner Production*, 275, 122556.
- Fernandes, D., Lynch, J. G., & Netemeyer, R. G. (2014). Financial literacy, financial education, and downstream financial behaviors. *Management Science*, 60(8), 1861–1883.
- Luo, R., & Zhao, J. (2019). Inspired by BubbleView: Mouse-tracking as a proxy for visual attention. *Unpublished manuscript*, University of British Columbia.
- Radke, J., Argentopoulos, S., Dunn, E. W., & Zhao, J. (2024). Probabilistic refunds increase beverage container recycling behavior. SSRN. https://doi.org/10.2139/ssrn.5016156
- Salazar, G., Monroe, M. C., Ennes, M., Jones, J. A., & Veríssimo, D. (2022). Testing the influence of visual framing on engagement and pro-environmental action. *Conservation Science and Practice*, 4(10), e12812. https://doi.org/10.1111/csp2.12812
- Schwartz, L. M., Woloshin, S., Black, W. C., & Welch, H. G. (1997). The role of numeracy in understanding the benefit of screening mammography. *Annals of Internal Medicine*, 127(11), 966–972.
- Shi, C. (2023). *How does choice architecture influence attention and decision making?* (MA Thesis in Psychology, University of British Columbia).
- Stern, P. C. (2000). New environmental theories: Toward a coherent theory of environmentally significant behavior. *Journal of Social Issues*, 56(3), 407–424.
- Veríssimo, D., Fiennes, S., & Dunn, M. (2024). Using digital mobile games to increase the support for nature conservation. *Conservation Science and Practice*, 6(11), e13236. https://doi.org/10.1111/csp2.13236
