import pickle
import random

codes = dict()


def main():
    for i in range(26):
        codes[chr(65 + i)] = chr(random.choice(range(35, 126)))
        codes[chr(65 + i).lower()] = chr(random.choice(range(35, 126)))
    with open("codes.dat", "wb") as f:
        pickle.dump(codes, f)
    print(codes)

if __name__ == '__main__':
    main()