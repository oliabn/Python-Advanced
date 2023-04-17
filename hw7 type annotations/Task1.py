"""Task1
Створіть функцію, яка приймає список з елементів типу int,
а повертає новий список з рядкових значень вихідного масиву.
Додайте анотацію типів для вхідних і вислідних значень функції.
"""


def get_list_of_str_elem(input_list: list[int]) -> list[str]:
    """Converts elements of list from int to str"""
    return list(map(str, input_list))

# test
print(get_list_of_str_elem([1, 2, 3]))
