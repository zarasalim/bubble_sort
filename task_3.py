import random
import time

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

sizes = [200, 500, 1000, 2000]
results = {size: {} for size in sizes}

for size in sizes:
    original = [random.randint(0, 10000) for _ in range(size)]
    for name, sort_func in [('bubble', bubble_sort), ('selection', selection_sort), ('insertion', insertion_sort)]:
        arr = original.copy()
        start = time.perf_counter()
        sort_func(arr)
        elapsed = time.perf_counter() - start
        results[size][name] = elapsed

for size in sizes:
    b, s, i = results[size]['bubble'], results[size]['selection'], results[size]['insertion']
    print(f"Размер: {size}")
    print(f"  Пузырьком: {b:.6f} с")
    print(f"  Выбором:   {s:.6f} с")
    print(f"  Вставками: {i:.6f} с\n")