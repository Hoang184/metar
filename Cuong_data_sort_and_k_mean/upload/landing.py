import pandas as pd
import os
from tqdm import tqdm
data = dict() 



file_new = open("data_land_new.csv", mode="w")
header = file_new.writelines("timestamp"+","+"lat" + "," + "long" +","+ "flight number"+'\n')

folder_path = r'D:\Documents\Python Code\K-means\Extract_new_sort_descending'

def listDir(dir): #Lấy địa chỉ folder
    folders = os.listdir(dir)
    for folder in tqdm(folders):
        link1 = os.path.abspath(os.path.join(dir, folder))
        folder_path = r"%s" % (link1)
        def listDir(dir): #Lấy địa chỉ File
            fileNames = os.listdir(dir)
            # file_new = open("data_new.csv", mode="w")
            for fileName in fileNames:
                link2 = os.path.abspath(os.path.join(dir, fileName))
            
                df = pd.read_csv(r"%s" % (link2))      
            
                file_name=os.path.basename(link2)
                file_name2= os.path.splitext(file_name)[0]
                #Sắp xếp Data

            # df = df.sort_values(by=["timestamp"],ascending=True) #Sắp xếp timestamp từ bé đến lớn
            # df.to_csv()
                i = 1
                while i < len(df):
                    time= df.loc[i, "timestamp"]
                    time=float(time)
                    
                    alt= df.loc[i, "altitude"]
                    alt=float(alt)
                
                    if alt >0:
                    
                        alt1=df.loc[i+1, "altitude"]
                        alt1=float(alt1)
                        time1= df.loc[i+1, "timestamp"]
                        time1=float(time1)
                        alt2=df.loc[i, "altitude"]
                        alt2=float(alt2)
                        time2= df.loc[i, "timestamp"]
                        time2=float(time2)
                        time3=df.loc[i-1, "timestamp"]
                        time3=float(time3)
                        if alt2!=alt1:
                            time_land=((-alt2)/(alt2-alt1))*(time2-time1)+time1
                        else:
                            time_land=time3 
                        file_new.write(str(time_land)+","+str( ) + "," + str()+ ","+ str(file_name2)+'\n')
                        break
                    i=i+1
        if __name__ == '__main__':               
            listDir(folder_path)

if __name__ == '__main__':
    listDir(folder_path) 