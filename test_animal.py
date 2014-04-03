# Unit tests for animal.py


# IMPORTS
from animal import Animal
import unittest


# main
class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.tiger = Animal("tiger", 1, "Vitaly", "male", 180)

    def test_get_name(self):
        self.assertEqual("Vitaly", self.tiger.get_name())

    def test_get_species(self):
        self.assertEqual("tiger", self.tiger.get_species())

    def test_get_food_weight_ratio(self):
        self.assertEqual(0.06, self.tiger.get_food_weight_ratio())

    def test_get_food_type(self):
        self.assertEqual("carnivore", self.tiger.get_food_type())

    def test_fetch_data(self):
        query = "SELECT life_expectancy FROM animals WHERE species = ?;"
        self.assertEqual(20, self.tiger.fetch_data(query))

    def test_get_age(self):
        self.assertEqual(1, self.tiger.get_age())

    def test_get_can_breed(self):
        self.assertTrue(self.tiger.get_can_breed())

    def test_get_gestation(self):
        self.assertEqual(4, self.tiger.get_gestation())

    def test_is_alive(self):
        self.assertTrue(self.tiger.is_alive())

    def test_is_alive_when_dead(self):
        self.tiger.age(30)
        self.assertFalse(self.tiger.is_alive())

    def test_kill_animal(self):
        self.assertTrue(self.tiger.kill_animal())

    def test_grow(self):
        self.assertTrue(self.tiger.grow(5))
        self.assertEqual(185, self.tiger.get_weight())

    def test_grow_over_average_weight(self):
        self.assertFalse(self.tiger.grow(500))

    def test_age(self):
        self.assertTrue(self.tiger.age(1))
        self.assertEqual(2, self.tiger.get_age())

    def test_age_to_death(self):
        self.assertFalse(self.tiger.age(50))

    def test_eat(self):
        self.assertTrue(self.tiger.eat())
        self.assertEqual(190.8, self.tiger.get_weight())

    def test_eat_more_than_average_weight(self):
        self.tiger.weight = 240
        self.assertFalse(self.tiger.eat())

    def test_chance_to_die(self):
        self.assertTrue(self.tiger.chance_to_die())

    def test_chance_to_die_when_dead(self):
        self.tiger.current_age = 27
        self.assertFalse(self.tiger.chance_to_die())

    def test_get_expenses(self):
        self.assertEqual(self.tiger.weight * 4 * self.tiger.get_food_weight_ratio(), self.tiger.get_expenses())

    def test_fetch_gestation_from_db(self):
        self.assertEqual(4, self.tiger.fetch_gestation_from_db())


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
