import pickle


def main():
    with open("codes.dat", "rb") as f:
        codes = pickle.load(f)

    print(f"codes>{codes}")


if __name__ == '__main__':
    main()
