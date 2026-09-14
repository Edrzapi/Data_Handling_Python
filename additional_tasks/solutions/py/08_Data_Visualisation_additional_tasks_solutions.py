# ======================================================================
# SOLUTIONS - ADDITIONAL TASKS - 08 Data Visualisation
#
# Data files are loaded from a 'data' folder next to this file: run with
# the working directory set to a folder containing that 'data' folder.
# Run top to bottom. Uses matplotlib.use('Agg') so it can run headless
# for verification; remove that line for interactive use.
# ======================================================================

import matplotlib
matplotlib.use('Agg')  # headless backend for automated verification runs

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------------
# Additional Task 8.1: Iris in one figure (Stretch)
# ----------------------------------------------------------------
iris = pd.read_csv('data/IRIS2.csv')
print("IRIS2 columns:", iris.columns.tolist())
print("IRIS2 shape:", iris.shape)
assert 'species' in iris.columns

pairplot_grid = sns.pairplot(iris, hue='species')
pairplot_grid.figure.savefig('_tmp_iris_pairplot.png')
plt.close(pairplot_grid.figure)

# Which measurement separates the species best? Compare each measurement's
# between-species variance to its within-species variance (a quick proxy
# for separability) rather than eyeballing the grid.
measurement_cols = [c for c in iris.columns if c != 'species']
species_means = iris.groupby('species')[measurement_cols].mean()
overall_std = iris[measurement_cols].std()
species_spread = species_means.max() - species_means.min()
separability = species_spread / overall_std
print("separability score per measurement (higher = better separator):\n", separability.sort_values(ascending=False))
best_separator = separability.idxmax()
print("best separator:", best_separator)
# petal_length or petal_width should come out on top - confirms the answer sketch
assert best_separator in ('petal_length', 'petal_width')

fig, ax = plt.subplots()
sns.violinplot(data=iris, x='species', y=best_separator, ax=ax)
fig.savefig('_tmp_iris_violin.png')
plt.close(fig)

# setosa should be clearly separated (its max on the best separator is
# below the other two species' minimums, or very close to it)
# Note: species values in this file are 'Iris-setosa', 'Iris-versicolor',
# 'Iris-virginica' (the 'Iris-' prefix is retained), not the bare names.
setosa_max = iris.loc[iris['species'] == 'Iris-setosa', best_separator].max()
others_min = iris.loc[iris['species'] != 'Iris-setosa', best_separator].min()
print(f"setosa max {best_separator}: {setosa_max}, other species min: {others_min}")
assert setosa_max <= others_min + 0.5  # setosa sits clearly apart, allowing a small margin

# Answer: petal length/width separates the three species best; versicolor
# and virginica are the pair that overlaps most (setosa stands alone).

# ----------------------------------------------------------------
# Additional Task 8.2: Two histograms, one axis (Stretch)
# ----------------------------------------------------------------
cdc = pd.read_csv('data/cdc.csv')
fig, ax = plt.subplots()
bins = range(60, 400, 10)
for g in ['m', 'f']:
    ax.hist(cdc.loc[cdc['gender'] == g, 'weight'], bins=bins, alpha=0.5, label=g)
ax.legend()
ax.set_xlabel('weight (lbs)')
ax.set_ylabel('count')
ax.set_title('Weight distribution by gender')
fig.savefig('_tmp_cdc_hist.png')
plt.close(fig)

male_mean = cdc.loc[cdc['gender'] == 'm', 'weight'].mean()
female_mean = cdc.loc[cdc['gender'] == 'f', 'weight'].mean()
print(f"mean weight m={male_mean:.1f} f={female_mean:.1f}")
assert male_mean > female_mean  # male distribution sits visibly to the right

# Shared bins matter because different bin edges make two histograms
# visually incomparable - a taller bar in one plot could just be a wider
# bin, not more respondents.

# ----------------------------------------------------------------
# Additional Task 8.3: The trend behind the noise (Challenge)
# ----------------------------------------------------------------
r = pd.read_csv('data/renfe_trains_cleaned.csv')
r['departure'] = pd.to_datetime(r['departure'])
daily = r.set_index('departure')['price'].resample('D').mean()
rolling = daily.rolling(7).mean()

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(daily, alpha=0.4, linewidth=1, label='daily mean')
ax.plot(rolling, linewidth=2, label='7-day rolling')
ax.set_title('Renfe mean ticket price')
ax.set_xlabel('date')
ax.set_ylabel('price')
ax.legend()
fig.savefig('_tmp_renfe_trend.png')
plt.close(fig)

assert len(daily) == 603
assert rolling.iloc[:6].isna().all()

# Answer: the rolling line reveals the underlying trend by smoothing out
# day-to-day noise; it lags the raw series at turning points because each
# rolling value is an average that includes days before the turn.

# Clean up the plot files written for this verification run.
import os
for f in ('_tmp_iris_pairplot.png', '_tmp_iris_violin.png', '_tmp_cdc_hist.png', '_tmp_renfe_trend.png'):
    if os.path.exists(f):
        os.remove(f)

print("All Module 8 additional task checks passed.")
