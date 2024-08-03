# parallelogram
O =( 0,0)
B =(0,100)
C = (100,100)
D =(100,0)

import turtle
turtle.hideturtle()
turtle.goto(B)
turtle.goto(C)
turtle.goto(D)
turtle.goto(O)
#second triangle
turtle.penup()
turtle.goto(D)
turtle.pendown()
E = (200,0)
F = (200,-100)
G = (100,-100)
turtle.goto(E)
turtle.goto(F)
turtle.goto(G)
turtle.goto(D)

turtle.penup()
turtle.goto(O)
turtle.pendown()
turtle.goto(G)

turtle.penup()
turtle.goto(D)
turtle.pendown()
turtle.goto(F)

turtle.penup()
turtle.goto(B)
turtle.pendown()
turtle.goto(D)

turtle.penup()
turtle.goto(C)
turtle.pendown()
turtle.goto(E)

turtle.done()