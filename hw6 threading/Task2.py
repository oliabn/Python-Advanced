""" Task2
Створіть три функції, одна з яких читає файл на диску
із заданим ім'ям та перевіряє наявність рядка «Wow!».
Якщо файлу немає, то засипає на 5 секунд, а потім знову
продовжує пошук по файлу. Якщо файл є, то відкриває його
і шукає рядок «Wow!». За наявності цього рядка закриває
файл і генерує подію, а інша функція чекає на цю подію
і у разі її виникнення виконує видалення цього файлу.
Якщо рядки «Wow!» не було знайдено у файлі, то засипати
на 5 секунд. Створіть файл руками та перевірте виконання
програми.
"""

import os
import threading
from time import sleep

path = './data/my_file.txt'
searched_line = 'Wow'


def is_string_in_file(path, searched_line):
    """Return True if searched_line is in file"""

    with open(path) as file:
        if searched_line in file.read():
            return True


def generate_string_found_event(path, searched_line):
    """Generates a string_found_event if the file exists and
    a searched_line exists in it.
    The file would delete when the event has been
    called using delete_file function"""

    while True:
        lock.acquire()
        if os.path.isfile(path):
            if is_string_in_file(path, searched_line):
                print(f'<{searched_line}> exists in file')
                lock.release()
                string_found_event.set()
                string_found_event.clear()
        else:
            lock.release()
            sleep(5)


def delete_file(path):
    """Delete the file if string_found_event was colled"""

    while True:
        string_found_event.wait()

        lock.acquire()
        os.remove(path)
        lock.release()

        print("File was deleted")



if __name__ == '__main__':
    string_found_event = threading.Event()
    lock = threading.RLock()

    searching_for_file_and_string = threading.Thread(target=generate_string_found_event,
                                                     args=(path, searched_line))
    deleting_file = threading.Thread(target=delete_file,
                                     args=(path,))

    searching_for_file_and_string.start()
    deleting_file.start()

    searching_for_file_and_string.join()
    deleting_file.join()
