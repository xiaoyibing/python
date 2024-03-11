#计算圆周率3合1
q=0
import random
print("正在进入程序.......")
print("已进入。")
while(1):
    q=int(input("你想通过哪种方案计算圆周率：  1.公式法1   2.公式法2   3.蒙特卡罗法   4.退出"))
    if q==1:
        pi = 0
        N = 100
        for i in range(N):
            pi += 1 / pow(16, i) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
        print("公式1计算圆周率为%.10f" % pi)
    if q==2:
        N = pow(10, 6)
        pi = 0
        for i in range(1, N, 2):
            if ((i - 1) / 2) % 2 == 1:
                pi += -1 / i
            else:
                pi += 1 / i
        pi*=4
        print("方案2计算圆周率为%.10f" % pi)
    if q==3:
        n=0
        N=0
        for a in range(1000*1000):
            i = random.random()
            j = random.random()
            if i * i +(j * j)> 1:
                n += 1
            else:
                N += 1
        pi=(N / (n + N))*4
        print("蒙特卡罗法计算圆周率为%.10f" % pi)
    if q==4:
        print("正在退出......")
        break
    else:
        print("输入数字无效，请输入正确数字。")
print("已退出。")








