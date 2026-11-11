# =============================================================================
# Power analysis example (e): SAMPLE SIZE CALCULATOR for a non-experimental
# (observational) study that predicts an outcome from several predictors
# -----------------------------------------------------------------------------
# A HYPOTHETICAL study, invented for teaching:
#
#   Outcome    : willingness to let a bird nest on your house
#                (e.g., the mean of a 3-item, 7-point scale)
#   Predictors : the bird's FUNCTIONAL TRAITS - plumage colour, plumage
#                pattern, diet, (and, e.g., body size, song)
#
#   There is no intervention. The question is: "Which traits predict
#   willingness, and how many respondents (and how many birds!) do I need to
#   detect the effect of ONE trait?"
#
# The most important point in this script (read section 2 before the numbers):
#   Traits belong to BIRDS, not to PEOPLE. Who or what you sample decides the
#   sample size:
#     Part A - one rating per person, predictors measured on each person
#              -> classic multiple-regression power (pwr.f2.test)
#     Part B - a FIXED SET OF REAL SPECIES (e.g., 20 photos of real birds)
#              -> trait effects are estimated from differences BETWEEN
#                 SPECIES, so the number of species limits your power
#     Part C - DESIGNED PROFILES (a conjoint / factorial-vignette design: the
#              same bird drawing shown in different colours, patterns, and
#              diets, combined at random)
#              -> traits are independent by design; the number of people and
#                 profiles per person set the power (simulation with lme4)
#
# How to run it:
#   1. Install R (https://cran.r-project.org) and, optionally, RStudio.
#   2. Open this file in RStudio and click "Source", or in a terminal run:
#        Rscript power_example_e_sample_size_calculator_traits.R
#   3. Change the numbers in the "YOUR ASSUMPTIONS" section and run it again.
#      Parts B and C run simulations and take a minute or two.
#
# R packages used:
#   pwr  - closed-form power for regression (f2) and correlations
#          (Champely, CRAN: https://cran.r-project.org/package=pwr)
#   lme4 - mixed-effects models, used in the Part C simulation
#          (Bates et al., CRAN: https://cran.r-project.org/package=lme4)
# =============================================================================


# ---- 0. Install and load packages --------------------------------------------
# install.packages() downloads a package from CRAN. You only need to do this
# once per computer, so we install each package only if it is missing.
for (pkg in c("pwr", "lme4")) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, repos = "https://cloud.r-project.org")
  }
}
library(pwr)   # library() loads an installed package for this session
library(lme4)

# Print versions so your output records exactly what you ran.
cat("R version:", R.version.string, "\n")
cat("pwr version:", as.character(packageVersion("pwr")),
    "| lme4 version:", as.character(packageVersion("lme4")), "\n\n")


# ---- 1. Choosing and justifying the effect size -------------------------------
# In a regression with several predictors, the effect size for ONE predictor is
# Cohen's f-squared for that predictor:
#
#     f2 = delta_R2 / (1 - R2_full)
#
#   R2_full  = the share of variance in willingness explained by ALL predictors
#   delta_R2 = how much R2 DROPS when you remove the one predictor you care
#              about (its "unique" contribution, over and above the others)
#
# Cohen's (1988) benchmarks: f2 = .02 small, .15 medium, .35 large. In survey
# research on attitudes, a single predictor's unique contribution is often
# small (delta_R2 of .01 to .03), because predictors overlap.
#
# Where should delta_R2 come from? In order of preference:
#   (1) Prior studies that regressed preferences for animals on their traits.
#       Examples to look for (read them and extract the statistics yourself;
#       the effects are not quoted here):
#         * Liskova & Frynta (2013). What determines bird beauty in human
#           eyes? Anthrozoos, 26, 27-41.
#           https://doi.org/10.2752/175303713X13534238631399
#         * Schuetz & Johnston (2019). Characterizing the cultural niches of
#           North American birds. PNAS, 116, 10868-10873.
#           https://doi.org/10.1073/pnas.1820670116
#       Convert what they report: a partial correlation pr -> f2 = pr^2/(1-pr^2);
#       a standardized beta with uncorrelated predictors -> delta_R2 ~ beta^2.
#   (2) Your SMALLEST EFFECT SIZE OF INTEREST: the smallest unique effect that
#       would change a recommendation (e.g., which species to feature in a
#       nest-box campaign). Then report a sensitivity analysis (Lakens, 2022,
#       Sample size justification, Collabra: Psychology, 8, 33267,
#       https://doi.org/10.1525/collabra.33267).
#   Do NOT use a pilot study's estimate: small pilots give very noisy effect
#   sizes (see example a, section 1).
#
# A caution for observational designs: a significant trait coefficient is an
# ASSOCIATION. If traits are correlated (e.g., colourful birds also tend to eat
# fruit), the regression cannot tell you which trait people respond to
# (Rohrer, 2018, https://doi.org/10.1177/2515245917745629). Part C's designed
# profiles solve this by making the traits independent.

