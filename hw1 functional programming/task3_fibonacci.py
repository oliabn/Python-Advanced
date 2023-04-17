"""Task3
Створіть функцію-генератор чисел Фібоначчі.
Застосуйте до неї декоратор, який залишатиме
в послідовності лише парні числа.
"""

from functools import wraps


def even_numbers(func):
    @wraps(func)
    def wrapper(n):
        generator = func(n)
        for elem in generator:
            if not elem % 2:
                yield elem
    return wrapper


@even_numbers
def fibonacci(n):
    """Get n first Fibonacci numbers and
    return only even numbers from them"""

    last, next = 1, 2
    for _ in range(n):
        yield last
        last, next = next, last + next


print('Fib = 1 2 3 5 8 13 21 34 55 89 144...\n')
print("Result: ")
for num in fibonacci(11):
    print(num)
