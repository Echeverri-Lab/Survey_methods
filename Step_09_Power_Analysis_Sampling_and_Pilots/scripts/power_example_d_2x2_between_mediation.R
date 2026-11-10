# =============================================================================
# Power analysis example (d): 2 x 2 between-subjects message experiment with
#                             behavioural outcomes and mediation
# -----------------------------------------------------------------------------
# A HYPOTHETICAL study, invented for teaching:
#
#   Factor A (focal)       : message FORMAT - a first-person story (narrative)
#                            vs. a fact sheet with statistics (non-narrative)
#   Factor B (exploratory) : MESSENGER - a wetland scientist vs. a local farmer
#   Topic                  : restoring a drained wetland next to farmland
#
#   Each participant sees ONE of the 4 combinations (between subjects).
#   Planned N = 600: 150 per cell, so 300 per level of the focal factor.
#
#   H1  Narrative messages increase support for wetland restoration
#       (continuous attitude scale) compared with fact sheets.
#   H2  Narrative messages increase behaviour:
#         (a) the amount donated to a restoration fund from a study bonus
#         (b) signing a (real) petition, yes/no
#   H3  The effect of format on support is MEDIATED by emotional engagement
#       with the message (format -> engagement -> support).
#
# What this script does:
#   1. H1: the smallest effect N = 600 can detect (sensitivity analysis), and
#      the N needed for the smallest effect size of interest (a priori).
#   2. The same main effect expressed as a 2 x 2 ANOVA effect (f, f^2,
#      partial eta^2), and why the interaction is exploratory.
#   3. H2: power for the donation amount and the petition signature.
#   4. H3: Monte Carlo power for the indirect (mediated) effect.
#   5. A plain-language summary.
#
# How to run: open in RStudio and click "Source", or run
#   Rscript power_example_d_2x2_between_mediation.R
# The mediation simulation takes a few seconds.
#
# R packages used:
#   pwr   - pwr.t.test, pwr.f2.test, pwr.2p.test (closed-form power)
#   stats - comes with R; used for the simulation
# =============================================================================


# ---- 0. Setup ---------------------------------------------------------------------
if (!requireNamespace("pwr", quietly = TRUE)) {
  install.packages("pwr", repos = "https://cloud.r-project.org")
}
library(pwr)
set.seed(2026)  # makes the simulation reproducible: same numbers every run

cat("R version:", R.version.string, "\n")
cat("pwr version:", as.character(packageVersion("pwr")), "\n\n")

alpha       <- 0.05   # two-sided Type I error rate
power       <- 0.80   # target power
N_total     <- 600    # planned total sample (what the budget allows)
n_cells     <- 4      # 2 x 2 design
n_per_cell  <- N_total / n_cells      # 150
n_per_level <- N_total / 2            # 300 per level of the focal factor


# ---- Effect-size conversion helpers --------------------------------------------------
# Meta-analyses in communication research often report r; power functions for
# group comparisons use d. For two groups of equal size:
d_to_r <- function(d) d / sqrt(d^2 + 4)
r_to_d <- function(r) 2 * r / sqrt(1 - r^2)


# ---- Choosing and justifying the effect size -------------------------------------------
# Meta-analytic anchor (DOI checked with Crossref; values from the abstract):
#   Braddock & Dillard (2016). Meta-analytic evidence for the persuasive effect
#   of narratives on beliefs, attitudes, intentions, and behaviors.
#   Communication Monographs, 83(4), 446-467.
#   https://doi.org/10.1080/03637751.2015.1128555
#   -> narrative vs. non-narrative: r = .17 (beliefs), .19 (attitudes),
#      .17 (intentions), .23 (behaviors; only k = 5 studies).
r_meta_behavior <- 0.23
d_meta_behavior <- r_to_d(r_meta_behavior)
r_meta_attitude <- 0.19
d_meta_attitude <- r_to_d(r_meta_attitude)

# Smallest effect size of interest (SESOI). Our narrative and fact sheet share
# the same facts, the same length, and the same messenger, so the contrast is
# SUBTLER than many comparisons pooled in the meta-analysis. We therefore treat
# roughly HALF the meta-analytic behaviour effect as the smallest effect worth
# detecting: d = 0.23. Anything smaller would be too small to justify the cost
# of producing narrative materials for restoration outreach.
d_sesoi <- 0.23

