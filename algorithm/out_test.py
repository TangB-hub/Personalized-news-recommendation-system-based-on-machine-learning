import pandas as pd
import math
import os
import pymysql


def excel_one_line_to_list():
    df = pd.read_excel("E:\FishBall\demo\sinanews.xlsx", usecols=[1,2,3,4,6,7,],names=None)  # 读取项目名称和行业领域两列，并不要列名
    df_li = df.values.tolist()

    return df_li

MergeWord=['财经','彩票','房产','股票','家居','教育','科技','社会','时尚','时政','体育','星座','游戏','娱乐']

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toor', db='test',
                       charset='utf8')
username = []
sql = "select * from new "
cus1 = conn.cursor()
cus1.execute(sql)

lis=[[] for i in range(20)]
for i in range(100):
    row = cus1.fetchone()
    if not row:
        break
#    print(row)
    row_list=list(row)
    lis[i].extend(row_list[0:15])

conn.commit()
cus1.close()
conn.close()
newlist=[x for x in lis if x] #删除空列表[]


new=[[0 for j in range(16)] for i in range(20)]

for i in range(len(newlist)):
    for j in range(len(newlist[i])):
        if j<2:
            new[i][j] = newlist[i][j]
        else :
            if newlist[i][j] == 1:
                new[i][j] = MergeWord[j-2]

for i in range(len(new)):
    for j in range(len(new[i])-1, -1, -1):  # 倒序循环删除空字符串
        if new[i][j] == 0:
            del new[i][j]
new=[x for x in new if x] #删除空列表[]
#print(new)


all_list=excel_one_line_to_list()
new_new=[[0 for j in range(6)] for i in range(54)]

for i in range(len(new)):
    for j in range(len(new[i])-2):
#        print(new[i][j+2])
        for z in range(len(all_list)):

#            print(all_list[z][5])
            if new[i][j+2] == all_list[z][5]:
                new_new[z].extend(all_list[z])

for i in range(len(new_new)):
    for j in range(len(new_new[i])-1, -1, -1):  # 倒序循环删除空字符串
        if new_new[i][j] == 0:
            del new_new[i][j]
new_new=[x for x in new_new if x] #删除空列表[]

change=[]
for i in range(len(new_new)):
    change=new_new[i][3]
    new_new[i][3]=new_new[i][5]
    new_new[i][5]=change

for i in range(len(new_new)):
    print(new_new[i][5])
    print(new_new[i][0:5])
