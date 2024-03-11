#排序
#
n=[3,789,-98,0,-46,235,67,25]
def num():
    a=0
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            if n[i]>n[j]:
                n[i],n[j]=n[j],n[i]
                a+=1
    print(n)
    print(f"普通型选择排序的次数为{a}")
num()

# 改进型选择排序
n1=[3,789,-98,0,-46,235,67,25]
def num():
    a=0
    for i in range(len(n1)-1):
        f=i
        for j in range(i+1,len(n1)):
            if n1[f]>n1[j]:
                f=j
        n1[f],n1[i]=n1[i],n1[f]
        a+=1
    print(n1)
    print(f"改进型选择排序的次数为{a}")
num()

# 最优型选择排序
n2=[3,789,-98,0,-46,235,67,25]
def num():
    a=0
    for i in range(len(n2)-1):
        f=i
        for j in range(i+1,len(n2)):
            if n2[f]>n2[j]:
                f=j
        if f!=i:
            n2[f],n2[i]=n2[i],n2[f]
            a+=1
    print(n2)
    print(f"最优型选择排序的次数为{a}")
num()

# 冒泡排序
n3=[3,789,-98,0,-46,235,67,25]
def num():
    a=0
    for i in range(len(n3)-1):
        for j in range(len(n3)-1):
            if n3[j]>n3[j+1]:
                n3[j],n3[j+1]=n3[j+1],n3[j]
                a+=1
    print(n3)
    print(f"冒泡排序的次数为{a}")
num()
    
    
