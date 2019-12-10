"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from copy import copy
from random import randint
from timeit import timeit


# функция сортировки методом Пузырька по убыванию
def bubble_sort(numbers):
    n = 1
    while n < len(numbers):
        for i in range(len(numbers) - n):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        n += 1
    return numbers


QUANTITY = 30
random_numbers = [randint(-100, 100) for i in range(QUANTITY)]
time = timeit('bubble_sort(copy(random_numbers))', globals=globals(), number=100)
sorted_numbers = bubble_sort(copy(random_numbers))

print(f"Изначальный список случайных чисел:\n{random_numbers}\n")
print(f"Список чисел, сортированный методом Пузырька по убыванию:\n{sorted_numbers}")
print(f"Функция сортировки выполнена за {time} секунд.")  # 0.0171035 секунд
