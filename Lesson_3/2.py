"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

number_series = list(input("Введите список чисел через пробел( ): ").split())
indexes = []

for i in range(len(number_series)):
    if int(number_series[i]) % 2 == 0:
        indexes.append(i + 1)

print(f"В списке чисел {number_series} четные элементы находятся на следующих позициях: {indexes}.")
