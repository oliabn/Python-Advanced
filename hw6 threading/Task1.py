""" Task1
Створіть функцію для обчислення факторіала числа.
Запустіть декілька завдань,використовуючи Thread,
заміряйте швидкість їхнього виконання, а потім заміряйте
швидкість обчислення, використовуючи той же набір завдань
на ThreadPoolExecutor. Як приклади використовуйте останні
значення, від мінімальних і до максимально можливих, щоб
побачити приріст або втрату продуктивності.
"""

# import functools
from functools import reduce, wraps
from threading import *
from concurrent.futures import ThreadPoolExecutor
from time import time


def get_time_of_exetuting(func):
    """Prints time of function executing"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        srart_time = time()
        res = func(*args, **kwargs)
        exec_time = time() - srart_time
        print(f"Function execution time: {exec_time}")
        return res
    return wrapper


def get_factorial(number: int) -> int:
    """Returns the factorial of a number and print it"""

    chain = range(2, number+1)
    factorial = reduce(lambda prev_elem_product, next_elem:
                       prev_elem_product * next_elem,
                       chain)
    print(f'{number}!= {factorial}')
    return factorial


@get_time_of_exetuting
def run_by_tread_pool():
    """Gets the factorials by ThreadPoolExecutor and measures the execution time"""

    with ThreadPoolExecutor(max_workers=10) as executor:
        first_future = executor.submit(get_factorial, number=5)
        second_future = executor.submit(get_factorial, number=50)
        third_future = executor.submit(get_factorial, number=55)


@get_time_of_exetuting
def run_by_threads():
    """Gets the factorials by threads and measures the execution time"""

    first_tread = Thread(target=get_factorial, args=(5,))
    second_tread = Thread(target=get_factorial, args=(50,))
    third_thread = Thread(target=get_factorial, args=(55,))

    first_tread.start()
    second_tread.start()
    third_thread.start()

    first_tread.join()
    second_tread.join()
    third_thread.join()


run_by_tread_pool()
run_by_threads()
