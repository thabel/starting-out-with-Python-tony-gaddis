# This program uses recursion to print numbers
# from the Fibonacci series.


def main():
    print("The first 10 numbers in the")
    print("Fibonacci series are:")

    for number in range(1, 11):
        print(fibo(number))

    # The fib function returns the nth number
    # in the Fibonacci series.

def fibo(n):
    if n ==  0:
        return
    a = 0
    b = 1
    c = a+b
    for i in range(n-1):
        c = a + b 
        a= b
        b=c
    return c

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

    # Call the main function.


main()
