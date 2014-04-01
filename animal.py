import sqlite3


class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.current_age = age
        self.name = name
        self.gender = gender
        self.food_type = self.determine_food_type()
        self.weight = weight
        self.alive = True
        self.conn = sqlite3.connect("animals.db")
        self.cursor = self.conn.cursor()

    def get_expenses(self):
        if self.food_type == "carnivore":
            return 4 * (self.get_food_weight_ratio() * self.weight)

    def get_food_weight_ratio(self):
        return self.fetch_data("SELECT food_weight_ratio FROM animals WHERE species = ?;")

    def get_age(self):
        return self.current_age

    def get_weight(self):
        return self.weight

    def determine_food_type(self):
        query = "SELECT food_type FROM animals WHERE species = ?;"
        return self.fetch_data(query)

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
        query = "SELECT average_weight FROM animals WHERE species = ?;"
        average_weight = self.fetch_data(query)
        if self.weight + grow_weight <= average_weight:
            self.weight += grow_weight
            return True
        return False

    def eat(self):
        grow_weight = self.weight * self.get_food_weight_ratio()
        return self.grow(grow_weight)

    def kill_animal(self):
        query = "DELETE FROM animals WHERE species = ?;"
        self.cursor.execute(query, (self.species,))
        self.alive = False
        return True

    def chance_to_die(self):
        query = "SELECT life_expectancy FROM animals WHERE species = ?;"
        life_expectancy = self.fetch_data(query)
        if self.current_age >= life_expectancy:
            print("I`m sorry , but the animal has died ... ")
            self.kill_animal()
            return self.is_alive()
        return self.is_alive()

    def fetch_data(self, query):
        return self.cursor.execute(query, (self.species,)).fetchone()[0]
