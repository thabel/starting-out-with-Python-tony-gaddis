# Magic Dates
userMonth = int(input("Enter the month numerical value: "))
userDay = int(input("Enter the day (1-31): "))
userYear = int(input("Enter the year (two digit): "))
if(userDay<1 or userDay>31):
    print('invalid day.')
elif(userYear<0 or userYear>100):
    print('invalid yar')
elif(userMonth<0 or userMonth>12):
    print('invalid month.')
elif(userMonth*userDay == userYear):
    print('the day is magical')
else:
    print('the day is not magical')