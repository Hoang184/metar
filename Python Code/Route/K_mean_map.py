import pandas as pd
import geopandas
import folium
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

m = folium.Map(location=[53.941, 103.4864], tiles="Stamen Toner", zoom_start=5)
df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\Route\k_mean_final (1).csv')
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
        type_color = "green"
    if k_mean1 == 1 :
        type_color = "blue"
    if k_mean1 == 2 :
        type_color = "orange"
    if k_mean1 == 3 :
        type_color = "pink"
    print(lat1,long1,type_color)
    folium.Marker( location=[lat1, long1], color=type_color , raidus=1).add_to(m)
    m.save('Map.html')
    i = i+1