"""Task4
Створіть агрегатні функції для підрахунку
загальної кількості  витрат i прибуткiв за
місяць. Забезпечте відповідний інтерфейс
користувача.
"""

from Task1 import create_connection
from Task3_2 import path_to_costs, path_to_profits


class TotalAmount:
    """A class for an aggregate function to calculate
    the sum value of a certain db column"""

    def __init__(self):
        self.values = []

    def step(self, item):
        if item is not None:
            self.values.append(item)

    def finalize(self):
        return sum(self.values) if self.values else 0


def get_total_amount(path: str, db_name: str):
    """Returns the sum of the 'amount' column of the DB"""

    db = create_connection(path)
    db.create_aggregate('total_amount', 1, TotalAmount)
    sql = db.cursor()
    sql.execute(f'SELECT total_amount(amount) AS result FROM {db_name}')
    total_amount = sql.fetchall()
    return total_amount[0][0]


if __name__ == '__main__':

    step = input("Enter 1 to see the total amount of costs\n"
                "Enter 2 to see the total amount of profits ")

    match step:
        case "1":
            amount = get_total_amount(path_to_costs, 'costs')
            print("Total amount:", amount)
        case "2":
            amount = get_total_amount(path_to_profits, 'profits')
            print("Total amount:", amount)
        case _:
            print("Nothing was chosen")
