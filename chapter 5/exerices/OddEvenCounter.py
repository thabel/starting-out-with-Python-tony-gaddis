"""
In this chapter, you saw an example of how to write an algorithm that determines
whether a number is even or odd. Write a program that generates 100 random numbers
and keeps a count of how many of those random numbers are even, and how many of
them are odd.
"""

from random import randint

# geneate x numbers
x = 100
even = 0
odd = 0
for i in range(x):
    number = randint(0,1000)
    print("number ",i,"=",number,end=" ")
    if number%2:
        odd+=1
    else:
        even += 1
print("\nThere are",even,"evens and ",odd,"odd numbers!")


