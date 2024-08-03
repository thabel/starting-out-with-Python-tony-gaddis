"""
Write a program that gets strings containing a person’s first and last name as separate
values, and then displays their “initials”, “name in address book”, and “username”. For
example, if the user enters a first name of “John” and a last name of “Smith”, the program
should display “J.S.”, “John SMITH”, and “jsmith”.
"""


def main():
    fname, lname = take_input()

    print('Initial: .......... ', fname[0].upper() + '.' + lname[0].upper())
    print('Name in address book .', fname + ' ' + lname.upper())
    print('User name ...', fname[0].lower() + lname)


def take_input():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')

    return first_name, last_name


if __name__ == '__main__':
    main()
