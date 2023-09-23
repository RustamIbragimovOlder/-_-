# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

numbers = [3, -5, 2, 1, 10, -8, 6, 77, -15]
print(f"Before list: {numbers}")

# Вариант 1
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers

print(f"After list Var 1: {sort_list_declarative(numbers)}")

# Вариант 2
print(f"After list Var 2: {sorted(numbers, reverse=True)}")