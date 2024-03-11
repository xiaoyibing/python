#表情包
import turtle as t
t.speed(0)
t.hideturtle()
t.pensize(4)
#----------------数据--------------
cir1=[[0,-100,'yellow',100],[-300,-100,'yellow',100],[0,200,'yellow',100],[-300,200,'red',100],[-300,220,'white',80],[-300,240,'red',60],[-300,260,'blue',40]]#黄色圆形

cir2=[[-20,20,90],[60,20,90],[-320,-30,-90],[-80,310,-90],[0,310,-90]]#圆弧
cir3=[[-40,5],[40,5],[-50,305],[30,305],[-310,300],[-280,300]]#黑色
cir4=[[-35,-30,-30,30],[-360,10,30,150],[-240,10,150,30]]#萌樱身
cir5=[[-50,260,0],[60,380,-90],[70,378,-90],[80,376,-90],[90,374,-90]]
md=[[-300,200,'red',100],[-300,220,'white',80],[-300,240,'red',60],[-300,260,'blue',40]]
# 子函数
def pd(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def draw1(x,y,z,a):# 圆圈、半圆
    pd(x,y)
    t.color('black',z)
    t.begin_fill()
    t.circle(a)
    t.end_fill()
def draw2(x,y,a):
    pd(x,y)
    t.seth(a)
    t.color('black','white')
    t.begin_fill()
    t.circle(20,180)
    t.fd(15)
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(15)
    t.end_fill()
    t.seth(0)
def draw3(x,y,a,b):
    pd(x,y)
    t.seth(a)
    t.fd(40)
    t.seth(b)
    t.fd(40)
    t.seth(0)
def draw4(x,y,a):
    pd(x,y)
    t.seth(a)
    t.fd(50)
def star(x,y):
    pd(x,y)
    t.color('black','white')
    t.begin_fill()
    for i in range(5):
        t.fd(25)
        t.left(72)
        t.fd(25)
        t.right(144)
    t.end_fill()
    t.seth(0)
# -------------主程序----------
for i in range(7):# 三个黄色圆圈
    draw1(cir1[i][0],cir1[i][1],cir1[i][2],cir1[i][3])
for i in range(5):#半圆
    draw2(cir2[i][0],cir2[i][1],cir2[i][2])
for i in range(3):# 萌樱身
    draw3(cir4[i][0],cir4[i][1],cir4[i][2],cir4[i][3])

for i in range(6):# 黑色
    draw1(cir3[i][0],cir3[i][1],'black',10)

for i in range(5):
    draw4(cir5[i][0],cir5[i][1],cir5[i][2])
#for i in range(4):
 #   draw1(md[i][0],md[i][1],md[i][2],md[i][3])
star(-330,310)
t.color('black')
pd(-310,290)
t.fd(30)




