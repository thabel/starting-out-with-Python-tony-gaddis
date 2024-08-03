"""
Suppose you have taken out a loan for a certain amount of money with a fixed monthly inter-
est rate and monthly payments, and you want to determine the monthly payment amount
necessary to pay off the loan within a specific number of months. The formula is as follows:
P 5 R * A
1 2 (1 1 R)
2M
The terms in the formula are:
•	 P is the payment amount per month.
•	 R is the monthly interest rate, as a decimal (e.g. 2.5% 5 0.025).
•	 A is the amount of the loan.
•	 M is the number of months.
Write a program that prompts the user to enter the loan amount, monthly interest rate as
a percentage and desired number of months. The program should pass these values to a
function that returns the monthly payment amount necessary. The program should display
this amount.
"""
def take_input_monthly_payement_of_loan():
    amount = float(input("Enter loan amount: "))
    rate_monthly_interest = float(input("Enter monthly interest rate as a percentage: "))
    months = int(input("Enter desired month: "))
    print("The payement amount per month is  .............. ",round(calculate(amount,rate_monthly_interest,months),2))

def calculate(A,R,M):
    P = (R*A)/(1-pow((1-R),-M))
    return P

from app_frame import app_frame

app_frame(take_input_monthly_payement_of_loan)