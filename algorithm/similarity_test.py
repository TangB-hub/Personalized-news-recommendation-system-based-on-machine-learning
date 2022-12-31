import math
import os
import pandas as pd
import jieba as jb

dict = "E:\FishBall\demo\词典.txt"
stopwords="E:\FishBall\demo\stopword.txt"   # 停用词表


#关键词统计和词频统计，以列表形式返回
def Count(resfile):
    t = {}
    infile = open(resfile,'r',encoding='utf-8')
    f = infile.readlines()
    count = len(f)
    infile.close()

    s = open(resfile,'r',encoding='utf-8')
    i = 0
    while i < count:
        line = s.readline()
        #去换行符
        line = line.rstrip('\n')
        words = line.split(" ")

        for word in words:
            if word != "" and t.__contains__(word):
                num = t[word]
                t[word] = num+1
            elif word != "":
                t[word] = 1
        i = i+1
#字典按键值降序
    dic = sorted(t.items(),key=lambda t:t[1],reverse=True)
    s.close()
    return(dic)

#合并文档，得出共同文档
def MergeWord(T1,T2):
    MergeWord = []
    duplicateWord = 0
    for ch in range(len(T1)):
        MergeWord.append(T1[ch][0])
    for ch in range(len(T2)):
        if T2[ch][0] in MergeWord:
            duplicateWord = duplicateWord + 1
        else:
            MergeWord.append(T2[ch][0])

    return MergeWord

#得出文档向量
def CalVector(T1,MergeWord):
    TF1 = [0]*len(MergeWord)

    for ch in range(len(T1)):
        TermFrequence = T1[ch][1]
        word = T1[ch][0]
        i = 0
        while i<len(MergeWord):
            if word == MergeWord[i]:
                TF1[i] =TermFrequence
                break
            else:
                i = i + 1
    return(TF1)

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

    return format(float(B)/A,".3f")

def main(a,b):
    test1=a
    test2=b

    T1 = Count(test1)
#    print('文档1的词频统计如下：')
#    print(T1)
#    print()

    T2 = Count(test2)
#    print('文档2的词频统计如下：')
#    print(T2)
#    print()

    #合并两篇文档的关键词
    mergeword = MergeWord(T1,T2)

    #计算文档向量
    v1 = CalVector(T1,mergeword)
#    print('文档1向量化得到的向量如下：')
#    print(v1)
#    print()

    v2 = CalVector(T2,mergeword)
#    print('文档2向量化得到的向量如下：')
#    print(v2)
#    print()

    #计算余弦距离
    result = CalConDis(v1,v2,len(v1))
#    print(test1+'和'+test2+'两篇文章的相似度 = '+result)
    return result
