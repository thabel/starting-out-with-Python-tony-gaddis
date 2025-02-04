# The BankAccount class simulates a bank account.


class BankAccount:

    # The _ _init_ _ method accepts an argument for
    # the account's balance. It is assigned to
    # the _ _balance attribute.

    def __init__(self, bal:float):
        self.__balance = bal

    # The deposit method makes a deposit into the
    # account.

    def deposit(self, amount:float):
        self.__balance += amount

    # The withdraw method withdraws an amount
    # from the account.

    def withdraw(self, amount:float):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: Insufficient funds")

    # The get_balance method returns the
    # account balance.

    def get_balance(self):
        return self.__balance
