userNum = int(input("Enter a number: "))

if(userNum>0):
    print(userNum,'is positive')
elif(userNum<0):
    print(userNum,'is negative')
else:
    print(userNum,'= zero')

if(userNum%2==0):
    print(userNum,'is even')
else:
    print(userNum,'is odd')
