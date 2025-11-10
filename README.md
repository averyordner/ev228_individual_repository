# ev228_individual_repository
code for EV228 Analysis of Environmental Data class

Documentation:
In order to extract specific columns from a data table in Python, you can import the KRDU_temp_import.py file that includes the necessary function. I used this function in the practical4_function_tests.py in order to extract different variables from various monthly temperature datasets. To do this, I just made sure that I had the correct path, file name, and column for each data set entered in the code.

Generative AI Statement: I did not use generative AI for this assignment. 

# Individual Research Project 

For this project, I am performing exploratory data analysis on ERA5 mean surface runoff rate data for Houston, Texas and surrounding areas (1940-2025 timeslices). I am creating graphs of surface runoff rate data for the years 1940, 1970, 2000, and 2025 in order to see how this variable has changed over time in this area. Houston and surrounding areas have become more urbanized since 1940, so we would expect surface mean runoff rate to increase.

Steps for Important Workflows:
1. In order to start this exploratory analysis, I imported important files and packages such as:
import matplotlib.pyplot as plt,
import numpy as np,
import xarray as xr,
import cartopy.crs as ccrs,
import cartopy.feature as cfeature,
import fun_imports as fi, and
import fun_plots as fp
2. I then specified my file path and file name
3. I created my dataset by using xr.open_dataset(path + fn, engine="netcdf4")
4. I created the necessary data arrays (described in index)
5. I then created a function for extracting time slices for my data (described in index)
6. Finally, I used cartopy functions to create a graph of my data

Index of Code:

da_runoff: the data array that imports the mean surface runoff rate data 

da_time: data array that extracts the 'valid_time' values from the dataset, so I could print and read them

specific_timeslices: pulls out all data corresponding to the years 1940, 1970, 2000, and 2025

lon: pulls the longitude values from specific_timeslices

lat: pulls the latitude values from specific_timeslices

mesh: includes the pcolormesh cartopy step; all of the map inputs

city_lons: longitudes of the cities I chose

city_lats: latitudes of the cities I chose

fun_surface_runoff_plots: the function I made for creating a cartopy plot with gridded data


Generative AI Statement: I used generative AI to help me with my cartopy code because it was giving me a lot of trouble. Websites were not including all of the steps, and generative AI helped me to find out what extra components I needed. I also used generative AI for the city coordinates.

