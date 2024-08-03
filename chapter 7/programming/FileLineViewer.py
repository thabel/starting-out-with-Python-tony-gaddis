"""
Write a program that asks the user for the name of a file. The program should read all
the file’s data into a list and display the number of lines of data that the file contains, and
then ask the user to enter the number of the line that they want to view. The program should
display the specified line.
The program should handle the following exceptions by displaying an error message:
•	 IOError exceptions that are raised when the specified filename cannot be found or
opened.
•	 ValueError exceptions that are raised when a non-integer value is given as a line number.
•	 IndexError exceptions that are raised when the line number is outside the range of the
data list.
"""


def read_file_lines(file):
    try:
        with open(file, "r") as fp:
            read_list = fp.readlines()
            return read_list
    except IOError:
        print(f"{file} can not be read")
        exit(1)


def main():
    filename = input('Enter file name: ')
    read_list = read_file_lines(filename)
    print(f"file countains {len(read_list)} lines")
    lines_to_read = int(input("How many lines to read?: "))
    try:
        print("=" * 20)
        var = read_list[lines_to_read]
        for lines in read_list[:lines_to_read]:
            print(lines, end='')
    except IndexError:
        print("number of lines longuer than file lenght")


if __name__ == '__main__':
    main()
