# ev228_individual_repository
code for EV228 Analysis of Environmental Data class

Documentation:
In order to extract specific columns from a data table in Python, you can import the KRDU_temp_import.py file that includes the necessary function. I used this function in the practical4_function_tests.py in order to extract different variables from various monthly temperature datasets. To do this, I just made sure that I had the correct path, file name, and column for each data set entered in the code.

Generative AI Statement: I did not use generative AI for this assignment. 

# Individual Research Project 

For this project, I am performing exploratory data analysis on ERA5 mean surface runoff rate data for Houston, Texas and surrounding areas (1940-2025 timeslices). I am creating graphs of surface runoff rate data for the years 1940, 1970, 2000, and 2025 in order to see how this variable has changed over time in this area. Houston and surrounding areas have become more urbanized since 1940, so we would expect surface mean runoff rate to increase.

In order to start this exploratory analysis, I imported important files and packages such as:
import matplotlib.pyplot as plt,
import numpy as np,
import xarray as xr,
import cartopy.crs as ccrs,
import fun_imports as fi, and
import fun_plots as fp

Index of Code:
specific_timeslices: pulls out all data corresponding to the years 1940, 1970, 2000, and 2025

Generative AI Statement: I have not used Generative AI on this assignment.

