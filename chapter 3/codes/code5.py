# Mass and weight
GRAVITY = 9.8
mass = float(input("Enter object mass kg: "))

weight = mass*GRAVITY
if(weight>500):
    print('objects is too heavy',weight,'newton >','500 Newtons')
else:
    print('object is too light',weight,'newton <','500 Newtons')