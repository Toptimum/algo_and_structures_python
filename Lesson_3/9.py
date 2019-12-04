# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

N = 9
number_array = [[randint(1, N) for j in range(N)] for i in range(N)]
numbers_column = []

# сначала выводим двумерный массив для наглядности
for i in range(N):
    for j in range(N):
        print(number_array[i][j], end=' ')
    print()

# теперь определим максимальный элемент среди минимальных элементов в столбцах
for j in range(N):
    for i in range(N):
        numbers_column.append(number_array[i][j])  # собираем элементы столбцов в список
    numbers_column.sort()  # сортируем элементы столбца и тогда на втором месте будет второе минимальное число
    print(f"В {j + 1} столбце максимальный элемент среди минимальных является число '{numbers_column[1]}'")
    numbers_column = []
