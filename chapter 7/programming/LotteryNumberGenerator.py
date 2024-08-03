"""
Design a program that generates a seven-digit lottery number. The program should generate
seven random numbers, each in the range of 0 through 9, and assign each number to a
list element. (Random numbers were discussed in Chapter 5.) Then write another loop that
displays the contents of the list.
"""
from random import randrange

empty_list = list()


def generate_seven_numbers():
    for i in range(7):
        empty_list.append(randrange(0, 9))


generate_seven_numbers()
for i in empty_list:
    print(i,end="")