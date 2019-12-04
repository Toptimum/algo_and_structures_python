"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

N = 5
M = 4
array1 = []

print(f"Заполним двумерный массив, размером [{N}][{M}]")
for i in range(N):
    array2 = []
    sum = 0
    for j in range(M):
        array2.append(int(input(f"Введите число в ячейку [{i}][{j}]: ")))
        sum += array2[j]
    array2.append(sum)
    array1.append(array2)

print("\nВыведим заполненный массив с суммой элементов по строкам:")
for i in range(N):
    sum = 0
    for j in range(M):
        print(array1[i][j], end=' ')
        sum += array1[i][j]
    print(f"= {sum}", end=' ')
    print()
