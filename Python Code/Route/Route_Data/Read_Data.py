from multiprocessing.sharedctypes import Value
import pandas as pd

df1 = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\Route\Route_Data\AC7.csv')
lat1 = df1.loc[:, "lat"].values
long1 = df1.loc[:, "long"].values

df2 = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\Route\Route_Data\AC15.csv')
lat2 = df2.loc[:, "lat"].values
long2 = df2.loc[:, "long"].values

