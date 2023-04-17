"""Task4
Створіть таблицю «матеріали» з таких полів:
ідентифікатор, вага, висота та додаткові характеристики матеріалу.
Поле «додаткові  характеристики матеріалу» має зберігати у собі масив,
кожен елемент якого є кортежем із двох значень: перше – назва характеристики,
а друге – її значення.
"""

import json
import sqlite3

# Data for recording to the database:
# weight, height, additional_param: list of tuples
data = [(10, 30, [('volume', 3), ('color', 'green')]),
        (5, 15, [('volume', 1), ('color', 'yellow')]),
        (35, 45, [('volume', 75), ('color', 'white')])]


def adapt_json(data):
    """Convert data to JSON"""
    return json.dumps(data)


def convert_json(raw):
    """Convert raw from JSON to some python type"""
    return json.loads(raw)


"""If a list is to be written to the database, it will be written as JSON
If a JSON object is read from the DB, it will be converted from JSON to 
some python type"""
sqlite3.register_adapter(list, adapt_json)
sqlite3.register_converter('json', convert_json)

# Connect with DB
db = sqlite3.connect('materials.sqlite3')
sql = db.cursor()

# Create a DB 'materials' if it not exists
sql.execute("""CREATE TABLE IF NOT EXISTS 'materials'
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            weight INT, 
            height INT, 
            additional_param json)""")
db.commit()

# Filling the database with rows of data
sql.execute("SELECT weight, height, additional_param FROM materials")
for params in data:
    if sql.fetchone() is None:              # If Such record not exists
        sql.execute(
            """INSERT INTO 'materials' (id, weight, height, additional_param) 
            VALUES (NULL, ?, ?, ?)""", params)
        db.commit()
    else:
        print("Such record already exists")

# Test
if __name__ == '__main__':
    # Read from db for check it all
    materials = db.execute('SELECT * FROM "materials"').fetchall()
    for material in materials:
        print(material)
    db.close()
