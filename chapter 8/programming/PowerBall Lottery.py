from startingPython.utility import read_file_lines

MENU_OPTIONS = '123456'

TICKET = 1
POWER_BALL_NUM = 2


def main():
    menu()
    lists_of_counts, last_draws = tuple(Operation())

    print(lists_of_counts)
    user_choice = take_good_input(MENU_OPTIONS)
    while user_choice != 6:
        if user_choice == 1:
            ans = tenCommonNumbers(lists_of_counts, most=True)
            ans.reverse()
            display_answers(ans)
        elif user_choice == 2:
            ans = tenCommonNumbers(lists_of_counts)
            display_answers(ans)
        elif user_choice == 3:
            ans = tenCommonNumbers(last_draws, most=True)
            ans.reverse()
            display_answers(ans, prompt="last call in days : ")
        elif user_choice == 4:
            ans = Operation(use=TICKET)[0]
            display_answers(ans)
        else:
            ans = Operation(use=POWER_BALL_NUM)[0]
            display_answers(ans)
        menu()
        user_choice = take_good_input(MENU_OPTIONS)


def Operation(use=None):
    list_of_lines = read_file_lines("pbnumbers.txt")

    str_of_lines = " ".join(list_of_lines).replace("\n", "")
    if not use:
        new_list = [line[:-1] for line in list_of_lines]
        list_of_nbrs = [str(i).zfill(2) for i in range(1, 70)]
    else:
        if use == TICKET:
            new_list = [line[:-4] for line in list_of_lines]
            list_of_nbrs = [str(i).zfill(2) for i in range(1, 70)]
        elif use == POWER_BALL_NUM:
            new_list = [line[-4:-1] for line in list_of_lines]
            list_of_nbrs = [str(i).zfill(2) for i in range(1, 27)]
        str_of_lines = " ".join(new_list)

    new_list.reverse()
    last_draw = []

    # print(list_of_lines)

    lists_of_counts = []
    for nbrs in list_of_nbrs:
        lists_of_counts.append((nbrs, str_of_lines.count(nbrs)))
        for index, strings in enumerate(new_list):
            if nbrs in strings:
                last_draw.append((nbrs, index))
                break
    return lists_of_counts, last_draw


def menu():
    print("1- Display the 10 most common numbers")
    print("2- Display the 10 least common numbers")
    print("3- Display the 10 most overdue numbers")
    print("4- Display the frequency of each number 1–69")
    print("5- Display the frequency of each Powerball number 1–26")
    print("6-  quit")


def tenCommonNumbers(list_of_tuples, most=False):
    if most:
        return sorted(list_of_tuples, key=lambda item: item[1])[-10:]
    else:
        return sorted(list_of_tuples, key=lambda item: item[1])[:10]


def display_answers(list_of_tuples, prompt="occ"):
    for pos, tuples in enumerate(list_of_tuples):
        print(f"{pos + 1}-)  {tuples[0]} {prompt} {tuples[1]}")


def take_good_input(string):
    while True:
        try:
            user_value = input("Enter your choice: ")
            if user_value not in string:
                print(f"Enter {', '.join(string[:-1])} or {string[-1]}")
            else:
                return int(user_value)
        except ValueError:
            continue


if __name__ == '__main__':
    main()
