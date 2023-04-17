""""Task5
Для таблиці «матеріалу» з завдання 4 створіть користувальницьку
агрегатну функцію, яка рахує середнє значення ваги всіх матеріалів
вислідної вибірки й округляє значення до цілого.
"""

import sqlite3


class Average:
    """A class for an aggregate function to calculate
    the mean value of a certain db column"""

    def __init__(self):
        self.values = []

    def step(self, item):
        if item is not None:
            self.values.append(item)

    def finalize(self):
        return round(sum(self.values) / len(self.values)) if self.values else 0


with sqlite3.connect("materials.sqlite3") as db:
    db.create_aggregate('average_val', 1, Average)
    sql = db.cursor()
    sql.execute('SELECT average_val(weight) AS result FROM materials')
    mean_weight = sql.fetchall()[0][0]

    print(f'mean_weight = {mean_weight}')
    assert mean_weight == round((10+5+35)/3), f'mean_weight should be {round((10+5+35)/3)}'

db.close()
