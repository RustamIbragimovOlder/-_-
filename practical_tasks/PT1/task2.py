# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

# Вариант 1
numbers1 = [3, -5, 2, 1, 10, -8, 6, 77, -15]
print(f"Before list1: {numbers1}")

def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers

print(f"After list1: {sort_list_declarative(numbers1)}")

# Вариант 2
numbers2 = [3, -5, 2, 1, 10, -8, 6, 77, -15]
print(f"Before list2: {numbers2}")
print(f"After list2: {sorted(numbers2, reverse=True)}")