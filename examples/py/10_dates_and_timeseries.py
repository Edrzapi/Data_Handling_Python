# =====================================================================
# DATES AND TIME SERIES
# =====================================================================
# Worked reference for working with dates in pandas: getting text turned
# into real dates, pulling pieces out of them, putting them on the index
# so you can slice by date, changing the frequency of the data, and
# comparing each row to the one before it.
#
# The data is data/train_viz.csv, a log of Spanish train journeys with a
# departure time on every row. Every file used here is already in the
# data folder of this repo.
#
# Run from the repo root so the relative data/ paths resolve.
# =====================================================================

import pandas as pd

# ---------------------------------------------------------------------
# 1. Dates arrive as text, not as dates
# ---------------------------------------------------------------------
# A CSV file is just text. Nothing in the file says "this column is a
# date", so pandas leaves it as text unless you tell it otherwise.
trains = pd.read_csv("data/train_viz.csv", nrows=3000)   # nrows keeps the example quick

print(trains.dtypes)
# departure shows as "str" - pandas 3 labels text columns str. Older
# pandas called the same thing "object", so tutorials written before
# pandas 3 will show that instead. Either way it means "not a date".

# Text is no use for date work. Sorting is alphabetical, you cannot
# subtract one date from another, and you cannot ask what month it is.
print(trains["departure"].head(3))

# pd.to_datetime(series) - converts text to real timestamps
trains["departure"] = pd.to_datetime(trains["departure"])
print(trains["departure"].dtype)          # datetime64[us] - now it is a date
# The [us] part is the storage precision, microseconds. pandas 3 picks
# it to suit the data; older pandas always used nanoseconds, [ns].

# Two arguments worth knowing about:
#   format="%d/%m/%Y"   spell out the layout when the dates are ambiguous
#                       or when the file is large and you want the speed
#   errors="coerce"     turn anything unparseable into NaT (the date
#                       version of NaN) instead of raising an error
messy = pd.Series(["2019-06-15", "not a date", "2019-06-17"])
print(pd.to_datetime(messy, errors="coerce"))

# Guessing the layout is the classic trap. 05/06/2019 is the 5th of June
# to a British reader and the 6th of May to an American one. pandas
# reads it American-style by default, so say what you mean:
print(pd.to_datetime("05/06/2019", dayfirst=True))    # 2019-06-05


# ---------------------------------------------------------------------
# 2. Better: parse at read time
# ---------------------------------------------------------------------
# parse_dates=[...] does the conversion while the file is being read, so
# you never have a text version lying around to trip over later.
trains = pd.read_csv("data/train_viz.csv", nrows=3000, parse_dates=["departure", "arrival"])
print(trains.dtypes)

# Make this your habit. Converting afterwards works, but the whole class
# of "I forgot to convert" bugs disappears if you do it on the way in.


# ---------------------------------------------------------------------
# 3. The .dt accessor - getting the pieces out
# ---------------------------------------------------------------------
# A date column holds a lot of information. .dt is the doorway to it:
# it applies a date operation to every row at once.
dep = trains["departure"]

print(dep.dt.year.head(3))
print(dep.dt.month.head(3))         # 1 to 12
print(dep.dt.day.head(3))           # day of the month
print(dep.dt.hour.head(3))
print(dep.dt.dayofweek.head(3))     # 0 = Monday ... 6 = Sunday
print(dep.dt.day_name().head(3))    # 'Friday' etc, handier for charts
print(dep.dt.date.head(3))          # the calendar day, time thrown away

# Why this matters: the interesting questions are usually about a PIECE
# of the date, not the date itself. "Are weekend trains dearer?" is a
# question about dayofweek, and .dt is how you get a column to group by.
trains["weekday"] = dep.dt.day_name()
print(trains.groupby("weekday")["price"].mean().round(2))

# .dt only works on date columns. On a text column it raises
# AttributeError: Can only use .dt accessor with datetimelike values.
# If you see that, you skipped the conversion in section 1.


# ---------------------------------------------------------------------
# 4. Putting the date on the index
# ---------------------------------------------------------------------
# set_index("departure") makes the departure time the row label. The
# index is then a DatetimeIndex, and that unlocks the time series tools:
# date slicing, resample and rolling all expect it.
ts = trains.set_index("departure").sort_index()
print(type(ts.index).__name__)      # DatetimeIndex

# Sorting matters. Date slicing on an unsorted index either fails or
# quietly returns the wrong thing, so sort_index() straight after
# set_index is a good reflex.


