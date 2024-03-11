'''任务4：对网站www.icourse163.org/university/view/all.htm中
大学、学院输出显示，并进行统计大学多少所，学院多少所和绘网页型柱状图'''
import re
from pyecharts.charts import Bar
#----------提取文件-----------------
with open('第19课词频统计素材/大学.txt', encoding='utf-8') as f:
    lines=f.readlines()
#------------缩小范围到行---------
ls=''
for line in lines:
    if line[-5:-3]=='大学' or line[-5:-3]=='学院':
        ls+=line
#---------准确查找-----
'''正则函数查找'''
srch=r' alt="(.*?)">'
result=re.findall(srch,ls)
#-------统计个数------
number_daxue=0
number_xueyuan=0

for i in result:
    if i[-2:]=='大学':
        number_daxue+=1
    if i[-2:]=='学院':
        number_xueyuan+=1
#-------输出----------
print(f'学院共有{number_daxue}所')
print(f'大学共有{number_xueyuan}所')
#-------画图----------
list1=['大学','学院']
list2=[number_xueyuan,number_daxue]
Bar().add_xaxis(list1).add_yaxis('数据统计图',list2).render('高校.html')

