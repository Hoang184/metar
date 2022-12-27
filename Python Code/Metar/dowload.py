from metar import Metar
from multiprocessing.sharedctypes import Value
import requests
import json
import pandas as pd
import csv

file_new = open("data_new.csv", mode="w")
df1 = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\VVTS_2012,01,01,00,00_2012,04,27,00,00.csv')
valid = df1.loc[:, "valid"]
metar = df1.loc[:, "metar"]
date = pd.to_datetime(valid)

df2 = pd.concat([date, metar], axis=1)
df2.to_csv('data_new.csv', index= False)



