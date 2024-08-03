"""
Write a program that generates a random number in the range of 1 through 100, and asks
the user to guess what the number is. If the user’s guess is higher than the random number,
the program should display “Too high, try again.” If the user’s guess is lower than the
random number, the program should display “Too low, try again.” If the user guesses the
number, the application should congratulate the user and generate a new random number
so the game can start over.
Optional Enhancement: Enhance the game so it keeps count of the number of guesses that
the user makes. When the user correctly guesses the random number, the program should
display the number of guesses.
"""
from random import randrange


def guessing_number_game():
    while True:
        number = randrange(1, 100)
        count = 0
        user_number = int(input("Enter your number: "))
        while number != user_number:
            if user_number > number:
                print("your number is hight !")
            else:
                print("Your number is low !")
            user_number = int(input("Try again : "))
            count += 1
        print("Good guess. Guessed after",count,"guesses")


guessing_number_game()
