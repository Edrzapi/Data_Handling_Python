# =====================================================================
# PLOTTING
# =====================================================================
# Three libraries, one idea. pandas gives you a one-line chart for a
# quick look, matplotlib gives you the control you need for anything you
# will show somebody else, and seaborn gives you statistical charts
# without the assembly work. They all draw on the same matplotlib
# canvas, so you can mix them.
#
# The data is data/loan_data.csv and data/train_viz.csv from the data
# folder of this repo.
#
# Run from the repo root so the relative data/ paths resolve.
#
# The plt.show() calls below open a window when you run this yourself.
# Nothing is saved to disk. If you want to keep a chart, add
# fig.savefig("name.png") before plt.show().
# =====================================================================

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

loans = pd.read_csv("data/loan_data.csv")
trains = pd.read_csv("data/train_viz.csv", nrows=3000, parse_dates=["departure"])


# ---------------------------------------------------------------------
# 1. The quick route: .plot() on a DataFrame
# ---------------------------------------------------------------------
# pandas has matplotlib built in. df.plot() draws the frame and hands
# back the Axes object that matplotlib drew it on.
# kind= picks the chart type: "line" (the default), "bar", "barh",
# "hist", "box", "scatter", "area", "pie".
loans["Term"].value_counts().plot(kind="bar")
plt.show()                 # show() puts the figure on the screen

daily = trains.set_index("departure").sort_index()["price"].resample("D").mean()

daily.plot()               # a Series with a date index plots as a line
plt.show()

# One thing to know: .plot() draws onto matplotlib's "current" axes,
# whatever that happens to be. Run two of these in a notebook cell
# without a show() in between and the second lands on top of the first.
# That invisible current-axes idea is the root of most plotting
# confusion, and section 3 shows how to stop relying on it.
#
# .plot() is the right tool for looking at your own data while you work.
# It is a poor tool for a chart somebody else will read, because the
# labels are whatever your column happened to be called and you have
# little say over the layout. For that, use matplotlib directly.


# ---------------------------------------------------------------------
# 2. Figures and axes - the two words you need
# ---------------------------------------------------------------------
# A FIGURE is the sheet of paper. An AXES is one set of x and y axes
# drawn on it, in other words one chart. A figure can hold several axes.
#
# plt.subplots() - creates a figure and the axes on it, and returns both
fig, ax = plt.subplots(figsize=(8, 4))     # figsize is inches, (width, height)

ax.plot(daily.index, daily.values)
ax.set_title("Average train fare by day")
ax.set_xlabel("Departure date")
ax.set_ylabel("Mean price (euros)")

fig.tight_layout()         # stops the labels being cut off at the edges
plt.show()

# Everything you draw goes through ax. Everything about the whole sheet,
# such as saving or overall layout, goes through fig.


# ---------------------------------------------------------------------
# 3. Object-oriented style versus the pyplot state machine
# ---------------------------------------------------------------------
# You will see two styles in tutorials. They produce the same picture.
#
# The pyplot style talks to whichever chart matplotlib happens to think
# is "current", and every function quietly acts on that one:
plt.plot(daily.index, daily.values)
plt.title("Pyplot style")
plt.xlabel("Date")
plt.show()

# The object-oriented style names the chart it is talking to:
fig, ax = plt.subplots()
ax.plot(daily.index, daily.values)
ax.set_title("Object-oriented style")
ax.set_xlabel("Date")
plt.show()

# Why prefer the second one. As soon as there is more than one chart on
# the page, "the current one" becomes a guessing game, and a function
# that draws a chart cannot be handed an axes to draw on. With fig and
# ax in hand you always know what you are changing, and you can pass ax
# into a helper function so the same code draws panel 1 or panel 4.
#
# Note the naming: the pyplot version is plt.title, the axes version is
# ax.set_title. The set_ prefix catches people out constantly.


# ---------------------------------------------------------------------
# 4. The common chart types, and when each is right
# ---------------------------------------------------------------------
# The chart type is not a style choice. It follows from the question.

# LINE: something measured over time, where the order matters.
fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(daily.index, daily.values)
ax.set_title("Line: a value over time")
fig.tight_layout()
plt.show()

# BAR: comparing a number across a few named categories.
counts = trains["destination"].value_counts()
fig, ax = plt.subplots(figsize=(6, 3))
ax.bar(counts.index, counts.values)
ax.set_title("Bar: counts per category")
ax.set_ylabel("Trains")
fig.tight_layout()
plt.show()

