# Animal class for Zoo


# IMPORTS
import db_interface


class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.db = db_interface.DBinterface("animals.db")
        self.species = species
        self.current_age = age
        self.name = name
        self.gender = gender
        self.food_type = self.db.fetch_food_type(self.get_species())
        self.food_weight_ratio = self.db.fetch_food_weight_ratio(self.get_species())
        self.weight = weight
        self.alive = True
        self.gestation = self.db.fetch_gestation(self.get_species())
        self.cooldown = 0
        self.cost = self.get_expenses()

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_food_type(self):
        return self.food_type

    def get_age(self):
        return self.current_age

    def get_weight(self):
        return self.weight

    def get_gestation(self):
        return self.gestation

    def get_expenses(self):
        if self.food_type == "carnivore":
            return 4 * (self.food_weight_ratio * self.weight)
        elif self.food_type == "herbivore":
            return 2 * (self.food_weight_ratio * self.weight)

    def age(self, grow_age):
        query = "SELECT life_expectancy FROM animals WHERE species = ?;"
        life_expectancy = int(self.fetch_data(query))
        if self.get_age() + grow_age <= life_expectancy:
            self.current_age += grow_age
            return self.current_age
        self.kill_animal()
        return self.alive

    def is_alive(self):
        return self.alive

    def grow(self, grow_weight):
        average_weight = self.db.fetch_average_weight(self.get_species())
        if self.weight + grow_weight <= average_weight:
            self.weight += grow_weight
            return True
        return False

    def eat(self):
        grow_weight = self.weight * self.food_weight_ratio
        return self.grow(grow_weight)

    def kill_animal(self):
        self.alive = False
        return True

    def chance_to_die(self):
        life_expectancy = self.db.fetch_life_expectancy(self.get_species())
        return self.get_age() / life_expectancy
