# =====================================================================
# EXAMPLE - COLLECTIONS
# =====================================================================
# Four ways to hold more than one value: lists, tuples, dictionaries
# and sets. Which one you reach for depends on what you need to do with
# the data, so each section says what the type is good at.
#
# Nothing here needs any extra packages. Run from the repo root:
#     python examples/py/02_collections.py
# =====================================================================


# ---------------------------------------------------------------------
# 1. LISTS - an ordered run of values you can change
# ---------------------------------------------------------------------
# Square brackets, values separated by commas. A list keeps its order,
# allows duplicates, and can be changed after you make it.
temperatures = [12, 15, 9, 21, 18, 15]
cities = ["Leeds", "Bristol", "Cardiff", "Dundee"]

print(temperatures)
print(len(temperatures))      # len() - how many items are in it

# Counting starts at 0, not 1. The first item is at position 0.
print(cities[0])              # Leeds
print(cities[2])              # Cardiff

# Negative positions count back from the end, so -1 is the last item.
# Use this instead of cities[len(cities) - 1], which says the same thing
# the long way round.
print(cities[-1])             # Dundee
print(cities[-2])             # Cardiff

# Ask for a position that does not exist and you get an error. This is
# what an off-by-one mistake looks like: a four-item list has positions
# 0 to 3, so 4 is one too far.
try:
    print(cities[4])
except IndexError as error:
    print("IndexError:", error)


# ---------------------------------------------------------------------
# 2. SLICING - taking a section out
# ---------------------------------------------------------------------
# list[start:stop] gives you a NEW list from start up to but NOT
# including stop. The stop is exclusive. That trips everyone up once.
print(cities[0:2])            # ['Leeds', 'Bristol'] - positions 0 and 1 only
print(cities[1:3])            # ['Bristol', 'Cardiff']

# The reason it works that way: stop minus start is the number of items
# you get back. cities[1:3] gives 3 - 1 = 2 items. Handy once you see it.

# Leave either end off and Python assumes "from the start" or "to the end".
print(cities[:2])             # first two
print(cities[2:])             # everything from position 2 onwards
print(cities[:])              # a copy of the whole list

# A slice never falls off the end. Going past the last item just stops
# there, which is why slicing is safer than indexing when you are not
# certain how long something is.
print(cities[2:99])           # ['Cardiff', 'Dundee'], no error


# ---------------------------------------------------------------------
# 3. CHANGING A LIST
# ---------------------------------------------------------------------
# .append(item)  - add to the end
# .insert(i, x)  - put x at position i, shuffling the rest along
# .remove(x)     - delete the FIRST item equal to x
# .pop(i)        - remove the item at position i and hand it back
cities.append("Belfast")
print(cities)

cities.insert(0, "Aberdeen")  # goes to the front
print(cities)

cities.remove("Bristol")
print(cities)

dropped = cities.pop(1)       # pop() gives you the item it removed
print(dropped, cities)

# You can also overwrite a position directly.
cities[0] = "Aberdeen City"
print(cities)

# THE APPEND TRAP
# These methods change the list in place and return None. They do not
# hand you a new list. So assigning the result throws your list away.
scores = [10, 20]
scores = scores.append(30)    # looks reasonable, is wrong
print(scores)                 # None - the list is gone

# What happened: .append(30) added 30 to the list and returned None, and
# the = then stored that None in the name "scores".
# The fix is simply not to assign:
scores = [10, 20]
scores.append(30)             # the list is changed where it sits
print(scores)                 # [10, 20, 30]

# The same applies to .sort(), .reverse(), .insert() and .remove().
# If you want a sorted copy while keeping the original, use sorted(),
# which DOES return a new list:
print(sorted(temperatures))   # new sorted list
print(temperatures)           # original, still in its own order


# ---------------------------------------------------------------------
# 4. TUPLES - a list that cannot be changed
# ---------------------------------------------------------------------
# Round brackets instead of square. Everything about reading a tuple
# works exactly like a list: positions, negatives, slicing.
location = (53.8008, -1.5491)         # latitude, longitude of Leeds
print(location[0], location[-1])
print(location[0:1])

# What you cannot do is change it.
try:
    location[0] = 0.0
except TypeError as error:
    print("TypeError:", error)
# What happened: tuples are immutable, meaning fixed once created.
# There is no way to alter one in place, so there is no assignment.

# Why that is useful rather than annoying:
#   - it says "these values belong together and are not going to move",
#     which is exactly right for a coordinate pair or a database row;
#   - nothing elsewhere in your program can quietly modify it;
#   - unlike lists, tuples can be used as dictionary keys (section 5).
#
# Unpacking - pulling a tuple apart into named variables in one line -
# is the thing you will use most often:
latitude, longitude = location
print(f"Latitude {latitude}, longitude {longitude}")

# A one-item tuple needs a trailing comma, otherwise the brackets are
# just brackets around a value. This catches people out:
not_a_tuple = (5)
really_a_tuple = (5,)
print(type(not_a_tuple), type(really_a_tuple))


