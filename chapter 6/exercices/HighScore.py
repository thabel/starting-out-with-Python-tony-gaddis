"""
Assume that a file named scores.txt exists on the computer’s disk. It contains a series of
records, each with two fields – a name, followed by a score (an integer between 1 and 100).
Write a program that displays the name and score of the record with the highest score, as
well as the number of records in the file. (Hint: Use a variable and an “if” statement to
keep track of the highest score found as you read through the records, and a variable to
keep count of the number of records.)
"""

file_name = "students.txt"
try:
    with open(file_name,"r") as file:
        i = 0
        name = file.readline()
        hight_score,std_name = 0,0
        while name!="":
            score = file.readline()
            if(int(score) > hight_score):
                hight_score = int(score)
                std_name = name
            name = file.readline()
            i += 1

        print("There is a total of",i,"records in",file_name)
        print("they highest score: ", hight_score)
        print("Stduent: ",std_name)
except:
    print("Error when opening file!")
