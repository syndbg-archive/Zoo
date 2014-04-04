# Simulates a time span in a zoo


# IMPORTS
from random import random


class TimeSpanSimulator():
    """docstring for TimeSpanSimulator"""
    def __init__(self, zoo_object, period_type, period):
        self.zoo = zoo_object
        self.period_type = period_type
        self.period = self.get_total_period(period_type, period)
        self.going_to_die_animals = []
        self.newborn_animals = []

    def list_animals_stats(self):
        return self.zoo.see_animals()

    def list_newborn_animals(self):
        return "\n".join(self.newborn_animals)

    def list_going_to_die_animals(self):
        return "\n".join(self.going_to_die_animals)

    def grow_all_animals(self):
        for animal_object in self.zoo.accommodated_animals:
            animal_object.age()

    def get_dying_animals(self):
        for animal_object in self.zoo.accommodated_animals:
            chance_animal_to_die = random()
            if chance_animal_to_die <= animal_object.chance_to_die:
                self.going_to_die_animals.append("<{}> the <{}>".format())
                self.zoo.accommodated_animals.remove(animal_object)

    # def get_newborn_animals(self):
    #     for animal_object in self.zoo.accommodated_animals:
    #         chance_new_born = random()

    def get_total_period(self, period_type, period):
        if period_type == "weeks" or period_type == "week":
            period *= 7
        elif period_type == "months" or period_type == "month":
            period *= 30
        elif period_type == "years" or period_type == "year":
            period *= 365
        return period
