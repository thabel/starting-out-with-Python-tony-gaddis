"""
Write a program that asks the user for the name of a file. The program should display only
the first five lines of the file’s contents. If the file contains less than five lines, it should
display the file’s entire contents.
"""

file_name = input("Enter filename: ")
try:
    with open(file_name,"r") as file:
        i = 0
        line = file.readline()
        while line!="" and i<5:
            print(line,end="")
            line = file.readline()
            i += 1
except:
    print("Error when opening file!")

