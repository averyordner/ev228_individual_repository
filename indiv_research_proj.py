import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs

import fun_imports as fi
import fun_plots as fp

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\individual_research\\'
fn = 'data_stream-moda_stepType-avgad.nc'
out_path = 'C:\\Users\\avery\\Downloads\\ev228_data\\graphs\\'
out_fn = '1-surface_runoff.png'

ds= xr.open_dataset(path + fn, engine="netcdf4")

da = fi.import_era5(file_path=path + fn, var='avg_surfror')
da_time = ds['valid_time']
#print(da_time)

specific_timeslices = da.isel(valid_time=[0, 360, 720, 1020])
print("\nSpecific timeslices at indices 0, 360, 720, 1020:")
print(specific_timeslices)

#fp.map(da_timemn, out_path=out_path, out_name=out_fn)






