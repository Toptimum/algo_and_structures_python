"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

print("Программа найдет 'наибольшее число по сумме цифр' среди введенных чисел.")
number_series = list(input("Введите список натуральных чисел через пробел( ): ").split())
max_number = 0
max_sum = 0
sum = 0

for i in range(len(number_series)):
    for num in range(len(number_series[i])):
        sum += int(number_series[i][num])
    if max_sum < sum:
        max_sum = sum
        max_number = number_series[i]
        sum = 0

print(f"В последовательности чисел {number_series} число {max_number} является наибольшим по сумме цифр {max_sum}.")
