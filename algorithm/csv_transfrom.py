import os
import csv
import pandas as pd

def transfrom(filename,path):
     filename=filename
     if not os.path.exists(filename):
          os.makedirs(filename)
     path = path
     df = pd.read_excel('./news/sinanews.xlsx')
     for i in range(len(df)):
          f=open(filename+str(i)+'.txt','w+',encoding='utf-8')
          data = df.content[i]
          f.write(data)