# BARH: the same thing sideways. Use it when the category names are long
# or when there are many of them, because horizontal labels stay
# readable while vertical ones end up rotated and cramped.
classes = trains["vehicle_class"].value_counts()
fig, ax = plt.subplots(figsize=(6, 3))
ax.barh(classes.index, classes.values)
ax.set_title("Barh: long category names")
fig.tight_layout()
plt.show()

# HIST: the shape of ONE numeric column. Where do the values pile up?
fig, ax = plt.subplots(figsize=(6, 3))
ax.hist(loans["Income"], bins=30)
ax.set_title("Histogram: distribution of one column")
ax.set_xlabel("Income")
fig.tight_layout()
plt.show()

# SCATTER: the relationship between TWO numeric columns.
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(loans["Income"], loans["Balance"], alpha=0.3, s=12)
ax.set_title("Scatter: two numbers against each other")
ax.set_xlabel("Income")
ax.set_ylabel("Balance")
fig.tight_layout()
plt.show()
# alpha makes the dots see-through so you can tell a dense patch from a
# single point, and s sets their size. Both matter once you have more
# than a few hundred rows.

# BOX: comparing the spread of a number across groups. The box covers
# the middle half of the data, the line inside is the median and the
# dots beyond the whiskers are outliers.
short = loans.loc[loans["Term"] == "Short Term", "Balance"]
long = loans.loc[loans["Term"] == "Long Term", "Balance"]

fig, ax = plt.subplots(figsize=(6, 4))
ax.boxplot([short, long], tick_labels=["Short Term", "Long Term"])
ax.set_title("Box: spread within each group")
ax.set_ylabel("Balance")
fig.tight_layout()
plt.show()

# WATCH OUT: this argument used to be called labels=. matplotlib 3.9
# removed it in favour of tick_labels=, so older code raises:
fig, ax = plt.subplots()
try:
    ax.boxplot([short, long], labels=["Short Term", "Long Term"])
except TypeError as err:
    print("boxplot(labels=...) ->", err)
plt.close(fig)             # close a figure you are not going to show
# Axes.boxplot() got an unexpected keyword argument 'labels'.
# The fix is a rename, nothing more.


# ---------------------------------------------------------------------
# 5. Labelling - the part people skip
# ---------------------------------------------------------------------
# An unlabelled chart is a picture, not a finding. Three lines turn one
# into the other, and they take ten seconds.
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(daily.index, daily.values, label="Daily mean")
ax.plot(daily.rolling(7, min_periods=1).mean(), label="7 day average")

ax.set_title("Madrid train fares, April to May 2019")
ax.set_xlabel("Departure date")
ax.set_ylabel("Mean price (euros)")
ax.legend()                          # uses the label= given to each line
ax.grid(alpha=0.3)                   # faint gridlines help people read values
fig.autofmt_xdate()                  # angles the date labels so they fit
fig.tight_layout()
plt.show()

# Ask of every chart you produce: could somebody who has not seen the
# data say what it is about, what the axes are and what the units are?
# If not, it is not finished.


# ---------------------------------------------------------------------
# 6. Several charts on one figure
# ---------------------------------------------------------------------
# plt.subplots(rows, cols) returns the figure and an array of axes, one
# per panel. Put charts side by side when you want them compared.
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].hist(loans.loc[loans["Term"] == "Short Term", "Income"], bins=20)
axes[0].set_title("Short term")
axes[0].set_xlabel("Income")

axes[1].hist(loans.loc[loans["Term"] == "Long Term", "Income"], bins=20)
axes[1].set_title("Long term")
axes[1].set_xlabel("Income")

fig.suptitle("Income by loan term")      # a title for the whole figure
fig.tight_layout()
plt.show()

# Careful: by default each panel scales its own axes, so two charts that
# look alike may be on completely different scales. sharey=True forces
# them onto the same y axis, which is usually what you want when the
# whole point is a comparison.
fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
axes[0].hist(loans.loc[loans["Term"] == "Short Term", "Income"], bins=20)
axes[0].set_title("Short term")
axes[1].hist(loans.loc[loans["Term"] == "Long Term", "Income"], bins=20)
axes[1].set_title("Long term")
fig.tight_layout()
plt.show()

# With a grid of panels, axes is two-dimensional: axes[0, 1] is the top
# right. axes.flatten() gives a flat list if you would rather loop.


# ---------------------------------------------------------------------
# 7. Bin counts change the story
# ---------------------------------------------------------------------
# A histogram has no single correct answer. bins= decides how finely the
# values are chopped up, and the same column can look smooth or spiky
# depending on what you pick.
fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), sharey=False)

