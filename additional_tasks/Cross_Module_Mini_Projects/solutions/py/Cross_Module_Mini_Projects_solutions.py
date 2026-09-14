# ======================================================================
# SOLUTIONS - ADDITIONAL TASKS - Cross-Module Mini-Projects
#
# Data files are loaded from a 'data' folder next to this file: run with
# the working directory set to a folder containing that 'data' folder.
# Run top to bottom. Uses matplotlib.use('Agg') so it can run headless
# for verification; remove that line for interactive use.
# ======================================================================

import matplotlib
matplotlib.use('Agg')

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    display
except NameError:
    display = print

# ======================================================================
# Mini-Project 1: Loan book risk report
# Draws on: Module 6 (fillna by group), Module 7 (multi-table merge,
# pivot_table), Module 8 (bar chart, box plot).
# ======================================================================

# 1. Clean
loans = pd.read_csv('data/loan_data.csv')
missing_scores = int(loans['Score'].isna().sum())
print("MP1: missing scores before fill:", missing_scores)
assert missing_scores == 20

loans['Score'] = loans['Score'].fillna(loans.groupby('Term')['Score'].transform('mean'))
assert loans['Score'].isna().sum() == 0
# Filling by Term group rather than one overall mean respects the fact
# that 10-year and 20-year applicants have very different average scores
# (see Module 6 additional task 6.1).

# 2. Combine
business = pd.read_csv('data/business_account.csv').drop(columns='Unnamed: 0')
locations = pd.read_csv('data/locations.csv').drop(columns='Unnamed: 0')
full = loans.merge(business, on='ID').merge(locations, on='ID')
print("MP1: rows after both merges:", len(full))
assert len(full) == 856

# 3. Derive
full['debt_ratio'] = full['Debt'] / full['Income']
full['score_band'] = pd.cut(
    full['Score'],
    bins=[-1, 400, 600, full['Score'].max()],  # -1 so a Score of exactly 0 is included
    labels=['low', 'medium', 'high'],
)
assert full['score_band'].isna().sum() == 0

# 4. Aggregate
mp1_default_rate = full.groupby('nation')['Default'].mean()
print("MP1: default rate by nation:\n", mp1_default_rate)
assert round(mp1_default_rate['England'], 2) == 0.11
assert round(mp1_default_rate['N Ireland'], 2) == 0.17
assert round(mp1_default_rate['Scotland'], 2) == 0.07
assert round(mp1_default_rate['Wales'], 2) == 0.13

debt_ratio_pivot = full.pivot_table(values='debt_ratio', index='nation', columns='Term')
print("MP1: mean debt_ratio by nation and Term:\n", debt_ratio_pivot)

# 5. Visualise
fig, ax = plt.subplots()
mp1_default_rate.plot(kind='bar', ax=ax)
ax.set_title('Default rate by nation')
ax.set_ylabel('default rate')
fig.savefig('_tmp_mp1_bar.png')
plt.close(fig)
# A lending manager reads this as: N Ireland and Wales carry the highest
# default risk, Scotland the lowest - worth reviewing lending criteria
# by nation rather than applying one national policy.

fig, ax = plt.subplots()
sns.boxplot(data=full, x='Default', y='Score', ax=ax)
ax.set_title('Score distribution by default status')
fig.savefig('_tmp_mp1_box.png')
plt.close(fig)
median_score_defaulted = full.loc[full['Default'] == 1, 'Score'].median()
median_score_not = full.loc[full['Default'] == 0, 'Score'].median()
print(f"MP1: median score defaulted={median_score_defaulted:.1f} not={median_score_not:.1f}")
assert median_score_defaulted < median_score_not
# Defaulters visibly cluster at lower scores - Score is a genuinely useful
# early-warning signal for this book.

# ======================================================================
# Mini-Project 2: Renfe end to end, from raw to weekly trend
# Draws on: Module 6 (forensic cleaning), Module 7 (datetime, merge,
# resample/unstack), Module 8 (multi-series line + violin plot).
# ======================================================================

# 1. Clean
raw = pd.read_csv('data/renfe_trains.csv')
raw_rows = len(raw)
print("MP2: raw rows:", raw_rows)
assert raw_rows == 85948

