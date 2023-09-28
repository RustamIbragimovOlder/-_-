# Корреляция

# Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# Ваша задача: Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно упростит вам жизнь.


# Var1
import numpy as np
x = np.array([-2, -1, 0, 1, 2]) 
y = np.array([4, 1, 3, 2, 0])
print(np.corrcoef(x, y))

# Var2
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
seed(1)
# data1 = 20 * randn(500) + 100
# data2 = data1 + (10 * randn(500) + 50)
data1 = [-2, -1, 0, 1, 2]
data2 = [4, 1, 3, 2, 0]
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
pyplot.scatter(data1, data2)
pyplot.show()

# Var3
import math
from functools import reduce
numbers1 = [-2, -1, 0, 1, 2]
numbers2 = [4, 1, 3, 2, 0]
M_numbers1 = reduce(lambda x, y: x + y, numbers1) / len(numbers1)
M_numbers2 = reduce(lambda x, y: x + y, numbers2) / len(numbers2)
sum = 0
sum_sqrt = 0
for i in numbers2: # numbres1
    sum = sum + (numbers1[i] - M_numbers1) * (numbers2[i] - M_numbers2)
    sum_sqrt = sum_sqrt + ((numbers1[i] - M_numbers1) ** 2) * ((numbers2[i] - M_numbers2) ** 2)

coef_pearson = sum / math.sqrt(sum_sqrt)
print(numbers1)
print(numbers2)
print(M_numbers1)
print(M_numbers2)
print(coef_pearson)

