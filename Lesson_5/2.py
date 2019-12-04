"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

# подсказка алфавита HEX_ALPHABET = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

import copy


# для начала выровняем длины списков
def equal_lists(number1, number2):
    if len(number1) < len(number2):
        for i in range(len(number2) - len(number1)):
            number1 = ['0'] + number1
    else:
        for i in range(len(number1) - len(number2)):
            number2 = ['0'] + number2
    # print(number1, number2)
    return number1, number2


# теперь переведем наши числа в десятичную систему счисления для облегчения выполнения операций
def decimal_number_system(number1, number2):
    for i in range(len(number1)):
        # если символ - это число, то преобразуем его тип
        if number1[i].isdigit():
            number1[i] = int(number1[i])
        else:  # иначе это буква и нужно заменить на число
            number1[i] = ord(number1[i]) - 55  # берем ASCII-код и вычитаем разницу для соответствия алфавиту HEX
        if number2[i].isdigit():
            number2[i] = int(number2[i])
        else:
            number2[i] = ord(number2[i]) - 55
    # print(number1, number2)
    return number1, number2


# функция сложения двух чисел (двух списков)
def addition_numbers(number1, number2):
    # операции сложения удобно выполнять с конца, поэтому перевернем списки
    number1.reverse()
    number2.reverse()
    sum_numbers = []
    razryad = 0
    for i in range(len(number1)):
        sum = number1[i] + number2[i]
        if sum > 16:
            sum_numbers.append(sum - 16 + razryad)
            razryad = 1
            # исключение: если сложить последнее число и оно получится больше 16, то число превращается 4-х знаковое
            # например, AB7 + CD4 = 178B
            if i == len(number1) - 1:
                sum_numbers.append(1)
        else:
            sum_numbers.append(number1[i] + number2[i] + razryad)
            razryad = 0
    sum_numbers.reverse()
    # print(number1, number2, sum_numbers)
    return sum_numbers


# в итоговом числе заменим числа на буквы согласно шестнадцатеричной системе счисления
def replace_numbers(number3):
    for num in range(len(number3)):
        if number3[num] > 9:
            if number3[num] == 10:
                number3[num] = 'A'
            elif number3[num] == 11:
                number3[num] = 'B'
            elif number3[num] == 12:
                number3[num] = 'C'
            elif number3[num] == 13:
                number3[num] = 'D'
            elif number3[num] == 14:
                number3[num] = 'E'
            elif number3[num] == 15:
                number3[num] = 'F'
    # print(number3)
    return number3


print("Введите 2 шестнадцатеричных числа.")

number1_original = list(input("Введите первое шестнадцетиричное число (например, A2): "))
number2_original = list(input("и второе шестнадцетиричное число (например, C4F): "))

number1, number2 = equal_lists(copy.copy(number1_original), copy.copy(number2_original))
number1, number2 = decimal_number_system(number1, number2)

number3 = addition_numbers(number1, number2)
number3 = replace_numbers(number3)
print(f"\nОперация сложения: {number1_original} + {number2_original} = {number3}")
