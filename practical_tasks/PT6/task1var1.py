from random import randint

def binary_search(list , find):
    first_index = 0
    size = len(list)
    last_index = size - 1
    middle_index = (first_index + last_index) // 2
    middle_element = list[middle_index]
    is_found = True
    while is_found:
        if first_index == last_index:
            if middle_element != find:
                is_found = False
                return -1
        elif middle_element == find:
            return middle_index
        elif middle_element > find:
            new_position = middle_index - 1
            last_index = new_position
            middle_index = (first_index + last_index) // 2
            middle_element = list[middle_index]
            if middle_element == find:
                return middle_index
        elif middle_element < find:
            new_position = middle_index + 1
            first_index = new_position
            last_index = size - 1
            middle_index = (first_index + last_index) // 2
            middle_element = list[middle_index]
            if middle_element == find:
                return middle_index

array = [randint(1, 10) for i in range(7)]
print(array)
print(binary_search(array, 3))
print(binary_search(array, 5))