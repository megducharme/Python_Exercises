class Animal:
    def __init__(self, name = None, species = None):
        self.__name = name
        self.species = species
        self.speed = 0
        self.legs = 0


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, val):
       self.__name__ = val


    def get_name(self):
        return self.name

    def walk(self):
        if isinstance(self.legs, int) and self.legs > 0:
            self.speed = self.speed + (0.1 * self.legs)
        else:
            raise ValueError('Legs property must contain a number greater than 0')

    def set_legs(self, number_of_legs):
        """Set the species of the animal

        Arguments:
            number_of_legs (integer)
        """
        self.legs = number_of_legs

    def set_species(self, species):
        self.species = species

    def get_species(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")

    def walk(self):
        self.speed = self.speed + (0.2 * self.legs)
