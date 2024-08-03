def main():
    user_input = input("Enter your str: ")
    new_string = unique_chars(user_input)
    char, count = max(counter_list(user_input, new_string), key=larger_occurence)
    print(char, count)


def larger_occurence(tuple):
    return tuple[1]


def counter_list(string, unique_string):
    answer_list = [(ch, string.count(ch)) for ch in unique_string]
    print(answer_list)
    return answer_list


def unique_chars(string):
    new_str = ""
    for ch in string:
        if ch not in new_str and ch.isalpha():
            new_str += ch
    return new_str


if __name__ == '__main__':
    main()
