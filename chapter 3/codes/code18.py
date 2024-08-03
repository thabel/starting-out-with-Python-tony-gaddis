# 

vegflag = veganFlag = GlutenFree = False
ans = input('Is anyone in your party a vegetarian? <yes><no>: ')
if(ans=='yes'):
    vegflag = True
ans = input('Is anyone in your party a vegan? <yes><no>: ')
if(ans=='yes'):
    veganFlag = True
ans = input('Is anyone in your party gluten-free? <yes><no>: ')
if(ans=='yes'):
    GlutenFree = True

if(vegflag == False and GlutenFree == False and veganFlag == False):
    print('Joe’s Gourmet Burgers')

if(veganFlag== False ):
    print('Main Street Pizza Company')
if(veganFlag or vegflag or GlutenFree):
    print('Corner Café')
    print("The Chef's Kitchen")
if( veganFlag==False and GlutenFree==False):
    print("Mama's Fine Italians")