f2_from_delta <- function(delta_R2, R2_full) delta_R2 / (1 - R2_full)
f2_from_partial_r <- function(pr) pr^2 / (1 - pr^2)


# ---- 2. YOUR ASSUMPTIONS (edit these) -----------------------------------------
alpha <- 0.05   # Type I error rate (see example a)
power <- 0.80   # chance of detecting the effect if it is real

# Part A: one rating per person
k_predictors <- 5      # all predictors in the model (traits + controls such as
                       # age, home ownership, prior nesting experience)
R2_full      <- 0.10   # variance explained by the full model (guess from
                       # prior studies; a lower R2_full is the cautious choice
                       # only for the overall test - see the table below)
delta_R2     <- 0.02   # unique variance of the ONE trait you care most about
nonresponse_rate <- 0.10  # EXAMPLE value: replace with your platform's rate

# Part B: a fixed set of real species
n_species    <- 20     # how many species (photos) you can show
r_species    <- 0.30   # correlation, ACROSS SPECIES, between the trait and the
                       # species' average willingness score
n_people_B   <- 300    # respondents
ratings_each <- 5      # species rated by each respondent

# Part C: designed profiles (conjoint)
profiles_each <- 8     # profiles rated by each respondent
beta_trait    <- 0.15  # effect of each binary trait (e.g., bright vs dull),
                       # in SD units of the rating: a SMALL effect
sd_person     <- 0.60  # how much people differ in their overall willingness
                       # (SD of person intercepts, relative to residual SD = 1)
n_people_grid <- c(40, 80, 120, 200)  # respondent numbers to try

n_sims <- 300          # simulations per setting. 300 gives about +/- 0.05
                       # precision; use 1000 for your final numbers.
set.seed(2026)         # makes the random numbers reproducible


# =============================================================================
# PART A - one rating per person: standard multiple regression
# =============================================================================
# Use this when each respondent gives ONE willingness score and the predictors
# are measured on that respondent (e.g., how colourful they PERCEIVE the bird
# in their garden to be, their age, their attitude towards birds).
#
# pwr.f2.test() uses:
#   u  = numerator df = number of predictors being TESTED (1 for one trait)
#   v  = denominator df = N - k_predictors - 1  -> so N = v + k + 1
#   f2 = effect size
cat("==================== PART A: multiple regression ====================\n")

f2_one <- f2_from_delta(delta_R2, R2_full)
resA <- pwr.f2.test(u = 1, f2 = f2_one, sig.level = alpha, power = power)
N_A  <- ceiling(resA$v) + k_predictors + 1
cat(sprintf("One trait adding delta_R2 = %.2f (f2 = %.3f), %d predictors in the model:\n",
            delta_R2, f2_one, k_predictors))
cat(sprintf("  analysable N = %d; recruit %d after %.0f%% non-response\n\n",
            N_A, ceiling(N_A / (1 - nonresponse_rate)), 100 * nonresponse_rate))

# Sensitivity: N for a range of unique effects.
grid <- data.frame(delta_R2 = c(0.01, 0.02, 0.03, 0.05))
grid$f2 <- round(f2_from_delta(grid$delta_R2, R2_full), 4)
grid$N  <- sapply(grid$f2, function(f2) {
  ceiling(pwr.f2.test(u = 1, f2 = f2, sig.level = alpha, power = power)$v) +
    k_predictors + 1
})
cat("Sensitivity (one predictor's unique contribution):\n")
print(grid, row.names = FALSE)

# The overall F test ("do the predictors explain anything at all?") needs far
# fewer people. Students often power only this test: that is NOT enough when
# your hypotheses are about individual traits.
f2_all <- R2_full / (1 - R2_full)
N_overall <- ceiling(pwr.f2.test(u = k_predictors, f2 = f2_all,
                                 sig.level = alpha, power = power)$v) +
  k_predictors + 1
