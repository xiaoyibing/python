#斐波那契数列是一个经典的数学序列，
# 其中每个数字都是前两个数字的和。
# 斐波那契数列的前几个数字是 1, 1, 2, 3, 5, 8, 13, 21, ...以此类推。
def num(n):
    if n==1 or n==2:
        return 1
    else:
        return num(n-1)+num(n-2)

n=int(input("请输入数字："))
j=0
for i in range(1,n+1):
    # print(j)
    # print(num(i))
    j+=num(i)
print(j)