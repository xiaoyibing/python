"""使用数据驱动+填充法画直方图"""

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
# 打包填充法
def line(x,a,b):
    t.color('red','red')
    t.penup()
    t.goto(x,y0)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
    t.end_fill()


#  ---------主程序--------------
# ----------画坐标轴-------------
t.penup()
t.goto(x0,y0)
t.pendown()
t.forward(X_len)
t.goto(x0,y0)
t.left(90)
t.forward(Y_len)
#  ---------画直方图------
for i in range(len(num)):
    line((i+1)*50+x0,num[i][0],num[i][1])
