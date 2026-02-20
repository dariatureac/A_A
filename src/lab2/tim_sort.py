import time
import random

RUN = 32


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    left_part = arr[left : mid + 1]
    right_part = arr[mid + 1 : right + 1]

    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def timsort(arr):
    n = len(arr)

    # Sort individual runs with InsertionSort
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min(i + RUN - 1, n - 1))

    # Merge runs bottom-up
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sizes = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]

    print(f"{'n':>8} | {'Random (s)':>12} | {'Sorted (s)':>12} | {'Reversed (s)':>14}")
    print("-" * 55)

    for n in sizes:
        results = []
        for kind in ("random", "sorted", "reversed"):
            if kind == "random":
                arr = [random.randint(0, 10 * n) for _ in range(n)]
            elif kind == "sorted":
                arr = list(range(n))
            else:
                arr = list(range(n, 0, -1))

            arr_copy = arr[:]
            start = time.perf_counter()
            timsort(arr_copy)
            elapsed = time.perf_counter() - start
            results.append(f"{elapsed:.5f}")

        print(f"{n:>8} | {results[0]:>12} | {results[1]:>12} | {results[2]:>14}")