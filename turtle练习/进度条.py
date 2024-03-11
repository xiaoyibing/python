'''编程4：进度条
模拟进度条的动图效果（图形版的进度条），不少于两种明显不同效果（可以在百度中查看各种进度条
动图，参考并做出其中的两种就行）且用一个程序实现，进度条要显示出百分比值，显示不能有明显的
闪烁。
拒收1---明显闪烁，不流畅
拒收2---找不到一种相似的百度动图或其他参考'''
import time
import turtle as t
#--------------方案1-----------------
#设置画笔
def pd(pen,x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
def creat_pen(x,y):
    pen=t.Pen()
    pen.hideturtle()
    pen.speed(0)
    pd(pen,x,y)
    return pen

t.tracer(0)
pen1=creat_pen(-300,0)
pen2=creat_pen(-50,50)
pen3=creat_pen(0,200)
pen4=creat_pen(-20,280)
#调整位置
for i in range(2):
    pen1.fd(600)
    pen1.left(90)
    pen1.fd(20)
    pen1.left(90)
pd(pen1,-300,10)

pen3.circle(100)
pd(pen3,0,220)
pen3.circle(80)
pd(pen3,0,210)


t.tracer(1)

pen1.pensize(20)
pen3.pensize(20)

for i in range(1,101):
    t.tracer(0)
    pen2.clear()
    pen4.clear()
    pen1.fd(6)
    pen2.write(f'{i}%',font=('宋体',30,'normal'))
    pen3.circle(90,3.6)
    pen4.write(f'{i}%',font=('宋体',30,'normal'))
    time.sleep(0.1)
    t.tracer(1)


t.mainloop()

