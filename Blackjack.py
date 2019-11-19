int1 = int(input("Enter a whole number: "))
int2 = int(input("Enter another whole number: "))
if (int1 > 21):
    if (int2 > 21):
        print(0)
    else:
        print(int2)
elif (int2 > 21):
    print (int1)
else:
    print(int1 if (int1 > int2) else int2)
