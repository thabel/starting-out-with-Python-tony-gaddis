# This program demonstrates the BankAccount class
# with the _ _str_ _ method added to it.

import listen_9 as bankaccount2


def main():
    # Get the starting balance.
    start_bal = float(input("Enter your starting balance: "))

    # Create a BankAccount object.
    savings = bankaccount2.BankAccount(start_bal)

    # Deposit the user's paycheck.
    pay = float(input("How much were you paid this week? "))
    print("I will deposit that into your account.")
    savings.deposit(pay)

    # Display the balance.
    print(savings)

    # Get the amount to withdraw.
    cash = float(input("How much would you like to withdraw? "))
    print("I will withdraw that from your account.")
    savings.withdraw(cash)

    # Display the balance.
    print(savings)

    # Call the main function.
main()
