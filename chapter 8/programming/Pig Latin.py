def main():
    user_input = input("Enter your english sentence: ")
    user_input = user_input.upper()
    words = user_input.split()
    pig_latin = [word[1:] + word[0] + 'AY' for word in words]
    print(f'the pig lating equivalent = {" ".join(pig_latin)}')


if __name__ == '__main__':
    main()
