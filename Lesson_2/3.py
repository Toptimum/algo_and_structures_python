"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

number = input("Введите число, которое нужно вывести в обратном порядке: ")
inverse_number = ''
i = len(number)

# решение с циклом
while i != 0:
    inverse_number += number[i - 1]
    i -= 1
print(inverse_number)
