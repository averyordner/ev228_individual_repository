import numpy as np
import pandas as pd

path = 'C:\\Users\\avery\\Downloads\\ev228_data\\'
fn = 'KRDU_temp_188708-202508.csv'

KRDU_temp_data = pd.read_csv(path + fn)

fall_temp = KRDU_temp_data['S-O-N']

def fun_KRDU_column(path, fn, column):
   KRDU_temp_data = pd.read_csv(path + fn)
   variable_column = KRDU_temp_data[column]
   print(variable_column)

fun_KRDU_column(path, fn, 'S-O-N')