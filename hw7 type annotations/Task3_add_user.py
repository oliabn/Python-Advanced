""" Task3
Використовуючи модуль sqlite3 та модуль smtplib,
реалізуйте реальне додавання користувачів до бази.
·        функція реєстрації нового користувача (приймаємо екземпляр
 нового користувача та відправляємо email на пошту користувача з листом подяки).
"""
"""Functions for adding users to DB"""

import sqlite3
from sqlite3 import Error
from Task3_User import User
from Task3_send_email import send_email
from Task3_create_users_db import create_connection, create_users_db, read_from_users_db, path_to_users
from email_password import EMAIL, APP_PASSWORD
from datetime import date
from email_password import EMAIL


def add_user_to_users_db(user: User) -> bool:
    """Add new user to Users DB.
    We check whether this is a new user due
    to the absence of his email in the table"""

    insert_data_query = f"""
    INSERT INTO users (id, full_name, short_name, birthday, email)
    VALUES (NULL, ?, ?, ?, ?)"""
    user_data = (user.full_name, user.short_name, user.birthday, user.email)

    connection = create_connection(path_to_users)
    cursor = connection.cursor()

    # Filling the database with the user's data
    try:
        cursor.execute("SELECT * FROM users WHERE email=?", (user.email,))
        if cursor.fetchone() is None:  # If such an email record not exists
            cursor.execute(insert_data_query, user_data)
            connection.commit()
            print(f"The user {user.short_name} was added to the users table")
            if connection:
                connection.close()
            return True
        else:
            print("Such record already exists")
        cursor.close()
    except Error as err:
        print(f"The error {err} occurred")
        if connection:
            connection.close()
        return False


def add_user(user: User) -> None:
    """Add new user to Users DB and send him a message about registration"""

    MESSAGE = f"Hi {user.short_name}! You have been successfully registered, thank you."
    MSG_AND_SUBJ = f'Subject: Registration with Python\n{MESSAGE}'

    if add_user_to_users_db(user):      # if it is new user we'll add him
        if send_email(MSG_AND_SUBJ, EMAIL, APP_PASSWORD, user.email):
            print(f"The email has been sent to a new user {user.short_name}")


# Test
# if __name__ == '__main__':
#
#     user1 = User(full_name='Petrenko Igor Sergijovych',
#                 short_name='Petrenko I. S.',
#                 birthday=date(1991, 2, 4),
#                 email=EMAIL)
#     user2 = User(full_name='Sergienko Kiryl Oleksijovych',
#                 short_name='Sergienko K. O.',
#                 birthday=date(1992, 3, 4),
#                 email='olhaaliakina@gmail.com')
#
#     create_users_db()
#     add_user(user1)
#     add_user(user2)
#     read_from_users_db()
