#Implement few empirical analysis metrics (Time taken, number of operations involved, memory space) to compare all the sorting algorithms learnt in the data structures course.
import time
import random
data = [random.randint(1, 1000) for _ in range(1000)]
def clone():
    return data.copy()
def insertion_sort(arr):
    comparisons = 0
    start = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
    end = time.time()
    return round(end - start, 5), comparisons
def merge_sort(arr):
    comparisons = 0
    start = time.time()
    def merge_sort_recursive(arr):
        nonlocal comparisons
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort_recursive(L)
            merge_sort_recursive(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                comparisons += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    merge_sort_recursive(arr)
    end = time.time()
    return round(end - start, 5), comparisons
insertion_time, insertion_comparisons = insertion_sort(clone())
merge_time, merge_comparisons = merge_sort(clone())
print("\nEmpirical Comparison: Insertion vs Merge Sort")
print("Insertion Sort - Time:", insertion_time, "seconds,", "Comparisons:", insertion_comparisons)
print("Merge Sort     - Time:", merge_time, "seconds,", "Comparisons:", merge_comparisons)
