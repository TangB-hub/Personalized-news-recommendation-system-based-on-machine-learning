import math
import os
import pymysql

MergeWord=['财经','彩票','房产','股票','家居','教育','科技','社会','时尚','时政','体育','星座','游戏','娱乐']


def CalConDis(v1,v2,lengthVector):
    #计算出两个向量的乘积
    B = 0
    i = 0
    while i < lengthVector:
        B = v1[i]*v2[i] + B
        i = i + 1
    #计算两个向量模的乘积
    A = 0
    A1 = 0
    A2 = 0
    i = 0
    while i < lengthVector:
        A1 = A1 + v1[i]*v1[i]
        i = i+1
    i = 0
    while i < lengthVector:
        A2 = A2 + v2[i]*v2[i]
        i = i + 1

    A = math.sqrt(A1)*math.sqrt(A2)
#    print('两个用户的相似度 = '+format(float(B)/A,".3f"))
    return float(B)/A

