import time
import turtle as t
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
t2=t.Pen()
t2.hideturtle()
t2.pensize(15)
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


#文字版
def move(n,a,b,c):
    if n==1:
        c.append(a[len(a)-1])
        del a[len(a)-1]
        print(a,b,c)
        draw2()
    else:
        move(n-1,a,c,b)
        c.append(a[len(a)-1])
        del a[len(a)-1]
        print(a,b,c)
        draw2()

        move(n-1,b,a,c)




n=int(input("请输入层数:"))
a = list(range(n, 0, -1))
b=[]
c=[]
t.tracer(0)
draw()
draw2()
t.tracer(1)
move(n,a,b,c)
t.mainloop()