"""
One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
of feet as an argument and returns the number of inches in that many feet. Use the function
in a program that prompts the user to enter a number of feet then displays the number of
inches in that many feet
"""

from app_frame import app_frame

ONE_FOOT_TO_INCHES = 12


def feet_to_inches(number_of_feet):
    number_of_feet = float(number_of_feet)
    print("there is", number_of_feet * ONE_FOOT_TO_INCHES, "inches in", number_of_feet, "feet")


app_frame(feet_to_inches, number_of_feet="")
