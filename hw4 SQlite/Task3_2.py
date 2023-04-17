""""Task3
Змініть таблицю так, щоби можна було додати
не лише витрати, а й прибутки.
"""

"""Task3_2 Adding data to DB 'costs' and 'profits' """

import datetime
import sqlite3
from sqlite3 import Error
from Task1 import create_connection

path_to_costs = './data/costs.sqlite3'
path_to_profits = './data/profits.sqlite3'


def execute_insert_query(connection, query: list):
    """Execute sql query - INSERT INTO 'costs'/'profits' """

    insert_costs_query = """
        INSERT INTO costs (id, purpose, amount, time)
        VALUES (NULL, ?, ?, ?)"""
    insert_profits_query = """
        INSERT INTO profits (id, source, amount, time)
        VALUES (NULL, ?, ?, ?)"""

    cursor = connection.cursor()
    line_for_db = (query[1], float(query[2]), datetime.datetime.now())

    try:
        if query[0] == 'costs':
            cursor.execute(insert_costs_query, line_for_db)
            connection.commit()
            print("Query executed")

        if query[0] == 'profits':
            cursor.execute(insert_profits_query, line_for_db)
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
    if query[0] not in ['costs', 'profits']:
        print('Syntax Error')
        return False
    try:
        float(query[2])
        return True
    except ValueError:
        print("The amount must be a number")
        return False


def read_sqlite_table(connection, db_name: str):
    """Reading a db and print rows from it"""

    try:
        cursor = connection.cursor()
        sqlite_select_query = f"""SELECT * FROM {db_name}"""

        table = cursor.execute(sqlite_select_query).fetchall()
        for line in table:
            print(line)
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    query = input("Enter your insert query as: costs, purpose, amount."
                  "\nE.g.: costs, charity, 700\nE.g.: profits, work, 3000 ")
    query = query.strip().split(', ')

    if verify_query(query):
        match query[0]:
            case "costs":
                db = create_connection(path_to_costs)
                execute_insert_query(db, query)
                if db:
                    db.close()
            case "profits":
                db = create_connection(path_to_profits)
                execute_insert_query(db, query)
                if db:
                    db.close()
            case _:
                print("Syntax error")

    # Test: Checking what is now in the tables
    print('costs:')
    db = create_connection(path_to_costs)
    read_sqlite_table(db, 'costs')

    print('profits:')
    db = create_connection(path_to_profits)
    read_sqlite_table(db, 'profits')
