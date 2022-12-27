import pandas as pd
from tqdm import tqdm
import glob
import os
folder_path = r'D:\Documents\Python Code\K-means\Extract_new_sort_descending'

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
                    df.sort_values('timestamp',ascending=False, inplace=True)
                    df.to_csv(filename, index=False)
        if __name__ == '__main__':
            listDir(folder_path)

if __name__ == '__main__':
    listDir(folder_path)