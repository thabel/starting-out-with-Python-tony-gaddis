"""
The Springfork Amateur Golf Club has a tournament every weekend. The club president
has asked you to write two programs:
1. A program that will read each player’s name and golf score as keyboard input, then
save these as records in a file named golf.txt. (Each record will have a field for the
player’s name and a field for the player’s score.)
2. A program that reads the records from the golf.txt file and displays them.
"""

file_name = "golf.txt"
continue_oder = 'y'
from FileDisplay import read_file
i = 0
try:
    with open(file_name,"w") as file:
        while continue_oder.lower() == "y":
            file.write(input("Enter name of player  #"+str(i+1)+": ")+"\n")
            file.write(input("Enter score of player  #" + str(i + 1) + ": ") + "\n")
            i += 1
            continue_oder = input("Add another player? y or n?: ")
        print("Players save successfully")
    print("Here is the content .... ")
    read_file(file_name)
except:
    print("Error when opening file!")

