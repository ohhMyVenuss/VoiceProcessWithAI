MOD = 10 ** 9 + 7


def matrix_mult(a, b):
    size = len(a)
    return [
        [
            sum(a[i][k] * b[k][j] for k in range(size)) % MOD
            for j in range(size)
        ]
        for i in range(size)
    ]


def matrix_pow(mat, power):
    size = len(mat)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, mat)
        mat = matrix_mult(mat, mat)
        power //= 2
    return result


def calculate_bacteria(a, b, n):
    if n == 0:
        return a % MOD
    if n == 1:
        return b % MOD
    mat = [
        [1, 2, 3, 0, 0],  # F(n) = 1*F(n-1) + 2*F(n-2) + 3*n^2
        [1, 0, 0, 0, 0],  # F(n-1) = F(n-1)
        [0, 0, 1, 2, 1],  # n^2 = (n-1)^2 + 2*(n-1) + 1
        [0, 0, 0, 1, 1],  # n = (n-1) + 1
        [0, 0, 0, 0, 1]  # 1 = 1
    ]
    mat_n = matrix_pow(mat, n - 1)

    initial = [b % MOD, a % MOD, 1, 1, 1]
    F_n = sum(mat_n[0][k] * initial[k] for k in range(5)) % MOD
    return F_n

a, b, n = map(int, input().split())
print(calculate_bacteria(a, b, n))