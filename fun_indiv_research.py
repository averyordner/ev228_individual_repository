import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

import fun_imports as fi

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\individual_research\\'
fn = 'data_stream-moda_stepType-avgad.nc'

ds= xr.open_dataset(path + fn, engine="netcdf4")

da_runoff = fi.import_era5(file_path=path + fn, var='avg_surfror')

da_time = ds['valid_time']
#print(da_time)

specific_timeslices = da_runoff.isel(valid_time=[0, 360, 720, 1020])
#print(specific_timeslices)

def fun_surface_runoff_plot(specific_timeslices):
    lon = specific_timeslices['longitude']
    lat = specific_timeslices['latitude']
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.LAKES, edgecolor='black')
    ax.add_feature(cfeature.RIVERS)
    mesh = ax.pcolormesh(lon, lat, specific_timeslices[0], transform=ccrs.PlateCarree(), cmap='cividis')
    cb = plt.colorbar(mesh, ax=ax, orientation='vertical', label='mean surface runoff rate (kg m⁻² s⁻¹)')
    #plt.imshow(cb)
    #plt.clim(0, 3)
    city_lons = [-95.3701, -96.2572, -95.4611, -95.2009, -95.8245, -95.0938]
    city_lats = [29.7601, 29.9502, 30.1658, 29.6981, 29.7858, 29.5039]
    city_names = ['Houston', 'Bellville', 'The Woodlands', 'Pasadena', 'Katy', 'League City']

    for i, city_lon in enumerate(city_lons):
        ax.plot(city_lon, city_lats[i], 'o', color='red', markersize=5, transform=ccrs.PlateCarree())
        ax.text(city_lon + 0.5, city_lats[i] + 0.5, city_names[i], transform=ccrs.PlateCarree(), fontsize=9)

    ax.set_extent((-96, -94, 29, 31), crs=ccrs.PlateCarree())
    ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    ax.set_xlabel('longitude')
    ax.set_ylabel('latitude')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('Mean Surface Runoff Rate for Houston, Texas and Surrounding Areas (1940)')
    plt.show()

fun_surface_runoff_plot(specific_timeslices)






