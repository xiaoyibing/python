'''任务2：会议迟到缺课统计（实验室课）
已给定前15次课的腾讯会议记录数据文件和当前在学名单，
统计出目前在学名单中同学上课迟到和缺课的情况（统计不少于3次），输出结果为文本文件'''
import openpyxl


ll2 = []
ls2 = []  # 迟到（准确姓名）
aa={}#缺课
bb={}#迟到
def qk(aaa):
    ls = []  # 参会名单（包含不准确姓名）
    ls1 = []  # 迟到
    ll = []  # 实验室名单
    ll1 = []  # 参会姓名（准确姓名）
    #--------------将会议名单导出到ls------------------
    wb = openpyxl.load_workbook(aaa)
    ws = wb['成员参会概况']
    for row in ws.iter_rows(min_row=10, values_only=True):  # 从第10行开始
        a_cell = row[0]  # A列
        b_cell = row[1]  # b列
        ls.append([a_cell, b_cell[14:16], b_cell[17:19]])  # 从14读到16只读分钟
    wb.save(aaa)
    #--------------------判断迟到----------------------
    for i in ls:
        if int(i[1]) >= 45 and int(i[2]) >= 1:
            ls1.append([i[0]])
    # print(ls1)#迟到
    #----------------------将实验室名单导出到ll---------------
    f = open('实验室名单.txt', 'r', encoding='utf-8')
    ff = f.readlines()
    f.close()
    for i in ff:
        i = i.split()
        ll.append(i[0])
    #---------------判断参会名单（真实姓名）-----------------
    for i in ll:
        for j in range(len(ls)):
            if i in ls[j][0]:
                ll1.append(i)
        for j in range(len(ls1)):
            if i in ls1[j][0]:
                ls2.append([i][0])
    #------------------缺课名单（真实姓名）-------------------
    for i in ll:
        if i not in ll1:
            ll2.append(i)
#-----------主程序--------------------------
qk('12课.xlsx')
qk('13课.xlsx')
qk('14课.xlsx')
qk('15课.xlsx')
for i in ll2:
    a=ll2.count(i)
    if i not in aa:
        aa[i]=a
print(aa)
for i in ls2:
    b=ls2.count(i)
    if i not in bb:
        bb[i]=b
print(bb)
# -----------------写入缺课-------------------------------
f1 = open('缺课名单.txt', 'w')
for i in aa:
    f1.write(i + str(aa[i]) + '次'+'\n')
f1.close()
# ---------------------写入迟到-----------------------------
f2 = open('迟到名单.txt', 'w')
for i in bb:
    f2.write(i + str(bb[i]) + '次'+'\n')
f2.close()