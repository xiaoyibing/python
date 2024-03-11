#任务3：图形版扫雷2，在turtle版扫雷1基础上，增加计时、重启功能 （个人任务）
import random
import time
import turtle as t
import os
import sys

nnn=0
times=0
time_stop=0
class Lei:
    def __init__(self):
        t.tracer(0)
        self.pen0()
        self.create_main()
        t.tracer(1 )
        t.onscreenclick(self.click)  # 开始点击程序，跳转到click函数
    def pen0(self):
        pen0 = t.Pen()
        pen0.penup()
        pen0.hideturtle()
        pen0.goto(100, 100)
        pen0.write('■', font=('宋体', 40, 'normal'))
    def create_main (self):
        self.mains = [[0 for _ in range(10)] for _ in range(10)]  # 10*10列表
        for i in range(10):
            for j in range(10):
                self.mains[i][j] = Mine(i,j)  # 创建对象
        self.ran_lei()
        self.around_num()
    def ran_lei(self):
        # ----------------------随机数装雷（10个）---------------------------
        self.num_lie = 0  # 记录雷数
        while self.num_lie < 10:
            x, y = random.randint(0, 9), random.randint(0, 9)
            if self.mains[x][y].write_in != '*':  # 判断该位置是否已经是雷，避免重复
                self.mains[x][y].write_in = '*'
                self.num_lie += 1
    def around_num(self):
        # --------------------------计算周围的雷数-----------------------------
        for i in range(10):
            for j in range(10):
                if self.mains[i][j].write_in != '*':
                    n = 0
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            if (0 <= i - a <= 9) and (0 <= j - b <= 9):
                                if self.mains[i - a][j - b].write_in == '*':
                                    n += 1
                    self.mains[i][j].write_in = str(n)  # 将 ■替换成雷数

    # -----------------------------------
    def click(self,x, y):
        t.tracer(0)
        global times
        global nnn
        if 0 <= x % 25 <= 20 and 0 <= y % 25 <= 20 and 0<=x<=250 and -225<=y<=25 :
            i = int(x // 25)
            j = int((y // (-25)) + 1)
            self.mains[i][j].clear()
            self.mains[i][j].draw(i, j)
            if self.mains[i][j].yn == 'n':  # 判断是否是第一次点击，防止n无效增加
                nnn+=1
                self.mains[i][j].yn = 'y'
            if self.mains[i][j].write_in == '*':#判断失败
                self.mains[i][j].fail()
            if nnn==90 and self.mains[i][j].write_in != '*':
                self.mains[i][j].win()
            else:
                self.lian(i, j)  # 判断是否需要展开相邻的方格

        if 100 <= x <= 140 and 100 <= y <= 140:
            python = sys.executable
            os.execl(python, python, *sys.argv)

    # ------------------递归打开与‘0’相邻的方格-------------
    def lian(self,x, y):
        if self.mains[x][y].write_in == '0':
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if (0 <= x - a <= 9) and (0 <= y - b <= 9):
                        # mains[x - a][y - b].yn =='n'判断是否是第一次点击
                        if self.mains[x - a][y - b].write_in != '*' and self.mains[x - a][y - b].yn == 'n':
                            self.click((x - a) * 25, ((y - b) - 1) * (-25))

class Mine(t.Turtle):
    def __init__(self,x,y):
        self.write_in='■'#写入的字
        super().__init__()
        self.hideturtle()
        self.penup()
        self.yn='n'#判断是否已经点击过，已点击：y,未点击：n
        self.draw(x,y)
    def draw(self,x,y):#书写
        self.goto(x*25,y*-25)#每个 ■长20，25使得相邻之间间距为5
        self.write(self.write_in,font=('宋体',20,'normal'))#写入
    def create_pen(self,x, y):#创建书写胜利失败的画笔
        self.pen = t.Pen()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.color('red')
        return self.pen  # 返回设置好的画笔
    def win(self):#胜利
        global time_stop
        t.onscreenclick(None)  # 结束点击程序
        self.pen3 = self.create_pen(-100, 100)
        self.pen3.write('胜利！', font=('宋体', 20, 'normal'))
        time_stop=1
        t.onscreenclick(self.re)

    def fail(self):#失败
        global time_stop
        t.onscreenclick(None)#结束点击程序
        self.pen2 = self.create_pen(-100, 100)
        self.pen2.write('Game Over!', font=('宋体', 20, 'normal'))
        time_stop=1
        t.onscreenclick(self.re)
    def re(self,x,y):
        if 100 <= x <= 140 and 100 <= y <= 140:
            python = sys.executable
            os.execl(python, python, *sys.argv)

def time():
    if time_stop==0:
        global times
        pen_time.clear()
        pen_time.write(times,font=('宋体', 40, 'normal'))
        times+=1
        t.ontimer(time, 1000)

#------------------------主程序-------------------------
pen_time=t.Pen()
pen_time.penup()
pen_time.hideturtle()
pen_time.goto(0,150)

time()
Lei()
t.mainloop()#窗口不关闭