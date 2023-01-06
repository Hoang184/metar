import pandas as pd


df1 = pd.read_csv(r'D:\Documents\Python Code\K-means\k_mean_final.csv')
df2 = pd.read_csv(r'D:\Download\time_stamp.csv')


file_new = open("data16_new.csv", mode="w")
header = file_new.writelines("timestamp"+","+"timein"+","+"lat" + "," + "long" +","+ "flight number"+","+"k_mean"+","+"atm_score"+'\n')

a = 1


while a < len(df1):
    
    timestamp = df1.loc[a,"timestamp"]
    timein= df1.loc[a,"timein"]
    lat= df1.loc[a,"lat"]
    long = df1.loc[a,"long"]
    flight_number= df1.loc[a,"flight number"]
    k_mean=df1.loc[a,"k_mean"]
    

    b=1
    while b < len(df2):
        ts_score = df2.loc[b,"timestamp"]
        abstract =int(timestamp) - int(ts_score)
        # print('abstract=',abstract, 'mintime=',min_time)
        if abstract < 0:
            ts_score = df2.loc[b-1,"total_score"]
            if abs(abstract)<200:
                ts_score = df2.loc[b,"total_score"]
            break
        b=b+1      
    a=a+1
    file_new.write(str(timestamp)+","+str(timein)+","+str(lat)+","+str(long) + ","+ str(flight_number) +","+str(k_mean)+","+str(ts_score)+'\n')
               