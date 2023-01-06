import pandas as pd
import numpy as np

df =pd.read_csv(r'D:\Documents\Python Code\K-means\data16_new.csv')

csv_cluster_1 =df[df['k_mean']==0]
csv_cluster_2 =df[df['k_mean']==1]
csv_cluster_3 =df[df['k_mean']==2]
csv_cluster_4 =df[df['k_mean']==3]

csv_cluster_1.to_csv('cluster_1.csv', index=False)
csv_cluster_2.to_csv('cluster_2.csv', index=False)
csv_cluster_3.to_csv('cluster_3.csv', index=False)
csv_cluster_4.to_csv('cluster_4.csv', index=False)
df1= pd.read_csv(r'D:\Documents\Python Code\K-means\cluster_1.csv')

df1['atm_score'] = df1['atm_score'].apply(np.int64)
df1["timein"]=abs(df1["timein"]/(df1["timein"].mean()))
df1 = df1.drop(df1[df1.atm_score >7].index)
df1.to_csv('cluster_1.csv', index=False)

df2= pd.read_csv(r'D:\Documents\Python Code\K-means\cluster_2.csv')
df2['atm_score'] = df2['atm_score'].apply(np.int64)
df2["timein"]=abs((df2["timein"]/(df2["timein"].mean())))
df2 = df2.drop(df2[df2.atm_score >7].index)
df2.to_csv('cluster_2.csv', index=False)

df3= pd.read_csv(r'D:\Documents\Python Code\K-means\cluster_3.csv')
df3['atm_score'] = df3['atm_score'].apply(np.int64)
df3["timein"]=abs((df3["timein"]/(df3["timein"].mean())))
df3 = df3.drop(df3[df3.atm_score >7].index)
df3.to_csv('cluster_3.csv', index=False)

df4= pd.read_csv(r'D:\Documents\Python Code\K-means\cluster_4.csv')
df4['atm_score'] = df4['atm_score'].apply(np.int64)
df4["timein"]=abs((df4["timein"]/(df4["timein"].mean())))
df4 = df4.drop(df4[df4.atm_score >7].index)
df4.to_csv('cluster_4.csv', index=False)