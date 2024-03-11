import turtle as t
t.hideturtle()
t.speed(0)
# 建造数据库（数据不可更改）  数据驱动

tri1 = [[-300, 150], [-50, -50],[-125, -125]]
tri2 = [[-50, -50], [-30, -125], [-85, -85]]
tri3=[[-300, 150],[100,50], [0,0]]
line = [[0,0],[-30,-125],[75,25],[200,0],[50, -5],[250, -30],[10,-80],[100,-150],[-80,-125],[120,-200]]


# 打包三角形
def draw_tri(x1, x2, y1,y2,z1,z2):
    t.pensize(5)
    t.color('black', 'blue')
    t.begin_fill()
    t.penup()
    t.goto(x1,x2)
    t.pendown()
    t.goto(y1,y2)
    t.goto(z1,z2)
    t.goto(x1,x2)
    t.end_fill()
# 打包直线
def draw_line(x1,x2,y1,y2):
    t.pensize(5)
    t.penup()
    t.goto(x1,x2)
    t.pendown()
    t.goto(y1,y2)


# --------- 主程序--------
# 画飞机
draw_tri(tri1[0][0],tri1[0][1],tri1[1][0],tri1[1][1],tri1[2][0],tri1[2][1])
draw_tri(tri2[0][0],tri2[0][1],tri2[1][0],tri2[1][1],tri2[2][0],tri2[2][1])
draw_tri(tri3[0][0],tri3[0][1],tri3[1][0],tri3[1][1],tri3[2][0],tri3[2][1])
draw_line(line[0][0],line[0][1],line[1][0],line[1][1])
# 画线模仿空气流动
draw_line(line[2][0],line[2][1],line[3][0],line[3][1])
draw_line(line[4][0],line[4][1],line[5][0],line[5][1])
draw_line(line[6][0],line[6][1],line[7][0],line[7][1])
draw_line(line[8][0],line[8][1],line[9][0],line[9][1])

# 画太阳
t.penup()
t.goto(300,300)
t.pendown()
t.dot(120,'red')