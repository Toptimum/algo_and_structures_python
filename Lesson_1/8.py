# 8. Определить, является ли год, который ввел пользователь, високосным или не високосным.
# Год является високосным в двух случаях: либо он кратен 4, но при этом не кратен 100, либо кратен 400.

print("Определим, является ли год високосным?")

year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"Год {year} високосный!")
else:
    print(f"Год {year} не високосный.")
