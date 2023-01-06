import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\ATAMP\Score_perday.csv')
df_sort = df.groupby('date').mean()

df_sort.to_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\ATAMP\Score_byday.csv')

df1 = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\ATAMP\Score_byday.csv')
line_numbers = df1.shape[0]
date = df1["date"].array
ceiling = df1["ceiling"].array
wind = df1["wind"].array
precip = df1["precip"].array
freezing = df1["freezing"].array
phenomena = df1["phenomena"].array
total_score = df1["total_score"].array

plt.bar(date, total_score)
plt.xlabel("")
plt.ylabel("")image.png

plt.show()