# Benchmark: the average social-psychology effect is r = .21 (Richard, Bond &
# Stokes-Zoota, 2003, Review of General Psychology, 7, 331-363,
# https://doi.org/10.1037/1089-2680.7.4.331), i.e. d of about 0.43. Our SESOI
# is about half of that, which is a deliberately cautious target.
r_benchmark <- 0.21

cat(sprintf("Meta-analytic narrative effect on behaviour: r = %.2f -> d = %.2f\n",
            r_meta_behavior, d_meta_behavior))
cat(sprintf("Meta-analytic narrative effect on attitudes: r = %.2f -> d = %.2f\n",
            r_meta_attitude, d_meta_attitude))
cat(sprintf("Social-psychology benchmark r = %.2f -> d = %.2f\n",
            r_benchmark, r_to_d(r_benchmark)))
cat(sprintf("SESOI d = %.2f (= r %.3f), about half the behaviour effect\n\n",
            d_sesoi, d_to_r(d_sesoi)))
# Why not a pilot? A pilot of 20-40 people per group estimates d so
# imprecisely that it cannot tell 0.1 from 0.5, and pilots that "look
# promising" are biased upward (Albers & Lakens, 2018,
# https://doi.org/10.1016/j.jesp.2017.09.004).


# ---- 1. H1: main effect of message format ---------------------------------------------
# Sensitivity analysis (Lakens, 2022, Sample size justification, Collabra:
# Psychology, 8, 33267, https://doi.org/10.1525/collabra.33267): when N is
# fixed by the budget, ask "what is the smallest effect we can detect with
# 80% power?" Leave d out, give n, and pwr solves for d.
sens_h1 <- pwr.t.test(n = n_per_level, sig.level = alpha, power = power,
                      type = "two.sample", alternative = "two.sided")
d_min_h1 <- sens_h1$d
cat("== H1: main effect of format (narrative vs. fact sheet) ==\n")
print(sens_h1)
cat(sprintf("With %d per level, the minimum detectable effect is d = %.3f (r = %.3f).\n",
            n_per_level, d_min_h1, d_to_r(d_min_h1)))

# A priori analysis: how many people per level do we need for the SESOI?
apriori_h1 <- pwr.t.test(d = d_sesoi, sig.level = alpha, power = power,
                         type = "two.sample", alternative = "two.sided")
n_needed_h1 <- ceiling(apriori_h1$n)
cat(sprintf("For d = %.2f we need %d per level (%d total); we plan %d per level.\n",
            d_sesoi, n_needed_h1, 2 * n_needed_h1, n_per_level))
power_at_plan <- pwr.t.test(n = n_per_level, d = d_sesoi, sig.level = alpha,
                            type = "two.sample")$power
cat(sprintf("Power for d = %.2f with the planned N: %.3f\n\n", d_sesoi, power_at_plan))


# ---- 2. The same effect as a 2 x 2 ANOVA ------------------------------------------------
# In the full 2 x 2 model (format, messenger, format x messenger) each effect
# has 1 numerator df. pwr.f2.test() works with Cohen's f^2 for regression /
# ANOVA effects:
#   u = numerator df (1 for each 2-level effect)
#   v = denominator df = N - number of cells = N - 4
# For a 1-df effect with balanced cells, Cohen's f = d / 2, so f^2 = d^2 / 4.
# Partial eta^2 = f^2 / (1 + f^2).
f_sesoi  <- d_sesoi / 2
f2_sesoi <- f_sesoi^2
anova_main <- pwr.f2.test(u = 1, v = N_total - n_cells, f2 = f2_sesoi,
                          sig.level = alpha)
anova_sens <- pwr.f2.test(u = 1, v = N_total - n_cells, sig.level = alpha,
                          power = power)
f2_min <- anova_sens$f2
cat("== The main effect inside the 2 x 2 ANOVA ==\n")
cat(sprintf("d = %.2f -> f = %.3f, f^2 = %.4f, partial eta^2 = %.4f\n",
            d_sesoi, f_sesoi, f2_sesoi, f2_sesoi / (1 + f2_sesoi)))
cat(sprintf("Power for this main effect with N = %d: %.3f\n",
            N_total, anova_main$power))
