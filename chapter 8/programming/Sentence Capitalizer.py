def main():
    print(capitalize_sentences("hello. my name is Joe. what is your name?"))


def capitalize_sentences(text):
    new_string = str()
    sentences = text.split('. ')
    for line in sentences:
        new_string += line.capitalize() + ". "
    return new_string


if __name__ == '__main__':
    main()
