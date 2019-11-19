animal1 = input("Name an animal: ")
animal2 = input("Name another animal: ")
firstAnimal = animal1 if (animal2 > animal1) else animal2
print("The animal which comes first alphabetically is " + firstAnimal)
