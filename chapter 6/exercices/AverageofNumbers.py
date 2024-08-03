file_name = "number_list.txt"
try:
    with open(file_name, "r") as file:
        try:
            a = 0;
            i = 0
            for line in file:
                a += int(line)
                i += 1
            print("the sum is =", a)
            print("the average is =", a / i)
        except IOError:
            print("Error when reading data")
        except ValueError:
            print("Error when converting values to number")
except:
    print("Error when opening file!")
