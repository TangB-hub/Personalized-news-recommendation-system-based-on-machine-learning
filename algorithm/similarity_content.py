import pandas as pd
import math
import os
import pymysql
import sys


def read():
    shuru = sys.argv[1]
    lis = [[] for i in range(1000)]
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toor', db='test',
                       charset='utf8')
    sql = "select * from %s"%(shuru)
    cus1 = conn.cursor()
    cus1.execute(sql)
    for i in range(1000):
        row = cus1.fetchone()
        if not row:
            break
#        print(row)
        lis[i].extend(list(row))

    conn.commit()
    cus1.close()
    conn.close()

    newlist=[x for x in lis if x] #删除空列表[]
#    print(newlist)
    return newlist


def excel_one_line_to_list():
    df = pd.read_excel("E:\FishBall\demo\sinanews.xlsx", usecols=[1,2,3,4,5,6,7],names=None)  # 读取项目名称和行业领域两列，并不要列名
    df_li = df.values.tolist()

    return df_li

def result(a):
    newlist=a

    list_user = []
    for i in range(len(newlist)):
        list_user.append(newlist[i][1])

    list_all = excel_one_line_to_list()

    result_list=[[] for i in range(len(list_user))]


    for i in range(len(list_user)):
        for j in range(len(list_all)):
            if list_user[i] == list_all[j][3]:
                result_list[i] = list_all[j]
    return result_list

def creation(a,path):
    result_list = a
    list_all = excel_one_line_to_list()
    filename = path

    if not os.path.exists(filename):
        os.makedirs(filename)
    #    print(len(list_all))
    for i in range(len(result_list)):
        for j in range(len(list_all)):
            f = open(filename + str(i) + '.txt', 'w+', encoding='utf-8')
            data = result_list[i][4]
            f.write(data)

            g = open(filename + str(j) + '-j'+'.txt', 'w+', encoding='utf-8')
            data = list_all[j][4]
            g.write(data)
