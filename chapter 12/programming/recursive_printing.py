def print_rec(n:int):
    if n >= 0:
        print("n ",n)
        print_rec(n-2)


print_rec(6)