for ax, n in zip(axes, [5, 20, 100]):
    ax.hist(loans["Income"], bins=n)
    ax.set_title(f"bins={n}")
    ax.set_xlabel("Income")

fig.tight_layout()
plt.show()

# 5 bins hides the structure: everything lands in two or three blocks.
# 100 bins shows too much, and you start reading meaning into gaps that
# are just small samples. 20 to 30 is a sensible place to start, but the
# honest approach is to try a few and check that the story you are about
# to tell survives the change. If it only appears at one bin count, it
# is probably not there.


# ---------------------------------------------------------------------
# 8. A log scale for skewed data
# ---------------------------------------------------------------------
# Some columns are heavily lopsided: most values small, a few enormous.
# Debt is one. On a normal scale the chart is one tall bar and a flat
# line, and everything interesting is invisible.
print(loans["Debt"].describe().round(1))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].hist(loans["Debt"], bins=40)
axes[0].set_title("Linear scale")
axes[0].set_xlabel("Debt")
axes[0].set_ylabel("Customers")

axes[1].hist(loans["Debt"], bins=40)
axes[1].set_yscale("log")            # counts on a log scale
axes[1].set_title("Log scale on the counts")
axes[1].set_xlabel("Debt")

fig.tight_layout()
plt.show()

# On the right you can finally see the tail: the handful of customers
# with debts in the thousands, which the left chart squashes to nothing.
# Each step up the log axis is ten times the last, so read it carefully
# and always say on the chart that it is a log scale. set_xscale("log")
# does the same for the horizontal axis, which suits money and
# populations, but it cannot show zero or negative values.


# ---------------------------------------------------------------------
# 9. seaborn for statistical plots
# ---------------------------------------------------------------------
# seaborn sits on top of matplotlib. It takes a DataFrame plus column
# NAMES, does the grouping and the summarising itself, and labels the
# axes from the column names.
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=loans, x="Term", y="Income", ax=ax)
ax.set_title("seaborn: one call does the grouping")
fig.tight_layout()
plt.show()

# hue= splits by a third column, which is where seaborn really saves you
# work compared with plain matplotlib.
fig, ax = plt.subplots(figsize=(7, 4))
sns.scatterplot(data=loans, x="Income", y="Balance", hue="Default", alpha=0.5, ax=ax)
ax.set_title("seaborn: coloured by a third column")
fig.tight_layout()
plt.show()

# Other ones worth knowing: sns.histplot, sns.barplot (which draws a
# confidence interval on the mean), sns.heatmap for a correlation matrix
# and sns.countplot for category counts.
fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(loans[["Income", "Balance", "Debt", "Score"]].corr(), annot=True, cmap="Blues", ax=ax)
ax.set_title("Correlation between columns")
fig.tight_layout()
plt.show()

# WATCH OUT: seaborn has two kinds of function.
#   AXES-LEVEL functions draw onto an axes you give them. They take
#   ax= and fit into a subplot grid: boxplot, scatterplot, histplot,
#   barplot, lineplot, countplot, heatmap.
#
#   FIGURE-LEVEL functions build their OWN figure, with their own grid
#   of panels inside it: lmplot, relplot, catplot, displot, pairplot.
#   They do not take ax= at all.
fig, ax = plt.subplots()
try:
    sns.lmplot(data=loans, x="Income", y="Balance", ax=ax)
except TypeError as err:
    print("lmplot(ax=...) ->", err)
plt.close(fig)
# lmplot() got an unexpected keyword argument 'ax'. Nothing is broken:
# you have asked a function that manages a whole figure to squeeze into
# one panel of another figure, and it cannot.

# Use the figure-level version on its own, and set the size with
# height and aspect rather than figsize:
grid = sns.lmplot(data=loans, x="Income", y="Balance", hue="Term", height=4, aspect=1.4)
grid.figure.suptitle("lmplot builds its own figure", y=1.02)
plt.show()

# The rule of thumb: if you are assembling a multi-panel figure
# yourself, stick to the axes-level functions. Reach for a figure-level
# function when you want seaborn to do the whole layout, for example one
# panel per category via col=.


# ---------------------------------------------------------------------
# 10. THE POINT
# ---------------------------------------------------------------------
# Use .plot() to look, matplotlib to explain. Create the figure and axes
# yourself, name them, label them, and pick the chart type from the
# question you are answering rather than from habit. seaborn is worth
# learning on top for anything statistical, as long as you remember
# which of its functions will accept your axes and which insist on
# making their own.
