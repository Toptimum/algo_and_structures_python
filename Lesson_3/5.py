# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

N = 15
min_number = N
min_number_index = None

number_series = [randint(-N, N) for i in range(N)]
print(f"Список случайно сгенерированных чисел: {number_series}")

for i in range(len(number_series)):
    if number_series[i] < min_number:  # находим минимальное значение и запоминаем его
        min_number = number_series[i]
        min_number_index = i
print(f"В списке минимальное число '{min_number}' находится по индексу {min_number_index}.")