cat(sprintf("Minimum detectable 1-df effect with N = %d: f^2 = %.4f (f = %.3f, d = %.3f, partial eta^2 = %.4f)\n",
            N_total, f2_min, sqrt(f2_min), 2 * sqrt(f2_min), f2_min / (1 + f2_min)))

# Interactions: if the messenger changes the format effect by HALF of the
# main effect, the interaction f is half the main-effect f, so f^2 is a
# quarter as large and the required N is about FOUR times larger.
f2_interaction <- (f_sesoi / 2)^2
n_interaction <- ceiling(pwr.f2.test(u = 1, f2 = f2_interaction,
                                     sig.level = alpha, power = power)$v) + n_cells
n_main <- ceiling(pwr.f2.test(u = 1, f2 = f2_sesoi, sig.level = alpha,
                              power = power)$v) + n_cells
cat(sprintf("N for the main effect: %d. N for an interaction half that size: %d (%.1f x).\n",
            n_main, n_interaction, n_interaction / n_main))
cat("=> With N = 600 the messenger factor and the interaction are EXPLORATORY.\n",
    "   Pre-register them as exploratory and do not interpret a null interaction\n",
    "   as evidence that the messenger does not matter.\n\n", sep = "")


# ---- 3. H2: behavioural outcomes --------------------------------------------------------
cat("== H2: behavioural outcomes ==\n")
# (a) Donation amount (continuous). If treated as continuous, power is the same
# t-test as H1: the minimum detectable d with 300 per level is d_min_h1.
# Caution: donation amounts usually pile up at zero (many people give nothing)
# and are right-skewed. A t-test then loses power and the mean is a poor
# summary. Consider a HURDLE model (a logistic model for give / don't give
# plus a model for the amount among givers) and check its power by
# simulation, or pre-register a transformation or rank-based test.
cat(sprintf("(a) Donation (treated as continuous): minimum detectable d = %.3f\n",
            d_min_h1))

# (b) Petition signature (yes/no). For proportions, Cohen's effect size is h:
#   h = 2*asin(sqrt(p1)) - 2*asin(sqrt(p0)).
# First find the smallest h detectable with 300 per group...
sens_h2 <- pwr.2p.test(n = n_per_level, sig.level = alpha, power = power,
                       alternative = "two.sided")
h_min <- sens_h2$h
cat(sprintf("(b) Petition: minimum detectable Cohen's h = %.3f\n", h_min))

# ...then translate h into percentage points. h depends on the baseline rate
# p0 (the signing rate in the fact-sheet condition), so show several
# baselines. Solving the formula for h gives p1 = sin(asin(sqrt(p0)) + h/2)^2.
p0_grid <- c(0.20, 0.30, 0.40, 0.50)
p1_grid <- sin(asin(sqrt(p0_grid)) + h_min / 2)^2
petition <- data.frame(
  baseline_signing = sprintf("%.0f%%", 100 * p0_grid),
  detectable_signing = sprintf("%.1f%%", 100 * p1_grid),
  increase_points = round(100 * (p1_grid - p0_grid), 1)
)
print(petition, row.names = FALSE)
cat("Choose the baseline from prior petitions with this population if you can.\n\n")


# ---- 4. H3: mediation (Monte Carlo, joint significance) ----------------------------------
# Mediation model:
#   a path: format (X) -> engagement (M)
#   b path: engagement (M) -> support (Y), controlling for X
#   indirect effect = a * b
# There is no simple formula for the power of a*b, so we simulate it. We use
# the JOINT SIGNIFICANCE test: the indirect effect is "detected" when BOTH
# the a path and the b path are significant. It performs about as well as
# bootstrap tests at these sample sizes (Fritz & MacKinnon, 2007).
#
# Data-generating model for each simulated study:
#   X = -0.5 (fact sheet) or +0.5 (narrative), half the sample each
#   M = a_d * X + e_M,              e_M ~ Normal(0, 1)
#       -> a_d is the standardized mean difference (d) in engagement
#   Y = b * M + e_Y,                e_Y ~ Normal(0, sqrt(1 - b^2))
#       -> b is (approximately) the standardized effect of M on Y;
#          no direct effect of X on Y is assumed (c' = 0)

