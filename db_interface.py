# Common Database Interface for animal.py, zoo.py and zoo_simulator.py


# IMPORTS
import sqlite3
from animal import Animal
from zoo import Zoo


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DBinterface():
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.dict_cursor = self.conn.cursor()
        self.dict_cursor.row_factory = dict_factory

    def create_zoo(self, name, capacity, budget):
        try:
            self.dict_cursor.execute("INSERT INTO zoos VALUES(?, ?, ?);", (name, int(capacity), float(budget)))
        except (sqlite3.OperationalError, sqlite3.IntegrityError):
            return False
        self.conn.commit()
        return Zoo(name, capacity, budget)

    def get_zoos(self):
        return self.dict_cursor.execute("SELECT name, capacity, budget FROM zoos;").fetchall()

    def create_animal(self, zoo_name, species, age, name, gender, weight):
        try:
            self.dict_cursor.execute("INSERT INTO animals_from_zoos VALUES(NULL, ?, ?, ?, ?, ?, ?)", (zoo_name, species, name, age, gender, weight))
        except sqlite3.IntegrityError:
            return False
        self.conn.commit()
        return Animal(species, age, name, gender, weight)

    def remove_animal(self, zoo_name, species, name):
        self.dict_cursor.execute("DELETE FROM animals_from_zoos WHERE zoo_name = ? and species = ? and name = ?", (zoo_name, species, name))
        return True

    def update_zoos(self):
        zoos = []
        all_zoos = self.get_zoos()
        for zoo in all_zoos:
            zoo = Zoo(zoo["name"], zoo["capacity"], zoo["budget"])
            for animal in self.fetch_animals_from_zoo(zoo.get_name()):
                animal = Animal(animal["species"], animal["age"], animal["name"], animal["gender"], animal["weight"])
                zoo.add_animal(animal)
            zoos.append(zoo)
        return zoos

    def fetch_species(self):
        return self.dict_cursor.execute("SELECT species FROM animals;").fetchall()

    def fetch_animals_from_zoo(self, zoo_name):
        return self.dict_cursor.execute("SELECT species, name, age, gender, weight FROM animals_from_zoos WHERE zoo_name = ?", (zoo_name,)).fetchall()

    def fetch_gestation(self, species):
        return self.dict_cursor.execute("SELECT gestation FROM animals WHERE species = ?;", (species,)).fetchone()["gestation"]

    def fetch_food_type(self, species):
        return self.dict_cursor.execute("SELECT food_type FROM animals WHERE species = ?;", (species,)).fetchone()["food_type"]

    def fetch_food_weight_ratio(self, species):
        return self.dict_cursor.execute("SELECT food_weight_ratio FROM animals WHERE species = ?;", (species,)).fetchone()["food_weight_ratio"]

    def fetch_life_expectancy(self, species):
        return self.dict_cursor.execute("SELECT life_expectancy FROM animals WHERE species = ?;", (species,)).fetchone()["life_expectancy"]

    def fetch_average_weight(self, species):
        return self.dict_cursor.execute("SELECT average_weight FROM animals WHERE species = ?;", (species,)).fetchone()["average_weight"]
