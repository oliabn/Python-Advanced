"""Task5
Create an Exchange Rates To USD db using API Monobank (api.monobank.ua).
Do requests via request lib, parse results, write it into db.
(3 examples required)
Example:
Table - Exchange Rate To USD:

id (INT PRIMARY KEY) - 1, 2, 3, ...
currency_name (TEXT) - UAH
currency_value (REAL) - 39.5
current_date (DATETIME) - 10/22/2022 7:00 PM
"""

"""Task5_2 - Functions for creating 'exchange' table, 
filling it, and reading from a table."""

import sqlite3
from sqlite3 import Error

path_to_exchange = './data/exchange.sqlite3'


def create_connection(path):
    """Create connection with DB, return connection with DB"""

    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as err:
        print(f"The error {err} occurred")

    return connection


def create_exchange_table():
    """Create 'exchange' table"""

    create_exchange_table_query = """
    CREATE TABLE IF NOT EXISTS exchange (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_name TEXT NOT NULL,
    currency_value REAL NOT NULL,
    time timestamp);
    """

    connection = create_connection(path_to_exchange)
    cursor = connection.cursor()
    try:
        cursor.execute(create_exchange_table_query)
        connection.commit()
        print("Query executed")
        cursor.close()
    except Error as err:
        print(f"The error {err} occurred")
    finally:
        if connection:
            connection.close()


def insert_data_to_db_query(data_for_table: list):
    """Insert data to exchange table. data_for_table: list of tuples """

    insert_data_query = f"""
    INSERT INTO exchange (id, currency_name, currency_value, time)
    VALUES (NULL, ?, ?, ?)"""

    connection = create_connection(path_to_exchange)
    cursor = connection.cursor()

    # Filling the database with rows of data
    try:
        cursor.execute("SELECT id, currency_name, currency_value, time FROM exchange")
        for data in data_for_table:
            if cursor.fetchone() is None:  # If Such record not exists
                cursor.execute(insert_data_query, data)
                connection.commit()
                print("Query executed")
            else:
                print("Such record already exists")
        cursor.close()
    except Error as err:
        print(f"The error {err} occurred")
    finally:
        if connection:
            connection.close()


def read_from_db():
    """Reading a db and print rows from it"""

    connection = create_connection(path_to_exchange)
    try:
        cursor = connection.cursor()
        sqlite_select_query = """SELECT * FROM exchange"""

        currencies = cursor.execute(sqlite_select_query).fetchall()
        for currency in currencies:
            print(currency)
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    create_exchange_table()
