from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, type):
        self.type = type
        super(Animal).__init__()

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__("Mammal")

    def speak(self, type):
        print("Woof, I am a ", type)

pep = Dog("Pep")
print(pep.speak("mammal"))




class Bird():
    def __init__(self, wingspan):
        self.wingspan = wingspan

    def __len__(self):
        return self.wingspan

eagle = Bird(25)
print(len(eagle))
print(eagle.__len__())
