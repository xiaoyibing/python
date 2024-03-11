import turtle

turtle.pensize(8)
turtle.speed(0)
turtle.hideturtle()

colors = ['green', 'orange', 'sky blue', 'orange red']

for color in colors:
    turtle.color('white', color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right((90))
    turtle.end_fill()


turtle.done()
