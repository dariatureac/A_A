import time
import random


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


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

            start = time.perf_counter()
            mergesort(arr)
            elapsed = time.perf_counter() - start
            results.append(f"{elapsed:.5f}")

        print(f"{n:>8} | {results[0]:>12} | {results[1]:>12} | {results[2]:>14}")