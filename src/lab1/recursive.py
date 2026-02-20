import time
import matplotlib.pyplot as plt

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Твои значения n
n_values = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
times = []

for n in n_values:
    start = time.perf_counter()
    fibonacci_recursive(n)
    end = time.perf_counter()
    times.append(end - start)

# ===== ВЫВОД В КОЛОНКАХ =====
cols = 4  # количество колонок

print("\n n   | Time (sec)")
print("-" * 70)

for i in range(0, len(n_values), cols):
    for j in range(cols):
        if i + j < len(n_values):
            n = n_values[i + j]
            t = times[i + j]
            print(f"{n:>3}: {t:>8.6f}", end="   ")
    print()  # новая строка

# ===== ГРАФИК =====
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, marker='o', color='red', label='Recursive')
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Recursive Fibonacci Time Complexity")
plt.grid(True)
plt.legend()
plt.show()
