# Countif

# Предположим, нам необходимо реализовать программу, которая получает на вход список li и число n, а возвращает количество элементов в списке li равных этому заданному числу n

# 1. Структурная реализация

# input_li = input('Enter list li: ') # [1,2,3,4,5,6,7,7,6,5,5,4,1,2,3,4,5,6]
# input_n = input('Enter number n: ') # 6
input_li = [1,2,3,4,5,6,7,7,6,5,5,4,1,2,3,4,5,6]
input_n = 6
counter = 0
for el in input_li:
    if el == input_n:
        counter += 1
print(counter)

# 2. Процедурная реализация
# input_li = input('Enter list li: ') # [1,2,3,4,5,6,7,7,6,5,5,4,1,2,3,4,5,6]
# input_n = input('Enter number n: ') # 6
input_li = [1,2,3,4,5,6,7,7,6,5,5,4,1,2,3,4,5,6]
input_n = 6
def countif(li, n):
    counter = 0
    for el in li:
        if el == n:
            counter += 1
    return counter
print(countif(input_li, input_n))