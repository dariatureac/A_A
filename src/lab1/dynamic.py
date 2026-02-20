import time
import matplotlib.pyplot as plt

# Dynamic Programming with array
def fibonacci_dp_array(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


# Твои значения n
n_values = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981,
            5012, 6310, 7943, 10000, 12589, 15849]

times = []

for n in n_values:
    start = time.perf_counter()
    fibonacci_dp_array(n)
    end = time.perf_counter()
    times.append(end - start)

# ===== ВЫВОД В КОЛОНКАХ =====
cols = 4

print("\n n      | Time (sec)")
print("-" * 90)

for i in range(0, len(n_values), cols):
    for j in range(cols):
        if i + j < len(n_values):
            n = n_values[i + j]
            t = times[i + j]
            print(f"{n:>6}: {t:>10.6f}", end="   ")
    print()

# ===== ГРАФИК =====
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, marker='o', color='blue', label='DP Array')
plt.xlabel("n (Fibonacci Term)")
plt.ylabel("Time (seconds)")
plt.title("Dynamic Programming (Array) Fibonacci Time Complexity")
plt.grid(True)
plt.legend()
plt.show()