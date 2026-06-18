def bubble_sort(arr):
    n = len(arr)
   
    sorted_arr = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break
    return sorted_arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([]))
print(bubble_sort([1]))