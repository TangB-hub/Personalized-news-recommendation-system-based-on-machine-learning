import similarity_test as simi

import similarity_content as jisuan

import pretreat_test as pre

def change(list,a,b):
    new=list
    a=a
    b=b
    change=[]

    change=new[a]
    new[a]=new[b]
    new[b]=change

dict = "E:\FishBall\demo\词典.txt"

filename='E:/FishBall/demo/similarity/'

newlist=jisuan.read()

result_list = jisuan.result(newlist)

list_all = jisuan.excel_one_line_to_list()

jisuan.creation(result_list,filename)

source = 'E:/FishBall/demo/similarity'
pre.main(source)

for i in range(len(result_list)):
    for j in range(len(list_all)):
        test1=filename+'%s.txt'%str(i)
        test2=filename+'%s-j.txt'%str(j)
        similarity = simi.main(test1,test2)
#        print(test1,test2)
        if (float(similarity) >= 0.05) & (float(similarity)<=0.1):

            print(list_all[j][3])
            print(list_all[j][0:2])

