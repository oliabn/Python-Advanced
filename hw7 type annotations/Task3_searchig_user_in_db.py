""" Task3

·        функція пошуку користувачів у таблиці users за іменем, прізвищем і поштою.
"""
"""Function for searching user in DB"""

import sqlite3
from sqlite3 import Error
from Task3_create_users_db import create_connection, read_from_users_db, path_to_users
from typing import Optional


def find_user_in_db(full_name: Optional[str] = None,
                    email: Optional[str] = None) -> list[tuple]:
    """Searching user in users DB ard return List of found users,
    information about each user in the corresponding tuple"""

    # forming SELECT sql query for the user searching
    if email:
        sqlite_select_query = f'SELECT * FROM users WHERE email=\"{email}\"'
    elif full_name and not email:
        sqlite_select_query = f'SELECT * FROM users WHERE full_name=\"{full_name}\"'
    elif not full_name and not email:
        print("There are no input arguments for the database search")
        return []

    connection = create_connection(path_to_users)
    cursor = connection.cursor()

    # execure Select query
    try:
        users = cursor.execute(sqlite_select_query).fetchall()
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()
        return users


# Test
# if __name__ == '__main__':
#     print(find_user_in_db(email='ddd'))
#     print(find_user_in_db(email='olhaaliakina@gmail.com'))
#     print(find_user_in_db(full_name='Petrenko Igor Sergijovych'))
