"""
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list then display the following data:
•	 The lowest number in the list
•	 The highest number in the list
•	 The total of the numbers in the list
•	 The average of the numbers in the list
"""

# Enter a series of 20 numbers:
MAX_NUMBER = 5
numbers = [float(input('Enter number #' + str(i + 1) + " : ")) for i in range(MAX_NUMBER)]

print('the lowest : ...............', min(numbers))
print('the largest : ...............', max(numbers))
print('the total : .................', sum(numbers))
print('the average : ................', round(sum(numbers) / len(numbers), 2))
