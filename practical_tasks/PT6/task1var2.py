from random import randint

def binary_search(list, first_index, last_index, find):
    if last_index >= first_index:
       
        middle_index = (first_index + last_index) // 2
        middle_element = list[middle_index]
       
 
        if middle_element == find:
            return middle_index
 
        elif middle_element > find:
            new_position = middle_index - 1
            return binary_search(list, first_index, new_position, find)
 
        elif middle_element < find:
            new_position = middle_index + 1
            return binary_search(list, new_position, last_index, find)
 
    else:
        return -1
       
list_container = [ 1, 9, 11, 21, 34, 54, 67, 90 ]
 

array = [randint(1, 10) for i in range(7)]
print(array)
search1 = 3
search2 = 5
first = 0
last= len(array) - 1
print(binary_search(array, first, last, search1))
print(binary_search(array, first, last, search2))