from app_frame import app_frame

print("......................................")
print("       CALORIES FATS AND CAB          ")
print("......................................")


def calculateCalories():
    fat_gram = float(input("Enter fal gram value: "))
    cab_gram = float(input("Enter carbohydrate grams: "))
    print("calories from fat ...................... ", round(fat_gram * 9, 2))
    print("calories from carbohydrate .............", round(cab_gram * 4, 2))

app_frame(calculateCalories)