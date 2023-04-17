"""Task 3
 Functions for creating DB and reading DB"""

import sqlite3
from sqlite3 import Error
from datetime import date

path_to_users = './data/users.sqlite3'


def create_connection(path: str) -> None:
    """Create connection with DB, return connection with DB"""

    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as err:
        print(f"The error {err} occurred")

    return connection


def create_users_db() -> None:
    """Create users DB"""

    create_users_table_query = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    short_name TEXT,
    birthday timestamp,
    email TEXT NOT NULL);
    """

    connection = create_connection(path_to_users)
    cursor = connection.cursor()
    try:
        cursor.execute(create_users_table_query)
        connection.commit()
        print("The Users table has been created")
        cursor.close()
    except Error as err:
        print(f"The error {err} occurred")
    finally:
        if connection:
            connection.close()


def read_from_users_db() -> None:
    """Reading a DB and print users from it"""

    connection = create_connection(path_to_users)
    try:
        cursor = connection.cursor()
        sqlite_select_query = """SELECT * FROM users"""

        users = cursor.execute(sqlite_select_query).fetchall()
        for user in users:
            print(user)
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()
