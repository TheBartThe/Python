class Student():
    name = ""
    english = 0
    maths = 0
    science = 0
    
    def getAverage(self):
        return ((self.english + self.maths + self.science) / 3)
    
    def printMark(self):
        print(self.name, " got an average of ", self.getAverage())

james = Student()
james.name = "James"
##james.english = 67
##james.maths = 56
##james.science = 74
##
terry = Student()
terry.name = "Terry"
##terry.english = 76
##terry.maths = 97
##terry.science = 87
##
piers = Student()
piers.name = "Piers"
##piers.english = 14
##piers.maths = 23
##piers.science = 16
##
##james.printMark()
##terry.printMark()
##piers.printMark()

students = [james, terry, piers]

for student in students:
    print(student.name)
    student.english = int(input("enter english mark: "))
    student.maths = int(input("enter maths matks: "))
    student.science = int(input("enter science mark: "))
    print(student.name, "got an average mark of", student.getAverage())
