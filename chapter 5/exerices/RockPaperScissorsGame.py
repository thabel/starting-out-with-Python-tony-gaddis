"""
Write a program that lets the user play the game of Rock, Paper, Scissors against the com
puter. The program should work as follows:
1. When the program begins, a random number in the range of 1 through 3 is generated.
If the number is 1, then the computer has chosen rock. If the number is 2, then the
computer has chosen paper. If the number is 3, then the computer has chosen scissors.
(Don’t display the computer’s choice yet.)
2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
3. The computer’s choice is displayed.
4. A winner is selected according to the following rules:
•	 If one player chooses rock and the other player chooses scissors, then rock wins.
(Rock smashes scissors.)
•	 If one player chooses scissors and the other player chooses paper, then scissors wins.
(Scissors cuts paper.)
•	 If one player chooses paper and the other player chooses rock, then paper wins.
(Paper wraps rock.)
•	 If both players make the same choice, the game must be played again to determine
the winner.
"""
ROCK = 1
PAPER = 2
SCISSORS = 3
from random import randrange


def play_game():
    while True:
        computer_choose = randrange(1, 4)
        #  decide
        #  user input
        user_input = input("Enter your choice : “rock” “paper” or “scissors”: ")
        user_choose = choice_to_int(user_input)
        while user_choose is None:
            user_input = input("Invalid enter your choice : “rock” “paper” or “scissors”: ")
            user_choose = choice_to_int(user_input)
        # means user_choose is a valid choose
        if user_choose == computer_choose:
            print("Both choose", int_to_choice(computer_choose), "Play again!")
            continue
        if computer_choose == which_win(computer_choose, user_choose):
            print("You loose , computer choosed ", int_to_choice(computer_choose), "and you", user_input)
        else:
            print("You Win ! , computer choosed ", int_to_choice(computer_choose), "and you", user_input)


def choice_to_int(str):
    if str.lower() == "rock":
        return ROCK
    elif str.lower() == "paper":
        return PAPER
    elif str.lower() == "scissors":
        return SCISSORS
    else:
        return None


def int_to_choice(int_):
    if int_ == 1:
        return "rock"
    elif int_ == 2:
        return "paper"
    else:
        return "scissors"


def which_win(choice_1, choice_2):
    if choice_1 == ROCK and choice_2 == SCISSORS:
        return ROCK
    elif choice_1 == SCISSORS and choice_2 == PAPER:
        return SCISSORS
    elif choice_1 == PAPER and choice_2 == ROCK:
        return PAPER
    else:
        which_win(choice_2, choice_1)


play_game()
