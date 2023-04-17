"""Task1
Створіть співпрограму, яка отримує контент із зазначених посилань
і логує хід виконання в database, використовуючи стандартну
бібліотеку requests, а потім проробіть те саме з бібліотекою aiohttp.
Кроки, які мають бути залоговані: початок запиту до адреси X,
відповідь для адреси X отримано зі статусом 200. Перевірте хід
виконання програми на >3 ресурсах і перегляньте послідовність
запису логів в обох варіантах і порівняйте результати. Для двох
видів завдань використовуйте різні файли для логування, щоби
порівняти отриманий результат.
"""

"""Task1_1 - functions for create db, filling it, and reading from a table."""

import sqlite3
from sqlite3 import Error

path_to_db = './data/request_logs.sqlite3'


def create_connection(path):
    """Create connection with DB, return connection with DB"""

    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as err:
        print(f"The error {err} occurred")

    return connection


def create_db(path_to_db):
    """Create 'request_logs' table"""

    create_request_logs_query = """
        CREATE TABLE IF NOT EXISTS request_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status TEXT NOT NULL);
        """

    connection = create_connection(path_to_db)
    cursor = connection.cursor()
    try:
        cursor.execute(create_request_logs_query)
        connection.commit()
        print("Query executed")
        cursor.close()
    except Error as err:
        print(f"The error {err} occurred")
    finally:
        if connection:
            connection.close()


def insert_data_to_db_query(data_for_table: str):
    """Insert data to db"""

    insert_data_query = f"""
    INSERT INTO request_logs (id, status)
    VALUES (NULL, ?)"""

    connection = create_connection(path_to_db)
    cursor = connection.cursor()

    # Filling the database
    try:
        cursor.execute(insert_data_query, (data_for_table,))
        connection.commit()
        print("Query executed")
        cursor.close()
    except Error as err:
        print(f"The error {err} occurred")
    finally:
        if connection:
            connection.close()


def read_from_db():
    """Reading a db and print rows from it"""

    connection = create_connection(path_to_db)
    try:
        cursor = connection.cursor()
        select_query = """SELECT * FROM request_logs"""

        logs = cursor.execute(select_query).fetchall()
        for log in logs:
            print(log)
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()
