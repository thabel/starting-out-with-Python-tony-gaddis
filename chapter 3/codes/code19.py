# Hit the Target Game
import math
import turtle

#Named Constants
DIVIDE = 180/math.pi
#screens 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
#targets
TARGET_LLEFTX = 100
TARGET_LLEFTY = 250
TARGET_WIDTH = 25
#forces
FORCE_FACTOR = 30
#Projectile
PROJECTILE_SPEED = 1
#directions
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

#setup the window.
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

#draw target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFTX,TARGET_LLEFTY)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

#get the angle and force
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the lauch force(1-10): "))
#Calculate the distance:
distance = force*FORCE_FACTOR
#set thz heading.
turtle.setheading(angle)
#Lunch projectile
turtle.pendown()
turtle.forward(distance)

# Dit it hit the target ?

if(turtle.xcor() >= TARGET_LLEFTX and turtle.xcor()<= (TARGET_LLEFTX+TARGET_WIDTH)
    and turtle.ycor()>= TARGET_LLEFTX and turtle.ycor()<= (TARGET_LLEFTY+TARGET_WIDTH)):
    print("target hit!")
else:
    if(angle > ((math.atan2(TARGET_LLEFTY+TARGET_WIDTH,TARGET_LLEFTX))*DIVIDE)):
        print("Use less angle.")
    elif(angle< ((math.atan2(TARGET_LLEFTY,TARGET_LLEFTX+TARGET_WIDTH))*DIVIDE)):
        print("Use greater angle.")
    else : 
        if(distance <math.sqrt((TARGET_LLEFTX**2+TARGET_LLEFTY**2))):
            print("Use great Force.")
        elif(distance >math.sqrt(((TARGET_LLEFTX+TARGET_WIDTH)**2+(TARGET_LLEFTY+TARGET_WIDTH)**2))):
            print("Use less Force.")
        else:
            print("The next will be the best")
#turtle done method
turtle.done()
