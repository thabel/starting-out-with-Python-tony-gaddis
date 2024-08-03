"""
If you have downloaded the source code you will find the following files in the Chapter 07
folder:
•	 GirlNames.txt This file contains a list of the 200 most popular names given to girls
born in the United States from the year 2000 through 2009.
•	 BoyNames.txt This file contains a list of the 200 most popular names given to boys
born in the United States from the year 2000 through 2009.
Write a program that reads the contents of the two files into two separate lists. The user
should be able to enter a boy’s name, a girl’s name, or both, and the application will display
messages indicating whether the names were among the most popular.
"""


def main():
    boy_name, girl_name, any_gender_name = take_user_input()

    boy_files_content = read_file_content("BoyNames.txt")
    girl_file_content = read_file_content("GirlNames.txt")

    out_result(boy_name, boy_files_content, string_holder="boys")
    out_result(girl_name, girl_file_content, string_holder="girls")

    if any_gender_name in boy_files_content and any_gender_name in girl_file_content:
        print(any_gender_name, "is among both girls and boys popular")
    else:
        print(any_gender_name, "is not among any gender popular name.")


def out_result(name, file_list, string_holder):
    if name in file_list:
        print(name, "is among the most popular", string_holder, "name")
    else:
        print(name, "is not among the most popular name", string_holder, "name")


def take_user_input():
    """ taking 3 names : boy name , girl name or both """
    boy_name = input("enter boy name: ")
    girl_name = input("enter girl name: ")
    any_gender_name = input("enter name for both girl and boy: ")

    return boy_name, girl_name, any_gender_name


def read_file_content(filename):
    try:
        content = list()
        with open(filename, "r") as file:
            line = file.readline()
            while line:
                content.append(line.rstrip())
                line = file.readline()

    except FileNotFoundError:
        return list()
    return content


if __name__ == '__main__':
    main()
