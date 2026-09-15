# =====================================================================
# EXAMPLE - WORKING WITH FILES
# =====================================================================
# Opening files safely, the modes and what each of them does to what is
# already there, reading whole files against reading line by line, and
# writing your own.
#
# This uses data/data.txt, which is already in the repo, and creates a
# few small files of its own. It deletes those again at the end, so it
# leaves nothing behind.
#
# Nothing here needs any extra packages. Run from the repo root:
#     python examples/py/04_files.py
# =====================================================================

import os

# A throwaway file we create, read and delete inside this example.
SCRATCH = "example_scratch.txt"


# ---------------------------------------------------------------------
# 1. OPEN, AND WHY YOU SHOULD ALWAYS USE "with"
# ---------------------------------------------------------------------
# open(path, mode) - opens a file and hands back a file object you read
# from or write to. Every open file holds an operating system resource,
# so it has to be closed again.
#
# The manual way works, but only if nothing goes wrong in between:
handle = open("data/data.txt", "r")
contents = handle.read()
handle.close()                   # miss this and the file stays open
print(repr(contents))            # repr() shows the \n line breaks

# If an error is raised between open and close, the close never happens.
# On Windows that leaves the file locked, and if you were writing, your
# changes may still be sitting in a buffer rather than on disk.
#
# "with" solves it. It closes the file for you when the block ends,
# whether the block finished normally or blew up. Use it every time.
with open("data/data.txt", "r") as f:
    contents = f.read()
# Out here the file is already closed. Nothing to remember.
print(len(contents), "characters read")

# Writing text files across different computers is easier if you say
# which character encoding you mean, rather than letting each machine
# pick its own default:
with open("data/data.txt", "r", encoding="utf-8") as f:
    first_line = f.readline()    # .readline() - just the next line
print(repr(first_line))


# ---------------------------------------------------------------------
# 2. THE MODES
# ---------------------------------------------------------------------
#   "r"  read. The default. Errors if the file is not there.
#   "w"  write. Creates the file, or EMPTIES an existing one instantly.
#   "a"  append. Creates the file, or adds to the end of an existing one.
#   "x"  exclusive create. Creates the file, errors if it already exists.
#
# "w" is the dangerous one. It does not ask, it does not back anything
# up, and it empties the file the moment you open it, even if you then
# write nothing at all. Say that out loud before you point "w" at a file
# whose contents you care about.

with open(SCRATCH, "w", encoding="utf-8") as f:
    f.write("first version\n")

with open(SCRATCH, "r", encoding="utf-8") as f:
    print(repr(f.read()))        # 'first version\n'

# Open the same file with "w" again and the previous contents are gone.
with open(SCRATCH, "w", encoding="utf-8") as f:
    f.write("second version\n")

with open(SCRATCH, "r", encoding="utf-8") as f:
    print(repr(f.read()))        # 'second version\n' - the first is gone

# "a" adds to the end instead, which is what you want for logs and for
# anything you are building up over several runs.
with open(SCRATCH, "a", encoding="utf-8") as f:
    f.write("appended line\n")

with open(SCRATCH, "r", encoding="utf-8") as f:
    print(repr(f.read()))        # both lines present

# "x" refuses to overwrite. Use it when creating a file that must not
# already exist, and let the error tell you when something is wrong.
try:
    with open(SCRATCH, "x", encoding="utf-8") as f:
        f.write("this never runs")
except FileExistsError as error:
    print("FileExistsError:", error)
# What happened: SCRATCH already exists because we made it above, and
# "x" will not touch an existing file. Had this been "w", the file we
# just built would have been wiped without a word.

# Asking to read a file that is not there gives the matching error:
try:
    with open("data/no_such_file.txt", "r", encoding="utf-8") as f:
        f.read()
except FileNotFoundError as error:
    print("FileNotFoundError:", error)
