#升国旗
# 载入库
import turtle as t
import time
t.hideturtle()

t1 = t.Turtle()

# 旗杆
t.tracer(0)
t1.penup()
t1.goto(-100, -500)
t1.pendown()
t1.color('black', 'black')
t1.begin_fill()
for a in range(2):
    t1.forward(10)
    t1.left(90)
    t1.forward(1000)
    t1.left(90)
t1.end_fill()
t.tracer(1)

# 旗面
def num(x, y):
    t.speed(0)
    t.penup()
    t.goto(-300+x, y)
    t.pendown()
    t.color('red', 'red')
    t.begin_fill()
    for a in range(2):
        t.forward(300)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()

    def star(length, angle):
        t.color('yellow', 'yellow')
        t.pendown()
        t.left(angle)
        t.begin_fill()
        for i in range(5):
            t.forward(length)
            t.left(72)
            t.forward(length)
            t.right(144)
        t.end_fill()
        t.right(angle)
        t.penup()
    t.goto(-280+x, 160+y)
    star(24, 0)
    # 小五角星1
    t.goto(-210+x, 175+y)
    star(8, 53)
    # 小五角星2
    t.goto(-190+x, 160+y)
    star(8, 25)
    # 小五角星3
    t.goto(-190+x, 130+y)
    star(8, 0)
    # 小五角星4
    t.goto(-210+x, 110+y)
    star(8, 335)


for i in range(1,100):
    t.tracer(0)
    t.clear()
    num(-100,-300+i*5)
    t.tracer(1)
    time.sleep(0.1)

