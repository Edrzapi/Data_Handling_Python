# ======================================================================
# SOLUTIONS - 08 Data Visualisation
#
# Data files are loaded from a 'data' folder next to the tasks file: run
# with the working directory set to a folder containing that 'data' folder.
# The solutions build on each other in order; run the file top to bottom.
# ======================================================================

# ----------------------------------------------------------------
# 1. Load in the dataset `train_viz.csv` AND the following packages:
# ----------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/train_viz.csv')

# ----------------------------------------------------------------
# 2. Create a scatter plot of duration vs. price. Segment by destination.
# ----------------------------------------------------------------
# Create a scatter plot of duration vs. price. Segment by destination.

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='duration', y='price')
# In the interest of TIME: Dont need to include title etc
plt.title('Scatter plot of Duration vs Price')
plt.show()

# ----------------------------------------------------------------
# 3. Create a barplot of fare counts.
# ----------------------------------------------------------------
# Create a barplot of fare counts.
plt.bar(x=df['fare'].unique(), height=df['fare'].value_counts())
plt.title('Bar plot of Fare Counts')
plt.xticks(rotation=60)
plt.show()

# ----------------------------------------------------------------
# 3. Create a barplot of fare counts.
# ----------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='fare')
plt.title('Bar plot of Fare Counts')
plt.xticks(rotation=60)
plt.show()

# ----------------------------------------------------------------
# 4. Create a box & whisker plot of price with respect to destination.
# ----------------------------------------------------------------
# Create a box & whisker plot of price with respect to destination.
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='destination', y='price')
plt.title('Box & Whisker plot of Price by Destination')
plt.show()

# ----------------------------------------------------------------
# 5. Create a histogram of duration.
# ----------------------------------------------------------------
# Create a histogram of duration.
plt.hist(df['duration'])
plt.title('Histogram of Duration')
plt.show()

# ----------------------------------------------------------------
# 6. Compare this to a histogram of price.
# ----------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df['duration'], bins=20, kde=True)
plt.title('Histogram of Duration')
plt.show()

# ----------------------------------------------------------------
# 6. Compare this to a histogram of price.
# ----------------------------------------------------------------
# Compare this to a histogram of price.
plt.hist(df['price'])
plt.title('Histogram of Price')
plt.show()

# ----------------------------------------------------------------
# 7. Create a violin plot of price with respect to destination.
# ----------------------------------------------------------------
# Create a violin plot of price with respect to destination.
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='destination', y='price')
plt.title('Violin plot of Price by Destination')
plt.show()

# ----------------------------------------------------------------
# 8. Create a heatmap of the correlation between columns.
# ----------------------------------------------------------------
# Create a heatmap of the correlation between columns.
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Between Columns')
plt.show()

# ----------------------------------------------------------------
# 9. Create a proportional stacked bar plot of vehicle_class by destination.
# ----------------------------------------------------------------
# Create a proportional stacked bar plot of vehicle_class by destination.
plt.figure(figsize=(10, 6))
dest_vehicle_class = df.groupby(['destination', 'vehicle_class']).size().unstack()
dest_vehicle_class.div(dest_vehicle_class.sum(axis=1), axis=0).plot(kind='bar', stacked=True)
plt.title('Proportional Stacked Bar Plot of Vehicle Class by Destination')
plt.ylabel('Proportion')
plt.show()
