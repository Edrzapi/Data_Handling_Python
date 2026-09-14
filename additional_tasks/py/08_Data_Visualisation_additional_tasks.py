# ======================================================================
# ADDITIONAL TASKS - 08 Data Visualisation
#
# For students who are progressing well / have finished the standard
# exercises early. These go beyond the core material - attempt after the
# standard exercises in '08_Data_Visualisation_tasks.py' are complete.
#
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is
# alongside this script before running it.
#
# Solutions: solutions/08_Data_Visualisation_additional_tasks_solutions.py
# ======================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ## Additional Task 8.1: Iris in one figure (Stretch)
#
# Extends Module 8 exercises - Seaborn pairplot and violin plots.
#
# File: data/IRIS2.csv
#
# 1. Load data/IRIS2.csv and produce a Seaborn pairplot with
#    hue='species'.
# 2. In a markdown cell / comment, answer: which single measurement
#    separates the three species best, and which pair of species
#    overlaps most?
# 3. Back up the claim with a violin plot of that one measurement by
#    species.

# >>> Your code here

# ## Additional Task 8.2: Two histograms, one axis (Stretch)
#
# Extends Module 8 exercises - overlaid histograms, OO style plotting.
#
# File: data/cdc.csv
#
# 1. From data/cdc.csv, overlay histograms of weight for the two gender
#    values on the same Axes, with shared bins and alpha transparency so
#    both remain readable, plus a legend and labelled axes.
# 2. Use the OO style (fig, ax = plt.subplots()).
# 3. In one sentence: why do shared bins matter here?

# >>> Your code here

# ## Additional Task 8.3: The trend behind the noise (Challenge)
#
# Extends Module 8 exercises (and Module 7's resample/rolling) - line
# plots that combine raw and smoothed series.
#
# File: data/renfe_trains_cleaned.csv
#
# 1. Reuse the daily mean price series idea from additional task 7.1
#    (resampled from renfe_trains_cleaned.csv).
# 2. Plot the raw daily series and its 7-day rolling mean on the same
#    Axes, styled so the rolling line stands out (the raw series thin or
#    low-alpha).
# 3. Add a title, axis labels and a legend.
# 4. In a markdown cell / comment: what does the rolling line reveal
#    that the raw one hides?

# >>> Your code here
