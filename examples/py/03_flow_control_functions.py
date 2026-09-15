# =====================================================================
# EXAMPLE - FLOW CONTROL AND FUNCTIONS
# =====================================================================
# Making decisions with if, repeating work with for and while, and
# packaging code up into functions you can reuse.
#
# Nothing here needs any extra packages. Run from the repo root:
#     python examples/py/03_flow_control_functions.py
# =====================================================================


# ---------------------------------------------------------------------
# 1. IF, ELIF, ELSE
# ---------------------------------------------------------------------
# An if statement runs a block only when a condition is True. The colon
# ends the condition and the INDENTED lines beneath it are the block.
# Indentation is not decoration in Python: it is how the language knows
# where the block starts and stops. Four spaces is the convention.
temperature = 18

if temperature > 25:
    print("Hot")
elif temperature > 15:
    print("Mild")
elif temperature > 5:
    print("Cool")
else:
    print("Cold")

# elif means "otherwise, if". The branches are tested in order and the
# first True one wins, so the rest are skipped. That is why the order
# matters: if you put "> 5" first, everything warm would match it too.

# The comparison operators:
#   ==  equal to          !=  not equal to
#   <   less than         <=  less than or equal to
#   >   greater than      >=  greater than or equal to
print(5 == 5, 5 != 5, 5 >= 5)

# Combine conditions with and / or, and flip one with not. Python uses
# the English words, not the symbols you may have seen in other languages.
humidity = 80
if temperature > 15 and humidity > 70:
    print("Muggy")

if not (temperature > 25):
    print("Not hot")

# == VERSUS =
# One equals sign assigns a value. Two compare values. Putting one where
# you meant two is a syntax error, which is a small mercy: Python stops
# rather than quietly assigning inside your condition.
# The broken line would be:  if temperature = 18:
# and it raises:
#     SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# We cannot run that here, because a syntax error stops the whole file
# from loading rather than being something you can catch. Try typing it
# into a Python prompt to see the message for yourself.
if temperature == 18:
    print("== compares, = assigns")


# ---------------------------------------------------------------------
# 2. FOR LOOPS - doing something to every item
# ---------------------------------------------------------------------
# "for NAME in COLLECTION:" takes each item in turn, puts it in NAME,
# and runs the indented block once per item.
cities = ["Leeds", "Bristol", "Cardiff"]

for city in cities:
    print(f"  Visiting {city}")

# It works on anything you can step through, including strings, where
# the items are the individual characters:
for letter in "abc":
    print(f"  letter {letter}")

# Loop over a dictionary and you get its KEYS. Use .items() when you
# want the values too.
rainfall = {"Leeds": 782, "Cardiff": 1152}
for name in rainfall:
    print(f"  key {name}")
for name, mm in rainfall.items():
    print(f"  {name}: {mm} mm")

# Accumulating a result is the most common loop job. Start with an empty
# container or a zero, then add to it each time round.
total = 0
for mm in rainfall.values():
    total = total + mm
print("Total rainfall:", total)


# ---------------------------------------------------------------------
# 3. RANGE - looping a set number of times
# ---------------------------------------------------------------------
# range(stop) counts from 0 up to but NOT including stop, the same
# exclusive rule as slicing. range(5) gives five numbers: 0 to 4.
for i in range(5):
    print(f"  i = {i}")

# range(start, stop) and range(start, stop, step) give you more control.
print(list(range(2, 8)))        # [2, 3, 4, 5, 6, 7]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1] - counting down

# range() does not build the list of numbers, it produces them one at a
# time as the loop asks. That is why printing it directly is unhelpful
# and why list() is needed to see inside it.
print(range(5))


# ---------------------------------------------------------------------
# 4. WHILE LOOPS, AND THE LOOP THAT NEVER ENDS
# ---------------------------------------------------------------------
# A while loop repeats for as long as its condition stays True. Use it
# when you do not know in advance how many times you need to go round.
countdown = 3
while countdown > 0:
    print(f"  {countdown}...")
    countdown = countdown - 1      # or countdown -= 1, which is shorthand
print("Go")

# THE INFINITE LOOP TRAP
# If nothing inside the loop ever makes the condition False, it runs
# for ever and you have to stop the program by hand with Ctrl+C.
# The classic version is forgetting the line that changes the counter:
#
#     countdown = 3
#     while countdown > 0:
#         print(countdown)        # countdown never changes, so this
#                                 # prints 3 for ever
#
# Before you write a while loop, ask yourself: which line in here makes
# the condition eventually turn False? If you cannot point at it, the
# loop will not end.
#
# A safety counter is a good habit when the condition depends on data
# you do not control:
attempts = 0
value = 100
while value > 1:
    value = value / 2
    attempts += 1
    if attempts > 50:              # a limit you know is generous
        print("Giving up - something is wrong")
        break
print(f"Halved {attempts} times to reach {value:.4f}")

# If you can say "for each of these" or "this many times", use a for
# loop. It cannot run away from you, because the collection is finite.


# ---------------------------------------------------------------------
# 5. BREAK AND CONTINUE
# ---------------------------------------------------------------------
# break   - leave the loop entirely, right now
# continue - skip the rest of THIS turn and go on to the next item
readings = [12, 15, -1, 21, 99, 18]

# Stop at the first bad reading, because everything after it is suspect:
for reading in readings:
    if reading < 0:
        print("  Bad reading found, stopping")
        break
    print(f"  ok {reading}")

# Or ignore the bad ones and carry on with the rest:
clean_total = 0
for reading in readings:
    if reading < 0 or reading > 50:
        continue                   # skip it, next item please
    clean_total += reading
