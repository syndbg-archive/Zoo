# Unit tests for zoo.py


# IMPORTS
from animal import Animal
from zoo import Zoo
import unittest


# main
class ZooTests(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo("Alexandria Zoo", 2, 1000)
        self.tiger_vitaly = Animal("tiger", 1, "Vitaly", "male", 180)
        self.lion_alex = Animal("lion", 1, "Alex", "male", 210)
        self.hippo_gloria = Animal("hippo", 2, "Gloria", "female", 1600)

    def test_get_zoo_name(self):
        self.assertEqual("Alexandria Zoo", self.zoo.get_name())

    def test_get_zoo_max_capacity(self):
        self.assertEqual(2, self.zoo.get_max_capacity())

    def test_get_zoo_budget(self):
        self.assertEqual(1000, self.zoo.get_budget())

    def test_get_animals(self):
        self.assertEqual("", self.zoo.get_animals())

    def test_add_animal(self):
        self.assertTrue(self.zoo.add_animal(self.tiger_vitaly))
        self.assertEqual("<Vitaly>: <tiger>, <1>, <180>", self.zoo.get_animals())

    def test_add_animal_when_no_space(self):
        self.assertTrue(self.zoo.add_animal(self.tiger_vitaly))
        self.assertEqual("<Vitaly>: <tiger>, <1>, <180>", self.zoo.get_animals())
        self.assertTrue(self.zoo.add_animal(self.lion_alex))
        self.assertEqual("<Vitaly>: <tiger>, <1>, <180>\n<Alex>: <lion>, <1>, <210>", self.zoo.get_animals())
        self.assertFalse(self.zoo.add_animal(self.hippo_gloria))
        self.assertEqual("<Vitaly>: <tiger>, <1>, <180>\n<Alex>: <lion>, <1>, <210>", self.zoo.get_animals())

    def test_remove_animal(self):
        self.assertTrue(self.zoo.add_animal(self.tiger_vitaly))
        self.assertEqual("<Vitaly>: <tiger>, <1>, <180>", self.zoo.get_animals())
        self.assertTrue(self.zoo.remove_animal(0))
        self.assertEqual("", self.zoo.get_animals())

    def test_is_there_space(self):
        self.assertTrue(self.zoo.is_there_space())

    def test_is_there_space_when_no_space(self):
        self.assertTrue(self.zoo.add_animal("Tiger"))
        self.assertTrue(self.zoo.add_animal("Lion"))
        self.assertFalse(self.zoo.is_there_space())

    def test_get_daily_expenses_when_empty_zoo(self):
        self.assertEqual(0, self.zoo.get_daily_expenses())

    def test_get_daily_expenses(self):
        self.assertTrue(self.zoo.add_animal(self.tiger_vitaly))
        expected = 4 * (self.tiger_vitaly.get_food_weight_ratio() * self.tiger_vitaly.weight)
        self.assertEqual(expected, self.zoo.get_daily_expenses())


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
