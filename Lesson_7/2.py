"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from copy import copy
from random import uniform
from timeit import timeit


# функция сортировки методом Слияния (взято из примеров)
def merge_sort(orig_list):
    if len(orig_list) > 1:  # если длина массива больше единицы
        center = len(orig_list) // 2  # то мы делим массив на две части
        left = orig_list[:center]  # формируем массив из левой части
        right = orig_list[center:]  # и массив из правой части

        merge_sort(left)  # рекурсивно вызываем функцию разбиения массивов из левой
        merge_sort(right)  # правой частей

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


QUANTITY = 25
random_numbers = [round(uniform(0, 50), 2) for i in range(QUANTITY)]
time = timeit('merge_sort(copy(random_numbers))', globals=globals(), number=100)
sorted_numbers = merge_sort(copy(random_numbers))

print(f"Изначальный список случайных чисел:\n{random_numbers}\n")
print(f"Список чисел, сортированный методом Слияния:\n{sorted_numbers}")
print(f"Функция сортировки выполнена за {time} секунд.")  # 0.010090500000000002 секунд
