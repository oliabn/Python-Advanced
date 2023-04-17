"""Task4
Створіть звичайну функцію множення двох чисел.
Створіть каррувану функцію множення двох чисел.
Частково застосуйте її до одного аргументу, до двох аргументiв
"""


def mult(x, y):
    return x * y


def currying_multiply(x):
    """Currying func. of multiplying"""
    def multiply(y):
        return x * y

    return multiply


print(f'Normal func.: {mult(5, 5)}')
print(f'Currying func.: {currying_multiply(5)(5)}')

multiply_to_2 = currying_multiply(2)
print(f'multiply_to_2: {multiply_to_2(5)}')
