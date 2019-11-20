def createList():
    file = open("filename.txt", "w+")
    file.truncate(0)
    file.write("Reading FC \n")
    file.write("Liverpool FC \n")
    file.write("Manchester United \n")
    file.write("Chelsea FC \n")
    file.write("Arsenal FC \n")

    file.seek(0)
    print("Team 1: " + file.readline())
    print("Team 2: " + file.readline())

    file.close()

def addToList():
    file = open("filename.txt", "a")
    file.seek(0)
    file.write("Tottenham \n")
    file.close

def editFile():
    file = open("filename.txt", "r+")
    file.seek(0)
    lines = []
    for i in file:
        lines.append(file.readline())
    print(lines)
    lines[0] = "This is a new line \n"
    for i in range(len(lines)):
        file.write(lines[i])

    file.seek(0)
    print(file.read())

    file.close

##file.write("This is a new line \n")
##file.seek(0)
##
##file.readline()
##text = file.read()
##text = "This is a new line \n" + text
##file.truncate(0)
##file.write(text)
##print(text)
##
##file.seek(0)
##print(file.readlines())

##Not sure why this didn't work

createList()
addToList()
editFile()
