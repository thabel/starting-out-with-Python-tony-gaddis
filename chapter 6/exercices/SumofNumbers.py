
file_name = "number_list.txt"
try:
    with open(file_name,"r") as file:
        a=0
        for line in file:
            a+=int(line)
            print("the sum is =",a)
except:
    print("Error when opening file!")