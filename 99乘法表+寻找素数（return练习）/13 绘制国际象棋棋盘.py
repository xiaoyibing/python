 #绘制国际象棋棋盘
import turtle as t
t.hideturtle()
t.penup()
t.goto(-200,-200)
t.pendown()
# 子函数
def draw1(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('black','black')
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.left(90)
    t.end_fill()
# 主程序
t.tracer(0)
for i in range(4):
    t.fd(400)
    t.left(90)
for j in range(4):
    for h in range(4):
        draw1(-200+100*h,-200+j*100)
        draw1(-150+100*h,-150+j*100)
t.tracer(1)
