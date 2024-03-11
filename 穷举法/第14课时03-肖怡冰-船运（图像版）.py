import random
import turtle as t

t.register_shape('狼.gif')
t1 = t.Turtle()
t1.color("white")
t1.shape('狼.gif')

t.register_shape('羊.gif')
t2 = t.Turtle()
t2.color("white")
t2.shape('羊.gif')

t.register_shape('菜.gif')
t3 = t.Turtle()
t3.color("white")
t3.shape('菜.gif')

t1.goto(-300,300)
t2.goto(-300,100)
t3.goto(-300,-100)


#  任务2:狼羊菜问题（文字版）
# -----------------------------子函数----------------
def move(x,y):
    if x[0] == "狼":
        t1.fd(y*500)
    if x[0] == "羊":
        t2.fd(y*500)
    if x[0] == "菜":
        t3.fd(y*500)
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
            move(x, 1)
        else:
            move(x,-1)



        y.append(x[0])
        del x[0]            # 若满足此条件，则回运（任有不足，这是根据结果反推的，望改进）
    n+=1
def test1():
    global n
    for i in range(len(left)):
        ball.append(left[0])        # 将数据运上船
        del left[0]
        if check1(left) == True:    # 试用判断函数，若这个数据满足则可运过岸
            if n % 2 == 1:
                move(ball, 1)

            else:
                move(ball, -1)

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
t.penup()
t.speed(0)
t.goto(-200,-500)
t.color("#87CEEB",'#87CEEB')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.left(90)
    t.fd(1000)
    t.left(90)
t.end_fill()

n=1
left = ["狼", "羊", "菜"]
ball = []
right = []
test2()

