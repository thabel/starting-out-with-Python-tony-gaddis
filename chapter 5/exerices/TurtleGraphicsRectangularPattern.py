"""
In a program, write a function named drawPattern that uses the turtle graphics library
to draw the rectangular pattern shown in Figure 5-31. The drawPattern function should
accept two arguments: one that specifies the pattern’s width, and another that specifies the
pattern’s height. (The example shown in Figure 5-31 shows how the pattern would appear
when the width and the height are the same.) When the program runs, the program should
ask the user for the width and height of the pattern, then pass these values as arguments to
the drawPattern function.
"""

import turtle


def draw_rectangle(x, y, go_up=False):
    if go_up:
        turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)


def drawPattern(width=100, heigh=100):
    offset_width = width/10
    offset_heigh = heigh/10
    original_width, original_heigh = width, heigh
    turtle.begin_fill()
    turtle.fillcolor("black")
    draw_rectangle(width, heigh)
    turtle.end_fill()
    width += 2 * offset_width
    heigh += 2 * offset_heigh
    x, y = turtle.pos()
    turtle.goto(x - offset_width, y - offset_heigh)
    for i in range(3):
        draw_rectangle(width, heigh, True)
        width += 2 * offset_width
        heigh += 2 * offset_heigh
        x, y = turtle.pos()
        if i != 2:
            turtle.goto(x - offset_width, y - offset_heigh)
    x, y = turtle.pos()
    turtle.goto(x + original_width + 2 * 3 * offset_width, y + original_heigh + 2 * 3 * offset_heigh)
    turtle.penup()
    turtle.goto(x + 2 * 3 * offset_width + original_heigh, y)
    turtle.pendown()
    turtle.goto(x, y + original_heigh + 2 * 3 * offset_heigh)
    turtle.penup()
    turtle.goto(x, y + 3 * offset_width + original_heigh / 2)
    #
    turtle.pendown()
    turtle.goto(x + original_width + 2 * 3 * offset_width, y + 3 * offset_heigh + original_heigh / 2)

    turtle.penup()
    turtle.goto(x + 3 * offset_width + original_width / 2, y)
    turtle.pendown()
    turtle.goto(x + 3 * offset_width + original_width / 2, y + original_heigh + 2 * 3 * offset_heigh)


turtle.speed(0)
width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
drawPattern(width, height)
turtle.done()
