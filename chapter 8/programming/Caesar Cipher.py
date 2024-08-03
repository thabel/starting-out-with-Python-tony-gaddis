def main():
    # take user input
    user_input, shift_amount = input("Enter a string: "), int(input("Enter shift amount: "))
    user_input = user_input.upper()
    print(caesarCipher(user_input, shift_amount))


def caesarCipher(string: str, shift: int = 13):
    string = string.upper()
    new_string = ''
    for ch in string:
        if not ch.isspace():
            add = ord(ch) + shift
            if add <= ord('Z'):
                new_string += chr(add)
            else:
                new_string += chr(add - 26)
        else:
            new_string += ch
    print(new_string)
    return new_string


if __name__ == '__main__':
    main()
