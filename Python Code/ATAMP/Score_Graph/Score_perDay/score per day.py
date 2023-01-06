import pandas as pd
from datetime import datetime

df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\score.csv')
line_numbers = df.shape[0]
date = df["date"]
ceiling = df["ceiling"]
wind = df["wind"]
precip = df["precip"]
freezing = df["freezing"]
phenomena = df["phenomena"]

header = ('date,ceiling,wind,precip,freezing,phenomena,total_score' +'\n')
file = open(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\ATAMP\Score_perday.csv', mode="w")
file.write(header)

i = 0
while i<line_numbers:
    date_parsed = df["date"].iloc[i]
    total_score = df["ceiling"].iloc[i] + df["wind"].iloc[i] + df["precip"].iloc[i] + df["freezing"].iloc[i] + df["phenomena"].iloc[i]
    date = datetime.strptime(date_parsed, '%Y-%m-%d %H:%M:%S')
    a = date.strftime("%Y-%m-%d")
    print(a)
    file.write(a +','+ str(df["ceiling"].iloc[i]) +','+ str(df["wind"].iloc[i]) +','+ str(df["precip"].iloc[i]) +','+ str(df["freezing"].iloc[i]) +','+ str(df["phenomena"].iloc[i]) + ',' + str(total_score) + '\n')
    file.close
    i=i+1