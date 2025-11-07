import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import fun_imports as fi
import fun_plots as fp 

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'ASM00094998_temp_194804-202508.csv'
out_path = 'C:\\Users\\avery\\Downloads\\ev228_data\\graphs\\'
out_fn = '1-ASM_timeseries.png'

df_data, df_year = fi.import_ghcn(file_path=path + fn, var='metANN')
filter_data = df_data[df_data != 999.9]
filter_year = df_year[df_data != 999.9]

#print(df_data)

mean_var = np.mean(filter_data)
std_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)

print(mean_var, std_var, max_var, min_var)

fp.timeseries(filter_data, in_x=filter_year, out_path=out_path, out_name=out_fn)