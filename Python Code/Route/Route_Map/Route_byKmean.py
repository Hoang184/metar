import pandas as pd
import datetime
import folium

df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\Route\Book1.csv')
line_numbers = df.shape[0]
date = df['timestamp']

i=0

m = folium.Map(location=[53.941, 103.4864], tiles="Stamen Toner", zoom_start=5)
folium.Circle(
    radius=75000,
    location=[10.81879, 106.651802],
    color="crimson",
    fill=False,
).add_to(m)

folium.Marker(
    location=[10.81879, 106.651802],
    popup="VVTS",
    tooltip='Click me!',
).add_to(m)

while i<194:
    coordinates=[]
    flight_number = df['flight number'].iloc[i]
    cluster = df['k_mean'].iloc[i]
    epoch_time = df['timestamp'].iloc[i]
    date_time = datetime.datetime.fromtimestamp(int(epoch_time)) 
    date = datetime.datetime.strptime(str(date_time), '%Y-%m-%d %H:%M:%S')
    a = date.strftime("%Y-%m-%d")
    print(a,flight_number)
    link = ("C:\\Users\\Admin\\Desktop\\Study\\Đồ án\\Python Code\\Route\\Route_Data\\Extract_new_sort_descending" + "\\" + a + "\\" + flight_number + ".csv" )
    link = str(link)
    print(link)
    print(cluster)
    try:
        df1 = pd.read_csv(r"%s" % (link))
        lat = df1.loc[:, "latitude"].values
        long = df1.loc[:, "longitude"].values
        for lt, lng in zip(lat, long):
            coordinates.append((lt, lng))
            if cluster == 0:
                color = "#1E90FF"
            
            elif cluster == 1:
                color = "#FF7F50"
                
            elif cluster == 2:
                color = "#FF69B4"
                
            elif cluster == 3:
                color = "#32CD32"
            
            folium.PolyLine([coordinates], 
                            color=color, 
                            weight=0.5,).add_to(m)
        m.save("Map_route_cluster.html")
    except:
        print('lỗi')
    i=i+1
