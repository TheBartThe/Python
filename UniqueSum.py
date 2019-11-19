int1 = int(input("Enter a whole number: "))
int2 = int(input("Enter another whole number: "))
int3 = int(input("Enter another whole number: "))
if(int1 == int2):
    if(int1 == int3):
        print(0)
    else:
        print(int3)
elif(int1 == int3):
    print(int2)
elif(int2 == int3):
    print(int1)
else:
    print(int1 + int2 + int3)
