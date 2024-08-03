# Shipping charges.
userWeight = float(input("Enter the weight of the package: "))
if(userWeight <= 0):
    print("Not in charge.")
elif(userWeight<= 2):
    print('shipping charge :$1.50')
elif(userWeight>2 and userWeight<=6):
    print('shipping charge :$3.00')
elif(userWeight>6 and userWeight<=10):
    print('shipping charge :$4.00')
else:
    print('shipping charge :$4.75')