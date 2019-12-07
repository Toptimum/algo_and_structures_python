"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof


class Employee:
    """Базовый класс для всех сотрудников"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Employee.empCount)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))


class EmployeeSlots:
    __slots__ = ('name', 'salary')
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Employee.empCount)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))


emp1 = Employee("Андрей", 2000)
print(emp1.__dict__)
print(f"Для хранения объекта класса выделается {asizeof.asizeof(emp1)} байт памяти,")  # 240

emp2 = EmployeeSlots("Мария", 5000)
print(f"а для хранения объекта класса с __slots__ выделается {asizeof.asizeof(emp2)} байт памяти.")  # 96

# Вывод: использование классов с __slots__ значительно экономит память.
