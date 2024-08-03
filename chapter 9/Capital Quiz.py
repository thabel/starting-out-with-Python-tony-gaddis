import json
import random

TOTAL_QUIZES = 5

points = {
    "well guess": 0,
    "bad guess": 0
}


def main():
    with open("UsaCapitales.json", "r") as f:
        capitals = json.load(f)
    choice = set()
    while len(choice) != TOTAL_QUIZES:
        choice.add(random.choices(list(capitals))[0])
    print(choice)

    # ask for user inputs
    for index, sate in enumerate(choice):
        capital = input(f'N°- {index + 1} Enter the capital of {sate}: ')
        if capital == capitals[sate]:
            points["well guess"] += 1
            print("Correct")
        else:
            points["bad guess"] += 1
            print(f'No it s {capitals[sate]}')

    print(f'the total correct response is {points["well guess"]}')
    print(f'the total incorrect response is {points["bad guess"]}')

    print("Bye!")


if __name__ == '__main__':
    main()
