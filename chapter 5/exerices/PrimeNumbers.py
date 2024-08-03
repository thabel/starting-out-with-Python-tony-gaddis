"""
A prime number is a number that is only evenly divisible by itself and 1. For example, the
number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6.
Write a Boolean function named is_prime which takes an integer as an argument and
returns true if the argument is a prime number, or false otherwise. Use the function in
a program that prompts the user to enter a number then displays a message indicating
whether the number is prime.
"""


def is_prime(number):
    number = int(number)
    if number < 0:
        return None
    if number <= 2:
        print(number, "is  prime!")
        return True
    div = 2
    while div * div <= number:
        if number % div == 0:
            print(number, "is not prime.")
            return False
        div += 1
    print(number, "is  prime!")
    return True


from app_frame import app_frame

app_frame(is_prime, number="s")
