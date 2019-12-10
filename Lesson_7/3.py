"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from copy import copy
from random import randint
from timeit import timeit


# быстрый и простой способ найти медиану массива
def fast_way(random_numbers):
    random_numbers.sort()
    median = random_numbers[len(random_numbers) // 2]
    return random_numbers, median


QUANTITY = int(input("Введите натуральное число M: "))
random_numbers = [randint(0, 50) for i in range(2 * QUANTITY + 1)]
print(f"\nИзначальный список случайных чисел:\n{random_numbers},")

time = timeit('fast_way(random_numbers)', globals=globals(), number=100)
sorted_numbers, median = fast_way(copy(random_numbers))
print(f"\nСортированный список чисел:\n{sorted_numbers},")
print(f"В этом списке число '{median}' является медианой массива,")
print(f"Функция поиска медианы выполнена за {time} секунд.")  # 0.00010159999999981295 секунд
