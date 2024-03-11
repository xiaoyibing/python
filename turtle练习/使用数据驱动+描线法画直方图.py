"""使用数据驱动+描线法画直方图"""

#  -----初始化-----
import turtle as t
t.pensize(1)
t.speed(0)
t.hideturtle()
# 数据驱动
num=[[69,15],[292,10],[33,8],[131,10],[61,5],[254,10],[100,15],[80,25]]
x0=-100
y0=-100
X_len=500
Y_len=300

#  ---------主程序--------------
# ----------画坐标轴-------------
t.penup()
t.goto(x0,y0)
t.pendown()
t.forward(X_len)
t.goto(x0,y0)
t.left(90)
t.forward(Y_len)

# ---------画直方图------
t.pencolor('red')
for i in range(len(num)):
    x=x0+50*(i+1)
    t.penup()
    t.goto(x,y0)
    for a in range(num[i][1]):
        t.pendown()
        t.forward(num[i][0])
        x+=1
        t.penup()
        t.goto(x,y0)

