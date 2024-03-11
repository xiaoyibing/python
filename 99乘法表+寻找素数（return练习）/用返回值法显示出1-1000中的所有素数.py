# 用返回值函数法显示出1-1000中的所有素数
# 先打包一个判断素数的函数
def a(num):
        for i in range(2, num):
            if num % i == 0:  # 不是素数
                break
        else:
            return True
# 再将1-1000中的数一一判断，若为true则可输出，否者将跳过
for num in range(2, 1001):
    an = a(num)
    if an == True:
        print(f"{num},", end='')