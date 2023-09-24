# Сортировка пузырьком

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [64, 25, 12, 22, -2, 11, -34]
print(array)
sorted_array = bubble_sort(array)
print(sorted_array)