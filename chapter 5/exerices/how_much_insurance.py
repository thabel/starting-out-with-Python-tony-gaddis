"""Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a program
that asks the user to enter the replacement cost of a building, then displays the minimum
amount of insurance he or she should buy for the property."""
from app_frame import app_frame
RATE = 80/100
def amount_to_pay():
    replacement_cost = float(input("Enter the replacement cost: "))
    # amount of assurance to buy for the house
    print("You need to buy",round(replacement_cost*RATE,2))

app_frame(amount_to_pay)