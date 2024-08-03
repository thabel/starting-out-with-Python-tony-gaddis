"""
Write a function named max that accepts two integer values as arguments and returns the
value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
the function, the function should return 12. Use the function in a program that prompts the
user to enter two integer values. The program should display the value that is the greater
of the two.
"""

from app_frame import app_frame


def max_(a, b):
    a = float(a)
    b = float(b)

    if a > b:
        print("the max between", a, "and", b, "is", a)
    else:
        print("the max between", a, "and", b, "is", b)


app_frame(max_, a="", b="")
