import sys
def multiple(x,y):
    return x * y
def divide(x,y):
    return x / y
print("select operations \t 1.Add \t 2.Substract \t 3.Multiple \t 4.Divide: ")
test = True
while test:
    choice = int(input("Enter a number between 1 and 4 to perform operations: "))
    if choice in range(1, 5):
        first = float(input("Enter first number to perform: "))
        second = float(input("Enter second number to perform: "))
        if choice == 1:
            print(first, "+", second, "=", first+second)
        if choice == 2:
            print(first, "-", second, "=", first-second)
        if choice == 3:
            print(first, "*", second, "=", multiple(first, second))
        if choice == 4:
            print(first, "/", second, "=", divide(first, second))
        break    ### we can use test = False or sys.exit() to avoid looping in while 
    else:
        print("Invalid input")
        sys.exit() ### we can also use break or test = False 
