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

import random


# функция ввода значений
def func_input():
    print(f"\nСгенерируем случайное целое число, вещественное число или символ в диапазоне.")
    begin_range = input("Введите начало диапазона: ")
    end_range = input("и конец диапазона: ")
    begin_range, end_range = func_sort(begin_range, end_range)
    return begin_range, end_range


# функция сортировки значений, чтобы начало и конец диапазона были правильными
def func_sort(begin_range, end_range):
    if begin_range > end_range:  # начало диапазона должно быть меньше конца
        begin_range, end_range = end_range, begin_range
    return begin_range, end_range


# функция генерации случайного значения
def func_generate(type_symb, begin_range, end_range):
    if type_symb == "целое число":
        rand_num = random.randint(int(begin_range), int(end_range))
    elif type_symb == "вещественное число":
        rand_num = random.uniform(float(begin_range), float(end_range))
    else:
        rand_num = random.randint(ord(begin_range), ord(end_range))
    return rand_num


type_symb = "целое число"
begin_range, end_range = func_input()
rand_num = func_generate(type_symb, begin_range, end_range)
print(f"Случайное {type_symb} в диапазоне ({begin_range};{end_range}): {rand_num}.")

type_symb = "вещественное число"
begin_range, end_range = func_input()
rand_num = func_generate(type_symb, begin_range, end_range)
print(f"Случайное {type_symb} в диапазоне ({begin_range};{end_range}): {rand_num}.")

type_symb = "символ"
begin_range, end_range = func_input()
rand_char = func_generate(type_symb, begin_range, end_range)
print(f"Случайный {type_symb} в диапазоне ({begin_range};{end_range}): {chr(rand_char)}.")
