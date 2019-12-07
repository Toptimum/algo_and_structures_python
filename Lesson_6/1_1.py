import sys
from memory_profiler import profile


@profile
def addition_numbers(num1, num2):
    sum_numbers = hex(num1 + num2)
    sum_numbers = str(sum_numbers)[2:]
    return sum_numbers.upper()


@profile
def multiplication_numbers(num1, num2):
    multi_numbers = hex(num1 * num2)
    multi_numbers = str(multi_numbers)[2:]
    return multi_numbers.upper()


print("Введите 2 шестнадцатеричных числа.")

number1_original = input("Введите первое шестнадцетиричное число (например, A2): ")
number2_original = input("и второе шестнадцетиричное число (например, C4F): ")

num1, num2 = int(number1_original, 16), int(number2_original, 16)

sum_numbers = addition_numbers(num1, num2)
print(f"\nОперация сложения: {number1_original} + {number2_original} = {sum_numbers.upper()}")
print(f"Число {sum_numbers} занимает {sys.getsizeof(sum_numbers)} памяти")

multi_numbers = multiplication_numbers(num1, num2)
print(f"\nОперация умножения: {number1_original} + {number2_original} = {multi_numbers.upper()}")
print(f"Число {multi_numbers} занимает {sys.getsizeof(sum_numbers)} памяти")

# Вывод: числа в памти и функции сложения и умножениях этих чисел одинаково занимают памяти (13.4 MiB),
# подробнее на скриншоте по ссылке https://yadi.sk/d/vlhzKoAOAe5fpQ
