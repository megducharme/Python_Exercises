@property
def name(self):
  return self.__name

self.__name = name
#pseudo private variable (python doesn't have private variables)

@name.setter
#defining the setter for the name property
def name(self, val):
  if isinstance(val, str):
    self.__name__ = val

#to call the setter self.animal.name = "Goofball"


@property
def species(self):
  return self.__name

self.__name = species
#pseudo private variable (python doesn't have private variables)

@species.setter
#defining the setter for the species property
def species(self, val):
  if isinstance(val, str):
    self.__name__ = val

#to call the setter self.animal.species = "Goofball"

