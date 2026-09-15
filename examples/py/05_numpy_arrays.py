# =====================================================================
# NUMPY ARRAYS - THE LAYER UNDERNEATH PANDAS
# =====================================================================
# Worked reference for the NumPy array: how to make one, what its dtype
# is for, how broadcasting and boolean masking replace loops, and the
# two traps that catch nearly everyone (slices sharing memory, and
# nan not equalling itself).
#
# A pandas DataFrame column IS a NumPy array with a label on it, so
# everything here turns up again the moment you touch pandas.
#
# Run from the repo root so the relative data/ paths resolve.
# =====================================================================

import timeit

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------
# 1. WHY AN ARRAY AND NOT A LIST
# ---------------------------------------------------------------------
# A Python list can hold anything: numbers, text, other lists, all mixed
# together. That flexibility costs you. Every element is a separate
# Python object scattered around memory, and every operation on the list
# has to check "what type is this one?" before it can do anything.
#
# An array holds ONE type only, laid out in a single unbroken block of
# memory. NumPy can then hand the whole block to compiled C code and let
# it run at full speed with no per-element type checking. That is the
# whole trade: you give up mixed types, you get speed.

numbers = np.array([1, 2, 3, 4, 5])   # np.array(sequence) - build from a list
print(numbers)
print(type(numbers))                  # numpy.ndarray, not list
print(numbers.dtype)                  # int64 - ONE type for the whole array
print(numbers.shape)                  # (5,) - a 1-D array of 5 items
print(numbers.ndim)                   # 1 - number of dimensions

# The speed difference is not subtle. Doubling a million numbers:
setup = "import numpy as np; l = list(range(1_000_000)); a = np.arange(1_000_000)"
list_time = timeit.timeit("[x * 2 for x in l]", setup, number=3) / 3
array_time = timeit.timeit("a * 2", setup, number=3) / 3
print(f"list comprehension: {list_time:.4f}s")
print(f"numpy array:        {array_time:.4f}s")
print(f"array is roughly {list_time / array_time:.0f}x faster here")

# It is smaller too. A list of a million ints is a million pointers to a
# million separate objects; the array is a million 8-byte slots.
print(np.arange(1_000_000).nbytes, "bytes for the array itself")


# ---------------------------------------------------------------------
# 2. THREE WAYS TO MAKE ONE
# ---------------------------------------------------------------------
# (a) np.array(list) - when you already have the values
scores = np.array([225.0, 187.0, 85.0])

# (b) np.arange(start, stop, step) - like range(), but it gives an array
#     and accepts a decimal step. The stop is EXCLUSIVE, same as range().
print(np.arange(0, 10, 2))        # [0 2 4 6 8] - 10 is not there
print(np.arange(0, 1, 0.25))      # [0.   0.25 0.5  0.75] - 1.0 is not there

# (c) np.linspace(start, stop, num) - "num evenly spaced points between
#     start and stop". Here the stop IS included.
print(np.linspace(0, 1, 5))       # [0.   0.25 0.5  0.75 1.  ]

# That difference is the point. arange says "how big a step", linspace
# says "how many points". Use linspace whenever you need the endpoint to
# land exactly on the value you asked for - with a decimal step, arange
# can overshoot or undershoot because of floating point rounding.

# Handy fillers when you know the shape but not the values yet:
print(np.zeros(3))                # [0. 0. 0.] - note: floats by default
print(np.ones((2, 3)))            # 2 rows, 3 columns, all 1.0
print(np.full(3, 7))              # [7 7 7]


# ---------------------------------------------------------------------
# 3. DTYPE - THE ONE TYPE, AND CHANGING IT
# ---------------------------------------------------------------------
# NumPy picks a dtype when you build the array. Mix an int and a float
# and everything becomes float, because floats can hold ints but not the
# other way round. NumPy calls this "upcasting".
print(np.array([1, 2, 3]).dtype)        # int64
print(np.array([1, 2, 3.5]).dtype)      # float64 - the 1 and 2 became 1.0, 2.0

# Put a string in and the WHOLE array becomes strings, numbers included:
print(np.array([1, 2, "3"]).dtype)      # <U21 - see section 4
print(np.array([1, 2, "3"]))            # ['1' '2' '3'] - now text, not numbers

# .astype(dtype) - returns a NEW array converted to another type.
prices = np.array([1.7, 2.9, -1.7])
print(prices.astype(int))               # [ 1  2 -1]

# READ THAT AGAIN. 1.7 became 1, 2.9 became 2, -1.7 became -1. astype
# TRUNCATES towards zero, it does not round. 2.9 is not 3. If you want
# rounding you have to ask for it, and round() gives you a float back so
# you still need the astype afterwards:
print(np.round(prices).astype(int))     # [ 2  3 -2]

# Missing values force a float dtype, because there is no such thing as
# an integer nan. This is why an integer column in a spreadsheet often
# arrives in pandas as float64 - one blank cell did it.
print(np.array([1, 2, np.nan]).dtype)   # float64
try:
    holes = np.array([1, 2, 3])
    holes[0] = np.nan
