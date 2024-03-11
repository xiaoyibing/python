import turtle as t

# 创建游戏画布
game = t.Screen()
game.title("丘比特之箭")
game.setup(800, 300)

# 构建箭头形状
def draw_arrow():
    t.tracer(0)
    t.hideturtle()
    t.begin_poly()  # 开始构建

    t.goto(200, 0)
    t.right(90)
    t.fd(20)
    t.left(120)
    t.fd(60)
    t.left(120)
    t.fd(60)
    t.left(120)
    t.fd(20)
    t.right(90)
    t.fd(200)
    t.left(90)
    t.fd(20)
    t.clear()

    t.end_poly()  # 结束构建
    t.register_shape("arrow_shape", t.get_poly())  # 上传构建，并命名
    return "arrow_shape"

# 创建画笔并设置形状
pen = t.Turtle(shape=draw_arrow())
pen.color('red', 'red')
pen.penup()
pen.left(90)
pen.goto(-680, 0)
t.tracer(1)

# 移动箭头
while True:
    for i in range(150):
        pen.goto(-500 + i * 8, 0)
    t.tracer(0)
    pen.goto(-680, 0)
    t.tracer(1)
