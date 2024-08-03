"""
The local driver’s license office has asked you to create an application that grades the written portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here
are the correct answers:
1. A
2. C
3. A
4. A
5. D
6. B
7. C
8. A
9. C
10. B
11. A
12. D
13. C
14. A
15. D
16. C
17. B
18. B
19. D
20. A
Your program should store these correct answers in a list. The program should read the
student’s answers for each of the 20 questions from a text file and store the answers in
another list. (Create your own text file to test the application.) After the student’s answers
have been read from the file, the program should display a message indicating whether the
student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
to pass the exam.) It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions, and a list showing the question numbers
of the incorrectly answered questions

"""

STUDENT_FILE_NAME = "students_answer.txt"
CORRECT_ANSWERS_FILE_NAME = "correct_anwser_file.txt"
NUMBER_OF_QUESTION = 20


#  A menu
def menu(starting_menu=True):
    print("*" * 20)
    print("Hello choose your option")
    if starting_menu:
        print("1) next student result")
    else:
        print("1) generate student results")
    print("2) Consult result")
    print("3) quit ")
    print("*" * 20)


def validate_input():
    menu_input = int(input("Enter your choice: "))
    while 1 > menu_input > 3:
        menu_input = int(input("Choice not valid enter 1 or 2 or 3: "))
    return menu_input


def test_if_file_exist(filename=STUDENT_FILE_NAME):
    try:
        file = open(filename, "r")
        file_content = file.read()
        file.close()
        if len(file_content):
            return True
        return False
    except Exception as e:
        return False


def correct_menu():
    if test_if_file_exist():
        menu(starting_menu=True)
    else:
        menu(starting_menu=False)


def main():
    correct_menu()
    current_student_notes()
    user_choice = validate_input()

    while user_choice != 3:
        if user_choice == 1:
            generating_student_results()
        else:
            compute_results()
        # reafficher le menu
        correct_menu()
        current_student_notes()
        user_choice = validate_input()
    print("Bye")


# We cannot generate a result if students_answer is empty or do not exist
def generating_student_results():
    import random
    CHARACTER_A, NUMBER_OF_CHOICE = 65, 4

    with open(STUDENT_FILE_NAME, "w") as file:
        # writing in file
        for i in range(NUMBER_OF_QUESTION):
            student_answer = random.randrange(CHARACTER_A, CHARACTER_A + NUMBER_OF_CHOICE)
            file.write(str(i + 1) + ". " + chr(student_answer) + "\n")


# result computing file
def list_of_result_in_file(filename, delimiter='.', use_delimiter=True):
    results = list()
    if test_if_file_exist(filename):
        with open(filename, "r") as file:
            line = file.readline()
            while line:
                if use_delimiter:
                    results.append(line.split(delimiter)[-1].rstrip())
                else:
                    results.append(line.rstrip())
                line = file.readline()
    return results


# taking the two list : result and correct

def compute_results():
    student_answer = list_of_result_in_file(filename=STUDENT_FILE_NAME)
    correct_answer = list_of_result_in_file(filename=CORRECT_ANSWERS_FILE_NAME)

    if not len(student_answer):
        print("Can not compute results no student answers found !")
    elif not len(correct_answer):
        print("Can not compute results no correct anwsers  found")
    else:
        # everything works well so
        total_point = 0
        not_correct_ans_list = list()
        for i in range(NUMBER_OF_QUESTION):
            if student_answer[i] == correct_answer[i]:
                total_point += 1
            else:
                not_correct_ans_list.append(i + 1)
        # finally
        if is_succed(total_point):
            print("STUDENT SUCCED !!! ")
        else:
            print("student failed ...")
        print("the Final point is : ", total_point, "/", NUMBER_OF_QUESTION)
        print("Missing", NUMBER_OF_QUESTION - total_point, "questions")
        print("Lists of questions failed", not_correct_ans_list)


def is_succed(note):
    if note > 15:
        return True
    else:
        return False


def current_student_notes():
    notes = list_of_result_in_file(filename=STUDENT_FILE_NAME, use_delimiter=False)
    print("current student note:",notes[:NUMBER_OF_QUESTION//2],notes[NUMBER_OF_QUESTION//2:],sep="\n")


# executing the main function
if __name__ == '__main__':
    main()
