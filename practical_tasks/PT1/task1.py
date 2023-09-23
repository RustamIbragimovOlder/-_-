# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

# Использован алгоритм пузырьковой сортировки

numbers = [3, -5, 2, 1, 10, -8, 6, 77, -15]
print(f"Before list: {numbers}")

def sort_list_imperative(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers

print(f"After list: {sort_list_imperative(numbers)}")