import pandas as pd
import math
import os
import pymysql
import sys
import one_out_test as out
import user_similarity as simi


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toor', db='test',charset='utf8')
username = []
sql = "select * from new "
cus1 = conn.cursor()
cus1.execute(sql)

lis=[[] for i in range(20)]
for i in range(100):
    row = cus1.fetchone()
    if not row:
        break
#      print(row)
    row_list=list(row)
    lis[i].extend(row_list[0:16])

conn.commit()
cus1.close()
conn.close()
newlist=[x for x in lis if x] #删除空列表[]


if len(newlist) == 1:
    out.one(newlist[0])
else:
    id = sys.argv[1]

    for i in range(len(newlist)):
        if id == newlist[i][0]:
            t = i

    count = 0
    same=[]
    for i in range(len(newlist)):
        similarity = simi.CalConDis(newlist[t][2:16],newlist[i][2:16],len(newlist[i])-2)
        if (similarity >= 0.7) & (similarity <= 0.9999):
#            print(newlist[t][0]+' and '+newlist[i][0]+' similarity is %s'%(similarity))
            same.append(newlist[i][0])
            count += 1

    if count == 0:
        out.one(newlist[t])
    else:
        same_all = newlist[t]

        for i in range(len(same)):
            for j in range(len(newlist)):
                if same[i] == newlist[j][0]:
                    for z in range(len(newlist[j])-2):
                        if (same_all[z+2] == 1) &  (newlist[j][z+2] == 1)  :
                            same_all[z+2] = 1
                        else:
                            same_all[z+2] = 0
        out.one(same_all)
