"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

N = 15
min_number1 = N
min_number2 = N

number_series = [randint(1, N) for i in range(N)]
print(f"Список случайно сгенерированных чисел: {number_series}")

for i in range(len(number_series)):
    # логическая ошибка: если сначала попадется минимальное число, то поиск работает не совсем корректно
    if number_series[i] <= min_number1:
        min_number2 = min_number1
        min_number1 = number_series[i]
print(f"В списке минимальные числа '{min_number1}' и '{min_number2}'.")
