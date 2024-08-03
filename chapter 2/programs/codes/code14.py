# Compound interest:
#Inputs:
Principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the anual interest rate(scale of 100): "))
rate /= 100
nomberOfTimeCompounded = float(input("Enter the number of time interest is compounded: "))
tyears = int(input("Enter the number of year account will be left: "))
#Process
Amount = Principal*(1+rate/nomberOfTimeCompounded)**(nomberOfTimeCompounded*tyears)
#Output 
print("the amount after",tyears,"is :",Amount)