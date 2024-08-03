""" #performing variables:
# question 4
w=5
x =4
y=8
z=2
result = x+y
#result = 12
print(result)
result = z*2
#result = 4
print(result)
result = y/x
#result = 2
print(result)
result = y-z
#result = 6
print(result)
result = w//z
#result = 5//2 = 2
print(result)
product = 10*15
#question 5
print(product)
# question 6
down_payement = 50
total = 25
due = total-down_payement

#question 7
RATE = 0.15
subtotal = 5
total = subtotal*RATE 

#question 8
a = 5
b = 2
c= 3
result = a+b*c
print(result) # it would be 5 +2*3 = 11

#question 9
num = 99
num = 5
print(num) # it would be 5

# question 10
sales = 10589255.00785125554
print(format(sales,".2f")) # we can use the format fonction
#in order to format a number 

# question 11
number = 1234567.456
print(format(number,",.1f"))

# question 12
print('X\tO\tX\nO\tX\tO\nX\tO\tX\n')
#output X   O   X
#       O   X   O
#       X   O   X
#  

# question 14
import turtle
turtle.showturtle()
turtle.circle(75)
turtle.done()

# question 14
import turtle
turtle.showturtle()
turtle.fillcolor("blue")
turtle.begin_fill()
#One line
turtle.forward(100)
turtle.left(90)
#two line
turtle.forward(100)
turtle.left(90)
#three line
turtle.forward(100)
turtle.left(90)
#last line
turtle.forward(100)
turtle.end_fill()
turtle.done() """

# question 15
# Center Coordinate
CENTER_C =(0,-40)
# A
A_Cor = (-50,50)
# B
B_Cor = (-50,-50)
#C
C_Cor = (50,-50)
# D 
D_Cor = (50,50)
import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(A_Cor)
turtle.pendown()
turtle.goto(B_Cor)
turtle.goto(C_Cor)
turtle.goto(D_Cor)
turtle.goto(A_Cor)
turtle.penup()

turtle.goto(CENTER_C)
turtle.begin_fill()
turtle.fillcolor("red")
turtle.circle(40)
turtle.end_fill()
turtle.end_fill()

turtle.done()