import pandas as pd


file_new = open("data_new.csv", mode="w")
df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\Metar\Metar_Data\VVTS_2021,01,01,00,00_2021,04,28,00,00.csv')
valid = df.loc[:, "valid"]
metar = df.loc[:, "metar"]
date = pd.to_datetime(valid)

df2 = pd.concat([date, metar], axis=1)
df2.to_csv('data_new.csv', index= False)



