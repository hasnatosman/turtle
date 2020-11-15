import turtle

#turtle.shape("turtle")
turtle.color("blue")
turtle.speed(1)

def curve():

    for i in range(200):
        turtle.forward(1)
        turtle.right(1)

def  heart():

    turtle.left(140)
    turtle.forward(113)
    curve()
    turtle.left(120)
    curve()
    turtle.forward(120)
    turtle.fillcolor("red")

heart()