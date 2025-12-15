#num = int(input("Enter a number you want to calculate: "))
def mult(x, y):
    return x * y

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def dev(x, y):
    return x / y 

def sqr(x, y):
    return x ** y

procces =  {
    "1" : "Mltiplay",
    "2" : "Add",
    "3" : "Sub",
    "4" : "Devide",
    "5" : "Squere"
}

again = "y"
while again == "y":
    c = input(f"Which process you want? {procces}: ")
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if c == "1":
        print(mult(x, y))
    elif c == "2":
        print(add(x, y))
    elif c == '3':
        print(sub(x, y))
    elif c == '4':
        print (dev(x, y))
    elif c == '5':
        print(sqr(x, y))
    else:
        print("invalid choice")
    again = input("do you want to calculate again? Enter y for yes: ")



