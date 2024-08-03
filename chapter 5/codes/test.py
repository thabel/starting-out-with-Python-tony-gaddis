""" def main():
    print("__execute file___",__file__)
    a = input("type a simple string: ")
    for i in range(len(a)):
        many(arg=i)
    
def many(arg:int):
    for val in range(arg):
        print("*",end='')
    print()

if __name__=='__main__':
    main()
 """
""" 
def main():
 print("I do not know about you ! ")
 print("OK . . . ")
 print(main.__name__)

if __name__ == '__main__':
    main() """
import math

