"""Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a
random response to a yes or no question. In the student sample programs for this book, you
will find a text file named 8_ball_responses.txt. The file contains 12 responses, such
as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. The program should
read the responses from the file into a list. It should prompt the user to ask a question, then
display one of the responses, randomly selected from the list. The program should repeat
until the user is ready to quit"""
import random


def read_file_lines(file="8_ball_responses.txt"):
    try:
        with open(file, "r",encoding="utf8") as fp:
            read_list = fp.readlines()
            return read_list
    except IOError:
        print(f"{file} can not be read")
        exit(1)

def main():
    question = input('Ask a question or tape q to quit: ')
    lit_answers = read_file_lines()
    while question != 'q':
        print(lit_answers[random.randrange(0,len(lit_answers))],end="")
        question = input('Ask another question or tape q to quit: ')

if __name__ == '__main__':
    main()