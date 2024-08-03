def main():
    user_input = input("Enter your string: ")
    print(f"Number of vowels = {count(user_input, is_vowels)}")
    print(f"Number of consonants = {count(user_input, is_consonant)}")


def is_vowels(ch):
    return ch in "aeiouy"


def count(string, f):
    res = 0
    for ch in string:
        if f(ch):
            res += 1
    return res


def is_consonant(ch):
    return ch.isalpha() and not is_vowels(ch)


if __name__ == '__main__':
    main()