except ValueError as err:
    print(f"ValueError: {err}")
# ValueError: cannot convert float NaN to integer
# The array is int64 and nan is a float value with no integer equivalent,
# so there is nowhere to put it.


# ---------------------------------------------------------------------
# 4. <U9 - WHAT THAT STRING DTYPE ACTUALLY MEANS
# ---------------------------------------------------------------------
# Print the dtype of a text array and you get something cryptic:
composers = np.array(["Beethoven", "Bach"])
print(composers.dtype)      # <U9

# Read it in three parts:
#   <   byte order (little-endian; ignore it, it is a machine detail)
#   U   Unicode text
#   9   NINE CHARACTERS. The length of the longest string you gave it.
#
# NumPy needs every slot to be the same size, so it measured your longest
# string and made every slot exactly that wide. "Beethoven" is 9 letters,
# so every slot is 9 characters.
#
# The trap: that width is now fixed. Write a longer string into the array
# and the extra characters are cut off, with no error and no warning.
composers[1] = "Shostakovich"
print(composers)            # ['Beethoven' 'Shostakov'] - silently truncated

# This is why text belongs in pandas (which stores real Python strings)
# rather than in a fixed-width NumPy array. NumPy is built for numbers.


# ---------------------------------------------------------------------
# 5. BROADCASTING - MATHS WITHOUT LOOPS
# ---------------------------------------------------------------------
# An operation between an array and a single number is applied to every
# element. NumPy "broadcasts" the single value across the whole array.
# No loop, and the work happens in C.
balances = np.array([1460, 890, 880, 920, 1260])
print(balances * 2)
print(balances + 100)
print(balances / 1000)

# Two arrays of the SAME shape work element by element, position against
# matching position:
debts = np.array([272, 970, 884, 0, 0])
print(balances + debts)
print(debts / balances)         # debt as a fraction of balance, per row

# Mismatched shapes have nothing to pair up, so NumPy refuses:
try:
    np.array([1, 2, 3]) + np.array([1, 2])
except ValueError as err:
    print(f"ValueError: {err}")
# ValueError: operands could not be broadcast together with shapes (3,) (2,)
# Three things and two things: there is no sensible pairing, so rather
# than guess, NumPy stops. Check .shape on both when you see this.


# ---------------------------------------------------------------------
# 6. BOOLEAN MASKING - FILTERING WITHOUT AN IF
# ---------------------------------------------------------------------
# Compare an array to something and you do not get one True or False.
# You get an array of True/False, one per element. That is a "mask".
big = balances > 1000
print(big)                      # [ True False False False  True]
print(big.dtype)                # bool

# Put a mask inside the square brackets and you get back only the
# elements where the mask is True.
print(balances[big])            # [1460 1260]
print(balances[balances > 1000])   # same thing written in one line

# Combine conditions with & (and) and | (or). You MUST bracket each
# condition, because & binds more tightly than > does. Skip the brackets
# and Python tries to evaluate 1000 & balances first, and the error you
# get will not point at the real problem.
mid = balances[(balances > 800) & (balances < 1300)]
print(mid)                      # [890 880 920 1260]

# Masks are just arrays, so you can count and average them directly.
# True counts as 1 and False as 0, which makes .sum() a count and
# .mean() a proportion:
print((balances > 1000).sum())     # 2 rows match
print((balances > 1000).mean())    # 0.4 - so 40% of rows

# np.where(mask) - gives you the POSITIONS instead of the values, useful
# when you need to look the same rows up in another array.
print(np.where(balances > 1000))   # (array([0, 4]),)


# ---------------------------------------------------------------------
# 7. SLICING, AND THE VIEW-VERSUS-COPY TRAP
# ---------------------------------------------------------------------
# Slicing works like lists: [start:stop], stop excluded.
grid = np.arange(12).reshape(3, 4)   # .reshape - same data, new shape
print(grid)
print(grid[0])          # first row
print(grid[:, 1])       # every row, column 1 - rows first, then columns
print(grid[1:, 2:])     # from row 1 on, from column 2 on

# Now the trap. A slice does NOT copy the data. It is a "view": a second
# label pointing at the same block of memory. Change the view and you
# change the original.
#
# np.shares_memory(a, b) - tells you straight out whether two arrays sit
# on the same memory. Use it any time you are unsure.
window = grid[0:2]
print(np.shares_memory(grid, window))    # True - same memory

window[0, 0] = 99
print(grid[0, 0])                        # 99 - the original changed too

# "Fancy indexing" (passing a list of positions) cannot be a view,
# because the elements you asked for may be scattered anywhere in memory.
# NumPy has to gather them into a new block, so you get a copy:
grid = np.arange(12).reshape(3, 4)       # fresh start
picked = grid[[0, 1]]                    # a LIST of row numbers
print(np.shares_memory(grid, picked))    # False - separate memory

picked[0, 0] = 99
print(grid[0, 0])                        # 0 - the original is untouched

