"""Write a program that asks the user to enter five test scores. The program should display a
letter grade for each score and the average test score. Write the following functions in the
program:
•	 calc_average. This function should accept five test scores as arguments and return the
average of the scores.
•	 determine_grade. This function should accept a test score as an argument and return
a letter grade for the score based on the following grading scale:
Score Letter Grade
90–100 A
80–89 B
70–79 C
60–69 D
Below 60 F
"""
def calc_average():
    # accept five score and display his grade
    score_1 = float(input("Enter score 1: "))
    score_2 = float(input("Enter score 2: "))
    score_3 = float(input("Enter score 3: "))
    score_4 = float(input("Enter score 4: "))
    score_5 = float(input("Enter score 5: "))

    total = score_1+score_2+score_3+score_4+score_5
    print("         SCORE           |           GRADE           ")
    print(round(score_1,2),".................................",determine_grade(score_1))
    print(round(score_2, 2), "................................", determine_grade(score_2))
    print(round(score_3, 2), "................................", determine_grade(score_3))
    print(round(score_4, 2), "................................", determine_grade(score_4))
    print(round(score_5, 2), "................................", determine_grade(score_5))

    print("                     TOTAL                           ")
    print(format(total,"4.2f"))
    print("                     AVERAGE                         ")
    print(format(total/5,"4.2f"))
def determine_grade(test_core):
    if test_core>=90 and test_core <= 100:
        return "A"
    elif test_core>=80 and test_core >=89:
        return "B"
    elif test_core>=70 and test_core >=79:
        return "C"
    elif test_core>=60 and test_core >=69:
        return "D"
    elif test_core<60:
        return "F"
    else:
        return None
calc_average()