import pandas as pd
import os
from shapely.geometry import Point
from tqdm import tqdm
from decimal import Decimal

data = dict() 
def circle_line_segment_intersection(circle_center, circle_radius, pt1, pt2, full_line=False, tangent_tol=1e-9):
    """ Find the points at which a circle intersects a line-segment.  This can happen at 0, 1, or 2 points.

    :param circle_center: The (x, y) location of the circle center
    :param circle_radius: The radius of the circle
    :param pt1: The (x, y) location of the first point of the segment
    :param pt2: The (x, y) location of the second point of the segment
    :param full_line: True to find intersections along full line - not just in the segment.  False will just return intersections within the segment.
    :param tangent_tol: Numerical tolerance at which we decide the intersections are close enough to consider it a tangent
    :return Sequence[Tuple[float, float]]: A list of length 0, 1, or 2, where each element is a point at which the circle intercepts a line segment.

    Note: We follow: http://mathworld.wolfram.com/Circle-LineIntersection.html
    """

    (p1x, p1y), (p2x, p2y), (cx, cy) = pt1, pt2, circle_center
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx ** 2 + dy ** 2)**.5
    big_d = x1 * y2 - x2 * y1
    discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2

    if discriminant < 0:  # No intersection between circle and line
        return []
    elif dr!=0:
          # There may be 0, 1, or 2 intersections with the segment
        intersections = [
            (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
             cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]  # This makes sure the order along the segment is correct
        if not full_line:  # If only considering the segment, filter out intersections that do not fall within the segment
            fraction_along_segment = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
            intersections = [pt for pt, frac in zip(intersections, fraction_along_segment) if 0 <= frac <= 1]
        if len(intersections) == 2 and abs(discriminant) <= tangent_tol:  # If line is tangent to circle, return just one point (as both intersections have same location)
            return [intersections[0]]
        else:
            return intersections


coords_1 = (10.817996728,106.651164062)
file_new = open("data15_new.csv", mode="w")
header = file_new.writelines("timestamp"+","+"timeland"+","+"timein"+","+"lat" + "," + "long" +","+"heading_angle"+"," "flight number"+'\n')

folder_path = r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\Route\Route_Data\Extract_new_sort_descending'

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
                # path=link2
                # files=glob.glob(path)
                # for filename in files:
                #     df = pd.read_csv(filename)
                #     df.sort_values('timestamp', inplace=True)
                #     df.to_csv(filename, index=False)
                # print(link2)
                file_name=os.path.basename(link2)
                # print('filename=',file_name)
                file_name2= os.path.splitext(file_name)[0]
                    #Sắp xếp Data
    
                # df = df.sort_values(by=["timestamp"],ascending=True) #Sắp xếp timestamp từ bé đến lớn
                # df.to_csv()
                i = 1
                while i < len(df):
                    time= df.loc[i, "timestamp"]
                    time=float(time)
                    lat = df.loc[i, "latitude"]
                    lat = float(lat)
                    long = df.loc[i, "longitude"] 
                    long = float(long)
                    
                    
                       
                    if  Point(10.817996728,106.651164062).distance(Point(lat,long)) ==0.68313907753:
                        time_new= df.loc[i, "timestamp"]
                        time_new=float(time_new)
                        lat_new = df.loc[i, "latitude"]
                        lat_new = float(lat_new)
                        long_new = df.loc[i, "longitude"] 
                        long_new = float(long_new)
                
                    
                    elif Point(10.817996728,106.651164062).distance(Point(lat,long)) >0.68313907753:
                        time1= df.loc[i-1, "timestamp"]
                        time1=float(time1)
                        lat1 = df.loc[i-1, "latitude"]#Lấy lat ở dòng 1 sau khi sắp xếp lại
                        lat1 = float(lat1)
                        long1 = df.loc[i-1, "longitude"] #Lấy long ở dòng 1 sau khi sắp xếp lại
                        long1 = float(long1)
                        alt1=df.loc[i-1, "altitude"]
                        alt1=float(alt1)
                        
                        time2= df.loc[i, "timestamp"]
                        time2=float(time2)
                        lat2 = df.loc[i, "latitude"]#Lấy lat ở dòng 1 sau khi sắp xếp lại
                        lat2 = float(lat2)
                        long2 = df.loc[i, "longitude"] #Lấy long ở dòng 1 sau khi sắp xếp lại
                        long2 = float(long2)
                        alt2=df.loc[i, "altitude"]
                        alt2=float(alt2)
                        # if Point(lat1,long1).distance(Point(lat2,long2))> 0.68313907753:
                        #     os.remove(link2)
                        # elif (alt2-alt1)>= 10000:
                        #     os.remove(link2)
                        new= circle_line_segment_intersection((10.817996728,106.651164062), 0.68313907753, (lat1,long1), (lat2,long2), full_line=False, tangent_tol=1e-9)
                     
                        lat_new=float(new[0][0])
                        round(Decimal(lat_new), 3)
                        long_new=float(new[0][1])
                        round(Decimal(long_new), 3)
                        if lat2!=lat1:
                            time_new=((lat_new-lat1)/(lat2-lat1))*(time2-time1)+time1
                            round(Decimal(time_new), 3)
                        else:
                            time_new=((long_new-long1)/(long2-long1))*(time2-time1)+time1
                            round(Decimal(time_new), 3)
                        
                        break
                    i =i +1
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
                        heading= df.loc[i, "heading_angle"]
                        heading=float(heading)
                        if alt2>10000:
                            os.remove(link2)
                        if alt2>5000:
                            time_land=time3
                            round(Decimal(time3), 3)
                        elif alt2!=alt1 and alt1 > alt2:
                            
                            time_land=(alt1*time2-alt2*time1)/(alt1-alt2)
                            round(Decimal(time_land), 3)
                            if time_land>time3:
                                time_land=time3
                                round(Decimal(time_land), 3)
                        else:
                            time_land=time3
                            round(Decimal(time_land), 3)
                        
                        break
                    i=i+1
                time_in=time_land-time_new
                # if time_in <=0:
                #     os.remove(link2)
                file_new.write(str(time_new)+","+str(time_land)+","+str(time_in)+","+str(lat_new)+","+str(long_new) + "," +str(heading)+ ","+ str(file_name2) +'\n')
               


                
        if __name__ == '__main__':
            listDir(folder_path)

if __name__ == '__main__':
    listDir(folder_path)
listDir(r'C:\Users\Admin\Desktop\Study\Đồ án\Python Code\Route\Route_Data\Extract_new_sort_descending')
