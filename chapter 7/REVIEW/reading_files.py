try:
    with open("file_", "r") as f:
        read = f.readlines()
        read = [read[i].strip() for i in range(len(read))]
    print(read)
except:
    L = ["i for " + str(i) + " in list \n" for i in range(1, 10)]
    with open("file_", "w") as f:
        f.writelines(L)
