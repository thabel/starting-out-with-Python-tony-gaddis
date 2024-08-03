# payment intalments 
TAXES = 5/100
amount= float(input("Enter the purchase amount: "))
numberOfInst = int(input('Enter the number of payment instalments: '))
#processing
total = amount + amount*TAXES
print("total cost = ",str(amount),"*",str(TAXES)," + ",amount," = ",total,"$",sep='')
print("the versement by instalmenents = ",total/numberOfInst,"$",sep='')
