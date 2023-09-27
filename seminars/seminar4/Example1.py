# 1. Что за парадигма: конвертация

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

temps_cels = [0, 5, 10, 15, 20, 25, 30]
temp_fahr = list(map(celsius_to_fahrenheit, temps_cels))
print(temp_fahr)

# Ответ: функциональная и процедурная парадигмы.
# Почему это так: создана функция для конвертации единиц температуры и применена с помощью метода map, то есть она использована не только как процедура, но и как функция функциональной парадигмы, с помощью map.

# 2. Что за парадигма: стандартизация данных
from math import sqrt
from statistics import mean, variance

def standardize(data):
    avg = mean(data)
    var = variance(data)
    std = sqrt(var)
    def standardize_element(x):
        return (x - avg) / std
    return list(map(standardize_element, data))

data = [1, 2, 3, 4, 5]
print(standardize(data))
      
# Ответ: функциональная, процедурная и структурная парадигмы.
# Почему это так: с одной стороны мы используем функцию stanardize_element как отображение, но с другой - объявляем внешнюю функцию standardize как обычную процедуру внутри которой происходит последовательность шагов в рамках структурной парадигмы.

# 3. Что за парадигма: reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)

# Ответ: это функциональная парадигма.
# Почему это так: суммирование чисел происходит без явного объявления цикла и элементов на каждом шаге (это происходит под капотом метода reduce).
