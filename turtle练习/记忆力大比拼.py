
import turtle as t
import random as r
import time
t1=t.Pen()
t2=t.Pen()
t1.speed(0)
t1.hideturtle()
t2.hideturtle()

#---------数据驱动--------------
n0=[[-300,-300],[100,-300],[-300,50],[100,50],[-300,-300]]
n1=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
n2=["\u2660", "\u2663", "\u2665", "\u2666"]
#  ♠，梅花，  红心，菱形
# ---------子函数---------
def pd(x,y):  # goto函数
    t1.pu()
    t1.goto(x,y)
    t1.pd()
def iif():  # 定义颜色
    if b==0:
        t1.color('red')
    if b==1:
        t1.color('black')
    if b==2:
        t1.color('red')
    if b==3:
        t1.color('black')
def draw1(x,y):# 方框
    t1.color('black')
    pd(x,y)
    for i in range(2):
        t1.fd(210)
        t1.left(90)
        t1.fd(300)
        t1.left(90)
def draw2():
    pd(-200, 370)
    t1.write("记忆大比拼", font=("楷体", 50, 'normal'))

# ------------主程序------------
while(1):
#-------------------第一幕-------------------
    draw2()
    t.tracer(False)# 关闭显示
    for i in range(4):
        draw1(n0[i][0], n0[i][1])
        b = r.randint(0, 3)
        iif()
        pd(n0[i][0] + 5, n0[i][1] + 210)
        t1.write(n2[b], font=('楷体', 30, 'normal'))  #左上角肖图案
        pd(n0[i][0] + 20, n0[i][1] + 60)
        t1.write(n2[b], font=('楷体', 180, 'normal'))# 中心大图案
        a = r.randint(0, 12)
        pd(n0[i][0] + 10, n0[i][1] + 250)
        t1.write(n1[a], font=('楷体', 30, 'normal'))# 左上角小数字
    t.tracer(True)  # 显示图案
    num = 4
    add = -1
    pd(n0[4][0], n0[4][1])
    for i in range(4):  # 第一次倒计时
        num += add
        t2.write(num, font=("楷体", 70, 'normal'))
        time.sleep(1)
        t2.clear()
    t1.clear()
# ---------------第二幕--------------------
    draw2()
    num = 11
    add = -1
    pd(n0[4][0], n0[4][1])
    for i in range(11):# 第二次倒计时
        num += add
        t2.write(num, font=("楷体", 70, 'normal'))
        time.sleep(1)
        t2.clear()






