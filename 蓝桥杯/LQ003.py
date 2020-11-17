import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.color('red','yellow')
def square(x):
    for i in range(4):
        t.fd(x)
        t.right(90)
t.penup()
t.goto(-50,100)
t.pendown()
square(100)
t.penup()
t.goto(0,0)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()