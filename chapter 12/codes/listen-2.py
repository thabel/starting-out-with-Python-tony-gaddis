# This program has a recursive function.


def main():
    # By passing the argument 5 to the message
    # function we are telling it to display the
    # message five times.
    message(5)


def message(times):
    print("Hello times",times)
    if times > 0:
        print("This is a recursive function.")
        message(times - 1)
    print("ended with times",times)

# Call the main function.
main()
