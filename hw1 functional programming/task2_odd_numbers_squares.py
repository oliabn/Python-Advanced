"""Task2
Створіть список цілих чисел. Отримайте список
квадратів непарних чисел із цього списку.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_num_squares = [num ** 2 for num in numbers if num % 2]
odd_num_squares_2 = list(map(lambda x: x**2, filter(lambda x: x % 2, numbers)))

print(odd_num_squares)
print(odd_num_squares_2)
