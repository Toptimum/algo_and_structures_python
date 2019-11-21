"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


# функция генерации ряда чисел
def generate_range(quantity):
    i = 1
    num = 1
    series_numbers = []
    while i < quantity + 1:
        if i % 2 != 0:  # на четную позицию записываем положительное число
            series_numbers.append(num)
        else:  # на нечетную позицию записываем отрицательное число
            series_numbers.append(-num)
        num = num / 2
        i += 1
    return series_numbers


# суммируем числа в ряде чисел
def sum_numbers(series_numbers):
    sum = 0
    for i in range(len(series_numbers)):
        sum += series_numbers[i]
    return sum


quantity = int(input("Введите количество элементов для генерации ряда чисел: "))
series_numbers = generate_range(quantity)
print(f"Сгенерировали ряд чисел: {series_numbers}")
sum = sum_numbers(series_numbers)
print(f"Cумма чисел в ряде = {sum}.")
