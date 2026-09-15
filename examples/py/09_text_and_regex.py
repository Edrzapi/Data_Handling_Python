# =====================================================================
# TEXT COLUMNS, REGULAR EXPRESSIONS AND BINNING
# =====================================================================
# Cleaning numbers is the easy half. Most of the mess in a real dataset
# is in the text: stray spaces, inconsistent capitals, two facts crammed
# into one column. This file covers the .str accessor that gets at all
# of it, regular expressions for the patterns .str cannot express, and
# pd.cut for turning a continuous number into labelled bands.
#
# Files used: data/renfe_trains.csv (read with nrows= because it is
# large), data/mortgage_applicants.csv and data/cdc.csv.
#
# Run from the repo root so the relative data/ paths resolve.
# =====================================================================

import pandas as pd

trains = pd.read_csv("data/renfe_trains.csv", nrows=3000)

# This file has stray copies of its own header line scattered through
# it, so strip those out first. The cleaning example covers why.
trains = trains[trains["company"] != "company"]
print(trains.shape)                 # (2947, 8)


# ---------------------------------------------------------------------
# 1. THE .str ACCESSOR, AND WHY IT EXISTS
# ---------------------------------------------------------------------
# A Series holding text is not itself a string, so Python's string
# methods are not available on it:
try:
    trains["origin"].lower()
except AttributeError as err:
    print(f"{type(err).__name__}: {err}")
# AttributeError: 'Series' object has no attribute 'lower'
# The Series is a container of many strings. Asking it to lowercase
# itself is like asking a filing cabinet to lowercase itself.

# .str is the accessor that says "apply this to every string inside".
print(trains["origin"].str.lower().head(3).tolist())
# ['madrid', 'madrid', 'madrid']

# Two things it gives you for free:
#  - it loops for you, so no for loop and no .apply
#  - it skips missing values. NaN stays NaN instead of blowing up with
#    "float has no attribute lower", which is what .apply(str.lower)
#    would do on a column with gaps.
print(trains["vehicle_class"].str.lower().isna().sum())     # 4, unchanged


# ---------------------------------------------------------------------
# 2. THE EVERYDAY .str METHODS
# ---------------------------------------------------------------------
# These are the Python string methods you already know, applied down a
# column. Every one returns a NEW Series, so assign the result.

# .str.strip() - remove whitespace from both ends. Leading and trailing
# spaces are invisible on screen but break every comparison and every
# groupby, so strip on import as a matter of habit.
messy = pd.Series(["  MADRID ", "Barcelona  ", " sevilla"])
print(messy.str.strip().tolist())
# ['MADRID', 'Barcelona', 'sevilla']
# .str.lstrip() and .str.rstrip() do one end only.

# .str.lower() / .str.upper() - normalise case. "MADRID" and "Madrid"
# are two different groups to pandas until you make them one.
print(messy.str.strip().str.lower().tolist())
# ['madrid', 'barcelona', 'sevilla']
# Note the chaining: .str.strip() gives back a Series, so you need .str
# again before the next string method. It is not a typo.

# .str.title() capitalises each word, which is how you would want a
# place name to read on a chart.
print(trains["origin"].str.title().head(3).tolist())

# .str.replace(old, new) - swap text. regex=False means "treat old as
# literal text", which is what you nearly always want; set regex=True
# only when old is a pattern (section 4).
tidy_class = trains["vehicle_class"].str.replace(
    "Turista con enlace", "Turista (connecting)", regex=False
)
print(tidy_class.value_counts().head())

# .str.split(sep) - cut each string at the separator. By default you get
# a column of LISTS, which is awkward to work with.
print(trains["departure"].str.split(" ").head(2).tolist())

# expand=True gives you a DataFrame with one column per piece instead.
# That is how you split one column into two real columns.
parts = trains["departure"].str.split(" ", expand=True)
print(parts.head(2))
trains["dep_date"] = parts[0]
trains["dep_time"] = parts[1]
print(trains[["dep_date", "dep_time"]].head(2))

# .str.len() - length of each string, handy for spotting bad values
print(trains["dep_date"].str.len().value_counts())      # all 10, as expected


# ---------------------------------------------------------------------
# 3. FILTERING ON TEXT
# ---------------------------------------------------------------------
# These return True/False Series, so you use them inside df[...] the way
# you would use a > comparison on a number.

# .str.contains(sub) - is sub anywhere in the string?
# na=False decides what a missing value counts as. Without it you get
# NaN in the result, and NaN is not usable as a filter, so set it.
is_turista = trains["vehicle_class"].str.contains("Turista", na=False)
print(is_turista.sum())                         # 2553
print(trains[is_turista].shape)                 # (2553, 10)

# case=False makes the match case-insensitive, which saves you
# lowercasing the column first just to search it.
print(trains["fare"].str.contains("promo", case=False, na=False).sum())    # 2156

