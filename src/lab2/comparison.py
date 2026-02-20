import sys
import time
import random

sys.setrecursionlimit(200000)

# ── QuickSort ─────────────────────────────────────────────────────────────────
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

# ── MergeSort ─────────────────────────────────────────────────────────────────
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))

# ── HeapSort ──────────────────────────────────────────────────────────────────
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
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# ── TimSort ───────────────────────────────────────────────────────────────────
RUN = 32

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_inplace(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]; i += 1
        else:
            arr[k] = right_part[j]; j += 1
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]; i += 1; k += 1
    while j < len(right_part):
        arr[k] = right_part[j]; j += 1; k += 1

def timsort(arr):
    n = len(arr)
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min(i + RUN - 1, n - 1))
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge_inplace(arr, left, mid, right)
        size *= 2

# ── Benchmark ─────────────────────────────────────────────────────────────────
def benchmark(sort_fn, arr):
    """Run sort_fn on a copy of arr, return elapsed seconds."""
    copy = arr[:]
    start = time.perf_counter()
    result = sort_fn(copy)
    # mergesort returns a new list, others sort in-place
    elapsed = time.perf_counter() - start
    return elapsed

def make_array(n, kind):
    if kind == "random":
        return [random.randint(0, 10 * n) for _ in range(n)]
    elif kind == "sorted":
        return list(range(n))
    else:  # reversed
        return list(range(n, 0, -1))

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sizes = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]
    kinds = ["random", "sorted", "reversed"]

    algorithms = {
        "QuickSort": lambda arr: quicksort(arr, 0, len(arr) - 1),
        "MergeSort": mergesort,
        "HeapSort":  heapsort,
        "TimSort":   timsort,
    }

    # QuickSort is too slow on sorted/reversed for large n
    QUICKSORT_LIMIT = 10000

    for kind in kinds:
        print(f"\n{'='*75}")
        print(f"  Input type: {kind.upper()}")
        print(f"{'='*75}")

        # Header
        header = f"{'Algorithm':<12}" + "".join(f"{n:>10}" for n in sizes)
        print(header)
        print("-" * len(header))

        for name, fn in algorithms.items():
            row = f"{name:<12}"
            for n in sizes:
                # Skip QuickSort on sorted/reversed for large n (too slow / stack overflow)
                if name == "QuickSort" and kind in ("sorted", "reversed") and n > QUICKSORT_LIMIT:
                    row += f"{'—':>10}"
                    continue
                arr = make_array(n, kind)
                t = benchmark(fn, arr)
                row += f"{t:>10.5f}"
            print(row)

    print("  SUMMARY: Average time at n=10,000 (seconds)")
    print(f"{'Algorithm':<12} {'Random':>12} {'Sorted':>12} {'Reversed':>12}")
    print("-" * 52)
    for name, fn in algorithms.items():
        row = f"{name:<12}"
        for kind in kinds:
            n = 10000
            if name == "QuickSort" and kind in ("sorted", "reversed"):
                row += f"{'—':>12}"
            else:
                arr = make_array(n, kind)
                t = benchmark(fn, arr)
                row += f"{t:>12.5f}"
        print(row)