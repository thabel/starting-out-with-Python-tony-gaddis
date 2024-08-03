import turtle

def triange(A,B,C,color):
    """
    Write a function named triangle that uses the turtle graphics library to draw a triangle.
The functions should take arguments for the X and Y coordinates of the triangle’s vertices, and the color with which the triangle should be filled. Demonstrate the function in a
program
    :param A:tuple
    :param B:tuple
    :param C:tuple
    :param color:string
    :return: None
    """
    turtle.penup()
    turtle.goto(A[0],A[1])
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(B[0], B[1])
    turtle.goto(C[0], C[1])
    turtle.goto(A[0], A[1])
    turtle.end_fill()
    turtle.done()

triange((0,0),(50,100),(100,0),"red")
