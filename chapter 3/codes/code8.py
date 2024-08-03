# Hot dog Cook Out Program
# the program calculate the
# -the number of packages of hot dogs and the number of packages of 
# hot dog buns needed for a cookout, with the minimum amount of leftovers.
HOTDOGPACK = 10
HOTDOGBUNSPACK = 8
userPeople = int(input("Enter the number of people "
    "attending the cookout: "))
userHotDogPerPerson =  int(input("the number of hot-dog each person will be given: "))

totalHot = userPeople*userHotDogPerPerson
# out puts:
# package (mini) of hot-dog need 
# min of hot-dog burns needed
# hot dog left overs
# burns left overs
hot = totalHot//HOTDOGPACK
buns = totalHot//HOTDOGBUNSPACK

if((totalHot -hot*HOTDOGPACK) != 0):
    hot +=1
if((totalHot-buns*HOTDOGBUNSPACK)!= 0):
    buns += 1
print('package of hot dog needed = ',hot)
print('package of hot burns needed = ',buns)

print("Dog left over ",HOTDOGPACK*hot-totalHot)
print("Buns left over ",HOTDOGBUNSPACK*buns-totalHot)