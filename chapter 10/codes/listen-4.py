import random
from math import sqrt
 # The Coin class simulates a coin that can
 # be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):
        self.__sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(this):
        return this.__sideup
    
    
# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()
    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    # Toss the coin.
    # But now I'm going to cheat! I'm going to
    # directly change the value of the object's
    # sideup attribute to 'Heads'.
    print('I am tossing the coin 10 times ...')
    for i in range(10):     
        my_coin.toss()
        print(my_coin.get_sideup())

    # Call the main function.
main()