# .str.startswith(sub) / .str.endswith(sub) - anchored at one end.
# "Promo" and "Promo +" are two fare types; this catches both.
print(trains["fare"].str.startswith("Promo", na=False).sum())              # 2156

# Combine conditions with & (and) and | (or). The brackets round each
# condition are required, because & binds tighter than == in Python.
cheap_turista = trains[is_turista & (trains["fare"] == "Promo")]
print(len(cheap_turista))                       # 1803


# ---------------------------------------------------------------------
# 4. REGULAR EXPRESSIONS: PULLING VALUES OUT
# ---------------------------------------------------------------------
# A regular expression (regex) is a small pattern language for
# describing the SHAPE of a string: "two letters then a digit" rather
# than a literal value. Use one when the thing you want varies but its
# shape does not.

# .str.extract(pattern) - returns the bracketed part of the pattern,
# one column per pair of brackets. Brackets mark a "capture group": the
# piece you want back, as opposed to the pieces that only have to match.
apps = pd.read_csv("data/mortgage_applicants.csv", index_col=0)
print(apps["Term"].value_counts())        # '10 Years', '20 Years'

# \d means "any digit", + means "one or more of the thing before it", so
# (\d+) captures the run of digits and ignores the word after it.
years = apps["Term"].str.extract(r"(\d+)")
print(years.head(3))
print(type(years))                        # a DataFrame, even for one group

# extract always returns a DataFrame. Take column 0 to get a Series, and
# convert it, because a digit pulled out of text is still text.
apps["Term_years"] = pd.to_numeric(apps["Term"].str.extract(r"(\d+)")[0])
print(apps["Term_years"].dtype)           # int64
print(apps["Term_years"].mean().round(1))    # 13.2

# The r in r"(\d+)" makes it a raw string, so Python leaves the
# backslash alone and passes it to the regex engine. Always write
# patterns as raw strings; without the r you will eventually hit a
# sequence like \b that Python quietly converts to something else.

# Several groups give you several columns at once
ym = trains["departure"].str.extract(r"^(\d{4})-(\d{2})")
print(ym.head(2))
# {4} is a quantifier meaning "exactly four of these", so \d{4} is a
# four digit year. {2,} means two or more, {1,2} means one or two.

# .str.extract only returns the FIRST match in each string. Use
# .str.extractall(pattern) when a string can contain several.


# ---------------------------------------------------------------------
# 5. BUILDING A REGEX A PIECE AT A TIME: UK POSTCODES
# ---------------------------------------------------------------------
# Nobody writes a pattern like this in one go. You build it up and test
# each step against real examples, including ones that should fail.
postcodes = pd.Series([
    "SW1A 1AA",        # central London, four character outward part
    "  m1 1ae ",       # untidy: lowercase, padded with spaces
    "EC1A1BB",         # no space in the middle
    "B33 8TH",         # single letter area
    "DN55 1PT",        # two digits in the outward part
    "CR2 6XH",
    "not a postcode",  # should NOT match
])

# Step 0: normalise first. Half of what looks like a hard pattern
# problem is really a whitespace and capitals problem.
pc = postcodes.str.strip().str.upper()
print(pc.tolist())

# A UK postcode is an outward part (SW1A) and an inward part (1AA).
# Take the inward part first, because it never varies:
#     \d[A-Z]{2}  -  one digit, then exactly two letters
# [A-Z] is a CHARACTER CLASS: the square brackets mean "any one
# character from this set", and A-Z is a range covering the alphabet.
print(pc.str.extract(r"(\d[A-Z]{2})").head(3))

# Now the outward part. It is one or two letters, then a digit, then
# optionally one more letter or digit:
#     [A-Z]{1,2}   one or two letters
#     \d           a digit
#     [A-Z\d]?     ? means "zero or one of these", so this last
#                  character is optional. The class holds letters AND
#                  digits because both occur (SW1A, DN55).
outward = r"[A-Z]{1,2}\d[A-Z\d]?"
print(pc.str.extract(f"({outward})").head(3))

# Join them with \s* : \s is any whitespace, * is "zero or more", so
# this accepts "SW1A 1AA" and "SW1A1AA" alike.
pattern = rf"({outward})\s*(\d[A-Z]{{2}})"
print(pc.str.extract(pattern))
# The doubled {{2}} is an f-string detail, not a regex one: inside an
# f-string a literal brace has to be written twice.

# ANCHORS. ^ means "start of the string", $ means "end of it". Without
# them the pattern can match a fragment buried in a longer string, so a
# tidy-looking result may be hiding junk either side of it.
loose = pc.str.extract(pattern)
anchored = pc.str.extract(rf"^{pattern}$")
print(loose[0].notna().sum(), "match unanchored")     # 6
print(anchored[0].notna().sum(), "match anchored")    # 6

