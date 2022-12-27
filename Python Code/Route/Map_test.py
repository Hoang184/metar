from turtle import color
import folium
from ast import With
from cgi import test
import pandas as pd
import os
from tqdm import tqdm

file_new = open("Route.csv", mode="w")
header = file_new.writelines("lat" + "," + "long" + '\n')
m = folium.Map(location=[53.941, 103.4864], tiles="Stamen Toner", zoom_start=5)
coordinates = []

#Đọc Data
folder_path = r'C:\Users\Admin\Desktop\Study\Đồ án\Cuong_data_sort_and_k_mean\upload\Extract_new_sort_descending'
def listDir1(dir): #Lấy địa chỉ folder
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        link1 = os.path.abspath(os.path.join(dir, fileName))
        folder_path = r"%s" % (link1)
        listDir2(folder_path)
def listDir2(dir): #Lấy địa chỉ File
    fileNames = os.listdir(dir)
    for fileName in tqdm(fileNames):
        link2 = os.path.abspath(os.path.join(dir, fileName))
        df = pd.read_csv(r"%s" % (link2))
        lat = df.loc[:, "latitude"].values
        long = df.loc[:, "longitude"].values
        for lt, lng in zip(lat, long):
            coordinates.append((lt, lng))
            # print(coordinates)
            folium.PolyLine([coordinates], color="red", weight=0.5,).add_to(m)
        m.save("Map.html")
        # Ghi data vào file
        
        file_new.write(str(lat) + "," + str(long) + '\n')
    file_new.close
if __name__ == '__main__':
    listDir1(folder_path)