# triangles 
O =( 0,0)
B =(50,100)
C = (100,0)

import turtle
turtle.hideturtle()
turtle.goto(B)
turtle.goto(C)
turtle.goto(O)
#second triangle
B = (50,50)
turtle.begin_fill()
turtle.fillcolor("red")

turtle.goto(B)
turtle.goto(C)
turtle.goto(O)
turtle.end_fill()
turtle.done()