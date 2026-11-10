# =============================================================================
# Power analysis example (b): BACI with repeated measures
#   (Before-After x Control-Impact, each person measured twice)
# -----------------------------------------------------------------------------
# Design: participants are assigned to a CONTROL or an IMPACT (treatment)
#         group. Everyone completes the survey BEFORE the intervention (T0) and
#         AFTER it (T1). Time is within subjects; group is between subjects.
#
# The effect of interest is the group x time INTERACTION: did the impact group
# change more than the control group? With two time points this is exactly the
# same test as comparing CHANGE SCORES (T1 - T0) between the two groups.
#
# Why BACI needs its own power analysis: each person serves as their own
# baseline, which removes stable person-to-person differences. How much that
# helps depends on the CORRELATION between T0 and T1 scores (rho). High rho
# (a stable, reliable measure) means much smaller samples; low rho means the
# advantage shrinks, and below rho = .5 a change-score analysis is LESS
# powerful than simply comparing post-test scores.
#
# We estimate power two ways:
#   1. a closed-form calculation with pwr, using the effect size for change
#      scores, and
#   2. a SIMULATION that generates fake BACI data, fits the mixed model you
#      would actually run (lme4::lmer), and counts significant interactions.
#      Simulation is the general tool: it works for designs no formula covers
#      (more waves, clustering, unequal groups, missing data).
#
# How to run: open in RStudio and click "Source", or run
#   Rscript power_example_b_baci.R
# The simulation section takes a few seconds to a minute, depending on your computer.
#
# R packages used:
#   pwr  - closed-form power for t-tests
#   lme4 - linear mixed-effects models (random intercept per participant)
#   stats (built in) - rnorm(), lm(), etc.
# For more complex mixed models, see also the simr package, which wraps this
# kind of simulation around a fitted lme4 model.
# =============================================================================


# ---- 0. Install and load packages --------------------------------------------
for (pkg in c("pwr", "lme4")) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, repos = "https://cloud.r-project.org")
  }
}
library(pwr)
library(lme4)

cat("R version:", R.version.string, "\n")
cat("pwr version:", as.character(packageVersion("pwr")),
    "| lme4 version:", as.character(packageVersion("lme4")), "\n\n")


# ---- 1. Choosing the effect size ------------------------------------------------
# Express the expected effect as d_raw: the extra change in the impact group,
# relative to the control group, in units of the outcome's standard deviation
# at one time point. This is the same metric as a between-subjects d, so you
# can take it from meta-analyses and prior studies the same way (see
# power_example_a_two_groups.R for conversion formulas and the reasons not to
# use a pilot-study estimate).
#
# Example source (DOI checked with Crossref):
#   Bergquist, Thiel, Goldberg & van der Linden (2023). Field interventions
#   for climate change mitigation behaviors: A second-order meta-analysis.
#   PNAS, 120. https://doi.org/10.1073/pnas.2214851120
#   -> d = 0.18 after adjusting for publication bias (d = 0.31 unadjusted).
#
# Smallest effect size of interest (SESOI): if a change smaller than some
# amount would not matter to managers or to your theory, power the study for
# that amount instead (Lakens, Scheel & Isager, 2018,
# https://doi.org/10.1177/2515245918770963).
#
# The pre-post correlation rho must also be justified. Good sources: the
# test-retest reliability reported for your scale over a similar interval, or
# the T0-T1 correlation in a published study using the same measure. We run a
# sensitivity analysis over rho below because it matters so much.


# ---- 2. YOUR ASSUMPTIONS (edit these) -------------------------------------------
d_raw  <- 0.18   # impact-minus-control difference in change, in SD units
rho    <- 0.50   # EXAMPLE value for the T0-T1 correlation; replace with a
                 # cited test-retest correlation for your measure
alpha  <- 0.05
power  <- 0.80

# EXAMPLE loss rates; replace with figures from your platform or prior waves.
nonresponse_rate <- 0.10  # recruited but unusable at T0 (incomplete, failed
                          # pre-registered attention checks)
attrition_rate   <- 0.25  # completed T0 but did not return at T1. Repeated
                          # measures designs lose people between waves; plan
                          # for it, and check whether dropout differs by group.


# ---- 3. Closed-form calculation --------------------------------------------------
# Change score for person i: change_i = T1_i - T0_i.
# If each time point has SD = 1 and correlation rho, then
#   SD(change) = sqrt(2 * (1 - rho)).
# The effect size for comparing change scores between groups is therefore
#   d_change = d_raw / sqrt(2 * (1 - rho)).
d_change <- d_raw / sqrt(2 * (1 - rho))
cat(sprintf("d on the raw scale = %.2f; with rho = %.2f, d for change scores = %.3f\n\n",
            d_raw, rho, d_change))

