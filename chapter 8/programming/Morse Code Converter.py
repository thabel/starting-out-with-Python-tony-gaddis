"""
Morse code is a code where each letter of the English alphabet, each digit, and various
punctuation characters are represented by a series of dots and dashes. Table 8-4 shows part
of the code.
Write a program that asks the user to enter a string, then converts that string to Morse code.

Character Code Character Code Character Code
space space 6 – . . . .          G – – . Q – – . –
comma – – . . – – 7 – – . . .                  H . . . . R . – .
period . – . – . – 8 – – – . . I . . S . . .
question mark . . – – . .                               9 – – – – . J . – – – T –
0 – – – – –         A . – K – . – U . . –
1 . – – – – B – . . . L . – . . V . . . –
2 . . – – – C – . – . M – – W . – –
3 . . . – – D – . . N – . X – . . –
4 . . . . – E . O – – – Y – . –
5 . . . . . F . . – . P . – – . Z – – . .

"""
PONC_GROUP = 0
DIGIT_GOUP = 1
LETTERS_GROUP = 2

morse_characters = [
    [
        ' ',  # sapce
        '– – . . – –',  # comma
        '. – . – . –',  # periodd
        '. . – – . .',  # Question Mark
    ],

    [
        '– – – – –',  # 0
        '. – – – –',  # 1
        '. . – – –',  # 2
        '. . . – –',  # 3
        '. . . . –',  # 4
        '. . . . .',  # 5
        '– . . . .',  # 6
        '– – . . .',  # 7
        '– – – . .',  # 8
        '– – – – .',  # 9
    ],
    [
        '. –',  # A
        '– . . .',  # B
        '– . – .',  # C
        '– . .',  # D
        '.',  # E
        '. . – .',  # F
        '– – .',  # G
        '. . . .',  # H
        '. .',  # I
        '. – – –',  # J
        '– . –',  # K
        '. – . .',  # L
        '– –',  # M
        '– .',  # N
        '– – –',  # O
        '. – – .',  # P
        '– – . –',  # Q
        '. – .',  # R
        '. . .',  # S
        '–',  # T
        '. . –',  # U
        '. . . –',  # V
        '. – –',  # W
        '– . . –',  # X
        '– . –',  # Y
        '– – . .'  # Z
    ]
]


def main():
    morse_text = ''
    english_sentence = take_input()
    for ch in english_sentence:
        morse_text += convert_to_morse(ch, character_group(ch))
    print('morse : \n', morse_text)


def take_input():
    english_sentence = input("Enter your text: ")
    return english_sentence


def convert_to_morse(ch, group_code):
    if group_code == PONC_GROUP:
        if ch == ' ':
            return morse_characters[group_code][0]
        if ch == ',':
            return morse_characters[group_code][1]
        if ch == '.':
            return morse_characters[group_code][2]
    elif group_code == DIGIT_GOUP:
        return morse_characters[group_code][int(ch)]
    else:
        return morse_characters[group_code][ord(ch.upper()) - ord('A')]


def character_group(ch):
    if ch in ' .!,':
        return PONC_GROUP
    if ch.isalpha():
        return LETTERS_GROUP
    if ch.isdigit():
        return DIGIT_GOUP


if __name__ == '__main__':
    main()
