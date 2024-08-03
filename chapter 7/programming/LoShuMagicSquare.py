"""
The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-18. The
Lo Shu Magic Square has the following properties:
•	 The grid contains the numbers 1 through 9 exactly.
•	 The sum of each row, each column, and each diagonal all add up to the same number.
This is shown in Figure 7-19.
In a program you can simulate a magic square using a two-dimensional list. Write a func-
tion that accepts a two-dimensional list as an argument and determines whether the list is
a Lo Shu Magic Square. Test the function in a program.

"""


# test the lo shu Magic

def main():
    print(is_lo_shu_magic([[4,9,2],[3,5,7],[7,1,6]]))


# determine weather a 2D list is Lo shu Magic
def is_lo_shu_magic(two_d_list):
    if not is_2d_list(two_d_list):
        return False
    # we are dealing with 3x3 list
    matching_number = sum(two_d_list[0])

    # sum of other row
    colums_item = []
    diagonal_items_sum_1 =0
    diagonal_items_sum_2 = 0

    for i in range(len(two_d_list)):
        col = i

        if sum(two_d_list[i]) != matching_number:
            return False

        for row in range(len(two_d_list)):
            colums_item.append(two_d_list[row][col])

            if row == col:
                diagonal_items_sum_1 += two_d_list[row][col]
            if row+col == len(two_d_list) -1 :
                diagonal_items_sum_2 +=  two_d_list[row][col]

        if sum(colums_item) != matching_number:
            return False
        colums_item = []

    if diagonal_items_sum_1 != matching_number or diagonal_items_sum_2 != matching_number:
        return False

    return True

def is_2d_list(two_d_list):
    if len(two_d_list) != 3:
        return False
    for item in two_d_list:
        if len(item) != 3:
            return False
        for num in item:
            if not isinstance(num,int):
                return False
    return True





if __name__ == '__main__':
    main()
