# Software Sales.
TEN_NINETINE = 10 / 100
TWENTY_FORTYNINE = 20 / 100
FIFTY_NINETYNINE = 30 / 100
HUNDRED_MORE = 40 / 100
# 99$
PRICE = 99
# inputs
package = int(input("Enter the number of package: "))
if 10 <= package <= 19:
    discount = TEN_NINETINE
    price = package * PRICE
elif 20 <= package <= 49:
    discount = TWENTY_FORTYNINE
    price = package * PRICE
elif 50 <= package <= 99:
    discount = FIFTY_NINETYNINE
    price = package * PRICE
elif package >= 100:
    discount = HUNDRED_MORE
    price = package * PRICE
else:
    discount = 0
    price = package * PRICE
    print('No discount!')

print('Initial price = ', price, '$', sep='')
price -= price * discount
print('Discount = ', format(discount, '.2%'))
print('Final total = ', price, '$', sep='')
