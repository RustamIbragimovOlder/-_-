# Поиск числа в массиве

# Императив
def search_imperative(array, target):
    for num in array:
        if num == target:
            return True
    return False

array = [1,2,3,4,5,6,7,8]
target = 9
print(search_imperative(array, target))

# Декларатив
def search_declarative(array, target):
    return target in array
print(search_declarative(array, target))
