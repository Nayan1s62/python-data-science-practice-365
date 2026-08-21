# Seaborn Practice — 10 Questions
# Name: ______________________
# Date: ______________________
#
# Instructions:
# 1. Solve each question using Seaborn and Matplotlib.
# 2. Try to write the code yourself before checking any solution.
# 3. Add suitable titles and axis labels where requested.

import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets when required:
# tips = sns.load_dataset("tips")
# titanic = sns.load_dataset("titanic")
# iris = sns.load_dataset("iris")
# fmri = sns.load_dataset("fmri")
# flights = sns.load_dataset("flights")


# ============================================================
# Question 1 — Scatter Plot
# ============================================================
# Using the "tips" dataset:
# Create a scatter plot with:
# X-axis: total_bill
# Y-axis: tip
# Use different colors for each day.
# Add a suitable title.
#
# Your code:
#


# ============================================================
# Question 2 — Line Plot
# ============================================================
# Using the "fmri" dataset:
# Create a line plot with:
# X-axis: timepoint
# Y-axis: signal
# Create separate lines for each event.
# Add a suitable title.
#
# Your code:
#


# ============================================================
# Question 3 — Bar Plot
# ============================================================
# Using the "titanic" dataset:
# Create a bar plot showing the average fare for each
# passenger class.
#
# X-axis: class
# Y-axis: average fare
# Add a suitable title and axis labels.
#
# Your code:
#


# ============================================================
# Question 4 — Count Plot
# ============================================================
# Using the "titanic" dataset:
# Create a count plot showing the number of passengers
# in each passenger class.
# Use hue="sex" to compare males and females.
#
# Add a suitable title.
#
# Your code:
#


# ============================================================
# Question 5 — Box Plot
# ============================================================
# Using the "tips" dataset:
# Create a box plot showing total_bill for each day.
#
# After creating the plot, identify:
# 1. Which day has the highest median bill?
# 2. Which day has the largest spread?
#
# Your code:
#


# ============================================================
# Question 6 — Violin Plot
# ============================================================
# Using the "tips" dataset:
# Create a violin plot showing the distribution of total_bill
# for each day.
# Separate the distributions by sex using hue="sex".
#
# Add a suitable title.
#
# Your code:
#


# ============================================================
# Question 7 — Histogram
# ============================================================
# Using the "tips" dataset:
# Create a histogram of total_bill.
#
# Requirements:
# - Use 20 bins.
# - Display KDE.
# - Add a suitable title.
# - Add X-axis and Y-axis labels.
#
# Your code:
#


# ============================================================
# Question 8 — Heatmap
# ============================================================
# Using the "flights" dataset:
# 1. Create a pivot table.
# 2. Use month as rows.
# 3. Use year as columns.
# 4. Use passengers as values.
# 5. Create a heatmap from the pivot table.
# 6. Display the values inside each cell.
#
# Your code:
#


# ============================================================
# Question 9 — Pair Plot
# ============================================================
# Using the "iris" dataset:
# Create a pair plot using the numerical features.
#
# Requirements:
# - Use species to differentiate the points by color.
# - Add a suitable hue.
#
# After creating the plot, identify which two features
# appear to have the strongest relationship.
#
# Your code:
#


# ============================================================
# Question 10 — Challenge
# ============================================================
# Using the "titanic" dataset:
# Create a visualization comparing survival rate by
# passenger class and gender.
#
# Requirements:
# - X-axis: class
# - Y-axis: survival rate
# - Use hue="sex"
# - Add a suitable title.
# - Add axis labels.
# - Add a legend.
#
# Bonus:
# Add annotations showing the survival percentage
# on each bar.
#
# Your code:
#


# ============================================================
# END OF PRACTICE
# ============================================================
# Tip:
# Run each question separately and understand what every
# parameter in the Seaborn function does.
