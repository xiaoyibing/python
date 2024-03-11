import turtle as t
t.hideturtle()

star_weizhi=[[-280,160],[-210,175],[-190,160],[-190,130],[-210,110]]
star_length_angle=[[25, 0],[8,53],[8,25],[8,0],[8,335]]
X=300
Y=200
def num(x, y):
    t.tracer(0)
    t.speed(0)
    t.penup()
    t.goto(-300+x, y)
    t.pendown()
    t.color('red', 'red')
    t.begin_fill()
    for a in range(2):
        t.forward(X)
        t.left(90)
        t.forward(Y)
        t.left(90)
    t.end_fill()

    def star(length, angle):
        t.color('yellow', 'yellow')
        t.pendown()
        t.left(angle)
        t.begin_fill()
        for i in range(5):
            t.forward(length)
            t.left(72)
            t.forward(length)
            t.right(144)
        t.end_fill()
        t.right(angle)
        t.penup()
    # -------大五角星
    for i in range(5):
        t.goto(star_weizhi[i][0]+x, star_weizhi[i][1]+y)
        star(star_length_angle[i][0], star_length_angle[i][1])
    t.tracer(0)


num(0, -100)
t.mainloop()



