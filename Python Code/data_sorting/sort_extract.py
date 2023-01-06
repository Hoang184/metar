import pandas as pd
from tqdm import tqdm
import glob
import os
from shapely.geometry import Point
# xoa cac chuyen bay qua it du lieu
# filepaths = glob.glob('D:\Documents\Python Code\K-means\Extract_new_sort\..\*.csv')
# # tao duong dan den cac file cua tung chuyen bay
# for filepath in tqdm(filepaths):
#     #xoa cac dong bi lap
#     df = pd.read_csv(filepath)
#     df.drop_duplicates(subset=None, inplace=True)
#     df.to_csv(filepath, index=False)
#     if len(df)<=10:
#         os.remove(filepath)

folder_path = r'D:\Documents\Python Code\K-means\Extract_new_sort_descending'
# xoa cac chuyen bay khong du du lieu
def listDir(dir): 
    folders = os.listdir(dir)
    for folder in tqdm(folders):
        link1 = os.path.abspath(os.path.join(dir, folder))
        folder_path = r"%s" % (link1)
        def listDir(dir):
            fileNames = os.listdir(dir)
           
            for fileName in fileNames:
                link2 = os.path.abspath(os.path.join(dir, fileName))
            
                df = pd.read_csv(r"%s" % (link2))
                path=link2
                files=glob.glob(path)

                for filename in files:
                    df = pd.read_csv(filename)
                #     df.sort_values('timestamp', inplace=True)
                #     df.to_csv(filename, index=False)
                # dfsort = df.sort_values(by=["timestamp"],ascending=True) #Sắp xếp timestamp từ bé đến lớn
                # dfsort.to_csv()
                i = 1
                while i < len(df):
                    # time= dfsort.loc[1, "timestamp"]
                    # time=float(time)
                    # lat = dfsort.loc[1, "latitude"]
                    # lat = float(lat)
                    # long = dfsort.loc[1, "longitude"] 
                    # long = float(long)
                    # lat2 = dfsort.loc[len(dfsort)-1, "latitude"]
                    # lat2 = float(lat2)
                    # long2 = dfsort.loc[len(dfsort)-1, "longitude"] 
                    # long2 = float(long2)
                    # alt = dfsort.loc[len(dfsort)-1, "altitude"] 
                    # alt = float(alt)
                    alt1=df.loc[i, "altitude"]
                    alt1=float(alt1)
                    # xoa cac chuyen bay chi nam trong vung ha canh
                    # if  Point(10.817996728,106.651164062).distance(Point(lat,long)) <=0.68313907753:
                    #    os.remove(link2)
                    # #xoa cac chuyen bay khong vao vung ha canh
                    # elif Point(10.817996728,106.651164062).distance(Point(lat2,long2)) >=0.68313907753:
                    #     os.remove(link2)
                    # #xoa cac chuen bay khong ha canh

                    if alt1> 0:
                        if alt1 >10000:
                            print(alt1,link2)
                        
                        # os.remove (link2)
                    # elif alt2>0:
                    #     alt3=df.loc[i, "altitude"]
                    #     alt3=float(alt3)
                    #     if alt3>1000:
                    #         print(link2)
                    break
                i =i +1
               
                
        if __name__ == '__main__':
            listDir(folder_path)

if __name__ == '__main__':
    listDir(folder_path)
