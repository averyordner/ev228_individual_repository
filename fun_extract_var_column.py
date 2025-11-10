import numpy as np
import pandas as pd

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'KRDU_temp_188708-202508.csv'

df = pd.read_csv(path + fn)

fall_temp = df['S-O-N']

def fun_extract_column(path, fn, column):
   df = pd.read_csv(path + fn)
   variable_column = df[column]
   print(variable_column)

fun_extract_column(path, fn, 'S-O-N')