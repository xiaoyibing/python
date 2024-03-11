"""对二维列表内各一位列表元素进行排序（升序）"""

ls=[[12,0,8,9,61,21,46],[3,88,-2,90,100],[6,-3,9,12,44,0,50,70,-23,8]]
print(ls)
n=0
# 子函数打包：第x个一维列表进行排序
def num(x):
    global n
    for j in range(len(ls[x])):
        f=j
        for i in range(len(ls[x])-1-j):
            if ls[x][f]>ls[x][i+j+1]:
                f=i+j+1
        if f!=j:
            ls[x][f],ls[x][j]=ls[x][j],ls[x][f]
            n+=1
    return ls[x]   # 输出
# -------主程序--------
ls[0]=num(0)
ls[1]=num(1)
ls[2]=num(2)
print(ls)
print(n)