"""
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
$15, and Class C seats cost $10. Write a program that asks how many tickets for each class
of seats were sold, then displays the amount of income generated from ticket sales.
"""
from app_frame import app_frame
CLASS_A_PRICE = 20
CLASS_B_PRICE = 15
CLASS_C_PRICE = 10
print("......................................")
print("       STADIUM STATES CALCULATION          ")
print("......................................")


def StadiumSeatsCalulation():
    seats_for_class_A = float(input("Enter seats for class A: "))
    seats_for_class_B = float(input("Enter seats for class B: "))
    seats_for_class_C = float(input("Enter seats for class C: "))

    print("Class A income .......................... ", seats_for_class_A * CLASS_A_PRICE)
    print("Class B income .......................... ", seats_for_class_B * CLASS_B_PRICE)
    print("Class C income .......................... ", seats_for_class_C * CLASS_C_PRICE)


app_frame(StadiumSeatsCalulation)
