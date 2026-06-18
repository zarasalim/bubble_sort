def selection_sort(arr):
    arr = list(arr)
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([5, 2, 9, 1]))
print(selection_sort([]))
print(selection_sort([42]))