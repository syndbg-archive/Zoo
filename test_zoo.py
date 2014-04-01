# Unit tests for zoo.py


# IMPORTS
from zoo import Zoo
import unittest


# main
class ZooTests(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo("Alexandria Zoo", 2, 1000)

    def test_get_zoo_name(self):
        self.assertEqual("Alexandria Zoo", self.zoo.get_name())

    def test_get_zoo_max_capacity(self):
        self.assertEqual(2, self.zoo.get_max_capacity())

    def test_get_zoo_budget(self):
        self.assertEqual(1000, self.zoo.get_budget())

    def test_get_animals(self):
        self.assertEqual([], self.zoo.get_animals())

    def test_add_animal(self):
        self.assertTrue(self.zoo.add_animal("Tiger"))
        self.assertEqual(["Tiger"], self.zoo.get_animals())

    def test_add_animal_when_no_space(self):
        self.assertTrue(self.zoo.add_animal("Tiger"))
        self.assertTrue(self.zoo.add_animal("Tiger"))
        self.assertFalse(self.zoo.add_animal("Elephant"))

    def test_remove_animal(self):
        self.assertTrue(self.zoo.add_animal("Tiger"))
        self.assertEqual(["Tiger"], self.zoo.get_animals())
        self.assertTrue(self.zoo.remove_animal(0))
        self.assertEqual([], self.zoo.get_animals())

    def test_is_there_space(self):
        self.assertTrue(self.zoo.is_there_space())

    def test_is_there_space_when_no_space(self):
        self.assertTrue(self.zoo.add_animal("Tiger"))
        self.assertTrue(self.zoo.add_animal("Lion"))
        self.assertFalse(self.zoo.is_there_space())


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
