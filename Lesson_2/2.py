"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

natural_number = input("Введите целое натуральное число: ")

even_number = 0  # четное число
even_number_list = ""
odd_number = 0  # нечетное число
odd_number_list = ""

for i in range(0, len(natural_number)):
    if int(natural_number[i]) % 2 == 0:
        even_number_list += natural_number[i] + ' '
        even_number += 1
    else:
        odd_number_list += natural_number[i] + ' '
        odd_number += 1

print(f"В введенном числе {natural_number}: {even_number} четные цифры ({even_number_list.rstrip()}) и "
      f"{odd_number} нечетных ({odd_number_list.rstrip()}).")
