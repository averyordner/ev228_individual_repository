import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

import fun_imports as fi
import fun_plots as fp

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\individual_research\\'
fn = 'data_stream-moda_stepType-avgad.nc'
out_path = 'C:\\Users\\avery\\Downloads\\ev228_data\\graphs\\'
out_fn = '1-surface_runoff.png'

ds= xr.open_dataset(path + fn, engine="netcdf4")

da_runoff = fi.import_era5(file_path=path + fn, var='avg_surfror')
da_timemn = ds.mean(dim='valid_time')
#fp.map(specific_timeslices, out_path=out_path, out_name=out_fn)

da_time = ds['valid_time']
#print(da_time)

specific_timeslices = da_runoff.isel(valid_time=[0, 360, 720, 1020])
#print("\nSpecific timeslices at indices 0, 360, 720, 1020:")
#print(specific_timeslices)

lon = np.linspace(-97, -94)
lat = np.linspace(31, 28)
data = np.random.rand(len(lat), len(lon)) * 100
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAKES, edgecolor='black')
ax.add_feature(cfeature.RIVERS)
mesh = ax.pcolormesh(lon, lat, data, transform=ccrs.PlateCarree(), cmap='viridis')
plt.colorbar(mesh, ax=ax, orientation='vertical', label='Data Value')
city_lons = [-95.3701]
city_lats = [29.7601]
city_names = ['Houston']

for i, city_lon in enumerate(city_lons):
    ax.plot(city_lon, city_lats[i], 'o', color='red', markersize=5, transform=ccrs.PlateCarree())
    ax.text(city_lon + 0.5, city_lats[i] + 0.5, city_names[i], transform=ccrs.PlateCarree(), fontsize=9)

ax.set_extent((-97, -94, 28, 31), crs=ccrs.PlateCarree())
ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
plt.title('Mean Surface Runoff for Houston, Texas and Surrounding Areas')
plt.show()







