"""
This exercise assumes that you have already written the is_prime function in Programming
Exercise 17. Write another program that displays all the prime numbers from 1 to 100.
The program should have a loop that calls the is_prime function
"""

def is_prime(number):
    if number < 0:
        return None
    if number <= 2:
        return True
    div = 2
    while div * div <= number:
        if number % div == 0:
            return False
        div += 1
    return True

for i in range(1, 101):
    if is_prime(i):
        print(i)
