# parallelogram
A = (0,150)
B = (-150,0)
C= (0,-150)
D = (150,0)
import turtle
turtle.hideturtle()

turtle.penup()
turtle.goto(A)

turtle.pendown()
turtle.goto(C)


turtle.penup()
turtle.goto(B)

turtle.pendown()
turtle.goto(D)


turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(50)

A = (-10,150)
B = (-180,-5)
C= (-10,-170)
D = (155,-5)

turtle.penup()
turtle.goto(A)
turtle.write("North")

turtle.goto(B)
turtle.write("West")

turtle.goto(C)
turtle.write("South")

turtle.goto(D)
turtle.write("East")
turtle.done()