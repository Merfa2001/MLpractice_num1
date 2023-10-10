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
#done