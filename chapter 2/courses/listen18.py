#get the desired future value

future_value = float(input('Enter the desired future value: '))

#get the annual interest rate
rate = float(input('Enter the annual interest rate: '))

#get the number of years that the money willl appreciate
years = int(input('Enter the number of years the monney will grow: '))

#calculate the deposit
present_value = future_value/(1.0+rate)**years

#displays the amount needed to deposist
print('You will need to deposit this amoount:',present_value)
