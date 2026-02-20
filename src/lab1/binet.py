import time
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Увеличим точность, чтобы корректно считать большие Fibonacci
getcontext().prec = 5000  # 5000 цифр — достаточно для n ≈ 15849

def fibonacci_binet(n):
    sqrt5 = Decimal(5).sqrt()
    phi = (Decimal(1) + sqrt5) / 2
    psi = (Decimal(1) - sqrt5) / 2
    F_n = (phi**n - psi**n) / sqrt5
    return int(F_n.to_integral_value(rounding='ROUND_HALF_EVEN'))

# Твои значения n
n_values = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981,
            5012, 6310, 7943, 10000, 12589, 15849]

times = []

for n in n_values:
    start = time.perf_counter()
    fibonacci_binet(n)
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
plt.plot(n_values, times, marker='o', color='orange', label='Binet Formula')
plt.xlabel("n (Fibonacci Term)")
plt.ylabel("Time (seconds)")
plt.title("Binet Formula Fibonacci Time Complexity")
plt.grid(True)
plt.legend()
plt.show()