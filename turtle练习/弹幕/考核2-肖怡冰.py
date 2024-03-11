'''模拟发文字弹幕的效果，弹幕支持多条同框的效果且刚开始时并不是同时出现，所有弹幕都是从右向左
（或从左向右）移动的循环弹幕，有的弹幕快有的慢，有的字大有的字小，有的字颜色是彩色的，VIP嘛
有特权。文字内容来源于一个文本文件（其中每一段就是一条弹幕），随机抽取发送。弹幕只占屏幕的
上方区域，弹幕之间可以重叠，显示不能有明显的闪烁，不能有冷场（成片的空白）。
拒收1---冷场
拒收2---有明显的闪烁
拒收3---没有快慢/大小的区别
拒收4---内容有规律
提交方式：现场电脑展示或QQ发运行30秒视频'''
with open('弹幕.txt','r',encoding='utf-8') as f:
    lines=f.read()
    line=lines.split('\n')
#print(line)
import turtle as t
import random
import time
#数据
ll=[]
c=['red','black','blue']
hhhigh = [200, 300, 250,210,310]
big=[20,50,15,25,21,9,18,20]
def r():
    for i in range(5):
        r1 = random.choice(line)
        r2 = random.choice(hhhigh)
        r3 = random.choice(c)
        r4 = random.choice(big)
        ll.append([r1, r2, r3, r4])
   # print(ll)
def rr(i):
    r1 = random.choice(line)
    r2 = random.choice(hhhigh)
    r3 = random.choice(c)
    r4 = random.choice(big)
    ll[i]=[r1,r2,r3,r4]

# 窗口
name=t.Screen()
name.title('弹幕测试')
name.bgcolor('white')
name.setup(500,700)
t1=t.Pen()
t2=t.Pen()
t3=t.Pen()
t4=t.Pen()
t5=t.Pen()
def draw(x,i,f):
    t.tracer(0)
    x.clear()
    x.backward(f)
    x.write(ll[i][0], font=('宋体', ll[i][3], 'normal'))
    t.tracer(1)
    time.sleep(0.005)
def pd(x,i):
    r()
    x.penup()
    x.color(ll[i][2])
    x.hideturtle()
    x.goto(250,ll[i][1])
pd(t1, 1)
pd(t2, 2)
pd(t3, 0)
pd(t4, 3)
pd(t5, 4)
while(1):
    draw(t1, 1, 5)
    if t1.xcor()<=-300:
        rr(1)
        t.tracer(0)
        t1.goto(250, ll[1][1])
        t.tracer(1)
    draw(t2, 2, 4)
    if t2.xcor() <= -300:
        rr(2)
        t.tracer(0)
        t2.goto(250, ll[2][1])
        t.tracer(1)
    draw(t3, 0, 5)
    if t3.xcor() <= -300:
        rr(0)
        t.tracer(0)
        t3.goto(250, ll[0][1])
        t.tracer(1)
    draw(t4, 3, 1)
    if t4.xcor()<=-300:
        rr(3)
        t.tracer(0)
        t4.goto(250, ll[3][1])
        t.tracer(1)
    draw(t5, 4, 3)
    if t5.xcor()<=-300:
        rr(4)
        t.tracer(0)
        t5.goto(250, ll[4][1])
        t.tracer(1)