print("Total of sensible readings:", clean_total)


# ---------------------------------------------------------------------
# 6. ENUMERATE - when you need the position as well as the item
# ---------------------------------------------------------------------
# Sooner or later you want to print "1. Leeds, 2. Bristol". The tempting
# way is to loop over positions and index back into the list:
for i in range(len(cities)):
    print(f"  {i + 1}. {cities[i]}")

# It works, but it is noisier than it needs to be and the cities[i] step
# is an extra chance to get the position wrong.
# enumerate(collection) hands you the position and the item together:
for i, city in enumerate(cities):
    print(f"  {i + 1}. {city}")

# enumerate(collection, start=1) counts from 1, so the +1 disappears too:
for i, city in enumerate(cities, start=1):
    print(f"  {i}. {city}")

# Rule of thumb: if the only thing you do with the number from range() is
# index straight back into the list, use enumerate instead.


# ---------------------------------------------------------------------
# 7. DEFINING FUNCTIONS
# ---------------------------------------------------------------------
# A function is a named piece of code you can run whenever you like.
# "def" names it, the brackets list what it needs, the colon and indent
# hold the body, exactly like a loop.
def to_fahrenheit(celsius):
    """Convert a temperature in Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

# The text in triple quotes just under the def is a docstring. It is
# what help(to_fahrenheit) shows, and it is the cheapest documentation
# you will ever write, so put one on anything non-obvious.

print(to_fahrenheit(0))          # 32.0
print(to_fahrenheit(100))        # 212.0

# celsius is a parameter: a name that only exists inside the function.
# The 0 and 100 above are the arguments: the actual values passed in.

# Write the function once, use it anywhere, and fix a bug in one place.
for c in [0, 20, 37]:
    print(f"  {c}C = {to_fahrenheit(c)}F")


# ---------------------------------------------------------------------
# 8. PARAMETERS AND DEFAULTS
# ---------------------------------------------------------------------
# A parameter can be given a default, used when the caller leaves it out.
# Parameters with defaults have to come after those without.
def describe(city, rainfall_mm, unit="mm"):
    return f"{city} had {rainfall_mm} {unit} of rain"

print(describe("Leeds", 782))                  # unit falls back to "mm"
print(describe("Leeds", 30.8, unit="inches"))  # naming it makes it clear

# Naming arguments at the call site also protects you from getting the
# order wrong, which matters as soon as a function takes more than two
# things:
print(describe(rainfall_mm=1152, city="Cardiff"))

# ONE TO AVOID: never use a list or dictionary as a default value.
# The default is created ONCE, when the function is defined, so every
# call that relies on it shares the same object:
def add_reading_broken(value, readings=[]):
    readings.append(value)
    return readings

print(add_reading_broken(1))     # [1]
print(add_reading_broken(2))     # [1, 2] - the 1 is still there
# Use None as the default and build a fresh list inside instead:
def add_reading(value, readings=None):
    if readings is None:
        readings = []
    readings.append(value)
    return readings

print(add_reading(1))            # [1]
print(add_reading(2))            # [1] - a new list each time


# ---------------------------------------------------------------------
# 9. RETURN VERSUS PRINT
# ---------------------------------------------------------------------
# This catches nearly everyone. print() shows something on screen for a
# human. return hands a value back to the code that called the function,
# so it can be used. They are not alternatives.
def double_and_print(n):
    print(n * 2)                 # shows it, gives nothing back

def double_and_return(n):
    return n * 2                 # hands the value back

shown = double_and_print(5)      # prints 10
print(shown)                     # None - there was nothing to catch

got = double_and_return(5)       # prints nothing
print(got)                       # 10 - and now we can use it
print(got + 1)                   # 11

# Only the second kind is any use inside a bigger calculation:
print(double_and_return(3) + double_and_return(4))

# A function with no return statement returns None. That is fine when
# the function's job IS the side effect, such as writing a file. It is a
# bug when you meant to hand a value back.

# return also stops the function immediately. Anything after it in the
# same branch never runs, which makes early returns a tidy way to deal
# with awkward cases first:
def safe_divide(a, b):
    if b == 0:
        return None              # leave now, nothing else runs
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))


# ---------------------------------------------------------------------
# 10. SCOPE - where a name is visible
# ---------------------------------------------------------------------
# Names created inside a function live only inside that function. That
# is deliberate: it means you can use "total" in fifty functions without
# them interfering with each other.
def compute_total(values):
    running = 0                  # local to this function
    for value in values:
        running += value
    return running

print(compute_total([1, 2, 3]))

try:
    print(running)
except NameError as error:
    print("NameError:", error)
# What happened: "running" stopped existing the moment the function
# finished. If you want the value outside, return it.

# A function CAN read a name defined outside it:
vat_rate = 0.2

def add_vat(amount):
    return amount * (1 + vat_rate)   # reads the outer vat_rate

print(add_vat(100))

# But assigning to that name inside the function creates a separate
# local one instead of changing the outer value:
def try_to_change_rate():
    vat_rate = 0.5               # a brand new local name
    return vat_rate

print(try_to_change_rate())      # 0.5
print(vat_rate)                  # 0.2 - untouched

# Relying on outer names makes a function harder to test and harder to
# move, because it only works in the right surroundings. Pass what the
# function needs in as a parameter and return what it produces.


# ---------------------------------------------------------------------
# 11. THE POINT
# ---------------------------------------------------------------------
# if chooses, for and while repeat, functions give a lump of work a name.
# Once you are writing the same handful of lines a second time, that is
# the signal to turn them into a function: take arguments in, return a
# value out, and keep printing for the part of the program whose job is
# talking to a person.
