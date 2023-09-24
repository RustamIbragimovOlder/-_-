# Структурная парадигма
# Четность числа (Процедуры в данной программе не объявляются, но при этом все держится на структурных управляющих конструцкиях: последовательностях и условиях (без циклов))

if __name__ == '__main__':
    num = int(input('Enter a number: \n'))
    if num % 2 == 0:
        print(True)
    else:
        print(False)

# Процедурная парадигма + Структурная парадигма
# print_numbers (Структурная, поскольку используется for и нет goto. Процедурная, поскольку код оформлен в виде процедуры.)

def print_numbers(numbers):
    for num in numbers:
        print(num)

# Процедурная парадигма + Структурная парадигма
# quicksort (Процедурная: есть процедура quicksort(arr), Структурная: goto тут нет, вся программа находится в рамках трех управляющих конструкций)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        base = arr[0]
        less = [x for x in arr[1:] if x <= base]
        greater = [x for x in arr[1:] if x > base]
        return quicksort(less) + [base] + quicksort(greater)
    
numbers = [8, 3, 1, 11, 5, 9, 2, 7, 4, 6, 0, 10]
print(numbers)
sorted_numbers = quicksort(numbers)
print(sorted_numbers)