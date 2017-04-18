# In the test class' setUpClass() method, create an instance of Animal and Dog.
# Animal object has the correct name property.
#------------------------
# Set a species and verify that the object property of species has the correct value.
# Invoking the walk() method set the correct speed on the both objects.
# The animal object is an instance of Animal.
# The dog object is an instance of Dog.


import unittest
from animals import *

class TestAnimalClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.animal_to_test = Animal("Ellie", "Elephant")
        self.dog_to_test = Dog("Knox")
        print(self.animal_to_test.name())


    def test_animal_name(self):
        self.assertEqual(self.animal_to_test.name, "Ellie")


    def test_animal_species(self):
        self.assertEqual(self.animal_to_test.species, "Elephant")


    def test_dog_species(self):
        self.assertEqual(self.dog_to_test.species, "Dog")


    def test_speed_in_walk_method(self):
        legs = 4
        self.animal_to_test.set_legs(legs)
        self.animal_to_test.walk()

        self.dog_to_test.set_legs(legs)
        self.dog_to_test.walk()

        self.assertEqual(self.animal_to_test.speed, 0.4)
        self.assertEqual(self.dog_to_test.speed, 0.8)



if __name__ == '__main__':
    unittest.main()
