# Zoo Simulator


# IMPORTS
from commandparser import CommandParser
from db_interface import DBinterface
from time_span import TimeSpanSimulator


class ZooSim():
    def __init__(self, database_name):
        self.cp = CommandParser()
        self.db = DBinterface(database_name)
        self.zoos = self.db.update_zoos()
        self._init_callbacks()
        self._loop()

    def callback_list_animal_species(self, arguments):
        output = []
        for i, specie in enumerate(self.db.fetch_species()):
            output.append("[{}] {}".format(i+1, specie["species"]))
        return "\n".join(output)

    def callback_list_zoos(self, arguments):
        output_list = []
        for i, zoo in enumerate(self.db.get_zoos()):
            output_list.append("[{}] <{}> <{}> <${}>".format(i+1, zoo["name"], zoo["capacity"], zoo["budget"]))
        return "\n".join(output_list)

    def callback_create_zoo(self, arguments):
        name = input("name>")
        capacity = input("capacity>")
        budget = input("budget>")
        zoo = self.db.create_zoo(name, capacity, budget)
        if zoo is False:
            return "Zoo with name <{}> already exists. Try to be more original!".format(name)
        self.zoos.append(zoo)
        return "Zoo <{}> created.".format(name)

    def callback_see_animals(self, arguments):
        zoo_id = arguments[0]
        try:
            desired_zoo = self.zoos[int(zoo_id)-1]
        except (ValueError, IndexError):
            return "No zoo with id <{}>.".format(zoo_id)
        return desired_zoo.see_animals()

    def callback_exit(self, arguments):
        exit(0)

    def callback_add_animal(self, arguments):
        zoo_id = int(arguments[0]) - 1
        desired_zoo = self.zoos[zoo_id]
        zoo_name = desired_zoo.get_name()
        species = input("species>")
        age = int(input("age>"))
        name = input("name>")
        gender = input("gender>")
        weight = float(input("weight>"))
        animal = self.db.create_animal(zoo_name, species, age, name, gender, weight)
        if animal is False:
            return "Failed to add <{}> the <{}>. He/she already exists!".format(name, species)
        if desired_zoo.add_animal(animal) is True:
            return "Added <{}> to zoo <{}>".format(name, desired_zoo.get_name())
        return "Failed to add <{}> the <{}>. Zoo <{}> is already full!".format(name, species, zoo_name)

    def callback_remove_animal(self, arguments):
        zoo_id = int(arguments[0]) - 1
        animal_id = int(arguments[0]) - 1
        desired_zoo = self.zoos[zoo_id]
        try:
            desired_zoo.remove_animal(animal_id)
        except IndexError:
            return "Animal with ID <{}>, doesn't exist in Zoo <{}>".format(animal_id, desired_zoo.get_name())
        return "Removed animal from zoo <{}>".format(desired_zoo.get_name())

    def callback_simulate_time(self, arguments):
        zoo_id = int(arguments[0]) - 1
        zoo_object = self.zoos[zoo_id]
        period_type = arguments[1]
        period = int(arguments[2])
        simulation = TimeSpanSimulator(zoo_object, period_type, period)

    def callback_help(self, arguments):
        help_message = ("* list_species - lists known animal species",
                        "* list_zoos - lists all created zoos",
                        "* see_animals <zoo_id> - lists all animal from the zoo matching the zoo_id (use list_zoos before hand)",
                        "* create_zoo - creates a zoo. Science!",
                        "* accommodate <zoo_id> - accommodates an animal in the zoo matching the zoo_id",
                        "* move_to_habitat <zoo_id> - releases an animal from the zoo matching the zoo_id",
                        "* simulate <zoo_id> <period_type> <period> - simulates a time span for the given zoo",
                        "* exit - exits. Yes, it does.")
        return "\n".join(help_message)

    def _init_callbacks(self):
        self.cp.on("list_species", self.callback_list_animal_species)
        self.cp.on("list_zoos", self.callback_list_zoos)
        self.cp.on("see_animals", self.callback_see_animals)
        self.cp.on("create_zoo", self.callback_create_zoo)
        self.cp.on("accommodate", self.callback_add_animal)
        self.cp.on("move_to_habitat", self.callback_remove_animal)
        self.cp.on("simulate", self.callback_simulate_time)
        self.cp.on("help", self.callback_help)
        self.cp.on("exit", self.callback_exit)

    def _loop(self):
        while True:
            command = input(">")
            self.cp.take_command(command)


# PROGRAM RUN
if __name__ == '__main__':
    ZooSim("animals.db")