# ---------------------------------------------------------------------
# 5. Slicing by date string
# ---------------------------------------------------------------------
# With a DatetimeIndex you can select rows using plain strings, and you
# can be as vague as you like. pandas expands a partial date for you.
print(ts.loc["2019-04-15"].shape)        # everything on that day
print(ts.loc["2019-04"].shape)           # everything in April 2019

# A range works too.
week = ts.loc["2019-04-15":"2019-04-21"]
print(week.index.min(), week.index.max())

# WATCH OUT: this slice is END-INCLUSIVE. Normal Python slicing stops
# before the last item, so you may expect the 21st to be left out. Date
# slicing includes it. Compare:
letters = ["a", "b", "c", "d"]
print(letters[0:2])                      # ['a', 'b'] - 'c' excluded

small = pd.Series([1, 2, 3], index=pd.to_datetime(["2019-06-01", "2019-06-15", "2019-07-01"]))
print(small.loc["2019-06-01":"2019-06-15"])   # both ends present

# The reason is that a label slice with .loc is always end-inclusive in
# pandas, dates or not. It is worth knowing because an off-by-one day at
# the end of a reporting period is an easy mistake to make and a hard
# one to spot.


# ---------------------------------------------------------------------
# 6. Making your own dates: date_range
# ---------------------------------------------------------------------
# pd.date_range(start, end/periods, freq) - builds a run of evenly
# spaced timestamps. Useful for test data, for axis labels, and for
# spotting days that are missing from real data.
print(pd.date_range("2019-06-01", periods=5, freq="D"))       # daily
print(pd.date_range("2019-06-01", periods=3, freq="h"))       # hourly
print(pd.date_range("2019-06-01", "2019-06-30", freq="W"))    # weekly, Sundays

# The freq codes you will use most:
#   "h"    hour                "D"   calendar day
#   "min"  minute              "W"   week
#   "ME"   month end           "MS"  month start
#   "QE"   quarter end         "YE"  year end
# "ME" means the LAST day of each month, "MS" the first. Pick the one
# that matches how your organisation reports.
print(pd.date_range("2019-06-01", periods=3, freq="ME"))
print(pd.date_range("2019-06-01", periods=3, freq="MS"))

# WATCH OUT: pandas 3 removed the old capital-letter aliases. Plenty of
# tutorials and older code still use "H" for hourly and "M" for monthly.
# Both now raise, so you need to recognise the error:
for code in ["H", "M"]:
    try:
        pd.date_range("2019-06-01", periods=2, freq=code)
    except ValueError as err:
        print(f"freq={code!r} ->", err)
# "H" reports Invalid frequency: H ... Did you mean h?
# "M" reports 'M' is no longer supported for offsets. Please use 'ME'.
# The fix is always the same: lower case for times, add E for the
# end-of-period codes.


# ---------------------------------------------------------------------
# 7. resample - changing the frequency
# ---------------------------------------------------------------------
# The raw data has one row per train, which is too fine-grained to see a
# pattern. resample(freq) groups the rows into time buckets. It behaves
# like groupby, except the groups are periods of time, so you still have
# to say how to combine the rows in each bucket.
daily_price = ts["price"].resample("D").mean()
print(daily_price.head())

# Any aggregation works, and different questions need different ones:
print(ts["price"].resample("D").size().head())      # how many trains ran
print(ts["price"].resample("W").max().head())       # dearest fare each week
print(ts["price"].resample("D").agg(["mean", "min", "max"]).head(3))

# resample fills in empty buckets. If no train ran on a given day you
# still get a row for it, with NaN for the mean. That is usually what
# you want: a gap in the data should look like a gap, not vanish. This
# sample happens to have trains every day, so the count below is 0.
print(daily_price.isna().sum(), "days with no trains in this sample")

# Going the other way (daily up to hourly) is called upsampling and
# creates rows you have no data for, so you have to say how to fill
# them: .ffill() carries the last value forward, .interpolate() draws a
# straight line between known points.


# ---------------------------------------------------------------------
# 8. Rolling windows - smoothing out the noise
# ---------------------------------------------------------------------
# Day to day prices jump around. A rolling average shows the trend
# underneath by averaging each day with its neighbours.
# .rolling(7) makes a window 7 rows wide that slides down the series.
rolling_7 = daily_price.rolling(7).mean()
print(rolling_7.head(8))

# Notice the first six values are NaN. With a 7 day window there are not
# yet 7 days of history, and rolling refuses to guess.

