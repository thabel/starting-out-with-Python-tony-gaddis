def show_lines(n):
    if n==1:
        print("*")
    else:
        print("*"*show_lines(n-1))
    return n+1

        

print(show_lines(5))