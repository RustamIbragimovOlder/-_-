# Императивное программирование
arr = [1,2,3,4,5,6,7,8,9,10]
summ = 0
for el in arr:
    summ += el
print(summ)

# Декларативное программирование
arr = [1,2,3,4,5,6,7,8,9,10]
print(sum(arr))

# Декларативное программирование с reduce
from functools import reduce
res = reduce(lambda x, y: x+y, arr)
print(res)

# Процедурное программирование (вычисление корней квадратного уравнения)
def calculate_x(a, b):
    return -b / (2*a)

def calculate_x1x2(a, b, D):
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    return x1, x2

def calculate_D(a, b, c):
    return b**2 - 4*a*c

def solve_for_x(a, b, c):
    D = calculate_D(a, b, c)
    if D > 0:
        return calculate_x1x2(a, b, D)
    elif D == 0:
        return calculate_x(a, b)
    else:
        return 'No real solutions'
    
if __name__ == "__main__":
    a, b, c = 6, -17, 12
    solution = solve_for_x(a, b, c)
    print(solution)