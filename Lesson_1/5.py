# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print("Введите две строчные буквы английского алфавита.")
first_letter = input("Первая буква: ")
last_letter = input("Вторая буква: ")
if first_letter > last_letter:  # начало диапазона должно быть меньше конца
    first_letter, last_letter = last_letter, first_letter

# функция ord(char) возвращает ASCII-код символа
print(f"В английском алфавите буква '{first_letter}' находится на {ord(first_letter) - 96} позиции,")
print(f"а буква '{last_letter}' на {ord(last_letter) - 96} позиции.")
print(f"Между ними находится {(ord(last_letter) - 96) - (ord(first_letter) - 96) - 1} букв(ы).")
