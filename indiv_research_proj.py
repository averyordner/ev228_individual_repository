import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

import fun_imports as fi
import fun_plots as fp

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\individual_research\\'
fn = 'data_stream-moda_stepType-avgad.nc'
out_path = 'C:\\Users\\avery\\Downloads\\ev228_data\\graphs\\'
out_fn = '1-surface_runoff.png'

da = fi.import_era5(file_path=path + fn, var='avg_surfror')
da_timemn = da.mean(dim='valid_time')

fp.map(da_timemn, out_path=out_path, out_name=out_fn)