"""
Write a program that asks the user how many words they would like to write to a file, and
then asks the user to enter that many words, one at a time. The words should be written
to a file.
"""

file_name = "wordlist.txt"
number = int(input('How many words you want to write?: '))
try:
    with open(file_name,"w") as file:
        for i in range(number):
            file.write(input("Enter word #"+str(i+1)+": ")+"\n")
        print("Words save successfully")
except:
    print("Error when opening file!")