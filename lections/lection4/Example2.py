# 1. Рекурсия

# Пример “Числа Фибоначчи”: последовательность чисел, в которой первые два числа равны 0 и 1 соответственно, а каждое следующее является суммой двух предыдущих

# Реализация чисел Фибоначчи на Python:

def fibonacci(n):
    if 0 <= n < 2:
        return n
    else:
        return fibonacci(n -1) + fibonacci(n -2)
    
print(fibonacci(10))


# 2. Каррирование

# До каррирования: функция двух аргументов, возвращающая сумму за один вызов add
def add(x, y):
    return x + y
print(add(2, 5)) # 7

# После каррирования: функция одного аргумента и возвращающая вторую функцию add_x
def add(x):
    def add_x(y):
        return x + y
    return add_x
print(add(2)(5)) # 7

# 3. Сумма квадратов: Python

# Вход: список с целыми числами
# Задача: возвести все числа в квадрат и вернуть их сумму (сумму квадратов)

# 3.1. Функциональная парадигма
def sum_squares(lst: list) -> int:
    return sum(map(lambda x: x**2, lst))

# 3.2. Структурно-процедурный подход
def sum_squares(lst: list) -> int:
    current_sum = 0
    for el in lst:
        current_sum += (el ** 2)
    return current_sum

# 3.3. ООП подход
class List:
    def __init__(self, lst):
        self.lst = lst

    def calculate_sum_squares(self):
        current_sum = 0
        for el in self.lst:
            current_sum += (el ** 2)
        self.sum_squares = current_sum


# 4. Функция композиции

# Вход: две функции
# Задача: вернуть функцию, являющуюся композицией двух полученных

def compose(f, g):
    return lambda x: f(g(x))