class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("The animal makes a sound.")

class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def speak(self):
        print("Meow!")
#done