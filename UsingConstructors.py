class Student():
    def __init__(self, maths, english, chemistry, physics = 0, biology = 0):
        self.maths = maths
        self.english = english
        self.chemistry = chemistry
        self.physics = physics
        self.biology = biology

    def getAverage(self):
        return ((self.maths + self.english + self.chemistry) / 3)

steve = Student(43, 54, 74, 45, 75)
print(steve.getAverage())

james = Student(46, 65, 11)
print(james.getAverage())
