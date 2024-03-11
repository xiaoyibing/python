#扫雷（turtle图像板）

import random
import turtle as t

#-----------------------创建窗口------------------------
game=t.Screen()
game.title('扫雷小游戏')
game.setup(600,700)#窗口宽，高

#------------------------定义类------------------------
class Mine(t.Turtle):
    def __init__(self):
        self.write_in='■'#写入的字
        super().__init__()
        self.hideturtle()
        self.penup()
        self.yn='n'#判断是否已经点击过，已点击：y,未点击：n
    def draw(self,x,y):
        self.goto(x*25,y*-25)#每个 ■长20，25使得相邻之间间距为5
        self.write(self.write_in,font=('宋体',20,'normal'))#写入

# ----------------设置10*10列表，创建对象，并将 ■画入画布-----------------
t.tracer(0)
mains = [[0 for _ in range(10)] for _ in range(10)]#10*10列表
for i in range(10):
    for j in range(10):
        mains[i][j] = Mine()#创建对象
        mains[i][j].draw(i,j)#画 ■
t.tracer(1)

# ----------------------随机数装雷（10个）---------------------------
num_lie = 0#记录雷数
while num_lie < 10:
    x, y = random.randint(0, 9), random.randint(0, 9)
    if mains[x][y].write_in != '*':#判断该位置是否已经是雷，避免重复
        mains[x][y].write_in = '*'
        num_lie += 1
# --------------------------计算周围的雷数-----------------------------
for i in range(10):
    for j in range(10):
        if mains[i][j].write_in != '*':
            n = 0
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if (0 <= i - a <= 9) and (0 <= j - b <= 9):
                        if mains[i - a][j - b].write_in == '*':
                            n += 1
            mains[i][j].write_in =str(n)#将 ■替换成雷数

#------------------递归打开与‘0’相邻的方格-------------
def lian(x, y):
    if mains[x][y].write_in == '0':
        for a in range(-1, 2):
            for b in range(-1, 2):
                if (0 <= x - a <= 9) and (0 <= y - b <= 9):
                    #mains[x - a][y - b].yn =='n'判断是否是第一次点击
                    if mains[x - a][y - b].write_in != '*' and mains[x - a][y - b].yn =='n':
                        click((x - a)*25,((y - b)-1)*(-25))
#------------------创建画笔，用于书写红色提示------------------
def create_pen(x,y):
    pen=t.Pen()
    pen.hideturtle()
    pen.penup()
    pen.goto(x,y)
    pen.color('red')
    return pen  #返回设置好的画笔
#-----------------------------------
# 调用self.draw方法更换 ■，
# 调用lian（）子函数判断是否需要展开相邻的方格，
# 判断是否成功或失败
#判断当前剩余非炸弹数
pen1=create_pen(0,100)
n = 0#记录点击次数
def click(x,y):
    t.tracer(0)
    global n
    if 0<=x%25<=20 and 0<=y%25<=20:
        i = int(x // 25)
        j = int((y // (-25)) + 1)
        mains[i][j].clear()
        mains[i][j].draw(i, j)

        if mains[i][j].yn=='n':#判断是否是第一次点击，防止n无效增加
            n += 1
            pen1.clear()
            pen1.write(f'再点击{90 - n}次即可通关', font=('宋体', 20, 'normal'))
        mains[i][j].yn = 'y'

        if mains[i][j].write_in == '*':#判断失败
            t.onscreenclick(None)#结束点击程序
            pen2=create_pen(0, 100)
            pen1.clear()
            pen2.write( 'Game Over!', font=('宋体', 20, 'normal'))

        if n == 90:#判断胜利
            t.onscreenclick(None)#结束点击程序
            pen3=create_pen(0, 100)
            pen1.clear()
            pen3.write( '胜利！', font=('宋体', 20, 'normal'))

        else:
            lian(i, j)#判断是否需要展开相邻的方格
        t.tracer(1)
# ----------------------------------------------
t.onscreenclick(click)#开始点击程序，跳转到click函数
t.mainloop()#窗口不关闭