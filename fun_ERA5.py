import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'ERA5_t2m_1997_2025.nc'

ds= xr.open_dataset(path + fn, engine="netcdf4")
print(ds)

da = ds['t2m']

#da_t2m_timestat = da.max('valid_time')

#da_t2m_timestat.plot();plt.show()

def fun_grid_variable(path, fn, column):
    ds= xr.open_dataset(path + fn, engine="netcdf4")
    variable_column = ds[column]
    print(variable_column)
    return variable_column 

def descrip_statistics(variable_column, da):
    dict_stat = {
        1: da.mean(variable_column),
        2: da.max(variable_column),
        3: da.min(variable_column),
        4: da.std(variable_column)
    }
    return dict_stat

def plot_grid_data(dict_stat):
    dict_stat.plot()
    plt.title('t2m')
    plt.show()


    
    






    
