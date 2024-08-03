"""
Write a program that asks the user to enter a series of single-digit numbers with nothing
separating them. The program should display the sum of all the single digit numbers in the
string. For example, if the user enters 2514, the method should return 12, which is the sum
of 2, 5, 1, and 4.
"""


def main():
    digit_string = take_input()
    somme = 0
    for _ in digit_string:
        somme += int(_)
    print(f"La somme de {digit_string} est {somme}")


def take_input():
    digit_string = input('Enter a series of single-digit numbers with nothing\
separating them: ')
    while not digit_string.isdigit():
        digit_string = input('Please enter a series of single-digit numbers with nothing\
        separating them: ')
    return digit_string


if __name__ == '__main__':
    main()
