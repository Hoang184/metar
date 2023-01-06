import time
import pandas as pd


df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\score.csv')
line_numbers = df.shape[0]
header = ('timestamp,total_score' +'\n')
file_new = open(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\ATAMP\time_stamp.csv', mode="w")
file_new.write(header)

i = 0
while i<line_numbers:
    date_time = df["date"].iloc[i]
    total_score = df["ceiling"].iloc[i] + df["wind"].iloc[i] + df["precip"].iloc[i] + df["freezing"].iloc[i] + df["phenomena"].iloc[i]
    b = str(time.mktime(time.strptime(date_time, "%Y-%m-%d %H:%M:%S")))
    file_new.write(b + ',' + str(total_score) + '\n')
    file_new.close
    print(b)
    i=i+1