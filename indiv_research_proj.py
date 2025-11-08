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

da_runoff = fi.import_era5(file_path=path + fn, var='avg_surfror')
da_time = ds['valid_time']
#print(da_time)

specific_timeslices = da_runoff.isel(valid_time=[0, 360, 720, 1020])
#print("\nSpecific timeslices at indices 0, 360, 720, 1020:")
#print(specific_timeslices)

def fun_cartopy_basemap(specific_timeslices):
    specific_timeslices.plot()
    fig = plt.figure(figsize=(10,10))
    imagery = OSM()
    ax = plt.axes(projection=imagery.crs, )
    ax.set_extent((31, -97, 28, -94))
    # Add the imagery to the map.
    zoom = 12
    ax.add_image(imagery, zoom)
    plt.title('Map of Houston, Texas and Surrounding Areas')
    plt.show()



#fp.map(specific_timeslices, out_path=out_path, out_name=out_fn)





