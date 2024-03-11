#任务1：普通时钟
import turtle as t
import time
import datetime as dt
import math
"""步骤：
1. 画表盘---由60个点，12条角度不同的线段，12个数字组成（采用for循环和sin，cos计算位置）
2.创建画笔形状的子函数，后期会用来表示指针
3.设置指针
4.设置文字时间
5.循环更新指针和文字时间"""
# -------------------1.画表盘------------------

t.tracer(0)
pen1=t.Pen()
pen1.penup()
pen1.hideturtle()
pen1.left(60)
for i in range(60):#画60个点
    x=200*math.sin(i/30*math.pi)#math.pi是圆周率，200是半径
    y=200*math.cos(i/30*math.pi)#i/30*math.pi 是i/60*2*math.pi的化简
    pen1.goto(x,y)
    pen1.dot(7)#画点
pen1.pensize(10)#调整画笔粗细，区分点与线段
for i in range(1,13):   #画长的线段，表示时刻，共12个
    x=200*math.sin(i/6*math.pi)
    y=200*math.cos(i/6*math.pi)
    pen1.goto(x,y)
    pen1.pendown()
    pen1.fd(20)
    pen1.penup()
    #写上时刻
    x=250*math.sin(i/6*math.pi)
    y=250*math.cos(i/6*math.pi)#半径改为250，防止字与图重合
    pen1.goto(x-10,y-10)
    pen1.write(i,font=('楷体',20,'normal'))
    pen1.right(30)

t.tracer(1)

#---------------------2.创建画笔子函数---------------
def create_pen(name,lenght,wideth):#lenght是指针长度，wideth是指针粗细
    t.reset()#删除上次的调用，使t可以重复从原点开始（使三个指针重叠）
    t.penup()
    t.hideturtle()
    #开始记录画笔形状
    t.begin_poly()
    t.fd(lenght)
    t.end_poly()
    #登记
    t.register_shape(name,t.get_poly())
    pen=t.Pen()
    pen.shape(name)
    pen.penup()
    pen.shapesize(1,1,wideth)#1表示长宽各1倍
    return pen#返回画笔
t.tracer(0)

#-------------------3.设置指针--------------
pen2=create_pen('zhizhen1',150,3)#秒针
pen4=create_pen('zhizhen2',120,7)#分针
pen5=create_pen('zhizhen3',80,11)#时针
#----------------4.设置文字时间---------------
pen3=t.Pen()
pen3.penup()
pen3.hideturtle()
pen3.goto(-200,-400)
t.tracer(1)
#---------------------5.循环更新指针和文字时间------------
while(1):
    t.tracer(0)
    #更新文字时间
    today = dt.datetime.now()
    a=int(today.strftime('%S'))#秒
    c=int(today.strftime('%M'))#分
    d=int(today.strftime('%H'))#时
    b=today.strftime('%Y.%m.%d %H:%M:%S')#年月日，时分秒
    pen3.clear()
    pen3.write(b,font=('宋体',30,'normal'))
    #旋转到正确角度
    pen2.seth(180-a*6)
    pen4.seth(180-c*6)
    pen5.seth(270-d*6)
    #暂停一秒
    time.sleep(1)
    t.tracer(1)

