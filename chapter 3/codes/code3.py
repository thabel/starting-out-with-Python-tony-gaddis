# Quater of the year
monthNum = int(input("Enter the number of the month(1-12): "))

if(monthNum>=1 and monthNum<=3):
    print("month is in first quarter.")
elif(monthNum>=4 and monthNum<=6):
    print("month is in second quarter.")
elif(monthNum>=7 and monthNum<=9):
    print("month is in third quarter.")
elif(monthNum>=10 and monthNum<=12):
    print("month is in fourth quarter.")
else:
    print("Error month need to be (1-12).")