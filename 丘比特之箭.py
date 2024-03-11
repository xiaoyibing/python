#丘比特之箭，一支箭从屏幕左侧移动到右侧，再回到左侧循环
#练习构建画笔
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
"""
在Turtle库中，register_shape() 函数的作用是将自定义的形状注册到Turtle模块中，以便后续在画布上使用这些形状。
通常，Turtle模块提供了一些默认的形状，比如箭头、圆形等，但有时候我们需要使用自己设计的形状。register_shape() 函数就是为了解决这个问题。
它的工作原理是将用户定义的形状信息上传到Turtle模块中，并给这个形状取一个名字，以便在之后的绘图中引用。
上传的形状信息通常是一个列表，其中包含一系列的坐标点，这些点连接起来就形成了所需的形状。
在上传后，我们就可以通过指定这个名字来使用这个自定义的形状，比如在创建Turtle对象时设置其形状为我们自定义的形状。
"""
