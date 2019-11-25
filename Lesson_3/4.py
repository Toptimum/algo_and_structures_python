# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

N = 10
number = None
max_quantity = 0

number_series = [randint(1, N) for i in range(N)]
print(f"Список случайно сгенерированных чисел: {number_series}")

for i in range(len(number_series)):
    quantity = 0
    for j in range(len(number_series)):  # подсчитываем птовторяющиеся числа
        if number_series[i] == number_series[j]:
            quantity += 1
    if quantity > max_quantity:  # запоминаем самое популярное число
        max_quantity = quantity
        number = number_series[i]
print(f"В списке чаще всего встречается число '{number}' - оно повторяется {max_quantity} раз(а).")
