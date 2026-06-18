# analyze_behavior_data.R
# Example script for analyzing behavioral data (donations / petitions)

library(dplyr)
library(ggplot2)

# Simulate some behavioral data collected after a survey
# e.g., Participants were asked if they want to donate their compensation
# or sign a petition related to the survey topic.
set.seed(42)
n_participants <- 200

# Simulated dataset
behavior_data <- data.frame(
  participant_id = 1:n_participants,
  treatment_group = sample(c("Control", "Intervention"), n_participants, replace = TRUE),
  donated_amount = runif(n_participants, 0, 10) * rbinom(n_participants, 1, 0.4), # Some don't donate
  signed_petition = sample(c(0, 1), n_participants, replace = TRUE, prob = c(0.6, 0.4))
)

# 1. Analyze Petition Signing (Binary outcome)
# Logistic regression to see if treatment influenced petition signing
model_petition <- glm(signed_petition ~ treatment_group, data = behavior_data, family = "binomial")
summary(model_petition)

# 2. Analyze Donation Amounts (Continuous outcome with zeros - e.g., Tobit or simple t-test/Wilcoxon)
# For simplicity, comparing mean donations between groups using a Wilcoxon rank sum test
wilcox_test_donations <- wilcox.test(donated_amount ~ treatment_group, data = behavior_data)
print(wilcox_test_donations)

# Plotting the results
# Petition signing proportion by group
plot_petition <- ggplot(behavior_data, aes(x = treatment_group, fill = as.factor(signed_petition))) +
  geom_bar(position = "fill") +
  labs(title = "Proportion of Participants Signing Petition by Group",
       y = "Proportion",
       x = "Group",
       fill = "Signed Petition") +
  theme_minimal()

# Donation amounts by group
plot_donation <- ggplot(behavior_data, aes(x = treatment_group, y = donated_amount)) +
  geom_boxplot(aes(fill = treatment_group), alpha = 0.6) +
  geom_jitter(width = 0.2, alpha = 0.5) +
  labs(title = "Donation Amounts by Group",
       y = "Donation Amount ($)",
       x = "Group") +
  theme_minimal()

print(plot_petition)
print(plot_donation)
