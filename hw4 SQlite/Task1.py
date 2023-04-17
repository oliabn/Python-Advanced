"""Task1
Зробіть таблицю для підрахунку особистих витрат
із такими полями: id, призначення, сума, час.
"""

import datetime
import sqlite3
from sqlite3 import Error

path_to_costs = './data/costs.sqlite3'

create_costs_table_query = """
CREATE TABLE IF NOT EXISTS costs (
id INTEGER PRIMARY KEY AUTOINCREMENT,
purpose TEXT NOT NULL,
amount REAL NOT NULL,
time timestamp);
"""


def create_connection(path):
    """Create connection with DB, return connection with DB"""

    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as err:
        print(f"The error {err} occurred")

    return connection


def execute_query(connection, query):
    """Execute sql query"""
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed")
        cursor.close()
    except Error as err:
        print(f"The error {err} occurred")
    # finally:
    #     if connection:
    #         connection.close()


if __name__ == '__main__':
    db = create_connection(path_to_costs)
    execute_query(db, create_costs_table_query)

    if db:
        db.close()
