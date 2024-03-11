#从键盘上输入一张扑克牌的文字，立即显示出这张牌的图形
import turtle as t
t.penup()
t.hideturtle()
pen=t.Pen()
pen.hideturtle()
def draw(q):
    # pen.color('red','red')
    # pen.begin_fill()
    for i in range(2):
        pen.fd(150)
        pen.left(90)
        pen.fd(200)
        pen.left(90)
    t.goto(40,100)
    t.write(q,font=('楷体',60,'normal'))

q=input('请输入：')
t.tracer(0)
draw(q)
t.tracer(1)

t.mainloop()
