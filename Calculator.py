while(True):
    validation = False
    while validation == False:
        try:
            num1 = float(input("Enter a number: "))
            validation = True
        except ValueError:
            print("Invalid Input")
            continue
    validation = False
    while validation == False:
        try:
            num2 = float(input("Enter another number: "))
            validation = True
        except ValueError:
            print("Invalid Input")
            continue
    operator = input("Enter an operator: +, -, *, / or %? ")
    if(operator == "+"):
        print(num1, operator, num2, "=", num1+num2)
    elif(operator == "-"):
        print(num1, operator, num2, "=", num1-num2)
    elif(operator == "*"):
        print(num1, operator, num2, "=", num1*num2)
    elif(operator == "/"):
        print(num1, operator, num2, "=", num1/num2)
    elif(operator == "%"):
        print(num1, operator, num2, "=", num1%num2)
    else:
        print("Invalid operator")
        continue
    repeat = input("Another calculation? y/n: ")
    repeat = repeat.lower()
    if(repeat == "y"):
        continue
    elif(repeat == "n"):
        print("Goodbye")
        break
    else:
        print("Invalid command, exiting calculator")
        break