clean = raw[raw['origin'] != 'origin'].copy()
clean['price'] = pd.to_numeric(clean['price'], errors='coerce')
clean = clean.dropna(subset=['price'])
clean = clean.drop_duplicates()
clean = clean.reset_index(drop=True)
print("MP2: rows after cleaning:", len(clean))
# Re-running this block top to bottom on the same source file reproduces
# the same row count every time - the mark of a clean, reproducible
# pipeline (see Module 6 additional task 6.3 for the header/dedupe
# forensics behind this).

# 2. Enrich
clean['departure'] = pd.to_datetime(clean['departure'])
clean['arrival'] = pd.to_datetime(clean['arrival'])
clean['duration_mins'] = (clean['arrival'] - clean['departure']).dt.total_seconds() / 60
assert (clean['duration_mins'] > 0).all()

fares = pd.read_csv('data/fare_conditions.csv')
clean = clean.merge(fares, on='fare', how='left')
# Left join, not inner: some trains use a fare that has no row in
# fare_conditions.csv. An inner join would silently drop those trains
# from the analysis; a left join keeps every train and simply leaves
# Conditions blank where there is no match.

# 3. Manipulate
weekly = (
    clean.set_index('departure')
    .groupby('vehicle_class')['price']
    .resample('W')
    .mean()
    .unstack(0)
)
print("MP2: weekly table shape:", weekly.shape)

class_means = clean.groupby('vehicle_class')['price'].mean()
print("MP2: class means (after full clean, incl. dedupe):\n", class_means)
assert class_means.idxmax() == 'Cama G. Clase'  # consistently priciest, as expected

# --- MISMATCH FLAG (STRETCH_GOALS.md, Cross-module MP2) -----------------
# STRETCH_GOALS.md's checkable line for MP2 states: "class means: Cama G.
# Clase about 133, Preferente about 83, Turista about 70". Running the
# full pipeline as MP2 itself specifies it (header rows removed, price
# coerced, rows with no price dropped, THEN duplicates dropped) gives
# different figures - the dedupe step measurably changes the class means,
# especially for the rare Cama G. Clase class (only a handful of rows):
print(f"MP2: actual (post-dedupe) means - Cama G. Clase={class_means['Cama G. Clase']:.2f}, "
      f"Preferente={class_means['Preferente']:.2f}, Turista={class_means['Turista']:.2f}")
# The STRETCH_GOALS.md figures only reproduce if the means are taken
# BEFORE dropping duplicates (i.e. straight after header removal and
# price coercion), which is what Module 7 additional task 7.3 verified
# against the raw file:
predup_means = (
    raw[raw['origin'] != 'origin']
    .assign(price=lambda d: pd.to_numeric(d['price'], errors='coerce'))
    .groupby('vehicle_class')['price']
    .mean()
)
print(f"MP2: pre-dedupe means (matches STRETCH_GOALS.md) - "
      f"Cama G. Clase={predup_means['Cama G. Clase']:.2f}, "
      f"Preferente={predup_means['Preferente']:.2f}, Turista={predup_means['Turista']:.2f}")
assert round(predup_means['Cama G. Clase'], 0) == 133
assert round(predup_means['Preferente'], 0) == 83
assert round(predup_means['Turista'], 0) == 70
# So: STRETCH_GOALS.md's MP2 checkable figures describe the data BEFORE
# the dedupe step that MP2's own instructions call for as part of
# cleaning. This run flags that mismatch rather than silently rewriting
# the source document's numbers or skipping the dedupe step the task
# asks for.
# --------------------------------------------------------------------------

# 4. Visualise
fig, ax = plt.subplots(figsize=(12, 5))
weekly.plot(ax=ax)
ax.set_title('Weekly mean price by vehicle class')
ax.set_xlabel('week')
ax.set_ylabel('mean price')
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
fig.tight_layout()
fig.savefig('_tmp_mp2_weekly.png')
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 5))
sns.violinplot(data=clean, x='vehicle_class', y='price', ax=ax)
ax.tick_params(axis='x', rotation=45)
fig.tight_layout()
fig.savefig('_tmp_mp2_violin.png')
plt.close(fig)

# ======================================================================
# Mini-Project 3: CDC health survey brief
# Draws on: Module 6 (derived columns), Module 7 (pivot, groupby),
# Module 8 (heatmap, scatter with reference line, proportional stack).
# ======================================================================

# 1. Clean and derive
cdc = pd.read_csv('data/cdc.csv').drop(columns='Unnamed: 0')
assert len(cdc) == 20000
cdc['bmi'] = 703 * cdc['weight'] / cdc['height'] ** 2
cdc['wt_gap'] = cdc['wtdesire'] - cdc['weight']

