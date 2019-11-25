# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

QUANTITY = 10
min_number = QUANTITY
min_number_index = None
max_number = 0
max_number_index = None

number_series = [randint(1, QUANTITY) for i in range(QUANTITY)]
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

# теперь можем поменять элементы местами
number_series[min_number_index] = max_number
number_series[max_number_index] = min_number
print(f"Список с поменянными минимальным и максимальным элементами: {number_series}.")
