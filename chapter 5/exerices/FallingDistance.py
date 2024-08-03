"""
When an object is falling because of gravity, the following formula can be used to deter
mine the distance the object falls in a specific time period:
d 5 ½ gt2
The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the
amount of time, in seconds, that the object has been falling.
Write a function named falling_distance that accepts an object’s falling time (in seconds)
as an argument. The function should return the distance, in meters, that the object has
fallen during that time interval. Write a program that calls the function in a loop that passes
the values 1 through 10 as arguments and displays the return value.
"""

G_CONSTANT = 9.8


def falling_distance(time):
    return 1 / 2 * G_CONSTANT * time * time


# calling the function in a loop
for i in range(1, 11):
    print("for time of falling =", i, "distance is=", round(falling_distance(i), 2))
