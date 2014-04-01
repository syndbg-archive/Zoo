import sqlite3
import create_animals_database

class Animal():

	def __init__ (self, species, age, name, gender, weight):
		self.species = species
		self.age = age
		self.name = name
		self.gender = gender
		self.weight = weight

	def age(self):
		conn = sqlite3.connect("animals.db")
		cursor = conn.cursor()

		select_animal = ("Enter animal species> ")
		result = ("SELECT animals(life_expectancy) FROM animals WHERE species = (?)")
		cursor.execute(result, (select_animal))

		conn.commit()
		conn.close()

		if self.age != result
			grow_age = input ("increase age by> ")
			self.age += grow_age

		return self.age

	def grow(self):
		conn = sqlite3.connect("animals.db")
		cursor = conn.cursor()

		select_animal = ("Enter animal species> ")

		result = ("SELECT animals(average_weight) FROM animals WHERE species = (?)")
		cursor.execute(result, (select_animal))

		conn.commit()
		conn.close()

		if self.weight != result:
			grow_weight = input ("increase weight by> ")
			self.weight += grow_weight
		
		return self.weight

	def eat(self):
		conn = sqlite3.connect("animals.db")
		cursor = conn.cursor()

		select_animal = ("Enter animal species> ")

		result = ("SELECT animals(food_weight_ratio) FROM animals WHERE species = (?)")
		cursor.execute(result, (select_animal))
		
		conn.commit()
		conn.close()


		food_needed = self.weight / result

		return food_needed


	def kill_animal(self):
		conn = sqlite3.connect("animals.db")
		cursor = conn.cursor()

		select_animal = ("Enter animal species> ")

		result = ("DELETE FROM animals WHERE species = (?)")
		cursor.execute(result, (select_animal))

		conn.commit()
		conn.close()

	def chance_to_die(self):
		conn = sqlite3.connect("animals.db")
		cursor = conn.cursor()

		select_animal = ("Enter animal species> ")

		result = ("SELECT animals(life_expectancy) FROM animals WHERE species = (?)")
		cursor.execute(result, (select_animal))

		conn.commit()
		conn.close()

		if self.age == result:
			print ("I`m sorry , but the animal has died ... ")
			kill_animal():
			break
		else:
			break