# Boolean masking is the same story: a mask returns a copy.
print(np.shares_memory(grid, grid[grid > 5]))     # False

# So grid[0:2] and grid[[0, 1]] can select identical rows and behave
# completely differently when you write to them. If you want to be sure
# you are working on your own data, say so with .copy():
safe = grid[0:2].copy()
print(np.shares_memory(grid, safe))      # False


# ---------------------------------------------------------------------
# 8. DESCRIPTIVE STATISTICS, AND ddof
# ---------------------------------------------------------------------
# Real numbers to work with: the credit scores from the loan dataset.
loans = pd.read_csv("data/loan_data.csv")
scores = loans["Score"].to_numpy()       # .to_numpy() - the raw array out
                                          # of a pandas column
print(scores.dtype, scores.shape)

# Drop the missing values for now; section 9 explains why we must.
clean = scores[~np.isnan(scores)]        # ~ means "not", so "keep the
                                          # ones that are NOT nan"
print(f"count:  {clean.size}")
print(f"mean:   {np.mean(clean):.2f}")   # the average
print(f"median: {np.median(clean):.2f}") # the middle value once sorted
print(f"std:    {np.std(clean):.2f}")    # typical distance from the mean
print(f"var:    {np.var(clean):.2f}")    # std squared

# Mean versus median matters when the data is lopsided. Debt here has a
# lot of zeros and a few very large values, which drags the mean well
# above the median. Quoting only the mean would misdescribe the typical
# customer.
debt = loans["Debt"].to_numpy()
print(f"debt mean {np.mean(debt):.0f} vs median {np.median(debt):.0f}")

# ddof - "delta degrees of freedom". NumPy divides by (n - ddof) and
# defaults to ddof=0, which is the POPULATION standard deviation: correct
# when your numbers are the entire group you care about.
#
# If your numbers are a SAMPLE and you are estimating the spread of a
# bigger population, ddof=0 underestimates it. ddof=1 is the fix.
sample = np.array([1, 2, 3, 4])
print(np.std(sample))              # 1.118033988749895  (ddof=0, population)
print(np.std(sample, ddof=1))      # 1.2909944487358056 (ddof=1, sample)
print(np.var(sample, ddof=1))      # 1.6666666666666667

# Worth knowing before you compare notes with anyone: NumPy defaults to
# ddof=0, pandas defaults to ddof=1. Same data, two different answers.
print(np.std(sample), pd.Series(sample).std())

# On a 2-D array, axis says which direction to collapse.
# axis=0 goes DOWN the rows and gives one answer per column;
# axis=1 goes ACROSS the columns and gives one answer per row.
grid = np.arange(12).reshape(3, 4)
print(np.mean(grid))            # 5.5 - everything, as one pool
print(np.mean(grid, axis=0))    # [4. 5. 6. 7.] - one per column
print(np.mean(grid, axis=1))    # [1.5 5.5 9.5] - one per row


# ---------------------------------------------------------------------
# 9. nan, AND WHY nan == nan IS FALSE
# ---------------------------------------------------------------------
# nan means "not a number": the marker NumPy uses for a missing value.
# The rule is that any calculation touching a nan produces a nan, which
# is deliberate - it stops a hole in your data from quietly turning into
# a wrong answer.
print(np.mean(scores))          # nan, because 20 scores are missing
print(f"{np.nanmean(scores):.2f}")   # 450.92 - the nan-skipping version

# There is a nan-skipping twin for most of them: nanmean, nanmedian,
# nanstd, nanvar, nansum, nanmin, nanmax.
print(f"{np.nanmedian(scores):.1f}  {np.nanstd(scores):.2f}")

# Now the bit that surprises everyone:
print(np.nan == np.nan)         # False

# nan is not a value, it is the ABSENCE of one. Two unknowns are not
# known to be equal, so the answer is False. That is by design, and it
# means you can never test for a missing value with ==:
print(scores[scores == np.nan].size)       # 0 - finds nothing, ever

# Use np.isnan(array) instead. It returns a boolean mask.
missing = np.isnan(scores)
print(missing.sum(), "scores are missing")
print(scores[~missing].size, "scores are present")

# A common slip: np.isna does not exist. isna and notna are PANDAS
# methods; NumPy spells it isnan.
try:
    np.isna(scores)
except AttributeError as err:
    print(f"AttributeError: {err}")
# AttributeError: module 'numpy' has no attribute 'isna'
# The pandas equivalents are loans["Score"].isna() and .notna(), and
# unlike np.isnan they also work on text columns.
print(loans["Score"].isna().sum())


# ---------------------------------------------------------------------
# 10. THE POINT
# ---------------------------------------------------------------------
# One dtype per array is what buys you the speed, and it is also what
# causes the surprises: truncating astype, fixed-width text, ints that
# turn into floats the moment a value goes missing.
#
# Two habits will save you most of the pain. Check .dtype and .shape when
# something looks wrong, and use np.shares_memory when you are not sure
# whether you are holding the original data or a copy of it.
