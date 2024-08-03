"""
Python allows you to repeat a string by multiplying it by an integer, e.g. 'Hi' * 3 will give
'HiHiHi'. Pretend that this feature does not exist, and instead write a function named
repeat that accepts a string and an integer as arguments. The function should return a
string of the original string repeated the specified number of times, e.g. repeat('Hi', 3)
should return 'HiHiHi'.
"""

# Own repeat function
from app_frame import app_frame


def repeat(string, number):
    a = ''
    number = int(number)
    for i in range(number):
        a += string
    print("Repeat(", string, ",", number, ") = ", a)


app_frame(repeat, string="", number=0)
