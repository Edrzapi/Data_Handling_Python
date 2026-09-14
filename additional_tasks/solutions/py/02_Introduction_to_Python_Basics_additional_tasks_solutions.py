# ======================================================================
# SOLUTIONS - ADDITIONAL TASKS - 02 Introduction to Python Basics
#
# Full runnable solutions for the additional (stretch/challenge) tasks.
# No data files are needed for this module. Run top to bottom.
# ======================================================================

# ----------------------------------------------------------------
# Additional Task 2.1: Seconds to hours, minutes, seconds (Stretch)
# ----------------------------------------------------------------
# In an interactive run this would use input(); a fixed test value is
# used here instead so the script runs unattended and can be verified.
total = 3725  # in an interactive run: total = int(input("Seconds: "))
hours = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60
print(str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s")
assert (hours, minutes, seconds) == (1, 2, 5)

# ----------------------------------------------------------------
# Additional Task 2.2: Reverse a three-digit number (Challenge)
# ----------------------------------------------------------------
n = 471
ones = n % 10  # 1
tens = (n // 10) % 10  # 7
hundreds = n // 100  # 4
reversed_n = ones * 100 + tens * 10 + hundreds
print(reversed_n)  # 174
assert reversed_n == 174

# 500 edge case: reversing 500 "should" give 005, but an int has no
# leading zeros, so the arithmetic answer is 5, not "005".
n2 = 500
ones2 = n2 % 10  # 0
tens2 = (n2 // 10) % 10  # 0
hundreds2 = n2 // 100  # 5
reversed_n2 = ones2 * 100 + tens2 * 10 + hundreds2
print(reversed_n2)  # 5 - leading zeros are not representable in an int
assert reversed_n2 == 5

# ----------------------------------------------------------------
# Additional Task 2.3: Type detective (Stretch)
# ----------------------------------------------------------------
# Prediction: float - "/" always returns float, even for exact division.
print(type(7 / 2))  # <class 'float'>

# Prediction: int - "//" follows the operand types; both operands are int.
print(type(7 // 2))  # <class 'int'>

# Prediction: float - "//" follows the operand types; one operand is float.
print(type(7.0 // 2))  # <class 'float'>

# Prediction: str - "+" on two strings concatenates, it does not add.
print(type("7" + "2"))  # <class 'str'>

# Prediction: int - int("7") casts first, then addition is numeric.
print(type(int("7") + 2))  # <class 'int'>

# Prediction: int - bool is a subclass of int, True behaves as 1.
print(type(True + 1))  # <class 'int'>
print(True + 1)  # 2 - relevant later for booleans inside pandas .sum()

assert type(7 / 2) is float
assert type(7 // 2) is int
assert type(7.0 // 2) is float
assert type("7" + "2") is str
assert type(int("7") + 2) is int
assert type(True + 1) is int
assert (True + 1) == 2

print("All Module 2 additional task checks passed.")
