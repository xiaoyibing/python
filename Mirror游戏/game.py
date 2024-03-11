import turtle as t
import random


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")  # 设置玩家形状为海龟
        self.pu()  # 抬起画笔，不绘制图形
        self.speed(0)  # 设置速度为最快
        self.shapesize(2, 2)


class Listen:
    def __init__(self):
        self.screen = t.Screen()
        self.creat_black()
        self.screen.tracer(0)  # 关闭动画，防止窗口刷新(k)

        self.player = Player()
        self.player2 = Player()

        self.canvas = self.screen.getcanvas()
        self.canvas.bind('<Motion>', self.motion)

    def creat_black(self):
        t.tracer(0)
        self.pen = t.Pen()
        self.pen.hideturtle()
        self.pen.color('black', 'black')
        self.pen.begin_fill()
        self.pen.goto(0, -500)
        self.pen.setx(600)
        self.pen.sety(500)
        self.pen.setx(0)
        self.pen.sety(0)
        self.pen.end_fill()
        t.tracer(1)

    def motion(self, event):
        self.x, self.y = event.x - self.screen.window_width() // 2, self.screen.window_height() // 2 - event.y
        if self.x < 0:
            self.player.color('black')
            self.player2.color('white')
        else:
            self.player.color('white')
            self.player2.color('black')

        self.player.goto(self.x, self.y)
        self.player2.goto(-self.x, self.y)


class Oblong(t.Turtle):
    def __init__(self, x, y, unspeed):
        super().__init__()
        self.shape("triangle")
        xuanzhuan = random.randint(0, 360)
        self.seth(xuanzhuan)
        if x < 0:
            self.color('black')
        else:
            self.color('white')
        self.pu()  # 抬起画笔，不绘制图形
        self.speed(0)  # 设置速度为最快
        self.goto(x, y)  # 将方块移动到指定位置
        self.unspeed = unspeed  # 控制下落速度

    def move(self):
        self.sety(self.ycor() - self.unspeed)  # 设置新的 y 坐标


class Nume(t.Turtle):
    def __init__(self, name):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(-500, 400)
        self.write(name, font=('楷书', 30, 'normal'))


class Game:
    def __init__(self):
        self.Listen = Listen()
        self.ls_turtle = []
        self.run()

    def run(self):
        name = 0
        jishu = Nume(name)
        while True:
            self.Listen.screen.update()  # 更新窗口
            if len(self.ls_turtle) < 10:
                speed = random.uniform(0.1, 0.5)
                x_turtle = random.randint(-500, 500)
                blong = Oblong(x_turtle, 500, speed)
                self.ls_turtle.append(blong)

            for blong in self.ls_turtle:
                blong.move()  # 让所有方块向下移动
                if blong.distance(self.Listen.player) < 20 or blong.distance(self.Listen.player2) < 20:
                    print(f'恭喜！你躲避了{name}个脆脆角后，终于吃到了它。')
                    return

                if blong.ycor() < -500:
                    blong.hideturtle()
                    self.ls_turtle.remove(blong)
                    name += 1
                    jishu.clear()
                    jishu = Nume(name)


game = Game()
