# Visualization Guide for Survey Research Data

Good visualizations communicate structure, not just summary statistics. This guide maps data types to recommended plots, common pitfalls to avoid, and working R and Python code using validated packages.

---

## Quick Reference Table

| Data type | Best plot | Avoid | R package + function | Python package |
|---|---|---|---|---|
| Likert distributions (single item) | Diverging stacked bar | Pie chart, simple bar of means | `likert::plot.likert()` | `plotnine`, custom `matplotlib` |
| Likert distributions (scale battery) | Grouped diverging stacked bar | — | `likert`, `ggplot2` | `plotnine` |
| Word-association frequencies | Word cloud + frequency bar | Word cloud alone (no frequency context) | `wordcloud2`, `ggplot2` | `wordcloud`, `plotnine` |
| Qualitative code co-occurrences / transitions | Sankey / Alluvial diagram | Table only | `ggalluvial`, `ggsankey` | `plotly`, `pySankey` |
| Group comparisons (continuous) | Boxplot + jitter + effect size annotation | Bar chart of means with SE bars | `ggplot2`, `ggdist`, `ggpubr` | `seaborn`, `plotnine` |
| Multivariate constructs / ordination | PCA/NMDS biplot | 3D scatter without clear axes | `vegan`, `ggplot2`, `ggvegan` | `sklearn`, `plotnine` |
| SEM path diagrams | Path diagram with standardized coefficients | Table of paths alone | `semPlot`, `lavaanPlot` | `semopy` (plot method) |
| Correlation matrix | Corrplot / heatmap | Raw table for many variables | `corrplot`, `ggcorrplot` | `seaborn.heatmap()` |
| Model predictions / marginal effects | Marginal effects plots | Coefficient tables alone | `marginaleffects`, `ggplot2` | `marginaleffects` (Python port), `statsmodels` |
| Time series / longitudinal | Line chart with confidence ribbon | — | `ggplot2` | `plotnine`, `matplotlib` |

---

## 1. Likert Distributions — Diverging Stacked Bar

**Why diverging?** Centering at the neutral midpoint makes it easy to compare relative weight of agreement vs. disagreement across items.

```r
library(likert)
library(dplyr)

# Prepare: convert Likert columns to ordered factors
likert_items <- df |>
  select(starts_with("Q")) |>
  mutate(across(everything(), ~ factor(.,
    levels = c("Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"),
    ordered = TRUE)))

result <- likert(as.data.frame(likert_items))
plot(result, type = "bar", centered = TRUE) +
  theme_minimal()
```

> ⚠️ **Never use pie charts for Likert data.** Pie charts distort proportional perception and make neutral vs. agreement comparisons nearly impossible (Mariano et al., 2018).

---

## 2. Word Clouds + Frequency Bar Charts

Word clouds are evocative but scientifically limited: frequency is mapped to font size, which is difficult to compare precisely. Always pair a word cloud with a frequency bar chart.

```r
library(wordcloud2)
library(ggplot2)
library(dplyr)

# Frequency table from coded word associations
word_freq <- df |>
  count(word, sort = TRUE) |>
  filter(n > 2)

# Word cloud
wordcloud2(word_freq, size = 1.2, color = "random-dark")

# Frequency bar (top 20)
word_freq |>
  slice_max(n, n = 20) |>
  ggplot(aes(x = reorder(word, n), y = n)) +
  geom_col(fill = "#2c7fb8") +
  coord_flip() +
  labs(x = NULL, y = "Frequency") +
  theme_minimal()
```

**Python:**
```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

word_freq = df["word"].value_counts().to_dict()

wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# Bar chart
pd.Series(word_freq).sort_values(ascending=False).head(20).plot(kind="barh", color="#2c7fb8")
plt.tight_layout()
```

---

## 3. Sankey / Alluvial Diagrams for Qualitative Transitions

Sankey diagrams are powerful for showing how respondents move between categories (e.g., from initial code → theme → valence), or how demographic groups distribute across response categories.

```r
library(ggalluvial)
library(ggplot2)

# Example: flow from sentiment to theme to conservation outcome
ggplot(df, aes(axis1 = sentiment, axis2 = theme, axis3 = outcome)) +
  geom_alluvium(aes(fill = sentiment), width = 1/12) +
  geom_stratum(width = 1/12, fill = "grey80", color = "grey40") +
  geom_label(stat = "stratum", aes(label = after_stat(stratum))) +
  scale_x_discrete(limits = c("Sentiment", "Theme", "Outcome")) +
  theme_minimal()
```

---

## 4. Group Comparisons — Boxplot with Jitter and Effect Size

Bar charts of means with standard error bars are discouraged because they hide distributional shape. Use boxplots with raw data jitter overlaid.

```r
library(ggplot2)
library(ggdist)
library(ggpubr)

ggplot(df, aes(x = group, y = score, fill = group)) +
  ggdist::stat_halfeye(adjust = 0.5, justification = -0.2, .width = 0, point_colour = NA) +
  geom_boxplot(width = 0.2, outlier.shape = NA, alpha = 0.5) +
  geom_jitter(width = 0.05, alpha = 0.3, size = 1) +
  stat_compare_means(comparisons = list(c("Group A", "Group B")), method = "wilcox.test") +
  theme_minimal()
```

---

## 5. Ordination Biplots for Multivariate Constructs

```r
library(vegan)
library(ggvegan)

# PCA on value orientation scale items
pca_result <- rda(scale(df[, scale_items]))
autoplot(pca_result, arrows = TRUE) +
  theme_minimal() +
  labs(title = "PCA Biplot of Value Orientation Items")
```

---

## 6. SEM Path Diagrams

```r
library(lavaan)
library(semPlot)

model <- "
  wildlife_tolerance ~ attitude + social_norms
  attitude ~ value_orientation
"
fit <- sem(model, data = df)
semPaths(fit, what = "std", layout = "tree", edge.label.cex = 0.8,
         residuals = FALSE, nCharNodes = 6)
```

---

## External Resources

- [R Graph Gallery](https://r-graph-gallery.com/) — Comprehensive gallery of ggplot2 examples with code.
- [Python Graph Gallery](https://python-graph-gallery.com/) — Python equivalents.
- [ggplot2 extensions gallery](https://exts.ggplot2.tidyverse.org/) — Full list of ggplot2 extension packages.
- [easystats/see](https://github.com/easystats/see) — Visualization tools specifically for statistical model outputs in R.
- [plotnine](https://plotnine.readthedocs.io/) — Grammar of graphics in Python (ggplot2 port).

---

## References
- Mariano, et al. (2018). (Reference on pie chart distortion for Likert data).
- Wickham, H. (2016). *ggplot2: Elegant Graphics for Data Analysis*. Springer. https://ggplot2-book.org/