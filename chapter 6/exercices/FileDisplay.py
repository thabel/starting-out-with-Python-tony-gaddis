"""
Assume a file containing a series of integers is named numbers.txt and exists on the com
puter’s disk.
Write a program that displays all the n
"""


def read_file(file_name, mode="r"):
    with open(file_name, mode) as file:
        for line in file:
            print(line, end="")

# read_file("numbers.txt","r")
