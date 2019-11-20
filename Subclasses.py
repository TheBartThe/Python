class Animal():
    def __init__(self, type):
        self.type = type

class Dog(Animal):
    def __init__(self, name):
        super().__init__("Mammal")
        self.name = name

pep = Dog("Pep")
print(pep.name, pep.type)
