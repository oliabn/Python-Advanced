""" Task3
Використовуючи модуль sqlite3 та модуль smtplib,
реалізуйте реальне додавання користувачів до бази.
Мають бути реалізовані такі функції та класи:
·        клас користувача, що містить у собі такі методи:
 - get_full_name (ПІБ з поділом через пробіл: «Петров Ігор Сергійович»),
 - get_short_name (формату ПІБ: «Петров І. С.»),
 - get_age (повертає вік користувача, використовуючи поле birthday типу datetime.date);
 - метод __str__ (повертає ПІБ та дату народження);
·        функція реєстрації нового користувача (приймаємо екземпляр
 нового користувача та відправляємо email на пошту користувача з листом подяки).
·        функція відправлення email з листом подяки.
·        функція пошуку користувачів у таблиці users за іменем, прізвищем і поштою.

Протестувати цей функціонал, використовуючи заглушки у місцях надсилання пошти.
Під час штатного запуску програми вона має відправляти повідомлення на вашу реальну
поштову скриньку (необхідно налаштувати SMTP, використовуючи доступи від провайдера
вашого email-сервісу)."""


import sqlite3
from sqlite3 import Error
from Task3_User import User
from Task3_send_email import send_email
from Task3_create_users_db import create_connection, create_users_db, read_from_users_db, path_to_users
from Task3_add_user import add_user
from Task3_searchig_user_in_db import find_user_in_db
from email_password import EMAIL, APP_PASSWORD
from datetime import date
from email_password import EMAIL


user1 = User(full_name='Petrenko Igor Sergijovych',
             short_name='Petrenko I. S.',
             birthday=date(1991, 2, 4),
             email=EMAIL)
user2 = User(full_name='Sergienko Kiryl Oleksijovych',
             short_name='Sergienko K. O.',
             birthday=date(1992, 3, 4),
             email='olha@gmail.com')

create_users_db()
add_user(user1)
add_user(user2)

print()
print("find_user_in_db()")
print(find_user_in_db(full_name='Petrenko Igor Sergijovych'))
print(find_user_in_db(email='olhaaliakina@gmail.com'))
print(find_user_in_db(email='non-existent'))

print()
print('read_from_users_db()')
read_from_users_db()