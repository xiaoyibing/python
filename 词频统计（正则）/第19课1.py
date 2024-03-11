'''任务1：分别统计出《政府工作报告2021》《政府工作报告2022》
中前20个两字高频词并画出柱状图，统计出“教育”的词频'''
import jieba
from pyecharts.charts import Bar
a1={}
a2={}
#打开文件放入sl
with open('政府工作报告2021.txt',encoding='utf-8')as f:
    sl=f.readlines()

for s in sl:
    w1=jieba.lcut(s,cut_all=True)  #将ls中的片段切成词
    for w2 in w1:
        if len(w2)==2:     #提取2字词语
            a1[w2]=a1.get(w2,0)+1  #每出现一次.value加一
ls=list(a1.items())
ls.sort(key=lambda s:s[1],reverse=True)#排序True表示降序False表示升序
for i in range(20):
    print(f'第{i+1}个高频词为：{ls[i][0]}   出现次数：{ls[i][1]}次；')
    a2[ls[i][0]]=ls[i][1]#将高频词放入a2的key
# 将字典中的key,value分别放入list1,list2
list1=list(a2.keys())
list2=list(a2.values())
# 绘制直方图,list1作为x轴,list2作为y轴，标题为'统计图.html'
Bar().add_xaxis(list1).add_yaxis('数据统计图',list2).render('政府工作报告2021.html')
#打开文件放入sl
a3={}
a4={}
with open('政府工作报告2022.txt',encoding='utf-8')as f:
    sl2=f.readlines()

for s in sl2:
    w3=jieba.lcut(s,cut_all=True)  #将ls中的片段切成词
    for w4 in w3:
        if len(w4)==2:     #提取2字词语
            a3[w4]=a3.get(w4,0)+1  #每出现一次.value加一
ls2=list(a3.items())
ls2.sort(key=lambda s:s[1],reverse=True)#排序True表示降序False表示升序
for i in range(20):
    print(f'第{i+1}个高频词为：{ls2[i][0]}   出现次数：{ls2[i][1]}次；')
    a4[ls2[i][0]]=ls2[i][1]#将高频词放入a2的key
# 将字典中的key,value分别放入list1,list2
list3=list(a4.keys())
list4=list(a4.values())
# 绘制直方图,list1作为x轴,list2作为y轴，标题为'统计图.html'
Bar().add_xaxis(list3).add_yaxis('数据统计图',list4).render('政府工作报告2022.html')