# 用双循环法显示出1-1000中的所有素数
for num in range(2, 1001):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            # 不是素数
            # 内循环将终止
            break
    # 对我而言，将else放在第二个for循环的外面是难点，需要加深理解
    else:
        print(f"{num},", end='')
        # end=“ 表示不分行