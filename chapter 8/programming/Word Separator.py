import re

PATTERNS = r"^[A-Z].*\.$"


def take_input():
    user_input = input("Enter a sentence: ")
    if re.search(PATTERNS, user_input):
        print("Yes")
        return user_input
    else:
        print("+No")
        exit(1)


def main():
    user_input = take_input()
    new_str = user_input[0]
    for ch in user_input[1:]:
        if ch.isupper():
            new_str += ' ' + ch.lower()
        else:
            new_str += ch
    print("the new text : ", new_str)


if __name__ == '__main__':
    main()
