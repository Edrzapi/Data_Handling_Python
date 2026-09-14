# ======================================================================
# TASKS - 08 Data Visualisation
#
# Converted from the delegate notebook '08_Data_Visualisation.ipynb' for use in PyCharm.
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is alongside
# this script before running it.
# Solutions: solutions/08_Data_Visualisation_solutions.py
# ======================================================================

# ## 08 Data Visualisation
#
# - Use Pandas, Seaborn and Matplotlib at least once across these exercises. This will help yoiu understand the utility and differences of each.
#
# - Which package you use for the majority of the exercises is up to you

# ## Anscombe's Quartet: A Note on Statistics and the necessary Visualisation
#
# It's worth mentioning Anscombe's Quartet. This is a famous example of four datasets that have nearly identical simple descriptive statistics (mean, variance, correlation, etc.) but look very different when graphed.
#
# It's a powerful reminder of why visualising your data is just as important as calculating statistics. They complement the other and contribute to growing evidence

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Anscombe's quartet dataset
anscombe = sns.load_dataset("anscombe")

anscombe.head()

# Create a FacetGrid to plot each quartet
g = sns.FacetGrid(anscombe, col="dataset", col_wrap=2, height=4)

# Map a scatter plot and a regression line to each facet, without confidence intervals
g.map(sns.regplot, "x", "y", ci=None)

# Add titles and labels
g.set_titles("Dataset {col_name}")
g.set_axis_labels("x", "y")

plt.tight_layout()
plt.show()

# 1. Load in the dataset `train_viz.csv` AND the following packages:
# ```python
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# >>> Your code here

# 2. Create a scatter plot of duration vs. price. Segment by destination.

# >>> Your code here

# 3. Create a barplot of fare counts.

# >>> Your code here

# 4. Create a box & whisker plot of price with respect to destination.

# >>> Your code here

# 5. Create a histogram of duration.

# >>> Your code here

# 6. Compare this to a histogram of price.

# >>> Your code here

# 7. Create a violin plot of price with respect to destination.

# >>> Your code here

# 8. Create a heatmap of the correlation between columns.

# >>> Your code here

# 9. Create a proportional stacked bar plot of vehicle_class by destination.

# >>> Your code here
