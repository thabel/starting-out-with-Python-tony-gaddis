"""
Write a turtle graphics program that draws a city skyline similar to the one shown in Figure
5-33. The program’s overall task is to draw an outline of some city buildings against a
night sky. Modularize the program by writing functions that perform the following tasks:
•	 Draw the outline of buildings.
•	 Draw some windows on the buildings.
•	 Use randomly placed dots as the stars (make sure the stars appear on the sky, not on the
buildings).

"""
import turtle
def draw_rectangle(x, y, go_up=False,color="black"):
    turtle.begin_fill()
    turtle.fillcolor(color)
    if go_up:
        turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.end_fill()

def draw_window():
    turtle.penup()

    x,y = turtle.pos()
    turtle.goto(x-x//10,y//2)
    draw_rectangle(10,10,color="white")

    turtle.goto(x+150,150)
    draw_rectangle(10, 10, color="white")

    turtle.goto(x + 150, 0)
    draw_rectangle(10, 10, color="white")

    turtle.goto(x + 150 + 175, 0)
    draw_rectangle(10, 10, color="white")

    turtle.goto(x + 150 + 175, -150)
    draw_rectangle(10, 10, color="white")

def draw_starts():

    turtle.penup()
    turtle.goto(0,0)
    turtle.dot(5,"white")
    x, y = turtle.pos()

    turtle.penup()
    turtle.goto(x+150, y)
    turtle.dot(5, "white")

    turtle.penup()
    turtle.goto(x + 150, y+150)
    turtle.dot(5, "white")

    turtle.penup()
    turtle.goto(x + 150  - 325, y + 150)
    turtle.dot(5, "white")



def draw_outline_of_building():
    turtle.begin_fill()
    turtle.fillcolor("gray")
    x,y = turtle.pos()
    turtle.goto(x,y//6)

    turtle.left(90)
    turtle.forward(50)

    turtle.left(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    # haut plat
    turtle.forward(145)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(82)
    turtle.left(90)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(80)

    turtle.left(90)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(80)

    turtle.left(90)
    turtle.forward(35)

    turtle.goto(-x,y)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.end_fill()

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()
draw_rectangle(500,500)
draw_outline_of_building()

draw_window()
draw_starts()
turtle.done()