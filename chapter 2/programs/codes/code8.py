# Tip , Tax,Total
TAXES = 7/100
TIP = 18/100
amount = float(input("Enter the amount of the food $: "))
tip=  amount*TIP
tax = amount*TAXES

print("amount: ",format(amount,".2f"),"$",sep='')
print("tip: ",format(tip,".2f"),"$",sep='')
print("taxes: ",format(tax,".2f"),"$",sep='')
print("total: ",format(amount+tip+tax,".2f"),"$",sep='')