
import jieba as jb
from os import path
import os
import time
import os


stopwords="E:\FishBall\demo\stopword.txt"   # 停用词表

def jiebaClearText(text):

    mywordlist= []
    seg_list=jb.cut(text, cut_all=False)    #jieba分词，默认模式
    liststr = "/".join(seg_list)      #先进行分词操作了，以 / 隔开

    f_stop = open(stopwords, encoding='gbk')      #在这里加编码 utf-8
    try:
        f_stop_text = f_stop.read()
        f_stop_text = f_stop_text.encode('gbk').decode('gbk')#unicode(f_stop_text, 'utf-8')
    finally:
        f_stop.close()

    f_stop_seg_list = f_stop_text.split('\n')       #以\n为分隔的txt停用词表，将每个词保存为list中的元素

    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)

    return ' '.join(mywordlist)

def main(a):
    sourcefiename = a  # 文件夹目录
    files = os.listdir(sourcefiename)  # 得到文件夹下的所有文件名称
    file_path=a       # 待处理文本路径


    for file in files:  # 遍历文件夹

#       print(outfile)
#       print(filepath)

        f = open(file_path+'/'+file, 'r', encoding='utf-8').read()


        k = open(file_path + '/' + file, 'w+', encoding='utf-8')
        k.write(jiebaClearText(f))
        k.close()

# 如果是多级目录，请千万千万 记得 在最后加上 /
