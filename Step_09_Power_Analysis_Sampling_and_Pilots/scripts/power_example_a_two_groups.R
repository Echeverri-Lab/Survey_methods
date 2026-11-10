# =============================================================================
# Power analysis example (a): two conditions, between subjects
# -----------------------------------------------------------------------------
# Design: participants are randomly assigned to ONE of two conditions
#         (control vs. treatment) and the outcome is measured once, after the
#         treatment. The analysis is an independent-samples t-test (or a
#         regression of the outcome on a treatment dummy, which is the same test).
#
# Question this script answers:
#   "How many people do I need per condition to detect the effect I expect?"
#
# How to run it:
#   1. Install R (https://cran.r-project.org) and, optionally, RStudio.
#   2. Open this file in RStudio and click "Source", or in a terminal run:
#        Rscript power_example_a_two_groups.R
#   3. Change the numbers in the "YOUR ASSUMPTIONS" section and run it again.
#
# R packages used:
#   pwr   - closed-form power calculations for t-tests, ANOVA, correlations
#           (Champely, CRAN: https://cran.r-project.org/package=pwr)
#   stats - comes with R; used for the simulation check (t.test)
# =============================================================================


# ---- 0. Install and load packages --------------------------------------------
# install.packages() downloads a package from CRAN. You only need to do this
# once per computer, so we install pwr only if it is missing.
if (!requireNamespace("pwr", quietly = TRUE)) {
  install.packages("pwr", repos = "https://cloud.r-project.org")
}
library(pwr)  # library() loads an installed package for this session

# Print versions so your output records exactly what you ran.
cat("R version:", R.version.string, "\n")
cat("pwr version:", as.character(packageVersion("pwr")), "\n\n")


# ---- 1. Choosing and justifying the effect size -------------------------------
# The effect size is the single most important (and most often unjustified)
# input. For two groups we use Cohen's d: the difference between the two group
# means divided by their pooled standard deviation.
#
# Where should d come from? In order of preference:
#
#   (1) A META-ANALYSIS of interventions like yours. It pools many studies, so
#       its estimate is far more precise than any single study. Prefer
#       estimates that are adjusted for publication bias, because published
#       effects are inflated on average.
#   (2) A few PRIOR STUDIES with a similar intervention, population, and
#       outcome. Convert their reported statistics to d (see section 2).
#   (3) Your SMALLEST EFFECT SIZE OF INTEREST (SESOI): the smallest effect that
#       would matter for theory or practice (Lakens, Scheel & Isager, 2018).
#       Powering for the SESOI means a null result is informative: if the true
#       effect were as large as you care about, you would likely have found it.
#
# Why NOT a pilot study's effect size? Pilots are small, so their effect-size
# estimates are very noisy. Researchers also tend to go ahead only when the
# pilot effect looked large, which biases the estimate upward and leaves the
# main study underpowered (Kraemer et al., 2006; Albers & Lakens, 2018). Use
# pilots to test procedures, timing, and measures, not to set d.
#
# Verified sources used below (DOIs checked with Crossref):
#   * Bergquist, Thiel, Goldberg & van der Linden (2023). Field interventions
#     for climate change mitigation behaviors: A second-order meta-analysis.
#     PNAS, 120. https://doi.org/10.1073/pnas.2214851120
#     -> overall d = 0.31 (unadjusted); d = 0.18 after adjusting for
#        publication bias (unique primary studies).
#   * Nisa, Bélanger, Schumpe & Faller (2019). Meta-analysis of randomised
#     controlled trials testing behavioural interventions to promote household
#     action on climate change. Nature Communications, 10.
#     https://doi.org/10.1038/s41467-019-12457-2
#     -> |d| = 0.093 while the intervention lasts (randomised trials only).
#   * Richard, Bond & Stokes-Zoota (2003). One hundred years of social
#     psychology quantitatively described. Review of General Psychology, 7,
#     331-363. https://doi.org/10.1037/1089-2680.7.4.331
#     -> typical social-psychology effect r = .21 (SD of r across literatures
#        = .15).
#
# These are examples for behaviour-change interventions. Replace them with the
# best evidence for YOUR intervention and outcome.


# ---- 2. Converting reported statistics to d -----------------------------------
# Papers rarely report d directly. These small functions convert the most
# common statistics (formulas from Lakens, 2013,
# https://doi.org/10.3389/fpsyg.2013.00863, and Borenstein et al., 2009,
# Introduction to Meta-Analysis, https://doi.org/10.1002/9780470743386).

# From group means and standard deviations (pooled SD):
d_from_means <- function(m1, m2, sd1, sd2, n1, n2) {
  sd_pooled <- sqrt(((n1 - 1) * sd1^2 + (n2 - 1) * sd2^2) / (n1 + n2 - 2))
  (m1 - m2) / sd_pooled
}

# From an independent-samples t statistic and the two group sizes:
d_from_t <- function(t, n1, n2) {
  t * sqrt(1 / n1 + 1 / n2)
}

# From a correlation r (e.g., a point-biserial correlation, or a meta-analytic
# average r):
d_from_r <- function(r) {
  2 * r / sqrt(1 - r^2)
}

# From an F statistic with 1 numerator df (a two-group ANOVA): t = sqrt(F).
d_from_F <- function(F, n1, n2) {
  d_from_t(sqrt(F), n1, n2)
}

