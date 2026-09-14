# ======================================================================
# ADDITIONAL TASKS - 03.2 Python Flow Control, Functions and File Handling
#
# For students who are progressing well / have finished the standard
# exercises early. These go beyond the core material - attempt after the
# standard exercises in
# '03.2_Python_Flow_Control,_Functions_and_File_Handling_tasks.py' are
# complete.
#
# These tasks come from Module 3 (Data Collections, Flow Control,
# Functions, and Basic Types) and use only open(), loops and if
# statements - no external libraries. They are placed alongside the
# Flow Control / File Handling tasks because every one of them reads a
# file with open() and processes it by hand.
#
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is
# alongside this script before running it.
#
# Solutions: solutions/03.2_Python_Flow_Control,_Functions_and_File_Handling_additional_tasks_solutions.py
# ======================================================================

# ## Additional Task 3.1: Statistics from a file, no libraries (Stretch)
#
# Extends Module 3 exercises - file handling, loops and if, no imports.
#
# File: data/data.txt
#
# 1. Read data/data.txt with open(), and convert its contents to a list
#    of integers.
# 2. Write a function describe(numbers) that returns the count, total,
#    mean, minimum and maximum WITHOUT using sum(), min(), max() or any
#    import - loops and if only.
# 3. Check your answers against the built-in sum()/min()/max() afterwards.

# >>> Your code here

# ## Additional Task 3.2: Fare conditions lookup from raw text (Challenge)
#
# Extends Module 3 exercises - dictionaries built by hand from a file.
#
# File: data/fare_conditions.csv
#
# 1. Without pandas: read data/fare_conditions.csv with open(), skip the
#    header line, and build a dictionary mapping each fare name to its
#    conditions text using split(',').
# 2. Write a function lookup(fare) that returns the conditions, or the
#    string "Unknown fare" if the key is absent.
# 3. Test with 'Promo' and 'Business'.

# >>> Your code here

# ## Additional Task 3.3: Folder audit (Challenge)
#
# Extends Module 3 exercises - os.listdir, dictionaries, file writing.
#
# 1. Use os.listdir('data') to list the data folder, and build a
#    dictionary counting files by extension (split each name on '.' and
#    take the last part).
# 2. Print one line per extension.
# 3. Write the report to folder_report.txt with open() in write mode,
#    one line per extension, and close the file.

# >>> Your code here
