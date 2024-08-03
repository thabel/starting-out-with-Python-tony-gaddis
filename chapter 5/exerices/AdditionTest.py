"""
Write a program that generates printable addition tests. The tests should consist of 5 ques
tions which present a simple addition question in the following format, where the question
number goes from 1 to 5, and num1 and num2 are randomly generated numbers between
1 and 10:
 Question 1
 num1 + num2 = _____
The program should simply display the 5 questions – it should not prompt the user for any
input
"""

from random import randint
from app_frame import app_frame
def generate_questions():
    for i in range(1,6):
        num_1 = randint(1,11);num_2 = randint(1,11)
        print("Question",i)
        print(num_1,"+",num_2,"= _____")
app_frame(generate_questions)