"""Task6
Для таблиці «матеріалу» з завдання 4 створіть функцію
користувача, яка приймає необмежену кількість полів
і повертає їх конкатенацію.
"""

import sqlite3


class Concatenation:
    """A class for a function to Concatenation
     of the values of a certain db rows"""

    def __init__(self):
        self.rows = set()

    def step(self, *item):
        if item is not None:
            self.rows.add(str(item))

    def finalize(self):
        return ';'.join(self.rows)


with sqlite3.connect("materials.sqlite3") as db:
    db.create_aggregate('concatenation_rows', -1, Concatenation)
    sql = db.cursor()
    sql.execute('SELECT concatenation_rows(weight, height) AS result FROM materials')
    concatenation_rows = sql.fetchall()

    print(f'concatenation_rows = {concatenation_rows}')

db.close()
