# turtle graphics
import turtle
O = (0,0)
A = (-50,50)
B = (-100,0)
C = (-50,-50)

turtle.showturtle()
turtle.fillcolor("blue")
turtle.begin_fill()
#first rectangle
turtle.goto(A)
turtle.goto(B)
turtle.goto(C)
turtle.goto(O)
#Second rectangles
A=(50,50)
B=(100,0)
C=(50,-50)

turtle.goto(A)
turtle.goto(B)
turtle.goto(C)
turtle.goto(O)

turtle.end_fill()
turtle.done()