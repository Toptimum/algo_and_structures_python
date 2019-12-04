"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

N = 5
min_number = N
min_number_index = None
max_number = 0
max_number_index = None
range_min_max = None
sum_numbers = 0

number_series = [randint(1, N) for i in range(N)]
print(f"Список случайно сгенерированных чисел: {number_series}")

# для начала найдем минимальный и максимальный элементы и запомним их индексы
for i in range(len(number_series)):
    if number_series[i] < min_number:
        min_number = number_series[i]
        min_number_index = i
    if number_series[i] > max_number:
        max_number = number_series[i]
        max_number_index = i
print(f"В списке минимальное число - {min_number} (с индексом {min_number_index}), "
      f"а максимальное - {max_number} (с индексом {max_number_index})")

# определим отрезок между минимальным и максимальным элементами, исключив их
if min_number_index < max_number_index:
    range_min_max = number_series[min_number_index + 1:max_number_index]
else:
    range_min_max = number_series[max_number_index + 1:min_number_index]
print(f"Отрезок массива между минимальным и максимальным элементами: {range_min_max}")

# теперь подсчитаем сумму элементов в отрезке
if len(range_min_max) > 0:
    for i in range(len(range_min_max)):
        sum_numbers += range_min_max[i]
    print(f"Сумма элементов = {sum_numbers}.")
else:
    print(f"К сожалению, в списке между минимальным и максимальным числами нет элементов.")
