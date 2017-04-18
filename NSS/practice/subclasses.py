class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0

    def getName(self):
        return self.name

    def walk(self):
        print("Parent class walk method")
        self.speed = self.speed + (0.1 * self.legs)

    def setSpecies(self, species):
        self.species = species

    def getSpecies(self):
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "{} is a {}".format(self.name, self.species)


class IsWhiskered:
    def __init__(self):
        self.whiskers = True
        self.whiskers_count = 0


class IsClawed:
    def __init__(self):
        self.claws = True
        self.claws_are_retractable = True


class Dog(Animal, IsWhiskered):
    def __init__(self, name):
        super().__init__(name, "Dog")
        #showing how to use super()over initializing the Animal class here--dont need to pass in self after the init b/c knows
        IsWhiskered.__init__(self)
        print("Dog Constructor made a new dog")

    def walk(self):
        self.speed = self.speed + (0.2 * self.legs)


class Cat(Animal, IsWhiskered, IsClawed):
    def __init__(self, name):
        Animal.__init__(self, name, "Cat")
        IsWhiskered.__init__(self)
        IsClawed.__init__(self)
        print("Cat constructor made a new cat")

    def walk(self):
        self.speed = self.speed + (0.25 * self.legs)


fido = Dog("fido")
print(fido)

mr_whiskers = Cat("Mr whiskers")
