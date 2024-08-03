1 # This program has a recursive function.
 2
 3 def main():
 4 # By passing the argument 5 to the message
 5 # function we are telling it to display the
 6 # message five times.
 7 message(5)
 8
 9 def message(times):
10 if times > 0:
11 print('This is a recursive function.')
12 message(times − 1)
13
14 # Call the main function.
15 main()