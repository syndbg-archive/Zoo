# Zoo class


class Zoo():
    """docstring for Zoo"""
    def __init__(self, name, capacity, budget):
        self._name = name
        self._max_capacity = capacity
        self._current_capacity = capacity
        self._budget = budget
        self.accommodated_animals = []

    def get_name(self):
        return self._name

    def get_max_capacity(self):
        return self._max_capacity

    def get_budget(self):
        return self._budget

    def get_daily_expenses(self):
        daily_expenses = 0
        for animal in self.accommodated_animals:
            daily_expenses += animal.get_expenses()
        return daily_expenses

    def add_animal(self, animal):
        if self.is_there_space() is True:
            self.accommodated_animals.append(animal)
            self._current_capacity -= 1
            return True
        return False

    def remove_animal(self, animal_id):
        self.accommodated_animals.pop(animal_id)
        self._current_capacity += 1
        return True

    def is_there_space(self):
        if self._current_capacity > 0 and self._current_capacity <= self._max_capacity:
            return True
        return False

    def see_animals(self):
        animals = []
        for animal in self.accommodated_animals:
            animals.append("<{}>: <{}>, <{}>, <{}>".format(animal.get_name(), animal.get_species(), animal.get_age(), animal.get_weight()))
        return "\n".join(animals)
