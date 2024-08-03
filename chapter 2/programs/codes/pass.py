# password Code 

password = input("enter your password: ")
while(len(password)<9):
    print("password too week only",len(password),"letters")
    password = input("enter your password: ")
if(len(password)>=9 or len(password)>= 12 ):
    print("medium password with",len(password),"letters")
else:
    print("perfet password !!!")
