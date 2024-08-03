import turtle

#drawing Orion Constellation with turtle !

#Set the window size
turtle.setup(500,600)


#Setup the turtle
turtle.penup()
turtle.hideturtle()

#Creating named constanrs for the star coordinate(7)

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y= 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGH_BELTSTAR_X = 40
RIGH_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140
#Draw the stars.
turtle.goto(LEFT_SHOULDER_X,LEFT_SHOULDER_Y)
turtle.dot()

turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.dot()

turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.dot()

turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y)
turtle.dot()

turtle.goto(RIGH_BELTSTAR_X,RIGH_BELTSTAR_Y)
turtle.dot()

turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.dot()

turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.dot()

#star's name
turtle.goto(LEFT_SHOULDER_X,LEFT_SHOULDER_Y)
turtle.write("Betegeuse")

turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.write("Meissa")

turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.write("Alnitak")

turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y)
turtle.write("Alnilam")

turtle.goto(RIGH_BELTSTAR_X,RIGH_BELTSTAR_Y)
turtle.write("Mintaka")

turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.write("Saiph")

turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.write("Rigel")

#drawing line

#Line 1
turtle.goto(LEFT_SHOULDER_X,LEFT_SHOULDER_Y)
turtle.pendown()

turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.penup()
#Line 2
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGH_BELTSTAR_X,RIGH_BELTSTAR_Y)
turtle.penup()
#Line 3
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y)
turtle.penup()
#Line 4
turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGH_BELTSTAR_X,RIGH_BELTSTAR_Y)
turtle.penup()
#Line 5
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.penup()
#Line 6
turtle.goto(RIGH_BELTSTAR_X,RIGH_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.penup()
turtle.done()