#imports
import turtle
""" # question 1
x =a= 1150
if(x>100):
    y=20
    z=40
# question 2
if a==100:
    b=10
    c=50
#question 3
if( a<10):
    b=0
else:
    b=99
# question 4
score = int(input('Enter your test score: '))
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

if(score>=A_SCORE):
    print('Your grade is A. ')
else:
    if(score>=B_SCORE):
        print('Your grade is B. ')
    else:
        if(score>=C_SCORE):
         print('Your grade is C. ')
        else:
            if(score>=D_SCORE):
                print('Your grade is D. ')
            else:
                print("Your grade is F.")
# question 5
amount1 = 100
amount2 = 90

if(amount1>10 and amount2<100):
   print(max(amount1,amount2))
# question 6
if(score>=40 and score<=49):
    again= True
else:
    again= False

# question 7
points = 7
if(points<9 or points>51):
    print("invalid points")
else:
    print('valid points')
# question 8
x=turtle.heading()
if(x>=0 and x<=45):
    turtle.penup()
# question 9
if(turtle.pensize()>1 or turtle.pencolor() == 'red'):
    turtle.pensize(1)
    turtle.pencolor('blue')
# question 10
 """
# drawing rectangle

A = (100,100)
turtle.penup()
turtle.goto(A)
turtle.pendown()
turtle.forward(100)
turtle.setheading(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
w = int(input("Enter x cor: "))
wa = int(input("Enter y cor: "))
turtle.goto(w,wa)
x = turtle.xcor()
y = turtle.ycor()

if(x>=100 and x<= (100+100) and y>=100 and y<= (100+100)):
    turtle.write("in rect")
else:
    turtle.write("not in rect")
#done
turtle.done()