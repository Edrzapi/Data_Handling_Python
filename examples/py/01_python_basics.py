# =====================================================================
# EXAMPLE - PYTHON BASICS
# =====================================================================
# Variables, the four types you will meet on day one, converting
# between them, printing, and the two division operators.
#
# Nothing here needs any extra packages. Run from the repo root:
#     python examples/py/01_python_basics.py
# =====================================================================


# ---------------------------------------------------------------------
# 1. VARIABLES - a name pointing at a value
# ---------------------------------------------------------------------
# A variable is a label you stick on a value so you can use it later.
# The = sign does NOT mean "is equal to" in maths. It means "put the
# value on the right into the name on the left".
town = "Leeds"
rainfall_mm = 782
average_temp = 9.4
is_coastal = False

print(town)
print(rainfall_mm)

# You never declare a type up front. Python works it out from the value
# you give it, and the same name can later hold something else entirely.
rainfall_mm = 803          # same name, new value, old one is gone
print(rainfall_mm)

# Names should say what the thing IS. Lowercase with underscores is the
# convention every Python codebase follows, so stick to it: readers of
# your code will assume anything else means something special.


# ---------------------------------------------------------------------
# 2. THE FOUR CORE TYPES
# ---------------------------------------------------------------------
# type(value) - tells you what kind of thing a value is.
# Worth knowing early, because most confusing errors in Python come
# down to something being a different type from what you assumed.
print(type(rainfall_mm))      # <class 'int'>   whole number
print(type(average_temp))     # <class 'float'> number with a decimal part
print(type(town))             # <class 'str'>   text, "string" of characters
print(type(is_coastal))       # <class 'bool'>  True or False, nothing else

# Strings can use single or double quotes, as long as you match them.
# Pick one style and stay consistent.
county = 'West Yorkshire'
print(county)

# True and False are capitalised and have no quotes. "True" with quotes
# is just a piece of text that happens to spell a word.
print(type(True))             # <class 'bool'>
print(type("True"))           # <class 'str'>


# ---------------------------------------------------------------------
# 3. CONVERTING BETWEEN TYPES
# ---------------------------------------------------------------------
# int(x), float(x), str(x) - build a new value of that type from x.
# They do not change x itself; they hand you a new value back.
reading = "42"                # text that looks like a number
print(type(reading))          # <class 'str'>

reading_number = int(reading)
print(reading_number + 8)     # 50 - now it really is a number

print(float("3.5") * 2)       # 7.0
print(str(99) + " red balloons")

# int() on a float throws the decimal part away. It does NOT round.
print(int(9.9))               # 9, not 10
print(round(9.9))             # 10 - round() is what you actually wanted

# Converting only works if the text really does describe a number.
# This is the error you will hit when a spreadsheet column has a stray
# word in it. We catch it here so the file keeps running.
try:
    int("nine")
except ValueError as error:
    print("ValueError:", error)
# What happened: int() reads the characters and tries to make a whole
# number out of them. "nine" is a word, not digits, so it gives up.


# ---------------------------------------------------------------------
# 4. PRINTING, AND F-STRINGS
# ---------------------------------------------------------------------
# print() writes to the screen. Give it several values separated by
# commas and it puts a space between each one.
print("Town:", town, "Rainfall:", rainfall_mm)

# An f-string is a string with an f in front of the opening quote. Any
# {name} inside it is replaced by the value of that variable. This is
# the readable way to build a message, and it is what you should use.
print(f"{town} had {rainfall_mm} mm of rain, averaging {average_temp} degrees.")

# You can put a calculation inside the braces too.
print(f"That is {rainfall_mm / 12:.1f} mm a month on average.")
# The :.1f part says "show this as a number with 1 decimal place".
# Formatting like that belongs in the output, not in the stored value:
# keep the full precision in the variable, round only when you display.

# Without an f-string you end up gluing strings together by hand, which
# is harder to read and breaks the moment a value is not text:
print(town + " had " + str(rainfall_mm) + " mm of rain.")


# ---------------------------------------------------------------------
# 5. INPUT FROM THE PERSON RUNNING THE PROGRAM
# ---------------------------------------------------------------------
# input(prompt) - shows the prompt, waits for someone to type a line,
# and hands back what they typed.
#
# The single most important thing about input(): it ALWAYS gives you a
# string. Even if they type 25, you get the text "25", not the number.
# So anything numeric has to go through int() or float() first.
#
# The real call is commented out because this file needs to run
# unattended. Uncomment it and run the file yourself to try it.
#
#     age_text = input("How old are you? ")
#     age = int(age_text)
#     print(f"Next year you will be {age + 1}.")

# Here is the same logic with the typed answer stood in for, so you can
# see the shape of it working:
age_text = "25"               # pretend this came back from input()
print(type(age_text))         # <class 'str'> - text, even though it looks numeric
age = int(age_text)
print(f"Next year you will be {age + 1}.")

# Skip the int() and you get string repetition or an error instead of
# arithmetic, which is the next section.


# ---------------------------------------------------------------------
# 6. THE TWO DIVISIONS
# ---------------------------------------------------------------------
# Python has two division operators and they answer different questions.
print(7 / 2)                  # 3.5  - / is "true" division, always a float
print(7 // 2)                 # 3    - // divides and throws away the remainder
print(7 % 2)                  # 1    - % gives you just the remainder

# / gives a float even when the numbers divide exactly. That surprises
# people: 10 / 5 is 2.0, not 2.
print(10 / 5, type(10 / 5))   # 2.0 <class 'float'>

# Use // when you want a count of whole things, for example working out
# how many full boxes of 12 you can fill:
eggs = 40
print(f"{eggs // 12} full boxes, {eggs % 12} eggs left over.")

# Dividing by zero is an error rather than infinity. Guard against it
# whenever the divisor comes from data you did not choose yourself.
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)


# ---------------------------------------------------------------------
# 7. THE CLASSIC "10" + 5 ERROR
# ---------------------------------------------------------------------
# The + symbol does two different jobs. Between numbers it adds. Between
# strings it joins them end to end.
print(3 + 4)                  # 7
print("3" + "4")              # 34 - joined, not added

# Ask it to do both at once and it refuses, because it cannot tell which
# job you meant.
try:
    print("10" + 5)
except TypeError as error:
    print("TypeError:", error)
# What happened: the left-hand side is text and the right-hand side is a
# number. Python will not silently guess, so it raises a TypeError.
# This is the error you get when a value came from input(), from a file,
# or from a web form, and you forgot to convert it.

# Fix it by deciding which one you meant, then converting:
print(int("10") + 5)          # 15 - treat both as numbers
print("10" + str(5))          # 105 - treat both as text

# A related surprise that is NOT an error, and so is harder to spot:
print("10" * 3)               # 101010 - repeats the text three times
# If you ever see a quantity come out as repeated digits, something
# upstream handed you a string.


# ---------------------------------------------------------------------
# 8. THE POINT
# ---------------------------------------------------------------------
# Almost every early Python error is a type error wearing a disguise.
# When something misbehaves, print type(value) before you do anything
# else. Nine times out of ten the value is a string when you assumed it
# was a number, and one int() call fixes it.
