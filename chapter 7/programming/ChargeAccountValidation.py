"""
If you have downloaded the source code from the Premium Companion Website you will
find a file named charge_accounts.txt in the Chapter 07 folder. This file has a list of a
company’s valid charge account numbers. Each account number is a seven-digit number,
such as 5658845.
Write a program that reads the contents of the file into a list. The program should then
ask the user to enter a charge account number. The program should determine whether
the number is valid by searching for it in the list. If the number is in the list, the program
should display a message indicating the number is valid. If the number is not in the list, the
program should display a message indicating the number is invalid.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.)
"""

# read the content into a list

with open("charge_account.txt", "r") as file:
    list_of_data = file.readlines()
    list_of_data = [float(i) for i in list_of_data]

charge_account_number = float(input("Enter charge account number: "))
if charge_account_number in list_of_data:
    print("number is valid")
else:
    print("number is not valid")