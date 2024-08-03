# LEAP YEAR
year = int(input("Enter the number of year: "))
if(year%100 == 0):
    if(year%400 == 0):
        print(year,"february has 29 days")
    else:
        print(year,"february has 28 days")
else :
    if(year%4 == 0):
        print(year,"february has 29 days")
    else:
        print(year,"february has 28 days")