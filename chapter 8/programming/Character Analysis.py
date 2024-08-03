from startingPython.utility import read_file_lines

character_analysis = {
    "uppercase": 0,
    "lowercase": 0,
    "digits": 0,
    "white_space": 0
}


def main():
    list_of_sentences = read_file_lines("text.txt")
    for line in list_of_sentences:
        for ch in line:
            if ch.isupper():
                character_analysis["uppercase"] += 1
            elif ch.islower():
                character_analysis["lowercase"] += 1
            elif ch.isdigit():
                character_analysis['digits'] += 1
            elif ch.isspace():
                character_analysis['white_space'] += 1
    print(f"uppercase  = {character_analysis['uppercase']}\n"
          f"lowercase  = {character_analysis['lowercase']}\n"
          f"digits  = {character_analysis['digits']}\n"
          f"white_space  = {character_analysis['white_space']}\n")


if __name__ == '__main__':
    main()
