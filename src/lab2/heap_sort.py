import time
import random


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


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
            heapsort(arr_copy)
            elapsed = time.perf_counter() - start
            results.append(f"{elapsed:.5f}")

        print(f"{n:>8} | {results[0]:>12} | {results[1]:>12} | {results[2]:>14}")