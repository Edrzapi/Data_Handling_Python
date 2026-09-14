# ======================================================================
# SOLUTIONS - ADDITIONAL TASKS - 03.2 Python Flow Control, Functions and
# File Handling
#
# Data files are loaded from a 'data' folder next to this file: run with
# the working directory set to a folder containing that 'data' folder.
# Run top to bottom.
# ======================================================================

# ----------------------------------------------------------------
# Additional Task 3.1: Statistics from a file, no libraries (Stretch)
# ----------------------------------------------------------------
values = open('data/data.txt').read().split('\n')
numbers = []
for v in values:
    v = v.strip()
    if v:
        numbers.append(int(v))


def describe(numbers):
    count = 0
    total = 0
    smallest = numbers[0]  # initialise from the data, not 0 - the -2 catches
    largest = numbers[0]   # that trap if you start both at 0
    for n in numbers:
        count = count + 1
        total = total + n
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    mean = total / count
    return count, total, mean, smallest, largest


count, total, mean, minimum, maximum = describe(numbers)
print(f"count={count} total={total} mean={mean:.2f} min={minimum} max={maximum}")

# Check against the built-ins
assert count == len(numbers) == 7
assert total == sum(numbers) == 25
assert minimum == min(numbers) == -2
assert maximum == max(numbers) == 11
assert round(mean, 2) == 3.57

# ----------------------------------------------------------------
# Additional Task 3.2: Fare conditions lookup from raw text (Challenge)
# ----------------------------------------------------------------
f = open('data/fare_conditions.csv')
f.readline()  # discard header - file position moves on
fares = {}
for line in f.read().split('\n'):
    line = line.strip()
    if not line:
        continue
    parts = line.split(',', 1)  # keep any commas inside the conditions text intact
    fares[parts[0]] = parts[1]
f.close()


def lookup(fare):
    if fare in fares:
        return fares[fare]
    else:
        return "Unknown fare"


promo_result = lookup('Promo')
business_result = lookup('Business')
print("Promo ->", promo_result)
print("Business ->", business_result)

assert promo_result == "Only valid on specified journey"
assert business_result == "Unknown fare"

# ----------------------------------------------------------------
# Additional Task 3.3: Folder audit (Challenge)
# ----------------------------------------------------------------
import os

counts = {}
for name in os.listdir('data'):
    ext = name.split('.')[-1]
    if ext in counts:
        counts[ext] = counts[ext] + 1
    else:
        counts[ext] = 1

for ext, n in counts.items():
    print(ext, n)

report = open('folder_report.txt', 'w')
for ext, n in counts.items():
    report.write(ext + '\n')
report.close()

# Reopen to prove the file was written correctly
with open('folder_report.txt') as check_file:
    written_lines = [line.strip() for line in check_file if line.strip()]

assert set(written_lines) == set(counts.keys())
assert 'csv' in counts and counts['csv'] == max(counts.values())  # csv is the majority
for expected_ext in ('csv', 'json', 'txt'):
    assert expected_ext in counts, f"expected extension {expected_ext} missing from data folder"

print("All Module 3 additional task checks passed.")
