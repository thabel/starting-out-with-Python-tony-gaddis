A = (-50,50)
B = (-50,-50)
C= (50,-50)
D = (50,50)

import turtle
turtle.hideturtle()

turtle.penup()
turtle.goto(A)
turtle.pendown()
turtle.dot()

turtle.goto(B)
turtle.dot()

turtle.goto(D)
turtle.dot()

turtle.goto(C)
turtle.dot()

turtle.goto(0,0)
turtle.dot()

turtle.goto(A)
turtle.forward(12.5)
turtle.penup()
turtle.forward(12.5)
turtle.pendown()
turtle.forward(25)
turtle.penup()
turtle.forward(12.5)
turtle.pendown()
turtle.forward(25)

turtle.penup()
turtle.goto(B)
turtle.forward(12.5)
turtle.penup()
turtle.forward(12.5)
turtle.pendown()
turtle.forward(25)
turtle.penup()
turtle.forward(12.5)
turtle.pendown()
turtle.forward(25)

turtle.done()

