# Book Sellers 
userNumBook = int(input("Enter the number of books pursached this month: "))

if(userNumBook == 0):
    point = 0
    print("you earned",point,'points')
elif(userNumBook==2):
    point = 5
    print("you earned",point,'points')
elif(userNumBook==4):
    point = 15
    print("you earned",point,'points')
elif(userNumBook==6):
    point = 30
    print("you earned",point,'points')
elif(userNumBook==8):
    point = 60
    print("you earned",point,'points')
else:
    print(userNumBook,"not considered in the awarding program")
