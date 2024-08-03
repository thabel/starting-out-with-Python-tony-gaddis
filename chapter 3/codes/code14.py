# Body Mass Index
BMI_CONSTANT = 703
LOWER_BMI = 18.5
UPPER_BMI = 25
weight = float(input("Enter weigh in pounds: "))
height = float(input("Enter height in inches: "))
bmi = weight*BMI_CONSTANT/(height**2)

if(bmi<LOWER_BMI):
    print('BMI =',format(bmi,".2f"),'\nConlusion: You are Underweight')
elif(bmi>= LOWER_BMI and bmi<= UPPER_BMI):
    print('BMI =',format(bmi,".2f"),'\nConlusion: Your weight is optimal')
else:
    print('BMI =',format(bmi,".2f"),'\nConlusion: You are Overweight')
