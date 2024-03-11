'''任务4：缺作业统计（实验室课）
已给定两次作业文件夹，统计出欠交作业同学的名单及其欠交数量，输出到文本文件中'''
import os
import subprocess
#----------------子函数------------------------------
def ee(aaa,bbb,ccc):

#------------------统计python文件名称---------------------
    # 指定目标目录的路径
    directory_path = aaa
    # 获取目录下所有文件的文件名
    names = os.listdir(directory_path)
    # 打印文件名列表
    # print(names)
    b = {}#未交名单和次数
    ll = []#实验室名单
    ll1 = []#交作业的名单（未统计次数）
#--------------将实验室名单赋予ll---------------------------
    f = open('实验室名单.txt', 'r', encoding='utf-8')
    ff = f.readlines()
    f.close()
    for i in ff:
        i = i.split()
        ll.append(i[0])
    # print(ll)
#----------------统计交作业的人------------------------------
    for i in ll:
        for j in names:
            if i in j:
                ll1.append(i)
#------------------统计未交作业的人（含次数）-------------------
    for i in ll:
        n = ll1.count(i)
        if n < bbb:
            if i not in b:
                b[i] =bbb - n
    print(b)
#--------------写入。txt文本文件-----------------------------------
    f=open('缺作业统计.txt','a')
    f.write(ccc+'\n')
    for i in b:
        f.write(i+'    '+str(b[i])+' 个作业未交'+'\n')
    f.close()
#----------------主程序------------------------------------------------------
f = open('缺作业统计.txt', 'w')
f.write('')
f.close()
ee(r'D:\Python学习\实验室作业\18\4缺作业统计\第15课走迷宫',6,'第15次')
ee(r'D:\Python学习\实验室作业\18\4缺作业统计\第16课扫码枪的应用作业',3,'第16次')
'''aaa:文件所在路径
bbb:这次作业分为几个小作业
ccc：分隔'''
subprocess.run(['start','缺作业统计.txt'],shell=True)#打开文件