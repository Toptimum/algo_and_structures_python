"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

# ссылка на источник http://practice.keyfire.ru/blog/kak-zakodirovat-stroku-s-pomoshyu-algoritma-haffmana/
# подробнее http://e-postulat.ru/index.php/Postulat/article/viewFile/617/638

import heapq  # модуль для работы с мин. кучей из стандартной библиотеки Python
from collections import Counter  # словарь в котором для каждого объекта поддерживается счетчик
from collections import namedtuple


# добавим классы для хранения информации о структуре дерева
# воспользуемся функцией namedtuple из стандартной библиотеки
class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов; у них есть потомки
    def walk(self, code, acc):
        # чтобы обойти дерево нам нужно:
        self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева, у него нет потомков, но есть значение символа
    def walk(self, code, acc):
        # потомков у листа нет, поэтому для значения мы запишем построенный код для данного символа
        code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"


def huffman_encode(s):  # функция кодирования строки в коды Хаффмана
    h = []  # инициализируем очередь с приоритетами
    for ch, freq in Counter(s).items():  # постоим очередь с помощью цикла, добавив счетчик, уникальный для всех листьев
        h.append((freq, len(h), Leaf(ch)))  # очередь будет представлена частотой символа, счетчиком и самим символом
    heapq.heapify(h)  # построим очередь с приоритетами
    count = len(h)  # инициализируем значение счетчика длиной очереди
    while len(h) > 1:  # пока в очереди есть хотя бы 2 элемента
        freq1, _count1, left = heapq.heappop(h)  # вытащим элемент с минимальной частотой - левый узел
        freq2, _count2, right = heapq.heappop(h)  # вытащим следующий элемент с минимальной частотой - правый узел
        # поместим в очередь новый элемент, у которого частота равна сумме частот вытащенных элементов
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # добавим новый внутренний узел у которого
        # потомки left и right соответственно
        count += 1  # инкрементируем значение счетчика при добавлении нового элемента дерева
    code = {}  # инициализируем словарь кодов символов
    if h:  # если строка пустая, то очередь будет пустая и обходить нечего
        [(_freq, _count, root)] = h  # в очереди 1 элемент, приоритет которого не важен, а сам элемент - корень дерева
        root.walk(code, "")  # обойдем дерева от корня и заполним словарь для получения кодирования Хаффмана
    return code  # возвращаем словарь символов и соответствующих им кодов


def main():
    s = input("Введите строку, которую необходимо закодировать: ")  # читаем строку
    code = huffman_encode(s)  # кодируем строку
    encoded = "".join(code[ch] for ch in s)  # отобразим закодированную версию, отобразив каждый символ
    # в соответствующий код и конкатенируем результат
    print(f"В строке {len(code)} уникальных символов, каждому символу соответствует код: ")
    for ch in sorted(code):  # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
        print(f"'{ch}' - {code[ch]}")  # выведем символ и соответствующий ему код
    print(f"Закодированная строка, длиной {len(encoded)} знаков: {encoded}.")  # выведем закодированную строку


main()
