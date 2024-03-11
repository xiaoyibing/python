"""这是一个美盾表情包，
先有不同大小不同颜色的圆圈，以同一个圆心排列，
再在圆心处加入一个五角星，这样一个正常的美盾就完成了，"""


# 载入turtle
import turtle as t
t.speed(0)
t.pensize(3)
t.hideturtle()

# 打包盾牌圆圈
def a(x,y,z,a):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(z)
    t.begin_fill()
    t.circle(a)
    t.end_fill()
# ---------主程序--------
#先画出盾牌的圈
a(0,-200,'red', 200)
a(0, -150,'white', 150)
a(0,-100,'red',100)
a(0,-50,'blue', 50)
# 画星星
t.penup()
t.goto(-44, 14)
t.pendown()
t.color('white', 'white')
t.begin_fill()
for a in range(5):
    t.forward(34)
    t.left(72)
    t.forward(34)
    t.right(144)
t.end_fill()
t.mainloop()