"""Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses."""
from app_frame import app_frame
print("        AUTOMOBILE PROGRAMS          ")
print("......................................")
def automobile_cost(loan_payment, insurance ,gas,oil,tires,maintenance):
    loan_payment = float(loan_payment)
    gas=float(gas)
    insurance=float(insurance)
    oil=float(oil)
    tires=float(tires)
    maintenance=float(maintenance)

    # compute the sum

    total_monthy = loan_payment+gas+insurance+oil+tires+maintenance
    print("The total monthly ...............",total_monthy)
    print("the total anual cost ............",total_monthy*12)

app_frame(automobile_cost,loan_payment="", insurance="" ,gas="",oil="",tires="",maintenance="")