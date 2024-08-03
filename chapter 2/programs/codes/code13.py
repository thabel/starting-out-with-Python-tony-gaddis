#Planting Grapevines
Vines_number=0
RowLength = float(input("the length of row in feet: "))
Espaceamount = float(input("the amount of space used by an end-post assembly,in feet: "))
Sapcebetween = float(input("the amount space between the vines, in feet: "))

print("the number of grapevines in the row will be :",(RowLength-2*Espaceamount)/Sapcebetween)