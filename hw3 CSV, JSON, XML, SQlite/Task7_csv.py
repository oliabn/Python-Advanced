"""Task7
Створіть функцію яка формує CSV-файл на основі данних
введених користувачем. Файл має містити стовпчики:
імена, призвища, дати народження та місто проживання.
Реалізуйте можливість перезапису файлу, додавання нових рядків,
рядкового читання з файлу, та конвертацію всього вмісту у json.
"""

import csv
import json
import os

help_info = "Enter Name, Surname, Date of birth, city of residence separated by a comma.\n" \
            "Example: Kate, Blackwood, 10.10.2010, New York"

menu_info = "Enter 1 for writing a row of data to a CSV file (!overwrite).\n" \
            "Enter 2 for adding a line of data to the CSV file.\n" \
            "Enter 3 to convert data to json"
csv_file_name = 'data/task7.csv'
json_file_name = 'data/task7.json'


def is_correct_lenght_data_list(data: list) -> bool:
    """ Check that list has 4 elements ('name', 'surname', 'dob', 'city')"""

    if len(data) != 4:
        raise TypeError("An incorrect amount of data. Enter only the \n"
                        "specified data separated by a comma and a space")
    return True


def overwrite_row_to_csv(data: list):
    """Get the list( with data: 'name', 'surname', 'dob', 'city')
    and write it to csv file. Previous data is deleted from file"""

    with open(csv_file_name, 'w') as file:
        writer = csv.DictWriter(file,
                                fieldnames=['name', 'surname', 'dob', 'city'])
        writer.writeheader()
        writer.writerow({'name': data[0], 'surname': data[1], 'dob': data[2], 'city': data[3]})


def write_row_to_csv(data: list):
    """Get the list( with data: 'name', 'surname', 'dob', 'city')
    and write it to csv file"""

    with open(csv_file_name, 'a') as file:
        writer = csv.DictWriter(file,
                                fieldnames=['name', 'surname', 'dob', 'city'])
        if os.stat(csv_file_name).st_size == 0:
            writer.writeheader()
        writer.writerow({'name': data[0], 'surname': data[1], 'dob': data[2], 'city': data[3]})


def is_file_exist_and_not_empty(file_name: str)->bool:
    """Return True if file exist and not empty"""
    return os.path.exists(file_name) and os.stat(file_name).st_size != 0


def read_csv_file() -> dict:
    """Read csv file with data and return dict with this data"""

    if not is_file_exist_and_not_empty(csv_file_name):
        print("File data/task7.csv not exist or is empty")
        return {}

    persons = {}
    with open(csv_file_name, 'r') as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            persons[idx] = row
        return persons


def write_to_json():
    """Read data from csv file and write it to json file"""

    data = read_csv_file()
    with open(json_file_name, 'w') as file:
        json.dump(data, file, indent=4)


step = input(f'{menu_info}: ')
match step:
    case "1":
        data = input(f'{help_info}: ').split(', ')
        is_correct_lenght_data_list(data)
        overwrite_row_to_csv(data)
    case "2":
        data = input(f'{help_info}: ').split(', ')
        is_correct_lenght_data_list(data)
        write_row_to_csv(data)
    case "3":
        write_to_json()
    case _:
        print("You entered incorrect step. Enter 1, 2 or 3")
