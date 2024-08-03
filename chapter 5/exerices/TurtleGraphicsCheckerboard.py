import turtle


def square(x, y, width, color):
    turtle.penup()  # Raise the pen
    turtle.goto(x, y)  # Move to the specified location
    turtle.fillcolor(color)  # Set the fill color
    turtle.pendown()  # Lower the pen
    turtle.begin_fill()  # Start filling
    for count in range(4):  # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()  # End filling


def draw_check_board():
    WIDTH = 50
    for i in range(5):
        for j in range(5):
            x, y = turtle.pos()
            if i%2 :
                if j % 2:
                    square(x,y,WIDTH, "white")
                else:
                    square(x,y, WIDTH, "black")
            else:
                if not j % 2:
                    square(x, y, WIDTH, "white")
                else:
                    square(x, y, WIDTH, "black")
            turtle.penup()
            turtle.goto(x+WIDTH,y)
            turtle.pendown()
        turtle.penup()
        turtle.goto(0, y+WIDTH)
        turtle.pendown()


turtle.speed(0)
draw_check_board()
turtle.done()