# Worked conversion: the typical social-psychology effect r = .21
# (Richard et al., 2003) corresponds to
d_typical_socpsych <- d_from_r(0.21)
cat(sprintf("Typical social-psychology effect r = .21  ->  d = %.2f\n",
            d_typical_socpsych))
# Note: this "typical" effect comes from a literature with publication bias and
# from many kinds of studies. Treat it as an upper benchmark, not a default.


# ---- 3. YOUR ASSUMPTIONS (edit these) -----------------------------------------
d_assumed <- 0.18   # publication-bias-adjusted d from Bergquist et al. (2023)
alpha     <- 0.05   # Type I error rate: chance of a false positive if the
                    # true effect is zero. .05 is the convention; justify any
                    # other value (e.g., a smaller alpha for many tests).
power     <- 0.80   # 1 - beta: chance of detecting the effect if it is real.
                    # .80 is a minimum convention; .90 is better when a missed
                    # effect would be costly.
sided     <- "two.sided"  # use "greater" only if you pre-register a
                          # directional test and an effect in the other
                          # direction would be treated as "no effect".

# Attrition and non-response. These are EXAMPLE values: replace them with
# rates from your recruitment platform, your partner organization, or prior
# studies with the same population, and cite the source in your proposal.
nonresponse_rate <- 0.10  # share of recruited people who start but never
                          # finish, or are excluded by pre-registered
                          # quality checks (attention checks, speeders)
attrition_rate   <- 0.00  # share lost between waves; 0 here because this
                          # design measures each person only once


# ---- 4. Solve for the sample size ----------------------------------------------
# pwr.t.test() solves for whichever argument you leave out. We leave out n, so
# it returns the n PER GROUP needed for the requested power.
res <- pwr.t.test(d = d_assumed, sig.level = alpha, power = power,
                  type = "two.sample", alternative = sided)
print(res)

n_per_group <- ceiling(res$n)  # always round UP: you cannot recruit 0.3 people

# Inflate for losses: if 10% of people are lost, you must recruit
# n / (1 - 0.10) so that n remain.
n_recruit_per_group <- ceiling(n_per_group /
                               ((1 - nonresponse_rate) * (1 - attrition_rate)))

cat(sprintf("\nAnalysable N needed per group : %d (total %d)\n",
            n_per_group, 2 * n_per_group))
cat(sprintf("N to RECRUIT per group        : %d (total %d), after inflating for\n",
            n_recruit_per_group, 2 * n_recruit_per_group))
cat(sprintf("  %.0f%% non-response and %.0f%% attrition\n\n",
            100 * nonresponse_rate, 100 * attrition_rate))


# ---- 5. Sensitivity analysis -----------------------------------------------------
# Your assumed d is uncertain, so show how N changes across plausible values.
# Here: Nisa et al. (2019) |d| = 0.093, Bergquist et al. (2023) adjusted 0.18
# and unadjusted 0.31, and the converted social-psychology benchmark 0.43.
d_grid <- c(0.093, 0.18, 0.31, round(d_typical_socpsych, 2))
sens <- data.frame(
  d = d_grid,
  n_per_group = sapply(d_grid, function(d) {
    ceiling(pwr.t.test(d = d, sig.level = alpha, power = power,
                       type = "two.sample", alternative = sided)$n)
  })
)
sens$n_total <- 2 * sens$n_per_group
sens$n_recruit_total <- 2 * ceiling(sens$n_per_group /
                                    ((1 - nonresponse_rate) * (1 - attrition_rate)))
cat("Sensitivity analysis (alpha =", alpha, ", power =", power, "):\n")
print(sens, row.names = FALSE)

# The reverse question: if you can only afford, say, 150 people per group,
# what is the smallest effect you could detect with 80% power?
n_feasible <- 150
d_detectable <- pwr.t.test(n = n_feasible, sig.level = alpha, power = power,
                           type = "two.sample", alternative = sided)$d
cat(sprintf("\nWith %d per group you have %.0f%% power to detect d >= %.2f\n",
            n_feasible, 100 * power, d_detectable))


# ---- 6. Check by simulation (optional but instructive) ---------------------------
# Simulation repeats a fake study many times under your assumptions and counts
# how often the test is significant. That share IS the power. It should match
# pwr's answer; the same idea extends to designs pwr cannot handle (see the
# BACI example, power_example_b_baci.R).
set.seed(2026)        # makes the random numbers reproducible
n_sims <- 2000        # more simulations = more precise estimate (but slower)
significant <- replicate(n_sims, {
  control   <- rnorm(n_per_group, mean = 0,         sd = 1)
  treatment <- rnorm(n_per_group, mean = d_assumed, sd = 1)  # SD = 1, so the
                                                             # mean shift = d
  t.test(treatment, control, var.equal = TRUE)$p.value < alpha
})
cat(sprintf("Simulated power with %d per group: %.3f (target %.2f)\n",
            n_per_group, mean(significant), power))

# ---- What to report ----------------------------------------------------------------
# "We assumed d = 0.18, the publication-bias-adjusted estimate from a
#  second-order meta-analysis of field interventions (Bergquist et al., 2023).
#  With alpha = .05 (two-sided) and 80% power, an independent-samples t-test
#  requires N analysable participants per condition (pwr::pwr.t.test).
#  Allowing for 10% non-response, we will recruit M per condition."
# Fill N and M from the output above, and attach the sensitivity table.
#
# Further reading: Lakens (2022). Sample size justification. Collabra:
# Psychology, 8. https://doi.org/10.1525/collabra.33267
