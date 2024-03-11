# 抢10免单
import turtle as t
import time
def g(x,y):
    global k   # global将k带出def函数
    k=False   # 改变k的值，使程序暂停

def creat_pen(x,y,color):
    pen=t.Pen()
    pen.hideturtle()
    pen.penup()
    pen.goto(x,y)
    pen.pencolor(color)
    return pen

t1=creat_pen(-100,100,'blue')
t2=creat_pen(40,-100,'black')

#-------标题--------

t1.write("抢10免单！",font=('楷体',50,'normal'))
#--------数值--------
num=0   # 初始值
k=True
t.onscreenclick(g)  # 使g一直循环运行
while(k):
    t2.clear()
    num+=1
    if num==11:
        num=0
    t2.write(num,font=('楷体',100,'normal'))
    time.sleep(0.01)

t.mainloop()

