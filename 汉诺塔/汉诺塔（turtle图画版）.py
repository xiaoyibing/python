import time
import turtle as t
#坐标数据
ls=[[-300,0],[-300,300],[-300,0],[0,0],[0,300],[0,0],[300,0],[300,300]]
ls2=[-300,0,300]

#屏幕
game=t.Screen()
game.title('汉诺塔')
game.screensize(700,600,'white')
#支架
def draw():
    t.pensize(15)
    t.hideturtle()
    for i in ls:
        a,b=i
        t.goto(a,b)
#创建一支新的笔，清除棋子（t2）时不会影响支架（t）
t2=t.Pen()
t2.hideturtle()
t2.pensize(15)
#通过abc三个数组中的数据绘制棋子
def draw1(x,y,z):
    t2.penup()
    t2.goto(x,y+40)
    t2.pendown()
    for i in range(len(z)):
        t2.forward(z[i]*30)
        t2.bk(z[i]*60)
        t2.fd(z[i]*30)
        t2.goto(x,y+40*(2+i))
def draw2():
    t.tracer(0)
    t2.clear()
    draw1(ls2[0],0,a)
    draw1(ls2[1],0,b)
    draw1(ls2[2],0,c)
    t.tracer(1)
    time.sleep(0.5)


#递归文字版+draw2（）
def move(n,a,b,c):
    if n==1:
        c.append(a[len(a)-1])
        del a[len(a)-1]
        print(a,b,c)
        draw2()
    else:
        move(n-1,a,c,b)#递归，注意abc位置的调换
        c.append(a[len(a)-1])#“c”数组添加数据（此处的“c”数组并不是初始创建的数组c，而是函数声明move(n,a,b,c)中的c）
        del a[len(a)-1]#“a”数组删除数据
        print(a,b,c)
        draw2()#绘制

        move(n-1,b,a,c)#递归，注意abc位置的调换




n=int(input("请输入层数:"))
#创建三个数组，保存每个支架上的棋子
a = list(range(n, 0, -1))
b=[]
c=[]
t.tracer(0)
#绘制支架
draw()
#绘制初始棋子位置
draw2()
t.tracer(1)
#开始移动
move(n,a,b,c)
t.mainloop()
