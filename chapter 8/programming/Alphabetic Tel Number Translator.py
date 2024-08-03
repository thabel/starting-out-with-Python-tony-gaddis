# take user inputs
import re

INPUT_PATTERNS = r"\w{3}-\w{3}-\w{4}"

NUMBER_OF_PACK = 3


def character_to_number(ch):
    ch = ord(ch) - ord('A')
    return str(ch // NUMBER_OF_PACK + 2)


def take_input():
    # accept only 10 character
    user_str = input("Enter the tel number: ")
    user_str = user_str.upper()
    match = re.search(INPUT_PATTERNS, user_str)
    if match:
        value = match.group()
        print("Yes", value)
        return value
    else:
        print("Not the correct format XXX-XXX-XXXX")


def main():
    user_value = take_input()
    new_string = ''
    for ch in user_value:
        if ch.isalpha():
            num = character_to_number(ch)
            new_string += num
        else:
            new_string += ch
    print(new_string)


if __name__ == '__main__':
    main()
