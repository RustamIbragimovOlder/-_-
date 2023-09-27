# Задача: На вход подается целочисленный массив. Необходимо получить список, элементы которого - это остаток от деления соответствующего элемента в исходном массиве на 5

# 1. Императивная реализация:

DIVISION_NUM = 5
arr = [i for i in range(100)]
res = []
for el in arr:
    res.append(el % DIVISION_NUM)
print(res)

# 1. Функциональная реализация:

DIVISION_NUM = 5
arr = [i for i in range(100)]
modulo = lambda x: x % DIVISION_NUM
print(list(map(modulo, arr)))