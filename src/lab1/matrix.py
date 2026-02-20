import time
import matplotlib.pyplot as plt

# Умножение матриц 2x2
def mat_mult(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

# Умножение матрицы на вектор
def mat_vec_mult(M, V):
    return [
        [M[0][0]*V[0][0] + M[0][1]*V[1][0]],
        [M[1][0]*V[0][0] + M[1][1]*V[1][0]]
    ]

# Быстрое возведение матрицы в степень
def power(Matrix, n):
    result = [[1, 0],
              [0, 1]]   # Identity matrix
    base = Matrix

    while n > 0:
        if n % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        n //= 2
    return result

# Fibonacci по твоему псевдокоду
def  fibonacci_matrix(n):
    Matrix = [[0, 1],
              [1, 1]]
    Vec = [[0],
           [1]]

    M = power(Matrix, n)
    Result = mat_vec_mult(M, Vec)
    return Result[0][0]


# Твои значения n
n_values = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981,
            5012, 6310, 7943, 10000, 12589, 15849]

times = []

for n in n_values:
    start = time.perf_counter()
    fibonacci_matrix(n)
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
plt.plot(n_values, times, marker='o', color='green', label='Matrix Power')
plt.xlabel("n (Fibonacci Term)")
plt.ylabel("Time (seconds)")
plt.title("Matrix Exponentiation Fibonacci Time Complexity")
plt.grid(True)
plt.legend()
plt.show()