cat(sprintf("\nFor comparison, the OVERALL test (R2 = %.2f) needs only N = %d.\n",
            R2_full, N_overall))
# A rough rule of thumb for individual predictors is N >= 104 + k
# (Green, 1991, https://doi.org/10.1207/s15327906mbr2603_7); it assumes a
# medium effect, so it is too small for the small effects typical here.
cat(sprintf("Green's (1991) rule of thumb N >= 104 + k gives %d (medium effects only).\n\n",
            104 + k_predictors))


# =============================================================================
# PART B - a fixed set of real species
# =============================================================================
# Suppose you show photos of 20 real species and ask about each. The trait
# (say, bright plumage) is a property of the SPECIES. Every respondent who
# rates a robin sees the same robin, so the information about "does
# brightness matter?" comes from comparing 20 species. Adding people makes each
# species' average more precise, but it cannot add species.
#
# Treating every rating as an independent observation (a plain regression on
# thousands of rows) is pseudoreplication and gives false positives
# (Judd, Westfall & Kenny, 2012, https://doi.org/10.1037/a0028347).
# The correct analysis treats species as a random factor; with one rating
# per person-species pair it is close to regressing the SPECIES MEANS on the
# trait, which is what we do below.
cat("==================== PART B: fixed set of real species ====================\n")

# Closed form: how many SPECIES to detect a between-species correlation?
for (r in c(0.30, 0.50)) {
  cat(sprintf("Between-species correlation r = %.2f needs %d species (80%% power)\n",
              r, ceiling(pwr.r.test(r = r, sig.level = alpha, power = power)$n)))
}

# Simulation: does adding respondents help when the species are fixed?
sim_species <- function(n_species, r_species, n_people, ratings_each,
                        sd_species = 0.5, sd_person = 0.6) {
  trait <- rnorm(n_species)                       # the trait, one value per species
  # each species' true mean willingness: partly the trait, partly everything
  # else about that species (sd_species sets how much species differ)
  sp_mean <- sd_species * (r_species * trait +
                           sqrt(1 - r_species^2) * rnorm(n_species))
  # each person rates a random subset of species
  person  <- rep(seq_len(n_people), each = ratings_each)
  species <- as.vector(replicate(n_people, sample(n_species, ratings_each)))
  rating  <- sp_mean[species] + rnorm(n_people, 0, sd_person)[person] +
             rnorm(length(person))
  # analyse species means (n = n_species), the honest unit of analysis
  means <- tapply(rating, species, mean)
  p <- summary(lm(means ~ trait[as.integer(names(means))]))$coefficients[2, 4]
  p < alpha
}

cat(sprintf("\nSimulated power, r = %.2f between species (%d simulations each):\n",
            r_species, n_sims))
tabB <- expand.grid(n_species = c(n_species, 40, 80),
                    n_people = c(n_people_B, 3 * n_people_B))
tabB$power <- mapply(function(s, p) {
  mean(replicate(n_sims, sim_species(s, r_species, p, min(ratings_each, s))))
}, tabB$n_species, tabB$n_people)
tabB$power <- round(tabB$power, 2)
print(tabB, row.names = FALSE)
cat("-> Tripling the number of PEOPLE barely changes power; adding SPECIES does.\n\n")


# =============================================================================
# PART C - designed profiles (conjoint / factorial vignettes)
# =============================================================================
# Instead of real species, show a drawing of a bird whose traits are varied
# independently: colour (dull/bright) x pattern (plain/patterned) x diet
# (insects/seeds), combined at random. Each person rates several profiles.
# Because the traits are randomised, they are uncorrelated, and you can tell
# which trait people respond to. People now differ in their overall
# willingness, so we fit a mixed model with a random intercept per person.
#
# If your profiles are PHOTOS with other idiosyncrasies, add a random effect
# for the image as well; Westfall, Kenny & Judd (2014,
# https://doi.org/10.1037/xge0000014) show how the number of stimuli then
# limits power, as in Part B. The simr package (Green & MacLeod, 2016,
# https://doi.org/10.1111/2041-210X.12504) automates simulations like this one.
cat("==================== PART C: designed profiles (conjoint) ====================\n")

