"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

import sys


# функция ввода данных
def enter_data():
    num1_enter = input("Введите первое число: ")
    num2_enter = input("Введите второе число: ")
    operation_enter = input("Введите знак операции сложения(+), вычитания(-), умножения(*) или деления(/), "
                            "либо ноль(0) для выхода из программы: ")
    return num1_enter, num2_enter, operation_enter


# функция проверки введенных данных
def check_data(num1_check, num2_check, operation_check):
    correct_data_message = True
    if operation_check == '0':
        print("Выход из программы. До свидания.")
        sys.exit()
    try:
        try:
            num1_check = int(num1_check)
            num2_check = int(num2_check)
        except:
            print("Введено нечисловое значение. Операции могут выполняться только с числами.")
            correct_data_message = False
        if operation_check == '/' and num2_check == 0:
            print("Невозможно делить на ноль.")
            correct_data_message = False
        elif operation_check != '+' and operation_check != '-' and operation_check != '*' and operation_check != '/':
            print("Введен ошибочный знак операции.")
            correct_data_message = False
    except:
        print("Ошибка ввода. Введите данные заново.")
        correct_data_message = False
    return num1_check, num2_check, correct_data_message


# функция выполнения математической операции с данными
def math_operation(num1_execution, num2_execution, operation_execution):
    if operation_execution == '+':
        resultant = num1_execution + num2_execution
    elif operation_execution == '-':
        resultant = num1_execution - num2_execution
    elif operation_execution == '*':
        resultant = num1_execution * num2_execution
    elif operation_execution == '/':
        resultant = num1_execution / num2_execution
    else:
        resultant = "Упс, что-то пошло не так. Математическая операция не выполнена."
    return resultant


# бесконечный цикл выполнения программы
while True:
    num1, num2, operation = enter_data()
    num1, num2, correct_data = check_data(num1, num2, operation)
    if not correct_data:
        print("Выполнение операции невозможно. Введите данные заново.")
    else:
        print(f"В итоге {num1} {operation} {num2} = {math_operation(num1, num2, operation)}.")

