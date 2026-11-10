# =============================================================================
# Power analysis example (c): ACI (After-only, Control-Impact)
# -----------------------------------------------------------------------------
# Design: the outcome is measured only AFTER the intervention, in an IMPACT
#         group and one or more CONTROL groups. There is no baseline survey,
#         either because a baseline was impossible (the intervention already
#         happened) or because a pre-test would tip participants off.
#
# Two features make ACI power analysis different from example (a):
#
#   1. No baseline, so no within-person gain in precision. Group differences
#      at baseline cannot be removed by design; you rely on random assignment
#      or on matching and covariates (see Step 04).
#
#   2. ACI studies in the field usually compare PLACES (villages, parks,
#      schools): people are sampled within sites, and the intervention happens
#      at the site level. People in the same site resemble each other, so 20
#      people from one village carry less information than 20 people from 20
#      villages. We correct for this with the DESIGN EFFECT.
#
# The script covers:
#   Part A - one impact vs. one control group (t-test, Cohen's d)
#   Part B - one impact vs. two control groups (one-way ANOVA, Cohen's f),
#            including how to convert d to f
#   Part C - inflating N for clustering (design effect) and for losses
#
# How to run: open in RStudio and click "Source", or run
#   Rscript power_example_c_aci.R
#
# R packages used:
#   pwr - closed-form power for t-tests and one-way ANOVA
# =============================================================================


# ---- 0. Install and load packages --------------------------------------------
if (!requireNamespace("pwr", quietly = TRUE)) {
  install.packages("pwr", repos = "https://cloud.r-project.org")
}
library(pwr)
cat("R version:", R.version.string, "\n")
cat("pwr version:", as.character(packageVersion("pwr")), "\n\n")


# ---- 1. Choosing the effect size ------------------------------------------------
# Use the same evidence hierarchy as in example (a): a meta-analysis
# (preferably adjusted for publication bias), then comparable prior studies
# converted to d, or your smallest effect size of interest (SESOI). Do not
# rely on a pilot-study estimate: small pilots give noisy, usually inflated
# effect sizes (Kraemer et al., 2006, https://doi.org/10.1001/archpsyc.63.5.484;
# Albers & Lakens, 2018, https://doi.org/10.1016/j.jesp.2017.09.004).
#
# Example source (DOI checked with Crossref):
#   Osbaldiston & Schott (2012). Environmental sustainability and behavioral
#   science: Meta-analysis of proenvironmental behavior experiments.
#   Environment and Behavior, 44, 257-299.
#   https://doi.org/10.1177/0013916511402673
#   -> the most effective treatment types (cognitive dissonance, goal setting,
#      social modeling, prompts) had Hedges' g > 0.60 on observed behaviour;
#      the authors note these averages rest on small numbers of studies.
#   Bergquist et al. (2023), https://doi.org/10.1073/pnas.2214851120
#   -> across field interventions, d = 0.18 after adjusting for publication
#      bias.
# The gap between these two numbers is the point: an optimistic estimate
# (0.60) and a conservative one (0.18) imply very different sample sizes, so
# justify your choice and show both in a sensitivity analysis.


# ---- 2. YOUR ASSUMPTIONS (edit these) -------------------------------------------
d_assumed <- 0.18   # impact vs. control, in SD units
alpha     <- 0.05
power     <- 0.80

# Clustering. EXAMPLE values: replace with your own plan and a cited ICC.
people_per_site <- 20     # respondents surveyed in each site (m)
icc             <- 0.05   # intraclass correlation: the share of outcome
                          # variance that lies BETWEEN sites. Look for ICCs
                          # reported for your outcome in multi-site surveys;
                          # if none exist, show a sensitivity range.

# Losses. EXAMPLE value: replace with your platform's or partner's figures.
nonresponse_rate <- 0.15  # people approached who do not complete the survey
                          # or fail pre-registered quality checks


# ---- Part A: one impact vs. one control group -------------------------------------
resA <- pwr.t.test(d = d_assumed, sig.level = alpha, power = power,
                   type = "two.sample", alternative = "two.sided")
print(resA)
n_A <- ceiling(resA$n)
cat(sprintf("Part A: %d per group if every respondent were independent.\n\n", n_A))


