import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\score.csv')
line_numbers = df.shape[0]
date = df["date"]
ceiling = df["ceiling"]
wind = df["wind"]
precip = df["precip"]
freezing = df["freezing"]
phenomena = df["phenomena"]

# i = 0
# while i < line_numbers:
#     dates = date.iloc[i]
#     ceiling_s = ceiling.iloc[i]
#     wind_s = wind.iloc[i]
#     precip_s = precip.iloc[i]
#     freezing_s = freezing.iloc[i]
#     phenomena_s = phenomena.iloc[i]
#     sum_score = int(ceiling_s) + int(wind_s) + int(precip_s) + int(freezing_s) + int(phenomena_s)
#     # print(sum_score)
#     plt.plot(dates, sum_score, '#FF66FF', label='phenomena')
#     i = i+1

df['total_score']=df["ceiling"] + df["wind"] + df["precip"] + df["freezing"] + df["phenomena"]
df.to_csv('df3.csv',index=False)

df1 = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\df3.csv')
df2 = df1[df1["total_score"] < 10]
total_score = df2["total_score"].array
date = df2["date"].array

plt.plot(date, total_score, '#FF66FF', label='phenomena')

plt.show()