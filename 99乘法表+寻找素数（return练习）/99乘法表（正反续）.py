# 正99乘法表
#
i = 1
while i <=9:
    j = 1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        # 输出，end=‘’表示不换行，\t表示对齐
        j +=1
        # 为进入下一口诀作准备
    i+=1
    # 为进入下一行做准备
    print()
    # 表示换行
print("\n")
# 反99乘法表
a = 9
while a>=1:
    # 判断规则与正表相反为大于等于号
    b=1
    while b<=a:
        print(f"{b}*{a}={b*a}\t", end='')
        b+=1
    a-=1
    print()