#任务3：将《论语》按要求提纯，输出提纯后的文本文件
#----------读取文件---------------------
with open('../../../000/论语解读版本.txt', encoding='utf-8') as f:
    lines=f.readlines()
#------------删除注释--------------------
n=0
relines=[]
for line in lines:
    if '【原文】'in line:
        n=1
    if '【注释】' in line:
        n=0
    if n==1 and '【原文】'not in line and'【注释】' not in line:
        relines.append(line)
#-------------删除（）内容--------------
n=0
a=''
for line in relines:
    for zi in line:
        if zi=='(':
            n=1
        if zi==')':
            n=0
        if n==0 and zi!=('(' and ')'):
            a=a+zi
#---------写入文件--------------------
with open('论语简化版.txt','w') as f:
    f.write(a)

