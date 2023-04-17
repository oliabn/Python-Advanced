"""Table2
Створіть консольний інтерфейс (CLI) на Python
для додавання нових записів до бази даних.
"""

import datetime
import sqlite3
from sqlite3 import Error
from Task1 import create_connection

path_to_costs = './data/costs.sqlite3'


def execute_insert_query(connection, query: list):
    """Execute sql query - INSERT INTO 'costs'"""

    insert_costs_query = """
        INSERT INTO costs (id, purpose, amount, time)
        VALUES (NULL, ?, ?, ?)"""
    cursor = connection.cursor()
    line_for_db = (query[1], float(query[2]), datetime.datetime.now())

    try:
        cursor.execute(insert_costs_query, line_for_db)
        connection.commit()
        print("Query executed")
        cursor.close()
    except Error as err:
        print(f"The error {err} occurred")
    finally:
        if connection:
            connection.close()


def verify_query(query: list) -> bool:
    """Checking whether the query was entered correctly.
     Returns True if query is correct"""

    if len(query) != 3:
        print('Syntax Error')
        return False
    if query[0] != 'costs':
        print('Syntax Error')
        return False
    try:
        float(query[2])
        return True
    except ValueError:
        print("The amount must be a number")
        return False


def read_sqlite_table(connection):
    """Reading a db and print rows from it"""

    try:
        cursor = connection.cursor()
        sqlite_select_query = """SELECT * FROM costs"""

        costs = cursor.execute(sqlite_select_query).fetchall()
        for cost in costs:
            print(cost)
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    query = input("Enter your insert query as: costs, purpose, amount.\nE.g.: costs, charity, 700 ")
    query = query.strip().split(', ')

    if verify_query(query):
        match query[0]:
            case "costs":
                db = create_connection(path_to_costs)
                execute_insert_query(db, query)
                if db:
                    db.close()
            case _:
                print("Syntax error")

    # Test: Checking what is now in the table
    db = create_connection(path_to_costs)
    read_sqlite_table(db)
