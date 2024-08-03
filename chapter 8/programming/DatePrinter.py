"""
Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.
It should print the date in the format March 12, 2018.
"""
list_of_months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]


def main():
    date_string = take_input()
    date_list = date_string.split('/')
    print(list_of_months[int(date_list[0])-1],date_list[1],date_list[2])

def take_input():
    date_string = input('Enter date in format mm/dd/yyyy: ')
    return date_string


if __name__ == '__main__':
    main()
