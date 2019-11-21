"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def math_expression1(number_n):
    sum_math_expression1 = 0
    for i in range(number_n + 1):
        sum_math_expression1 += i
    return sum_math_expression1


def math_expression2(number_n):
    sum_math_expression2 = int(number_n * (number_n + 1) / 2)
    return sum_math_expression2


number_n = int(input("Введите любое натуральное число: "))
sum_math_expr1 = math_expression1(number_n)
sum_math_expr2 = math_expression2(number_n)

if sum_math_expr1 == sum_math_expr2:
    print(f"Мы проверили и доказали, что для множества натуральных чисел равенство "
          f"'1+2+...+{number_n} = {number_n}*({number_n}+1)/2' выполняется!")
else:
    print("Упс, что-то пошло не так. Программа не смогла доказать равенство.")
