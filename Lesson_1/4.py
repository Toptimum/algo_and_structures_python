"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""


# не решена

def func_input():
    print("Сгенерируем случайное целое число, вещественное число или символ в диапазоне.")
    begin_range = input("Введите начало диапазона: ")
    end_range = input("и конец диапазона: ")
    if begin_range > end_range:  # начало диапазона должно быть меньше конца
        begin_range, end_range = end_range, begin_range
    return begin_range, end_range


def func_generate(begin_range, end_range):
    rand_num = int(begin_range) + int(end_range)
    return rand_num


begin_range, end_range = func_input()

print(f"Случайное значение в диапазоне ({begin_range};{end_range}): {func_generate(begin_range, end_range)}.")
