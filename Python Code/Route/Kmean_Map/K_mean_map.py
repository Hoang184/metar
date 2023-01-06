import pandas as pd
import geopandas
import folium
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

m = folium.Map(location=[53.941, 103.4864], tiles="Stamen Toner", zoom_start=5)
df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\Route\edit.csv')
line_numbers = df.shape[0]
k_mean = df["k_mean"]
lat = df["lat"]
long = df["long"]

i = 0
while i < line_numbers:
    k_mean1 = k_mean.iloc[i]
    lat1 = lat.iloc[i]
    long1 = long.iloc[i]
    if k_mean1 == 0 :
        type_color = "#32CD32"
    if k_mean1 == 1 :
        type_color = "#1E90FF"
    if k_mean1 == 2 :
        type_color = "#FF7F50"
    if k_mean1 == 3 :
        type_color = "#FF69B4"
    print(lat1,long1,type_color)
    folium.Circle(location=[lat1, long1], 
                radius=200, 
                color=type_color, 
                fill=True, 
                fill_color=type_color).add_to(m)
    m.save('Map.html')
    print(i)
    i = i+1