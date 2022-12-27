import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from kneed import DataGenerator, KneeLocator
from pathlib import Path  




df = pd.read_csv(r'C:\Users\Admin\Desktop\Study\Đồ án\data14_new (1).csv')
lat = df.loc[:, "lat"].values
lat = lat.tolist()
long = df.loc[:, "long"].values
long = long.tolist()


data = {'x':long,
        'y': lat
        
       }

df1 = pd.DataFrame(data, columns=['x', 'y'])
df1.head()
plt.scatter(df1.x,df1['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()


distortions = []
K = range(1,10)
for k in K:
    km = KMeans(n_clusters=k)
    km.fit(df[['long','lat']])
    distortions.append(km.inertia_)
plt.xlabel('K')
plt.ylabel('distortions')
plt.plot(K,distortions)
plt.show()    

kl = KneeLocator(range(1, 10), distortions,K, curve="convex", direction="decreasing")
print(kl.elbow)
kmeans = KMeans(n_clusters=4).fit(df[['long','lat']])
# print(kmeans.cluster_centers_)
centroids = kmeans.cluster_centers_
labels = kmeans.predict(df[['long','lat']])
print(centroids)
plt.scatter(df['long'], df['lat'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()
centroid_labels = [centroids[i] for i in labels]
df['k_mean']=kmeans.labels_
filepath = Path('D:\Documents\Python Code\K-means\k_mean_final_k=4.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  