# parallelogram
O =( 0,0)
R = 100
X = 110
import turtle
turtle.setup(500,500)
turtle.hideturtle()
turtle.circle(R)

turtle.penup()
O = (X,-X/2)
turtle.goto(O)
turtle.pendown()
turtle.circle(R)

turtle.penup()
O = (X*2,0)
turtle.goto(O)
turtle.pendown()
turtle.circle(R)

turtle.penup()
O = (X*3,-X/2)
turtle.goto(O)
turtle.pendown()
turtle.circle(R)
turtle.penup()

O = (X*4,0)
turtle.goto(O)
turtle.pendown()
turtle.circle(R)

turtle.done()