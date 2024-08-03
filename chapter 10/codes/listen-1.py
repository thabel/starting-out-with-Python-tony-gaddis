import random
from math import sqrt
 # The Coin class simulates a coin that can
 # be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(this):
        this.sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tai'
    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(this):
        return this.sideup


def binarySearch(number,v):
    l = 0
    h = len(number)-1
    while ( l< h):
        mid = (l+h)//2
        if v > number[mid]:
            l = mid+1
        elif v < number[mid]:
            h = mid
        else:
            return True
    return False


number = [random.randint(0,100) for _ in range(7)]
v = 14
number.sort()
print(v,"in", number,"=",binarySearch(number,v))