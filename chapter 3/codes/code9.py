# Roulette Wheel Color.

pocket = int(input("Pick a pocket number (0-36): "))

if(pocket==0):
    print(pocket,'color is','green')
# odd = red , even = black
elif((pocket >= 1 and pocket<= 10) or(pocket >= 19 and pocket<= 28) ):
    if(pocket%2 != 0):
        print(pocket,'color is','red')
    else:
        print(pocket,'color is','black')
# odd = black , even = red
elif((pocket >= 11 and pocket<= 18) or (pocket >= 29 and pocket<= 36)):
    if(pocket%2 != 0):
        print(pocket,'color is','black')
    else:
        print(pocket,'color is','red')

else:
    print("Error number must be in rage (0-36)")