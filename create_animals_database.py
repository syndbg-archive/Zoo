# Creates a database for animal.py


# IMPORTS
import sqlite3


# FUNCTIONS
def create_animals_table(cursor):
    create_animals = '''CREATE TABLE animals(species TEXT PRIMARY KEY,
                        life_expectancy INTEGER,
                        food_type TEXT,
                        gestation INTEGER,
                        newborn_weight REAL,
                        average_weight INTEGER,
                        weight_age_ratio REAL,
                        food_weight_ratio REAL)'''
    cursor.execute(create_animals)


def create_zoos_table(cursor):
    create_zoos = '''CREATE TABLE zoos(name TEXT PRIMARY KEY,
                    capacity INTEGER,
                    budget REAL)'''
    cursor.execute(create_zoos)


def create_animals_from_zoos_table(cursor):
    create_animals_from_zoos = '''CREATE TABLE animals_from_zoos(id INTEGER PRIMARY KEY,
                        zoo_name INTEGER,
                        species TEXT,
                        name TEXT,
                        age INTEGER,
                        gender TEXT,
                        weight REAL,
                        UNIQUE(species, name))'''
    cursor.execute(create_animals_from_zoos)


def insert_species_into_table(cursor, species, life_expectancy,
                              food_type, gestation, newborn_weight, average_weight,
                              weight_age_ratio, food_weight_ratio):
    insert_query = "INSERT INTO animals values(?, ?, ?, ?, ?, ?, ?, ?);"
    cursor.execute(insert_query,
        (species, life_expectancy, food_type,
        gestation, newborn_weight, average_weight,
        weight_age_ratio, food_weight_ratio))


def create_database(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    try:
        create_animals_table(cursor)
    except sqlite3.OperationalError:
        return "Error: Table animals already exists."
    try:
        create_zoos_table(cursor)
    except sqlite3.OperationalError:
        return "Error: Table zoos already exists."
    try:
        create_animals_from_zoos_table(cursor)
    except sqlite3.OperationalError:
        return "Error: Table animals from zoos already exists."

    animals = [("lion", 15, "carnivore", 3, 2, 200, 7.5, 0.035),
                ("tiger", 20, "carnivore", 4, 1, 250, 12, 0.06),
                ("red panda", 9, "herbivore", 4, 0.15, 5, 0.25, 1),
                ("kangaroo", 12, "herbivore", 9, 8, 50, 1.75, 0.1),
                ("koala", 15, "herbivore", 7, 1, 12, 0.5, 0.05),
                ("raccoon", 3, "herbivore", 2, 0.5, 7, 0.3, 0.35),
                ("baboon", 45, "herbivore", 6, 1, 41, 1, 0.074),
                ("impala", 15, "herbivore", 6, 1, 60, 0.33, 0.1),
                ("hippo", 45, "herbivore", 8, 30, 1500, 2.72, 25),
                ("cougar", 13, "carnivore", 3, 14, 80, 0.42, 0.075),
                ("goat", 18, "herbivore", 5, 5, 52, 0.217, 0.38)]
    for animal in animals:
        insert_species_into_table(cursor, *animal)
    conn.commit()
    conn.close()
    return "Database <{}> created.".format(database_name)


def main():
    database_name = input("database name>")
    print(create_database(database_name))


if __name__ == '__main__':
    main()