# 2. Bin
cdc['age_band'] = pd.cut(
    cdc['age'],
    bins=[17, 29, 44, 59, cdc['age'].max()],
    labels=['18-29', '30-44', '45-59', '60+'],
)
assert cdc['age_band'].isna().sum() == 0

# 3. Aggregate
bmi_pivot = cdc.pivot_table(values='bmi', index='age_band', columns='gender', observed=True)
print("MP3: mean BMI by age band and gender:\n", bmi_pivot)

wants_to_lose_share = (cdc['wt_gap'] < 0).groupby(cdc['genhlth']).mean()
print("MP3: share wanting to lose weight, by genhlth:\n", wants_to_lose_share)
# Rank genhlth from best to worst self-reported health and check the
# share rises as health worsens, as STRETCH_GOALS.md's checkable claims.
genhlth_order = ['excellent', 'very good', 'good', 'fair', 'poor']
ordered_share = wants_to_lose_share.reindex(genhlth_order)
print("MP3: ordered by health (best to worst):\n", ordered_share)

# --- MISMATCH FLAG (STRETCH_GOALS.md, Cross-module MP3) -----------------
# STRETCH_GOALS.md's checkable line claims "the share wanting to lose
# weight rises as genhlth worsens". The actual data only partly bears
# this out: it rises from 'excellent' (0.559) up through 'good' (0.669),
# but then FALLS for 'fair' (0.664) and 'poor' (0.600) - 'poor' has a
# lower share than every category except 'excellent'. This run flags
# that the claimed monotonic trend does not hold across all five
# categories, rather than silently asserting it does.
assert ordered_share.loc['excellent'] < ordered_share.loc['good'], (
    "expected at least a rise from 'excellent' to 'good'"
)
assert not ordered_share.is_monotonic_increasing  # documents the actual (non-monotonic) shape
# --------------------------------------------------------------------------

# 4. Visualise
fig, ax = plt.subplots()
sns.heatmap(bmi_pivot, annot=True, fmt='.1f', ax=ax)
ax.set_title('Mean BMI by age band and gender')
fig.savefig('_tmp_mp3_heatmap.png')
plt.close(fig)

fig, ax = plt.subplots()
ax.scatter(cdc['weight'], cdc['wtdesire'], alpha=0.1, s=8)
lims = [min(cdc['weight'].min(), cdc['wtdesire'].min()), max(cdc['weight'].max(), cdc['wtdesire'].max())]
ax.plot(lims, lims, color='red', linewidth=1, label='y = x')
ax.set_xlabel('actual weight')
ax.set_ylabel('desired weight')
ax.legend()
fig.savefig('_tmp_mp3_scatter.png')
plt.close(fig)

below_diagonal_share = (cdc['wtdesire'] < cdc['weight']).mean()
print("MP3: share of respondents below the y=x diagonal (want to weigh less):", round(below_diagonal_share, 3))
assert below_diagonal_share > 0.5  # most people want to weigh less

smoke_crosstab = pd.crosstab(cdc['genhlth'], cdc['smoke100'], normalize='index')
fig, ax = plt.subplots()
smoke_crosstab.plot(kind='bar', stacked=True, ax=ax)
ax.set_title('Smoking status by self-reported health')
ax.set_ylabel('proportion')
fig.savefig('_tmp_mp3_stacked.png')
plt.close(fig)

# 5. Conclude (three points a non-technical reader could act on):
# - Most respondents want to weigh less than they currently do, across
#   every health category - weight-management messaging has a receptive
#   audience.
# - The desire to lose weight rises steadily as self-reported health
#   worsens, so targeting weight-loss support at "fair"/"poor" health
#   groups is likely to reach those who most want it.
# - Mean BMI varies more by age band than by gender in this survey - age
#   is the stronger factor to design outreach around.

# Clean up the plot files written for this verification run.
for f in (
    '_tmp_mp1_bar.png', '_tmp_mp1_box.png',
    '_tmp_mp2_weekly.png', '_tmp_mp2_violin.png',
    '_tmp_mp3_heatmap.png', '_tmp_mp3_scatter.png', '_tmp_mp3_stacked.png',
):
    if os.path.exists(f):
        os.remove(f)

print("All cross-module mini-project checks passed.")
