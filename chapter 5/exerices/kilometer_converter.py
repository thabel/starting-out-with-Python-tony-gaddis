"""

Write a program that asks the user to enter a distance in kilometers, then converts that
distance to miles. The conversion formula is as follows:
Miles 5 Kilometers 3 0.6214
"""

KILO_TO_MILES = 0.6214
can_continue = 'y'
print("_______________Conversion Programm__________________")
while(can_continue != 'q'):
    a = float(input("Enter distance in kilometer: "))

    print(a,"kilometers ----------------- ",round(a*KILO_TO_MILES,2),"miles")
    can_continue = input("Continue? press q to quit or anything to continue : ")
    can_continue = can_continue[0].lower()
