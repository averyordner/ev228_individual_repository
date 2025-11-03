import ERA5_2mtemp_prac as era
path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'ERA5_t2m_1997_2025.nc'

define_variable = era.fun_grid_variable(path, fn, 'longitude')
#imports a netCDF file using xarray and selects a variable from it

define_descrip = era.descrip_statistics(define_variable, da)
#runs descriptive statistics on the variable you selected

define_plot = era.plot_grid_data(dict_stat)

