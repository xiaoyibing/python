#两个列表ls1=[12,40,10,9,8,-1,21,-6]，ls2=[12,7,10,9,88,-1,21,-6,10]，
#找出两个列表中不同的数据（ls1有而ls2没有是哪些，ls2有而ls1没有是哪些）和相同的数据
ls1=[12,40,10,9,8,-1,21,-6]
ls2=[12,7,10,9,88,-1,21,-6,10]
ls3=[]
ls4=[]
ls5=[]
for i in ls1:
    for j in ls2:
        if i==j and i not in ls3:
            ls3.append(i)
        if i not in ls2  and i not in ls4:
            ls4.append(i)
        if j not in ls1 and j not in ls5:
            ls5.append(j)            
print(f'相同数据为{ls3}')
print(f'{ls4}ls1有而ls2没有')
print(f'{ls5}ls2有而ls1没有')
