# Single inhertiance
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Meow!")

d = cat("Dog", "Doggerman")
d.make_sound()

a = Animal("Cat", "Bigcat")
a.make_sound()
