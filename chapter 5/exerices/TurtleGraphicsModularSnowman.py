import turtle

"""
Write a program that uses turtle graphics to display a snowman, similar to the one shown 
in Figure 5-30. In addition to a main function, the program should also have the following 
functions:
•	 drawBase. This function should draw the base of the snowman, which is the large snowball at the bottom.
•	 drawMidSection. This function should draw the middle snowball.
•	 drawArms. This function should draw the snowman’s arms.
•	 drawHead. This function should draw the snowman’s head, with eyes, mouth, and other 
facial features you desire.
•	 drawHat. This function should draw the snowman’s hat.

"""

START = -300
SNOW_RAYON = 150


def main():
    turtle.speed(0)
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()


def drawMidSection():
    turtle.penup()
    turtle.goto(0, 2 * SNOW_RAYON + START)
    turtle.pendown()
    turtle.circle(SNOW_RAYON / 2)


def drawHead():
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(0, 2 * SNOW_RAYON + START + SNOW_RAYON)
    x, y = turtle.pos()
    turtle.pendown()
    turtle.circle(SNOW_RAYON / 3)
    turtle.penup()
    turtle.goto(x - SNOW_RAYON / 3 + SNOW_RAYON / 10, y + SNOW_RAYON / 3 - SNOW_RAYON / 10)
    turtle.pendown()
    turtle.goto(x + SNOW_RAYON / 3 - SNOW_RAYON / 10, y + SNOW_RAYON / 3 - SNOW_RAYON / 10)

    # draw eyes
    turtle.penup()
    turtle.goto(x + SNOW_RAYON / 3 - 2 * SNOW_RAYON / 10, y + SNOW_RAYON / 3)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.circle(SNOW_RAYON / 20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x - SNOW_RAYON / 3 + 2 * SNOW_RAYON / 10, y + SNOW_RAYON / 3)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.circle(SNOW_RAYON / 20)
    turtle.end_fill()


def drawArms():
    xo, yo = turtle.pos()
    turtle.penup()
    turtle.goto(SNOW_RAYON / 2, 2 * SNOW_RAYON + START + SNOW_RAYON / 2)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(SNOW_RAYON / 2)
    v_arms()

    turtle.penup()
    turtle.goto(-SNOW_RAYON / 2, 2 * SNOW_RAYON + START + SNOW_RAYON / 2)
    turtle.pendown()
    turtle.right(45 + 180)
    turtle.forward(SNOW_RAYON / 2)
    v_arms()


def v_arms():
    x, y = turtle.pos()
    # the V for the right
    turtle.left(45)
    turtle.forward(SNOW_RAYON / 5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(-90)
    turtle.forward(SNOW_RAYON / 5)


def drawHat():
    x, y = turtle.pos()
    turtle.penup()
    turtle.goto(x, y + SNOW_RAYON / 3 - SNOW_RAYON / 10)
    turtle.pendown()
    x, y = turtle.pos()
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.forward(SNOW_RAYON / 2 + SNOW_RAYON / 5)
    turtle.left(90)
    turtle.forward(SNOW_RAYON / 7)
    turtle.left(90)
    turtle.forward(SNOW_RAYON / 3)
    turtle.right(90)
    turtle.forward(SNOW_RAYON / 2 - SNOW_RAYON / 8)
    turtle.left(90)
    # hat top
    turtle.forward(SNOW_RAYON / 2)
    turtle.left(90)
    turtle.forward(SNOW_RAYON / 2 - SNOW_RAYON / 8)
    turtle.right(90)
    turtle.forward(SNOW_RAYON / 3)
    turtle.left(90)
    turtle.forward(SNOW_RAYON / 7)
    turtle.goto(x, y)
    turtle.end_fill()


def drawBase():
    turtle.dot(5, "red")
    turtle.penup()
    turtle.goto(0, START)
    turtle.pendown()
    turtle.circle(SNOW_RAYON)
    turtle.dot(5, "red")


main()
turtle.done()