# Nine times out of ten this means you ran the script from the wrong
# folder, not that the file is missing. Relative paths like "data/..."
# are worked out from where you RAN python, not from where the script
# lives. os.getcwd() tells you where that is:
print("Running from:", os.getcwd())


# ---------------------------------------------------------------------
# 3. THREE WAYS TO READ
# ---------------------------------------------------------------------
# .read()        the entire file as one string
# .readlines()   a list of lines, each one still carrying its "\n"
# looping over the file object   one line at a time, nothing else held
with open("data/data.txt", "r", encoding="utf-8") as f:
    whole = f.read()
print(repr(whole))

with open("data/data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)                     # note the \n on the end of each

# Looping is the one to reach for by default. It reads a line, deals
# with it, then forgets it, so a file of any size uses the same small
# amount of memory. .read() on a several-gigabyte file will try to fit
# the lot in memory at once.
with open("data/data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"  line: {repr(line)}")

# .strip() removes whitespace, including the newline, from both ends.
# You almost always want it, because "3\n" is not a number you can add.
with open("data/data.txt", "r", encoding="utf-8") as f:
    numbers = [int(line.strip()) for line in f]
print(numbers, "total", sum(numbers))
# The [... for ... in ...] is a list comprehension: a for loop written
# on one line that collects its results into a list. It says exactly
# what the three-line version does, just more compactly.

# Without the strip you get the TypeError-flavoured complaint about the
# newline. int() is actually tolerant of surrounding whitespace, but
# most conversions are not, and a stray "\n" on the end of a name or a
# postcode will ruin any comparison you make with it later:
print("Leeds\n" == "Leeds")      # False - invisible difference
print("Leeds\n".strip() == "Leeds")


# ---------------------------------------------------------------------
# 4. READING TWICE GIVES YOU NOTHING THE SECOND TIME
# ---------------------------------------------------------------------
# An open file has a position marker, like a bookmark. Reading moves it
# forward. When you reach the end it stays there, so a second read
# starts at the end and finds nothing.
with open("data/data.txt", "r", encoding="utf-8") as f:
    first = f.read()
    second = f.read()            # nothing left to read
print(len(first), "characters first time")
print(len(second), "characters second time")
print(repr(second))              # '' - empty, and no error to warn you

# This is nastier than an error, because the code runs happily and your
# second pass just quietly does nothing. The same thing bites when you
# loop over a file twice:
with open("data/data.txt", "r", encoding="utf-8") as f:
    count_one = sum(1 for _ in f)
    count_two = sum(1 for _ in f)
print(count_one, count_two)      # the second count is 0
# The underscore is a normal variable name, used by convention when you
# do not care about the value and only want to count the turns.

# Two fixes. Either move the bookmark back to the start with .seek(0):
with open("data/data.txt", "r", encoding="utf-8") as f:
    first = f.read()
    f.seek(0)                    # 0 means "back to the beginning"
    second = f.read()
print(len(first), len(second))   # the same now

# Or, better, read it once into a list and use that list as often as
# you like. Reading the disk twice to answer two questions about the
# same small file is wasted work anyway:
with open("data/data.txt", "r", encoding="utf-8") as f:
    values = [int(line.strip()) for line in f]
print(len(values), max(values), min(values))


# ---------------------------------------------------------------------
# 5. WRITING, AND THE MISSING NEWLINE
# ---------------------------------------------------------------------
# .write(text) writes exactly the text you give it and nothing more.
# Unlike print(), it does NOT add a line break. Forget that and your
# whole file ends up on one line.
rows = ["Leeds", "Bristol", "Cardiff"]

with open(SCRATCH, "w", encoding="utf-8") as f:
    for row in rows:
        f.write(row)             # no "\n", so everything runs together

with open(SCRATCH, "r", encoding="utf-8") as f:
    print(repr(f.read()))        # 'LeedsBristolCardiff' - one long line

# Add the newline yourself:
with open(SCRATCH, "w", encoding="utf-8") as f:
    for row in rows:
        f.write(row + "\n")

with open(SCRATCH, "r", encoding="utf-8") as f:
    print(repr(f.read()))        # three separate lines

# .writelines(list) has the same catch, despite the name. It writes the
# items one after another and adds nothing between them, so you still
# have to supply the newlines.
with open(SCRATCH, "w", encoding="utf-8") as f:
    f.writelines(row + "\n" for row in rows)

# "\n".join(list) builds the whole thing as one string first. Note it
# puts newlines BETWEEN items, so there is none after the last one,
# which is the usual convention for a text file that ends tidily:
with open(SCRATCH, "w", encoding="utf-8") as f:
    f.write("\n".join(rows))
with open(SCRATCH, "r", encoding="utf-8") as f:
    print(repr(f.read()))

# You can also point print() at a file, and then it adds the newline for
# you exactly as it does on screen:
with open(SCRATCH, "w", encoding="utf-8") as f:
    for row in rows:
        print(row, file=f)
with open(SCRATCH, "r", encoding="utf-8") as f:
    print(repr(f.read()))


# ---------------------------------------------------------------------
# 6. A FILE WITH A HEADER ROW
# ---------------------------------------------------------------------
# Most data files name their columns on the first line. That line is not
# data, so if you feed it to int() or float() along with the rest you
# get a ValueError on the very first row.
report = "example_scratch_report.csv"

with open(report, "w", encoding="utf-8") as f:
    f.write("city,rainfall_mm\n")     # the header
    f.write("Leeds,782\n")
    f.write("Cardiff,1152\n")
    f.write("Dundee,699\n")

# What goes wrong if you ignore it:
try:
    with open(report, "r", encoding="utf-8") as f:
        for line in f:
            city, mm = line.strip().split(",")
            total = int(mm)                   # fails on the header row
except ValueError as error:
    print("ValueError:", error)
# What happened: the first line splits into "city" and "rainfall_mm",
# and int("rainfall_mm") is not a number.

# The fix: read the header separately before the loop. One .readline()
# takes it off the top, and the loop then sees only real rows.
with open(report, "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")
    print("Columns:", header)

    total = 0
    count = 0
    for line in f:                          # carries on from line 2
        if not line.strip():                # skip any blank lines
            continue
        city, mm = line.strip().split(",")
        # .split(",") - cuts a string at every comma into a list of pieces.
        # Assigning two names at once only works if there are exactly two
        # pieces, so a row with a stray comma in it would raise a
        # ValueError here. That is a reason to use the csv module, or
        # pandas, as soon as your data is anything but simple.
        print(f"  {city}: {mm} mm")
        total += int(mm)
        count += 1

print(f"Mean rainfall across {count} cities: {total / count:.1f} mm")

# For real work, prefer the csv module in the standard library, or
# pandas.read_csv, which is covered in the loading data example. They
# handle quoted fields, commas inside values and awkward encodings that
# hand-rolled splitting gets wrong. Doing it by hand once is still worth
# it, because it shows you what those tools are actually doing.


# ---------------------------------------------------------------------
# 7. CLEANING UP
# ---------------------------------------------------------------------
# os.path.exists(path) - True if there is a file or folder there.
# os.remove(path)      - deletes a file, and errors if it is not there.
# Check before you delete, so a half-finished run does not fail here.
for path in (SCRATCH, report):
    if os.path.exists(path):
        os.remove(path)
        print(f"Removed {path}")

print("Leftover scratch files:", [p for p in (SCRATCH, report) if os.path.exists(p)])


# ---------------------------------------------------------------------
# 8. THE POINT
# ---------------------------------------------------------------------
# Four habits will save you most of the trouble files cause:
#   use "with", so files always close;
#   know that "w" empties the file before you write a thing;
#   read once into a list rather than reading the same file twice;
#   strip the newline off every line before you use the value.