res <- pwr.t.test(d = d_change, sig.level = alpha, power = power,
                  type = "two.sample", alternative = "two.sided")
print(res)

n_per_group <- ceiling(res$n)   # people who must complete BOTH waves
n_recruit_per_group <- ceiling(n_per_group /
                               ((1 - nonresponse_rate) * (1 - attrition_rate)))
cat(sprintf("\nCompleters needed per group (T0 and T1): %d (total %d)\n",
            n_per_group, 2 * n_per_group))
cat(sprintf("N to RECRUIT per group at T0           : %d (total %d)\n",
            n_recruit_per_group, 2 * n_recruit_per_group))
cat(sprintf("  (inflated for %.0f%% non-response and %.0f%% attrition)\n\n",
            100 * nonresponse_rate, 100 * attrition_rate))


# ---- 4. Sensitivity to the pre-post correlation ----------------------------------
rho_grid <- c(0.3, 0.5, 0.7, 0.8)
sens <- data.frame(
  rho = rho_grid,
  d_change = round(d_raw / sqrt(2 * (1 - rho_grid)), 3),
  completers_per_group = sapply(rho_grid, function(r) {
    ceiling(pwr.t.test(d = d_raw / sqrt(2 * (1 - r)), sig.level = alpha,
                       power = power, type = "two.sample")$n)
  })
)
sens$recruit_total <- 2 * ceiling(sens$completers_per_group /
                                  ((1 - nonresponse_rate) * (1 - attrition_rate)))
# For comparison: an after-only design (no baseline) needs the same n as a
# two-group t-test with d_raw, whatever rho is.
n_after_only <- ceiling(pwr.t.test(d = d_raw, sig.level = alpha, power = power,
                                   type = "two.sample")$n)
cat("Sensitivity to rho (d_raw =", d_raw, "):\n")
print(sens, row.names = FALSE)
cat(sprintf("After-only comparison would need %d per group (no baseline used).\n",
            n_after_only))
cat("Note: at rho = .5 the change-score test needs the same N as the after-only\n",
    "test, and when rho < .5 it needs MORE. An ANCOVA (post-test adjusted for\n",
    "pre-test) is never worse than either, so these numbers are conservative.\n\n",
    sep = "")


# ---- 5. Simulation with a mixed model ----------------------------------------------
# The simulation builds a fake data set that looks like your real one:
#   score = person's own baseline level (random intercept, SD sqrt(rho))
#         + time effect common to both groups (here 0.10 SD; any value works)
#         + d_raw extra change in the impact group at T1 (the BACI effect)
#         + measurement noise (SD sqrt(1 - rho))
# With these variances each time point has SD 1 and corr(T0, T1) = rho.
# We fit  score ~ group * time + (1 | id)  and call the interaction significant
# if |t| > 1.96 (a normal approximation; fine for samples this large).

simulate_baci <- function(n_per_group, d_raw, rho, time_effect = 0.10) {
  n  <- 2 * n_per_group
  id <- rep(seq_len(n), each = 2)                    # each person has 2 rows
  group  <- rep(rep(c(0, 1), each = n_per_group), each = 2)  # 0 control, 1 impact
  time   <- rep(c(0, 1), times = n)                  # 0 = before, 1 = after
  person <- rnorm(n, 0, sqrt(rho))[id]               # stable person level
  noise  <- rnorm(2 * n, 0, sqrt(1 - rho))
  score  <- person + time_effect * time + d_raw * group * time + noise
  data.frame(id = factor(id), group, time, score)
}

power_by_simulation <- function(n_per_group, d_raw, rho, n_sims = 300) {
  hits <- replicate(n_sims, {
    dat <- simulate_baci(n_per_group, d_raw, rho)
    fit <- lmer(score ~ group * time + (1 | id), data = dat)
    t_value <- coef(summary(fit))["group:time", "t value"]
    abs(t_value) > qnorm(1 - alpha / 2)
  })
  mean(hits)
}

set.seed(2026)
cat("Simulating...\n")
sim_power <- power_by_simulation(n_per_group, d_raw, rho)
cat(sprintf("Simulated power with %d completers per group: %.3f (target %.2f)\n",
            n_per_group, sim_power, power))
cat("(With 300 simulations the estimate has a margin of error of about +/- 0.05;\n",
    "increase n_sims for a more precise check.)\n", sep = "")

# ---- What to report -----------------------------------------------------------------
# "We assumed the impact group would change d = 0.18 SD more than the control
#  group (publication-bias-adjusted estimate, Bergquist et al., 2023) and a
#  T0-T1 correlation of rho = [value] (source). For the group x time
#  interaction with alpha = .05 and 80% power we need N completers per group
#  (closed form via pwr; confirmed by simulating the mixed model in lme4).
#  Allowing for [x]% non-response and [y]% attrition, we will recruit M per
#  group at baseline."
