"""
2. Написать два алгоритма нахождения i-го по счёту простого числа:
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена».
"""

import timeit


# алгоритм Решето Эратосфена для генерации списка простых чисел
def sieve_of_eratosthenes(n):
    odds = range(3, n + 1, 2)
    sieve = set(sum([list(range(q * q, n + 1, q + q)) for q in odds], []))
    return [2] + [p for p in odds if p not in sieve]


# алгоритм нашел в интернете
def prime_gen(n):
    primes = [2]
    a = 2
    while a < n:
        counter = 0
        for i in primes:
            if a % i == 0:
                counter += 1
        if counter == 0:
            primes.append(a)
        else:
            counter = 0
        a = a + 1
    return primes


QUANTITY = int(input("Введите, сколько простых чисел нужно сгенерировать: "))

# Без использования «Решета Эратосфена»
number_series1 = prime_gen(QUANTITY)
time1 = timeit.timeit('prime_gen(QUANTITY)', globals=globals(), number=100)  # при 2000 чисел 3.4113548 секунд
print(f"\n2. Список простых чисел, сгенерированный простым алгоритмом: {number_series1},"
      f"\nпо времени это занимает {time1} секунд.")

# Используя алгоритм «Решето Эратосфена»
number_series2 = sieve_of_eratosthenes(QUANTITY)
time2 = timeit.timeit('sieve_of_eratosthenes(QUANTITY)', globals=globals(), number=100)  # 0.43259870000000067 секунд
print(f"\n2. Список простых чисел, сгенерированный алгоритмом 'Решето Эратосфена': {number_series2},"
      f"\nпо времени это занимает {time2} секунд.")
