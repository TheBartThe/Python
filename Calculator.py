def main():
    while(True):
        validation = False
        while (not validation):
            try:
                num1 = float(input("Enter a number: "))
                validation = True
            except ValueError:
                print("Invalid Input")
                continue
        validation = False
        while (not validation):
            try:
                num2 = float(input("Enter another number: "))
                validation = True
            except ValueError:
                print("Invalid Input")
                continue
        operator = input("Enter an operator: +, -, *, / or %? ")
        if(operator == "+"):
            add(num1, num2)
        elif(operator == "-"):
            subtract(num1, num2)
        elif(operator == "*"):
            multiply(num1, num2)
        elif(operator == "/"):
            divide(num1, num2)
        elif(operator == "%"):
            mod(num1, num2)
        else:
            print("Invalid operator")
            continue
        repeat = input("Another calculation? y/n: ").lower()
        if(repeat == "y"):
            continue
        elif(repeat == "n"):
            print("Goodbye")
            break
        else:
            print("Invalid command, exiting calculator")
        break
    
def add(a, b):
    print(a, "+", b, "=", a+b)
    
def subtract(a, b):
    print(a, "-", b, "=", a-b)
    
def multiply(a, b):
    print(a, "*", b, "=", a*b)
    
def divide(a, b):
    print(a, "/", b, "=", a/b)
    
def mod(a, b):
    print(a, "/", b, " leaves remainder ", a%b)

if __name__ == "__main__":
    main()
