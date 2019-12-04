"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# реализуем несколько алгоритмов сортировки списка чисел
import cProfile
import copy
import random

QUANTITY = 10000
NUMBER_SERIES_ORIGINAL = [random.randint(1, QUANTITY) for i in range(QUANTITY)]

# 1. стандартный способ сортировки с использованием .sort()
number_series_copy1 = copy.copy(NUMBER_SERIES_ORIGINAL)
cProfile.run('number_series_copy1.sort()')  # 4 function calls in 0.002 seconds

# 2. способ сортировки с использованием стандартной функции sorted()
cProfile.run('number_series_copy2 = sorted(NUMBER_SERIES_ORIGINAL)')  # 4 function calls in 0.002 seconds


# 3. знаменитый Пузырьковый алгоритм сортировки - долго выполняется! нужно ждать
def sort3(number_series_copy3):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(number_series_copy3) - 1):
            if number_series_copy3[i] > number_series_copy3[i + 1]:
                # Меняем элементы
                number_series_copy3[i], number_series_copy3[i + 1] = number_series_copy3[i + 1], number_series_copy3[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


number_series_copy3 = copy.copy(NUMBER_SERIES_ORIGINAL)
cProfile.run('sort3(number_series_copy3)')  # 9867 function calls in 30.458 seconds


# 4. алгоритм Быстрой сортировки (нашел в интернете)
def quicksort(number_series_copy4):
    if len(number_series_copy4) <= 1:
        return number_series_copy4
    else:
        q = random.choice(number_series_copy4)
    l_nums = [n for n in number_series_copy4 if n < q]
    e_nums = [q] * number_series_copy4.count(q)
    b_nums = [n for n in number_series_copy4 if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


number_series_copy4 = copy.copy(NUMBER_SERIES_ORIGINAL)
cProfile.run('quicksort(number_series_copy4)')  # 59832 function calls (50334 primitive calls) in 0.058 seconds