# min_periods controls exactly that refusal: the smallest number of real
# values a window needs before it returns an answer instead of NaN.
print(daily_price.rolling(7, min_periods=1).mean().head(8))

# With min_periods=1 the first value is just day one, the second is the
# average of days one and two, and so on until the window is full. That
# is convenient for a chart with no blank start, but be honest about it:
# those early points are averages of fewer days, so they are noisier
# than the rest of the line even though they look the same.

# min_periods also covers gaps in the middle: a window containing NaN
# days still reports a number, as long as at least min_periods real
# values sit inside it. Setting it to 5 out of 7 is a way of saying
# "give me an answer unless more than two days are missing".
print(daily_price.rolling(7, min_periods=5).mean().tail(3))


# ---------------------------------------------------------------------
# 9. shift - comparing with the previous period
# ---------------------------------------------------------------------
# .shift(1) moves every value down one row, so each row lines up beside
# the value that came before it. That is how you do "change since
# yesterday" without a loop.
change = pd.DataFrame({
    "price": daily_price,
    "yesterday": daily_price.shift(1),
})
change["difference"] = change["price"] - change["yesterday"]
change["pct_change"] = (change["difference"] / change["yesterday"] * 100).round(1)
print(change.head())

# The first row is NaN because there is no day before it. Correct, not a
# bug. pandas has a shortcut for the percentage version:
print(daily_price.pct_change().mul(100).round(1).head())

# shift(-1) looks forward instead, which is how you compare with
# tomorrow. Be careful with it in forecasting work: using tomorrow's
# value to predict today is called leakage and makes a model look far
# better than it really is.

# shift moves values by POSITION, not by time. On daily data with no
# gaps those are the same thing. On irregular data they are not, so
# resample to a fixed frequency first, as we did above.


# ---------------------------------------------------------------------
# 10. Time zones: tz_localize versus tz_convert
# ---------------------------------------------------------------------
# A timestamp with no time zone is "naive": 09:00, but nobody has said
# 09:00 where. The two methods do different jobs and the names are easy
# to mix up.
#
#   tz_localize  attaches a time zone. The clock reading does not move.
#   tz_convert   translates into another zone. The clock reading moves.
naive = pd.Timestamp("2019-06-15 09:00")
print(naive)                                       # 2019-06-15 09:00:00

madrid = naive.tz_localize("Europe/Madrid")        # this 09:00 is Madrid time
print(madrid)                                      # 2019-06-15 09:00:00+02:00

print(madrid.tz_convert("UTC"))                    # 2019-06-15 07:00:00+00:00
print(madrid.tz_convert("Europe/London"))          # 2019-06-15 08:00:00+01:00

# Same instant in all three, written three ways. That is the whole point
# of time zones: the moment is fixed, the label changes.

# Use the wrong one and pandas stops you:
try:
    pd.Timestamp("2019-06-15 09:00").tz_convert("UTC")
except TypeError as err:
    print("tz_convert on a naive timestamp ->", err)
# Cannot convert tz-naive Timestamp, use tz_localize to localize.
# You cannot translate a time until you know where it started.

# The daylight saving trap. Clocks in Madrid jump from 02:00 to 03:00 on
# the last Sunday in March, so 02:30 that day never existed:
try:
    pd.Timestamp("2019-03-31 02:30").tz_localize("Europe/Madrid")
except ValueError as err:
    print("localising a missing hour ->", err)
# 2019-03-31 02:30:00 is a nonexistent time due to daylight savings
# time. Try using the 'nonexistent' argument.
#
# This is why the examples above use a June date. The same thing happens
# in reverse in October, when 02:30 occurs twice and pandas raises
# AmbiguousTimeError. If you are stuck with real data that lands on
# those hours, tz_localize takes nonexistent= and ambiguous= to say what
# should happen, for example nonexistent="shift_forward".

# Whole columns work the same way, through .dt:
utc_departures = ts.index.tz_localize("Europe/Madrid").tz_convert("UTC")
print(utc_departures[:3])

# Practical advice: store timestamps in UTC and convert to local time
# only when you show them to somebody. Mixing local times from several
# countries in one column makes them impossible to compare.


# ---------------------------------------------------------------------
# 11. THE POINT
# ---------------------------------------------------------------------
# Dates come in as text and are useless until you convert them. Once
# converted, .dt gets the pieces out, a DatetimeIndex lets you slice by
# date, resample changes the frequency, rolling smooths the result and
# shift compares each period with the last. That handful of tools covers
# most of the time series work you will ever do.
