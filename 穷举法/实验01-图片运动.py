import turtle as t
def set(text1,text2,text3,text4):
    t.register_shape(text1)
    t1=t.Turtle()
    t1.color("white")
    t1.shape(text1)
    t1.fd(150)

    t.register_shape(text2)
    t2=t.Turtle()
    t2.color("white")
    t2.shape(text2)
    t2.fd(150)

    t.register_shape(text3)
    t3=t.Turtle()
    t3.color("white")
    t3.shape(text3)
    t3.fd(150)

    t.register_shape(text4)
    t4=t.Turtle()
    t4.color("white")
    t4.shape(text4)
    t4.fd(150)
set('狼.gif','羊.gif','菜.gif','船.gif')