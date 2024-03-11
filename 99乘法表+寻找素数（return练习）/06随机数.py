#生成10个（1-100）范围的随机整数并显示，求出最大数和最小数
import random
ls=[]
for i in range(10):
    num=random.randint(1,100)
    ls.append(num)
print(ls)
for i in range(1,10):
    if ls[0]<ls[i]:
        ls[0],ls[i]=ls[i],ls[0]
    if ls[9]>ls[i]:
        ls[9],ls[i]=ls[i],ls[9]
print(f'最大数是{ls[0]}')
print(f'最小数是{ls[9]}')

    