# On this small list both agree. The difference shows up on real input:
print(pd.Series(["FLAT 2 SW1A 1AA"]).str.extract(pattern)[0].tolist())
# ['SW1A'] - the loose pattern happily finds a postcode inside an address
print(pd.Series(["FLAT 2 SW1A 1AA"]).str.extract(rf"^{pattern}$")[0].tolist())
# [nan] - anchored, it correctly says "this whole string is not a postcode"
# Which you want depends on the job: anchored to VALIDATE a field,
# unanchored to FIND a postcode inside free text.

# .str.match(pattern) - True/False rather than the value, for validating
valid = pc.str.match(rf"^{pattern}$")
print(valid.tolist())
# [True, True, True, True, True, True, False]
print(pc[~valid].tolist())       # ~ inverts the mask: ['NOT A POSTCODE']

# This pattern is good enough for cleaning work. It is not the full
# official rule, which excludes certain letters in certain positions.
# Be clear which you need: a validator that is slightly too generous is
# fine for spotting typos, and wrong for rejecting a customer's address.

# The three you will use most, and the difference between them:
#   .str.contains(p)  True/False - is there a match anywhere?
#   .str.match(p)     True/False - does the match start at the beginning?
#   .str.extract(p)   the captured text itself
print(pc.str.contains(r"\d[A-Z]{2}$").tolist())


# ---------------------------------------------------------------------
# 6. REGEX IN .str.replace
# ---------------------------------------------------------------------
# With regex=True the first argument becomes a pattern, which lets you
# describe what to remove rather than listing every case.
noisy = pd.Series(["£1,299.00", "£450.50", "£12,000.00"])

# [£,] is a character class: any one of these characters. The pattern
# says "a pound sign or a comma", and "" replaces it with nothing.
numbers = pd.to_numeric(noisy.str.replace(r"[£,]", "", regex=True))
print(numbers.tolist())                  # [1299.0, 450.5, 12000.0]

# Collapsing runs of whitespace is the other common use. \s+ is "one or
# more whitespace characters", including the tabs you cannot see.
spaced = pd.Series(["MADRID    to   SEVILLA"])
print(spaced.str.replace(r"\s+", " ", regex=True).tolist())
# ['MADRID to SEVILLA']


# ---------------------------------------------------------------------
# 7. pd.cut - TURNING NUMBERS INTO BANDS
# ---------------------------------------------------------------------
# Sometimes a continuous number is more useful as a category: "under 30"
# rather than 27. pd.cut(series, bins=..., labels=...) sorts each value
# into a band and hands back a categorical column.
cdc = pd.read_csv("data/cdc.csv", index_col=0)
print(cdc["age"].describe())      # 18 to 99

# bins= is the list of EDGES, so four bands need five numbers.
# labels= names them, and must be one shorter than bins.
age_band = pd.cut(
    cdc["age"],
    bins=[17, 30, 45, 60, 120],
    labels=["18-30", "31-45", "46-60", "61+"],
)
print(age_band.head())
print(age_band.value_counts(sort=False))
#   18-30    4734
#   31-45    6463
#   46-60    4659
#   61+      4144

# Why 17 and not 18 as the first edge? By default each band excludes its
# lower edge and includes its upper one, written (17, 30]. Start at 18
# and every 18 year old falls outside every band and comes back NaN.
# Two fixes: start one below, as above, or pass include_lowest=True.
print(pd.cut(cdc["age"], bins=[18, 30, 45, 60, 120]).isna().sum())   # 306 lost
print(age_band.isna().sum())                                         # 0

# right=False flips the rule to [18, 31), including the lower edge and
# excluding the upper, which many people find easier to reason about.
left_closed = pd.cut(cdc["age"], bins=[18, 31, 46, 61, 120], right=False)
print(left_closed.isna().sum())                                      # 0

# Without labels= you get the intervals themselves as the labels, which
# is honest about the edges and ugly on a chart.
print(pd.cut(cdc["weight"], bins=3).value_counts(sort=False))
# bins=3 as a plain number means "three bands of equal WIDTH". Note how
# lopsided the counts are: equal width is not equal size.

# pd.qcut(series, 4) is the other one to know. It splits by QUANTILE,
# so each band holds roughly the same NUMBER of rows and the widths
# vary. Use cut for meaningful thresholds you choose, qcut for
# quartiles and percentiles.
print(pd.qcut(cdc["weight"], 4).value_counts(sort=False))

# The result is a category column, so it groups and sorts in the order
# you defined rather than alphabetically. That is the real payoff:
print(cdc.groupby(age_band, observed=True)["weight"].mean().round(1))


# ---------------------------------------------------------------------
# 8. THE POINT
# ---------------------------------------------------------------------
# .str is how you reach the strings inside a column, regex is how you
# describe a shape rather than a value, and pd.cut is how you turn a
# measurement into a group you can count. Between them they handle most
# of what "cleaning" means once the numbers are sorted out.
