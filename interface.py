# Interface for Zoo


# IMPORTS
from commandparser import CommandParser
from animal import Animal
from zoo import Zoo
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class CLI():
    """docstring for CLI"""
    def __init__(self, database):
        self.cp = CommandParser()
        self.conn = sqlite3.connect(database)
        self.dict_cursor = self.conn.cursor()
        self.dict_cursor.row_factory = dict_factory
        self.zoos = self.update_zoos()
        self._init_callbacks()
        self._loop()

    def callback_list_zoos(self, arguments):
        output_list = []
        for zoo in self.get_zoos():
            output_list.append("[{}] {}, {}, {}".format(zoo["id"], zoo["name"], zoo["capacity"], zoo["budget"]))
        return "\n".join(output_list)

    def callback_create_zoo(self, arguments):
        name = input("name>")
        capacity = input("capacity>")
        budget = input("budget>")
        new_zoo = Zoo(name, capacity, budget)
        self.zoos.append(new_zoo)
        self.dict_cursor.execute("INSERT INTO zoos VALUES(NULL, ?, ?, ?);", (name, capacity, budget))
        self.conn.commit()
        return "Zoo <{}> created.".format(name)

    def callback_see_animals(self, arguments):
        zoo_id = int(arguments[0]) - 1
        return self.zoos[zoo_id].get_animals()

    def get_zoos(self):
        return self.dict_cursor.execute("SELECT id, name, capacity, budget FROM zoos;").fetchall()

    def update_zoos(self):
        zoos = []
        all_zoos = self.get_zoos()
        for zoo in all_zoos:
            zoos.append(Zoo(zoo["name"], zoo["capacity"], zoo["budget"]))
        return zoos

    def fetch_data(self, query):
        return self.cursor.execute(query, (self.species,)).fetchone()

    def callback_exit(self, arguments):
        exit(0)

    def callback_add_animal(self, arguments):
        zoo_id = int(arguments[0]) - 1
        desired_zoo = self.zoos[zoo_id]
        species = input("species>")
        age = int(input("age>"))
        name = input("name>")
        gender = input("gender>")
        weight = float(input("weight>"))
        animal = Animal(species, age, name, gender, weight)
        desired_zoo.add_animal(animal)
        return "Added <{}> to zoo <{}>".format(name, desired_zoo.get_name())

    def callback_remove_animal(self, arguments):
        zoo_id = int(arguments[0]) - 1
        animal_id = int(arguments[0]) - 1
        desired_zoo = self.zoos[zoo_id]
        desired_zoo.remove_animal(animal_id)
        return "Removed animal from zoo <{}>".format(desired_zoo.get_name())

    def callback_simulate_time(self, arguments):
        zoo_id = int(arguments[0]) - 1
        desired_zoo = self.zoos[zoo_id]
        period = self.get_period(arguments[1], int(arguments[2]))


    def get_period(period_type, period):
        if period_type == "weeks" or period_type == "week":
            period *= 7
        elif period_type == "months" or period_type == "month":
            period *= 30
        elif period_type == "years" or period_type == "year":
            period *= 365
        return period

    def _init_callbacks(self):
        self.cp.on("list_zoos", self.callback_list_zoos)
        self.cp.on("see_animals", self.callback_see_animals)
        self.cp.on("create_zoo", self.callback_create_zoo)
        self.cp.on("accommodate", self.callback_add_animal)
        self.cp.on("move_to_habitat", self.callback_remove_animal)
        self.cp.on("exit", self.callback_exit)

    def _loop(self):
        while True:
            command = input(">")
            self.cp.take_command(command)

# PROGRAM RUN
if __name__ == '__main__':
    CLI("animals.db")