# ---------------------------------------------------------------------
# 5. DICTIONARIES - looking things up by name
# ---------------------------------------------------------------------
# Curly brackets, written as key: value. Instead of asking "what is at
# position 2", you ask "what is stored under this label". That is the
# right shape whenever your data has names rather than an order.
station = {
    "name": "Leeds",
    "rainfall_mm": 782,
    "coastal": False,
}

print(station["name"])
print(station["rainfall_mm"])

# Ask for a key that is not there and you get a KeyError.
try:
    print(station["altitude"])
except KeyError as error:
    print("KeyError:", error)
# Note the message is just the missing key name, which is terse but
# tells you exactly what you asked for that was not there.

# .get(key) returns None instead of raising, and .get(key, default)
# returns whatever you nominate. Use .get when a key being absent is a
# normal thing rather than a bug; use [] when a missing key means
# something has genuinely gone wrong and you want to hear about it.
print(station.get("altitude"))            # None
print(station.get("altitude", "unknown")) # unknown
print(station.get("name", "unknown"))     # Leeds

# Adding and changing are the same operation: assign to the key.
station["altitude"] = 62         # new key, so it is added
station["rainfall_mm"] = 803     # existing key, so it is replaced
print(station)

# del removes a key entirely.
del station["coastal"]
print(station)

# .pop(key, default) removes and returns, without an error if absent.
removed = station.pop("altitude", None)
print(removed, station)

# Three views onto the contents. They are the normal way to loop over a
# dictionary, and .items() is the one you will use most.
print(list(station.keys()))
print(list(station.values()))
print(list(station.items()))     # each item is a (key, value) tuple

for key, value in station.items():
    print(f"  {key} -> {value}")

# "in" checks KEYS, not values. Worth remembering before you write a
# check that silently never fires.
print("name" in station)         # True
print("Leeds" in station)        # False - that is a value, not a key


# ---------------------------------------------------------------------
# 6. SETS - unordered, and no duplicates allowed
# ---------------------------------------------------------------------
# Curly brackets like a dictionary, but bare values with no colons.
# A set cannot contain the same value twice, which makes it the quickest
# way to answer "what distinct values are in here".
readings = [15, 12, 15, 9, 12, 15, 21]
unique_readings = set(readings)
print(unique_readings)           # duplicates gone

# Sets have no order, so there are no positions and no slicing. Print
# one twice and the values may come out in a different arrangement.
try:
    print(unique_readings[0])
except TypeError as error:
    print("TypeError:", error)
# What happened: indexing means "the item at position 0", and a set has
# no positions. Convert to a list first if you need order.
print(sorted(unique_readings))   # sorted() gives you a list back

# Deduplicating while keeping the original order is a common need.
# set() alone will not do it, so pair it with a loop:
seen = set()
deduped = []
for value in readings:
    if value not in seen:
        deduped.append(value)
        seen.add(value)          # .add() is the set version of .append()
print(deduped)                   # [15, 12, 9, 21] - first appearance order

# Set arithmetic answers "what is in both" and "what is only in one".
monday = {"Leeds", "Bristol", "Cardiff"}
tuesday = {"Cardiff", "Dundee"}
print(monday & tuesday)          # in both
print(monday | tuesday)          # in either
print(monday - tuesday)          # in monday only


# ---------------------------------------------------------------------
# 7. NESTING - collections inside collections
# ---------------------------------------------------------------------
# Real data is rarely one flat row. A list of dictionaries is the shape
# you will meet constantly, because it is what a table looks like: one
# dictionary per row, one key per column.
stations = [
    {"name": "Leeds", "rainfall_mm": 782, "tags": ["inland", "urban"]},
    {"name": "Cardiff", "rainfall_mm": 1152, "tags": ["coastal"]},
    {"name": "Dundee", "rainfall_mm": 699, "tags": ["coastal", "urban"]},
]

# Read it one step at a time, left to right: pick the row, then the key,
# then the position within that value.
print(stations[1])                     # the whole Cardiff dictionary
print(stations[1]["name"])             # Cardiff
print(stations[1]["tags"][0])          # coastal

for row in stations:
    print(f"  {row['name']}: {row['rainfall_mm']} mm")
# Note the single quotes inside the f-string. The f-string itself is in
# double quotes, so the keys use singles to avoid ending it early.

# A dictionary of lists is the other common shape, and it is what a
# spreadsheet looks like read column by column rather than row by row:
by_column = {
    "name": ["Leeds", "Cardiff", "Dundee"],
    "rainfall_mm": [782, 1152, 699],
}
print(by_column["rainfall_mm"][1])     # 1152
# This is very close to how pandas holds a DataFrame internally, which
# is why column access there looks so much like dictionary access.


# ---------------------------------------------------------------------
# 8. THE POINT
# ---------------------------------------------------------------------
# Pick by what the data is, not by habit:
#   list       ordered, changeable, duplicates fine - the default
#   tuple      a fixed group that belongs together, safe to pass around
#   dict       values you look up by name rather than by position
#   set        membership and distinct values, order irrelevant
# Get this choice right and most of the code that follows writes itself.
