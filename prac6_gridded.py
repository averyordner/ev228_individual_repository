import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

import fun_imports as fi
import fun_plots as fp

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'era5_10mwind_1980-1989.nc'
out_path = 'C:\\Users\\avery\\Downloads\\ev228_data\\graphs\\'
out_fn = '1-ERA5_10mwind.png'

da = fi.import_era5(file_path=path + fn, var='si10')
da_timemn = da.mean(dim='valid_time')

fp.map(da_timemn, out_path=out_path, out_name=out_fn)