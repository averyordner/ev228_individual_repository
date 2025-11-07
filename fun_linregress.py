import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'KRDU_temp_188708-202508.csv'

df = pd.read_csv(path + fn)

df_yr = df['YEAR']
df_temp = df['metANN']

slope, intercept, r_value, p_value, std_err = linregress(np.squeeze(df_yr), np.squeeze(df_temp))
print(slope, intercept, r_value, p_value, std_err)

plt.scatter(df_yr, df_temp)
plt.plot(df_yr, intercept + slope * df_yr)
plt.xlabel('year')
plt.ylabel('annual temperature in degrees C')
plt.title('Raleigh-Durham Airport (KRDU) Annual Mean Temperature')
plt.show()