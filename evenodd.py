#("program to identify if the the number is even or odd")

def isEven(number):
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")
    
number=int(input("enter a number"))

isEven(number)