# ---- Part B: one impact vs. two control groups (Cohen's f) ------------------------
# With three or more groups the omnibus test is a one-way ANOVA and the effect
# size is Cohen's f = SD of the group means / within-group SD.
#
# Converting d to f:
#   * for TWO groups, f = d / 2.
#   * for k groups, write down the group means you expect (in SD units) and
#     compute f directly, as below. Here: both control sites at 0, the impact
#     site d_assumed higher.
#   * from a reported ANOVA: eta^2 = SS_effect / SS_total, then
#     f = sqrt(eta^2 / (1 - eta^2)).
expected_means <- c(control_1 = 0, control_2 = 0, impact = d_assumed)
f_from_means <- function(means) {
  sqrt(mean((means - mean(means))^2))  # population SD of the means, within SD = 1
}
f_from_eta2 <- function(eta2) sqrt(eta2 / (1 - eta2))
f_assumed <- f_from_means(expected_means)
cat(sprintf("Two groups: f = d / 2 = %.3f.  Three groups (0, 0, %.2f): f = %.3f\n",
            d_assumed / 2, d_assumed, f_assumed))
cat(sprintf("Example: a reported eta^2 = .01 corresponds to f = %.3f\n\n",
            f_from_eta2(0.01)))

resB <- pwr.anova.test(k = 3, f = f_assumed, sig.level = alpha, power = power)
print(resB)
n_B <- ceiling(resB$n)
cat(sprintf("Part B: %d per group (3 groups, %d total) for the omnibus F-test.\n",
            n_B, 3 * n_B))
cat("Note: the omnibus F-test only says the groups differ somewhere. If your\n",
    "hypothesis is 'impact differs from the controls', pre-register that\n",
    "contrast and power it with a t-test (Part A logic).\n\n", sep = "")


# ---- Part C: design effect for clustering, then losses -----------------------------
# Design effect (Kish): DEFF = 1 + (m - 1) * ICC, with m people per site.
# Multiply the independent-sample N by DEFF to get the N you need when people
# are clustered in sites. Then divide by (1 - non-response).
deff <- 1 + (people_per_site - 1) * icc
n_clustered <- ceiling(n_A * deff)
n_recruit   <- ceiling(n_clustered / (1 - nonresponse_rate))
sites_needed <- ceiling(n_recruit / people_per_site)
cat(sprintf("Design effect with m = %d and ICC = %.2f: DEFF = %.2f\n",
            people_per_site, icc, deff))
cat(sprintf("Completed surveys needed per group : %d\n", n_clustered))
cat(sprintf("People to approach per group       : %d (%.0f%% non-response)\n",
            n_recruit, 100 * nonresponse_rate))
cat(sprintf("Sites per group at %d people each   : %d\n\n",
            people_per_site, sites_needed))
# The t-test with a design-effect correction is an approximation. With few
# sites per group (fewer than about 15-20), analyse with a mixed model or
# site-level means and check power by simulation (see the BACI example).


# ---- Sensitivity analysis --------------------------------------------------------------
grid <- expand.grid(d = c(0.18, 0.31, 0.60), icc = c(0.01, 0.05, 0.10))
grid$n_independent <- sapply(grid$d, function(d)
  ceiling(pwr.t.test(d = d, sig.level = alpha, power = power,
                     type = "two.sample")$n))
grid$deff <- 1 + (people_per_site - 1) * grid$icc
grid$n_per_group <- ceiling(grid$n_independent * grid$deff)
grid$recruit_per_group <- ceiling(grid$n_per_group / (1 - nonresponse_rate))
grid$sites_per_group <- ceiling(grid$recruit_per_group / people_per_site)
cat("Sensitivity analysis (", people_per_site, " people per site):\n", sep = "")
print(grid, row.names = FALSE)

# ---- What to report ---------------------------------------------------------------------
# "Because no baseline could be collected, we use an after-only control-impact
#  design. We assumed d = [value] ([source]). With alpha = .05 and 80% power,
#  a two-sample t-test needs N per group (pwr). Respondents are clustered in
#  sites (m = [value], ICC = [value], source), giving a design effect of
#  [value]; allowing for [x]% non-response we will approach M people in
#  S sites per group."
