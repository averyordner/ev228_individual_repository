import time

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

import fun_imports as fi
import fun_plots as fp

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'ERA5_t2m_1997_2025.nc'
out_path = 'C:\\Users\\avery\\Downloads\\ev228_data\\graphs\\'
# out_fn = '3_era5.png'

tic = time.time()
da = fi.import_era5(file_path=path + fn, var='t2m')
toc = time.time() - tic
print(toc)
da_timemn = da.mean(dim='valid_time')
da_toplot = da_timemn - 273.15

weights = np.cos(np.deg2rad(da_toplot['latitude']))
da_wghtd = da_toplot.weighted(weights)
da_timemn_wghtd = da_wghtd.mean(dim=['latitude', 'longitude'])
ic(da_timemn_wghtd.data)
da_timemn_nowghtd = da_toplot.mean(dim=['latitude', 'longitude'])
ic(da_timemn_nowghtd.data)
# fp.map(da_toplot, out_path=out_path, out_name=out_fn)
