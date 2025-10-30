import numpy as np
import pandas as pd
import matplotlib as plt

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'Selected_Station_Observations_Daily_Xtab_202510261705.csv'

df = pd.read_csv(path + fn)
#print(df)

def fun_extract_variable(path, fn, column):
    df = pd.read_csv(path + fn)
    variable_column = df[column]
    print(variable_column)

#fun_extract_variable(path, fn, 'DISCHRG Value')

df.plot()