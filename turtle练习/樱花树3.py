import random
import turtle as t
def draw_tree(branch):
    if branch>2:
        if branch>=8 and branch<=10:
            t.color('red')
            t.pensize(branch/2)
        elif branch<8:
            t.color("pink")
            t.pensize(branch)
        elif branch>10 and branch<=20:
            t.color("#8a7081")
            t.pensize(branch/7)
        else:
            t.color('sienna')
            t.pensize(branch/10)
        t.forward(branch)#先画主干
        a = 1.6*random.random()
        #print(a)
        b = 1.6 * random.random()
        #print(b)
        t.left(20*a)#再画左支
        draw_tree(branch-10*b)#画左支
        t.right(40*a)
        draw_tree(branch-10*b)#右枝
        t.left(20*a)
        t.up()
        t.backward(branch)
        t.down()
    else:
        return

#w = t.Screen()
t.tracer(False)
t.up()
t.left(90)
t.backward(200)
t.down()
t.speed(0)
#t.hideturtle()
draw_tree(70)
t.tracer(True)
#print("draw_finish")
#w.exitonclick()

