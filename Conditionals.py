int1 = int(input("Enter a whole number: "))
int2 = int(input("Enter another whole number: "))
bool = True if (input("sum? y/n: ") == "y") else False
if (bool):
    print(int1 + int2)
else:
    print(int1 * int2)