sim_conjoint <- function(n_people, profiles_each, beta, sd_person) {
  n <- n_people * profiles_each
  d <- data.frame(
    person  = factor(rep(seq_len(n_people), each = profiles_each)),
    bright  = rbinom(n, 1, 0.5),   # each trait drawn at random for each profile
    pattern = rbinom(n, 1, 0.5),
    seeds   = rbinom(n, 1, 0.5)
  )
  d$rating <- beta * d$bright + beta * d$pattern + beta * d$seeds +
              rnorm(n_people, 0, sd_person)[d$person] + rnorm(n)
  fit <- lmer(rating ~ bright + pattern + seeds + (1 | person), data = d)
  # with hundreds of ratings, |t| > 1.96 is a good approximation to p < .05
  abs(coef(summary(fit))["bright", "t value"]) > qnorm(1 - alpha / 2)
}

tabC <- data.frame(n_people = n_people_grid)
tabC$ratings <- tabC$n_people * profiles_each
tabC$power_bright <- sapply(tabC$n_people, function(n) {
  mean(replicate(n_sims, sim_conjoint(n, profiles_each, beta_trait, sd_person)))
})
cat(sprintf("Effect of one trait = %.2f SD, %d profiles per person (%d simulations each):\n",
            beta_trait, profiles_each, n_sims))
tabC$power_bright <- round(tabC$power_bright, 2)
print(tabC, row.names = FALSE)


# ---- 3. Summary and a sentence for your proposal -----------------------------
cat("\n==================== SUMMARY ====================\n")
cat(sprintf("* Part A (one rating per person): N = %d analysable (%d to recruit) for one\n",
            N_A, ceiling(N_A / (1 - nonresponse_rate))))
cat(sprintf("  trait adding delta_R2 = %.2f with %d predictors.\n", delta_R2, k_predictors))
cat("* Part B (fixed real species): power depends on the NUMBER OF SPECIES; see the\n")
cat("  table. Report species as your unit of analysis for trait effects.\n")
first_ok <- tabC$n_people[tabC$power_bright >= power][1]
if (is.na(first_ok)) {
  cat("* Part C (designed profiles): none of the respondent numbers reached the target\n  power; extend n_people_grid.\n")
} else {
  cat(sprintf("* Part C (designed profiles): about %d respondents x %d profiles reach %.0f%%\n",
              first_ok, profiles_each, 100 * power))
  cat(sprintf("  power for a %.2f SD trait effect (check with n_sims = 1000).\n", beta_trait))
}
cat(sprintf(paste0(
  "\nExample sentence (Part A): \"We will recruit %d participants to obtain %d\n",
  "complete responses, which gives %.0f%% power at alpha = %.2f to detect a unique\n",
  "contribution of delta_R2 = %.2f (f2 = %.3f) for each trait in a %d-predictor\n",
  "regression [cite the source of your effect size].\"\n"),
  ceiling(N_A / (1 - nonresponse_rate)), N_A, 100 * power, alpha,
  delta_R2, f2_one, k_predictors))
cat("\nIf willingness is a single Likert item rather than a multi-item scale, use an\n",
    "ordinal model (e.g., ordinal::clmm) in your analysis and simulate with it.\n")

# References
# Cohen J (1988) Statistical Power Analysis for the Behavioral Sciences, 2nd ed.
# Green P, MacLeod CJ (2016) Methods Ecol Evol 7:493-498. doi:10.1111/2041-210X.12504
# Green SB (1991) Multivariate Behav Res 26:499-510. doi:10.1207/s15327906mbr2603_7
# Judd CM, Westfall J, Kenny DA (2012) J Pers Soc Psychol 103:54-69. doi:10.1037/a0028347
# Lakens D (2022) Collabra: Psychology 8:33267. doi:10.1525/collabra.33267
# Liskova S, Frynta D (2013) Anthrozoos 26:27-41. doi:10.2752/175303713X13534238631399
# Rohrer JM (2018) Adv Methods Pract Psychol Sci 1:27-42. doi:10.1177/2515245917745629
# Schuetz JG, Johnston A (2019) PNAS 116:10868-10873. doi:10.1073/pnas.1820670116
# Westfall J, Kenny DA, Judd CM (2014) J Exp Psychol Gen 143:2020-2045. doi:10.1037/xge0000014
