# Money Counting Game:
pennies = int(input("Enter the number of pennies: "))
nickels =  int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

total = pennies/100 +nickels/20 + quarters/4 + dimes/10
if(total>1):
    print(pennies,' pennis ',nickels,' nickels ',quarters,' quarters : ',format(total,".2f"),'$',sep='',end=' ')
    print('is > than 1$')
else:
    print(pennies,' pennis ',nickels,' nickels ',quarters,' quarters : ',total,'$',sep='',end=' ')
    print('is = 1$ !')