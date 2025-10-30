import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'ERA5_t2m_1997_2025.nc'

ds= xr.open_dataset(path + fn, engine="netcdf4")
print(ds)

da = ds['t2m']

da_t2m_timestat = da.mean('valid_time')

da_t2m_timestat.plot();plt.show()

