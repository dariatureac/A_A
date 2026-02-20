import sys
import time
import random

sys.setrecursionlimit(200000)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sizes = [100, 500, 1000, 2500, 5000, 10000]

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

            start = time.perf_counter()
            quicksort(arr, 0, len(arr) - 1)
            elapsed = time.perf_counter() - start
            results.append(f"{elapsed:.5f}")

        print(f"{n:>8} | {results[0]:>12} | {results[1]:>12} | {results[2]:>14}")