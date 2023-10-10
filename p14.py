class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def speak(self):
        print("Meow!")

dog = Dog("Rex", "Canis lupus familiaris", "German Shepherd")

cat = Cat("Luna", "Felis catus", "black")

animals = [dog, cat]

for animal in animals:
    print(animal.name, "is a", animal.species)
    animal.speak()
#done