# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

number_series = [i for i in range(2, 100)]
print("Список натуральных чисел: ", number_series)
multiple_numbers = [i for i in range(2, 10)]
print("Список кратных чисел: ", multiple_numbers)

for i in range(len(multiple_numbers)):
    sum = 0
    list_multiple = []
    for j in range(len(number_series)):
        if number_series[j] % multiple_numbers[i] == 0:
            sum += 1
            list_multiple.append(number_series[j])
    print(f"Числу {multiple_numbers[i]} кратно {sum} чисел: {list_multiple}.")
