# Grade Calculator.
test_1_ = int(input("Enter test one points (0-25): "))
test_2_ = int(input("Enter test one points (0-25): "))
exam = int(input("Enter exam points (0-50): "))

if(test_1_<0 or test_1_ >25):
    print(test_1_,'is not a valid mark')
elif(test_2_<0 or test_2_ >25):
    print(test_2_,'is not a valid mark')
elif(exam<0 or exam >50):
    print(exam,'is not a valid mark')
else:
    note = test_1_+test_2_+exam
    if(exam < 25 or note < 50):
        print('total =',note,'grade = Fail')
    elif(note>=80):
        print('total =',note,'grade = Distinction')
    elif(note < 80 and note>=60):
        print('total =',note,'grade = Credit')
    elif(note < 80):
        print('total =',note,'grade = Pass')