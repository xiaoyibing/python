#  任务2:狼羊菜问题（文字版）
# -----------------------------子函数----------------
def check1(x):# 条件判断函数
    if "人" not in x:
        if ("狼"in x and "羊"in x) or ("菜"in x and "羊"in x):#条件：如果人不在，且狼羊或羊菜共存，则不可行
            return False
        else:               #条件：人不在，但无狼羊或羊菜共存，可行
            return True
    else:                   # 如果人在，则全部可成立
        return True
def check2(x,y):            # 回运函数（仅支持含有两个数据的库）
    global n
    if ("狼" in x and "羊" in x) or ("菜" in x and "羊" in x):
        if n%2==1:
            print(f"将“{x[0]}”从河左岸运到河右岸")
        else:
            print(f"将“{x[0]}”从河右岸运到河左岸")

        y.append(x[0])
        del x[0]            # 若满足此条件，则回运（任有不足，这是根据结果反推的，望改进）
    else:
            print("人独自从河右岸到河左岸")

    n+=1
def test1():
    global n
    for i in range(len(left)):
        ball.append(left[0])        # 将数据运上船
        del left[0]
        if check1(left) == True:    # 试用判断函数，若这个数据满足则可运过岸
            if n % 2 == 1:
                print(f"将“{ball[0]}”从河左岸运到河右岸")
            else:
                print(f"将“{ball[0]}”从河右岸运到河左岸")
            right.append(ball[0])
            del ball[0]
            break
        else:                       #这个数据若不满足，将这个数据重新放下
            left.append(ball[0])
            del ball[0]
    n+=1
def test2():# 过程函数
    test1()
    check2(right, left)
    test1()
    check2(right, left)
    check2(left, right)
    check2(right, left)
    test1()
#------------------主函数-----------------
n=1
while(1):
    q=int(input("1.方法一    2.方法二     3.停止运行"))
    if q==1:
        left = ["狼", "羊", "菜"]
        ball = []
        right = []
        test2()
    if q==2:
        left = ["菜", "羊", "狼"]  #通过数据调整，得到不同方案
        ball = []
        right = []
        test2()
    if q==3:
        break
    else:
        print(f"抱歉，暂无方法{q}，请重新输入......")
print(".....正在关闭.....")