p_from_lm <- function(y, X, j) {
  # Fast least squares: coefficient j's two-sided p-value.
  fit <- lm.fit(X, y)
  df  <- nrow(X) - ncol(X)
  sigma2 <- sum(fit$residuals^2) / df
  XtX_inv <- chol2inv(qr.R(fit$qr))
  se <- sqrt(sigma2 * diag(XtX_inv))
  t  <- fit$coefficients / se
  2 * pt(-abs(t[j]), df)
}

mediation_power <- function(N, a_d, b, n_sims = 2000) {
  x <- rep(c(-0.5, 0.5), each = N / 2)
  X_a <- cbind(1, x)                       # design matrix for M ~ X
  hits <- 0
  for (s in seq_len(n_sims)) {
    m <- a_d * x + rnorm(N, 0, 1)
    y <- b * m + rnorm(N, 0, sqrt(1 - b^2))
    p_a <- p_from_lm(m, X_a, 2)            # a path
    p_b <- p_from_lm(y, cbind(1, x, m), 3) # b path, controlling for X
    if (p_a < alpha && p_b < alpha) hits <- hits + 1
  }
  hits / n_sims
}

cat("== H3: mediation power (joint significance, 2,000 simulations per cell) ==\n")
grid <- expand.grid(a_d = c(0.23, 0.30, 0.40), b = c(0.14, 0.20, 0.26))
grid$power <- mapply(function(a, b) mediation_power(N_total, a, b),
                     grid$a_d, grid$b)
grid$a_as_r <- round(d_to_r(grid$a_d), 3)
print(grid[, c("a_d", "a_as_r", "b", "power")], row.names = FALSE)
cat("Benchmark: Fritz & MacKinnon (2007, Table 3) report that with small a and b\n",
    "paths (both .14) about N = 558 (percentile bootstrap), 462 (bias-corrected\n",
    "bootstrap), or 530 (joint significance) give .80 power. Their a path is a\n",
    "standardized coefficient; our a_d = 0.23 corresponds to r of about 0.11\n",
    "(column a_as_r), which is why power is lowest in the first row.\n",
    "A SERIAL mediator (X -> M1 -> M2 -> Y) multiplies three paths, so its power\n",
    "is lower still; simulate it before pre-registering it as confirmatory.\n\n",
    sep = "")
# Fritz, M. S., & MacKinnon, D. P. (2007). Required sample size to detect the
# mediated effect. Psychological Science, 18(3), 233-239.
# https://doi.org/10.1111/j.1467-9280.2007.01882.x


# ---- 5. Summary -------------------------------------------------------------------------
# Detectable increases computed from h for every baseline (not hard-coded):
increase_range <- range(100 * (p1_grid - p0_grid))
cat("================ SUMMARY ================\n")
cat(sprintf("Design: 2 x 2 between subjects, N = %d (%d per cell, %d per level of format).\n",
            N_total, n_per_cell, n_per_level))
cat(sprintf("H1: minimum detectable d = %.2f; power for the SESOI d = %.2f is %.2f\n",
            d_min_h1, d_sesoi, power_at_plan))
cat(sprintf("    (the SESOI needs %d per level, so N = 600 is at or above 80%% power).\n",
            n_needed_h1))
cat(sprintf("    The messenger factor and the interaction are exploratory (an interaction\n    half the size of the main effect needs N of about %d).\n",
            n_interaction))
cat(sprintf("H2: donation - minimum detectable d = %.2f (check zero inflation; consider a hurdle model).\n",
            d_min_h1))
cat(sprintf("    petition - minimum detectable h = %.3f, i.e. an increase of %.1f to %.1f\n    percentage points for baselines from %.0f%% to %.0f%%.\n",
            h_min, increase_range[1], increase_range[2],
            100 * min(p0_grid), 100 * max(p0_grid)))
best <- grid[which.max(grid$power), ]
worst <- grid[which.min(grid$power), ]
cat(sprintf("H3: mediation power ranges from %.2f (a_d = %.2f, b = %.2f) to %.2f (a_d = %.2f, b = %.2f).\n",
            worst$power, worst$a_d, worst$b, best$power, best$a_d, best$b))
cat("Recruit 5-10% extra to cover pre-registered attention-check exclusions:\n")
cat(sprintf("    recruit %d to %d people to keep %d analysable.\n",
            ceiling(N_total / 0.95), ceiling(N_total / 0.90), N_total))
