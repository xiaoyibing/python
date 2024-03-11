"""使用数据驱动+子函数画国旗"""
# ------初始化-------
import turtle as t
t.hideturtle()
t.speed(0)
#---------数据-----------
num = [[-280, 160,24,0],[-210, 175,8,53],[-190, 160,8,25],[-190, 130,8,0],[-210, 110,8,335]]
X0=-300
Y0=0
x_len=300
y_len=200
# ------打包----------
def flag():
    t.penup()
    t.goto(X0, Y0)
    t.pendown()
    t.color('red', 'red')
    t.begin_fill()
    for a in range(2):
        t.forward(x_len)
        t.left(90)
        t.forward(y_len)
        t.left(90)
    t.end_fill()
# 五角星打包
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
# --------主程序----------
# ---------画红旗----------
flag()
# --------画星星-----------
for i in range(len(num)):
    t.goto(num[i][0],num[i][1])
    star(num[i][2],num[i][3])