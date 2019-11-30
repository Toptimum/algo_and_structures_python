"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# реализуем несколько алгоритмов сортировки списка чисел
import timeit
import copy
import random

QUANTITY = 50
NUMBER_SERIES_ORIGINAL = [random.randint(1, QUANTITY) for i in range(QUANTITY)]
print(f"Оригинальный список случайно сгенерированных чисел:\n{NUMBER_SERIES_ORIGINAL}")

# 1. стандартный способ сортировки с использованием .sort()
number_series_copy1 = copy.copy(NUMBER_SERIES_ORIGINAL)
time1 = timeit.timeit('number_series_copy1.sort()', globals=globals(), number=1000)  # 0.0005606999999999973 - победа!
print(f"\n1. Сортировка чисел встроенным методом .sort() выполняется за {time1} секунд, "
      f"сортированный список чисел:\n{number_series_copy1}.")

# 2. способ сортировки с использованием стандартной функции sorted()
time2 = timeit.timeit('sorted(NUMBER_SERIES_ORIGINAL)', globals=globals(), number=1000)  # 0.0023967000000000016
number_series_copy2 = sorted(NUMBER_SERIES_ORIGINAL)
print(f"\n2. Сортировка чисел стандартной функцией sorted() выполняется за {time2} секунд, "
      f"сортированный список чисел:\n{number_series_copy2}.")

# 3. знаменитый Пузырьковый алгоритм сортировки
number_series_copy3 = copy.copy(NUMBER_SERIES_ORIGINAL)
time3 = timeit.timeit('''
swapped = True
while swapped:
    swapped = False
    for i in range(len(number_series_copy3) - 1):
        if number_series_copy3[i] > number_series_copy3[i + 1]:
            # Меняем элементы
            number_series_copy3[i], number_series_copy3[i + 1] = number_series_copy3[i + 1], number_series_copy3[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True''', globals=globals(), number=1000)  # 0.010478000000000001
print(f"\n3. Сортировка чисел Пузырьковым алгоритмом выполняется за {time3} секунд, "
      f"сортированный список чисел:\n{number_series_copy3}.")


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
time4 = timeit.timeit('quicksort(number_series_copy4)', globals=globals(), number=1000)  # 0.1434489
print(f"\n4. Сортировка чисел Быстрым алгоритмом выполняется за {time4} секунд, "
      f"сортированный список чисел:\n{number_series_copy4}.")
