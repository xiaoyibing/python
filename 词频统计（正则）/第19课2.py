'''任务2：分析出两年的报告中共同的前10高频词与不同的前5高频词，
画出饼状图（使用不同的颜色块和颜色文字）'''
import jieba
from pyecharts.charts import Pie
a1={}
a2={}
def open1(name,di):
    with open(name,encoding='utf-8') as f:
        sl = f.readlines()
    for s in sl:
        w1 = jieba.lcut(s, cut_all=True)  # 将ls中的片段切成词
        for w2 in w1:
            if len(w2) == 2:  # 提取2字词语
                di[w2] = di.get(w2, 0) + 1  # 每出现一次.value加一

open1('政府工作报告2021.txt',a1)
open1('政府工作报告2022.txt',a2)
#-------------提取相同元素-------------------------
ls1=[item for item in a1.keys() if item in a2.keys()]
ls2=[]
for i in ls1:
    ls2.append([i,a1[i]+a2[i]])
a3={}
ls2.sort(key=lambda s:s[1],reverse=True)#排序True表示降序False表示升序
for i in range(10):
    a3[ls2[i][0]]=ls2[i][1]#将高频词放入a2的key
#-----------提取2021特殊元素------------
ls3=[item for item in a1.keys() if item not in a2.keys()]
ls4=[]
for i in ls3:
    ls4.append([i,a1[i]])

a4={}
ls4.sort(key=lambda s:s[1],reverse=True)#排序True表示降序False表示升序
for i in range(5):
    a4[ls4[i][0]]=ls4[i][1]#将高频词放入a2的key
#-----------提取2022特殊元素------------

ls5=[item for item in a2.keys() if item not in a1.keys()]
ls6=[]
for i in ls5:
    ls6.append([i,a2[i]])
a5={}
ls6.sort(key=lambda s:s[1],reverse=True)#排序True表示降序False表示升序
for i in range(5):
    a5[ls6[i][0]]=ls6[i][1]#将高频词放入a2的key
#--------------画图----------
list1=list(a3.items())
Pie().add('',list1).render('共同的前10高频词.html')

list2=list(a4.items())
Pie().add('',list2).render('2021.html')

list3=list(a5.items())
Pie().add('',list3).render('2022.html')