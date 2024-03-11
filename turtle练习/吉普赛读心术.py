#注：我理解的循环：显示图案后，再点击一下，图案消失（不足：点任何地方都会显示水晶球）

import turtle as t
import time
t.screensize(600,400,'pink')
t1=t.Pen()
t2=t.Pen()
t1.speed(0)
t2.speed(0)
t1.hideturtle()
t2.hideturtle()
# ---------------------------- 数据驱动--------------------
zi=['游戏规则：','请想10-99中任意一个数：','将这个数减去个位，并且在列表中找到结果对应的符号','请把这个符号记在心中，准备好被看穿内心了吗？请点击水晶球！']
ls = [
    # 1            2           3           4           5           6           7           8           9           10
    '\u264B', '\u2648', '\u2649', '\u264F', '\u264E', '\u264A', '\u264D', '\u2653', '\u264C', '\u264F',  # 1

    '\u2653', '\u264F', '\u264B', '\u2648', '\u2649', '\u264F', '\u264E', '\u264C', '\u264E', '\u264A',  # 2

    '\u2648', '\u2649', '\u264F', '\u2653', '\u264B', '\u264E', '\u264C', '\u264A', '\u2652', '\u264B',  # 3

    '\u264D', '\u2650', '\u2652', '\u264B', '\u2649', '\u264C', '\u2648', '\u264F', '\u264A', '\u264F',  # 4

    '\u264A', '\u2649', '\u264B', '\u2652', '\u264C', '\u264F', '\u2653', '\u2648', '\u2653', '\u2649',  # 5

    '\u2649', '\u264D', '\u264F', '\u264C', '\u2648', '\u2650', '\u264E', '\u2651', '\u264E', '\u264C',  # 6

    '\u2652', '\u2649', '\u264C', '\u2648', '\u264B', '\u264A', '\u2650', '\u264F', '\u264E', '\u264D',  # 7

    '\u264E', '\u264C', '\u2648', '\u2649', '\u264F', '\u264B', '\u264F', '\u2653', '\u264D', '\u264E',  # 8

    '\u264C', '\u264F', '\u264E', '\u264D', '\u2648', '\u2649', '\u264B', '\u2652', '\u264F', '\u264C',  # 9

    '\u264D', '\u2650', '\u2652', '\u264B', '\u2649', '\u264C', '\u2648', '\u264F', '\u2653', '\u264A'  # 10
]
# ----------------子函数-----------------------------------
def pd(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
def cir(x,y):# 紫色的水晶球
    pd(x,y)
   # t1.pensize(20)
    t1.color('red','orange')
    t1.begin_fill()
    t1.circle(100)
    t1.end_fill()
    #t.pensize(1)
def g(x,y):# 显示图标
    global k
    k=1
def h(x,y):# 清除图标
    global k
    k=2
def fangge():
    for i in range(11):  # 方格
        t1.seth(0)
        pd(0, 400 - 40 * i)  # 横
        t1.fd(400)
        t1.seth(-90)
        pd(0 + 40 * i, 400)  # 竖
        t1.fd(400)
def zi1():
    for i in range(10):  # 方格内的数字和图画---------竖行
        for j in range(10):  # 横行
            pd(5 + 40 * j, 370 - 40 * i)
            t1.color('red')
            t1.write(ls[i * 10 + j], font=("楷体", 20, 'normal'))  # 图画
            t1.color('black')
            pd(12 + 40 * j, 358 - 40 * i)
            t1.write(i * 10 + j, font=("楷体", 12, 'normal'))  # 数字
    #输入小号字
    for i in range(4):
        t1.color('blue')
        pd(-400,0-i*20)
        t1.write(zi[i],font=("楷体", 15, 'normal'))
    #输入大号字
    t1.color('black')
    pd(-360,320)
    t1.write('吉普赛读心术',font=("楷体", 40, 'normal'))
def draw():# 闪现图案
    t2.penup()
    t2.color('black')
    t2.goto(-260,60)
    t2.pendown()
    t2.write('\u264C',font=("楷体", 100, 'normal'))
# ------------------主程序-------------------------
t.tracer(False)
fangge() #方格
zi1()#字
cir(-300,120)#水晶球
t.tracer(True)
while(1):
    k=0
    t.onscreenclick(g)
    while (1):
        pd(-100, 200)  # 不知道是什么bug，总之加上就能运行了
        if k == 1:
            break
    draw()
    t.onscreenclick(h)
    while(1):#清除图标
        pd(300,90)
        if k==2:
            break
    t2.clear()



