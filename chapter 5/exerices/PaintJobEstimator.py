"""
A painting company has determined that for every 112 square feet of wall space, one gallon
of paint and eight hours of labor will be required. The company charges $35.00 per hour
for labor. Write a program that asks the user to enter the square feet of wall space to be
painted and the price of the paint per gallon. The program should display the following data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
"""
from app_frame import app_frame

# 112 square one gallon and 8 hours == 8*35 == payed

HOURLY_LABOUR = 35
SQUARE_PER_GALLONS = 112
HOUR_PER_GALLONS = 8


def PaintJobEstimator():
    square_feet = float(input("Enter square feet:  "))
    price_for_gallons = float(input("Enter price of the paint of gallons: "))

    # number of gallons of paint required

    number_of_gallons = square_feet / SQUARE_PER_GALLONS
    hours_required = number_of_gallons * HOUR_PER_GALLONS
    cost_of_paint = number_of_gallons * price_for_gallons
    labor_charge = hours_required * HOURLY_LABOUR
    total_const = cost_of_paint + labor_charge

    print("The number of gallons of paint required ............", number_of_gallons)
    print("The hours of labor required ........................", hours_required)
    print("The labor charges ..................................", labor_charge)
    print("The cost of the paint ..............................",cost_of_paint)
    print("The total cost of the paint job ....................", total_const)
app_frame(PaintJobEstimator)