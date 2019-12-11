"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

# вдохновение https://pastebin.com/zaEiu1t2

from hashlib import md5

STRING = input("Введите строку: ")

substrings = {}

print("Различные подстроки в строке и их хэши: ")
for i in range(len(STRING)):
    for j in range(len(STRING) - 1 if i == 0 else len(STRING), i, -1):
        hash = md5(STRING[i:j].encode('utf-8')).hexdigest()
        substrings[STRING[i:j]] = hash
        print(f"'{STRING[i:j]}' - {hash}")
print(f"В исходной строке найдено {len(substrings)} различных подстрок.")
