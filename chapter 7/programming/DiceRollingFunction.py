"""
In a program, write a function named roll that accepts an integer argument number_
of_throws. The function should generate and return a sorted list of number_of_throws
random numbers between 1 and 6. The program should prompt the user to enter a positive
integer that is sent to the function, and then print the returned list.
"""

from random import randrange


def roll(number_of_throws):
    rand_numbers = list()
    for i in range(number_of_throws):
        rand_numbers.append(randrange(1, 7))
    rand_numbers.sort()
    return rand_numbers


# prompt the user
postive_number = int(input('Enter positive number: '))

while postive_number<0:
    postive_number = int(input(' Please enter positive number: '))

print("List of choice = ", roll(postive_number))
