#A bill program , display the sum of total item
#takes item prices :
TAXES = 0.07
item1 = float(input("Enter item #1 price: "))
item2 = float(input("Enter item #2 price: "))
item3 = float(input("Enter item #3 price: "))
item4 = float(input("Enter item #4 price: "))
item5 = float(input("Enter item #5 price: "))
val = (item1+item2+item3+item4+item5)
# displays:
print("item#X       ","prices       ","taxes")
print("item#1       ",format(item1,".2f"), format(item1*TAXES,"13.2f"))          
print("item#2       ",format(item2,".2f"), format(item2*TAXES,"13.2f"))       
print("item#3       ",format(item3,".2f"), format(item3*TAXES,"13.2f"))       
print("item#4       ",format(item4,".2f"), format(item4*TAXES,"13.2f"))  
print("item#5       ",format(item5,".2f"), format(item5*TAXES,"13.2f")) 
print("subtotal     ",format(val,".2f"),format(val*TAXES,"13.2f"))   
print("")
print("total = ",format(val+val*TAXES,".2f"),"$",sep='')        