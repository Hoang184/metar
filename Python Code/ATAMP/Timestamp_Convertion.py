import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\data_new.csv')
line_numbers = df.shape[0]
timestamp = df['valid']

df['timestamp'] = pd(df['valid'])
print(df)
