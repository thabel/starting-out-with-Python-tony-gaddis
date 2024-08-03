"""
Write a program that asks the user for the name of a file. The program should display the
contents of the file with each line preceded with a line number followed by a colon. The
line numbering should start at 1.
"""

file_name = input("Enter filename: ")
try:
    with open(file_name,"r") as file:
        i = 1
        line = file.readline()
        while line!="":
            print(str(i)+":",line,end="")
            line = file.readline()
            i += 1
except FileNotFoundError as e:
    print("Error when opening file!",e)

