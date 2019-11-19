def getResults():
    validation = False
    while(not validation):
        try:
            hW = float(input("Enter Homework mark out of 25: "))
            if((hW > 25) or (hW < 0)):
                print("Out of range. Enter a valid mark")
                continue
            validation = True
        except ValueError:
            print("Invalid Input")
            continue
    validation = False
    while(not validation):
        try:
            assess = float(input("Enter Assessment mark out of 50: "))
            if((assess > 50) or (assess < 0)):
                print("Out of range. Enter a valid mark")
                continue
            validation = True
        except ValueError:
            print("Invalid Input")
            continue
    validation = False
    while(not validation):
        try:
            exam = float(input("Enter Final Exam mark out of 100: "))
            if((exam > 100) or (exam < 0)):
                print("Out of range. Enter a valid mark")
                continue
            validation = True
        except ValueError:
            print("Invalid Input")
            continue
    return (ITGrade(hW, assess, exam))

def ITGrade(hW, assess, exam):
    return (hW + (assess*0.7) + (exam*0.4))

def getName():
    return (input("Enter your name: "))

def getGrade(mark):
    if (mark >= 80):
        return "A"
    elif (mark >= 70):
        return "B"
    elif (mark >= 60):
        return "C"
    elif (mark >= 50):
        return "D"
    elif (mark >= 40):
        return "E"
    else:
        return "F"

def displayResults(name, mark, grade):
    print("Name: ", name)
    print("Your mark was ", mark, "%")
    print("Your achieved grade ", grade)

name = getName()
mark = getResults()
grade = getGrade(mark)
displayResults(name, mark, grade)
