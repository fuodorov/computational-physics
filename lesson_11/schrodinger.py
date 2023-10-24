import matplotlib.pyplot as plt
import numpy as np


def U(x):
    return x**2 / 2


n = 4000
N = 60
x1 = -10
x2 = 10
m = 4
y0 = np.ones(n) + np.linspace(0, 1, n)
x = np.linspace(x1, x2, n, True)
h = x[1] - x[0]
a = [-1.0 / (2 * h**2) for i in range(0, n)]
b = [1.0 / h**2 + U(x[i]) for i in range(0, n)]
c = [-1.0 / (2 * h**2) for i in range(0, n)]


def tridiag_matrix_alg(a, b, c, d, n):
    y = []
    for i in range(0, n):
        y.append(0)

    for i in range(1, n):
        xi = a[i] / b[i - 1]
        a[i] = 0
        b[i] -= xi * c[i - 1]
        d[i] -= xi * d[i - 1]

    y[n - 1] = d[n - 1] / b[n - 1]

    for i in range(n - 2, -1, -1):
        y[i] = 1 / b[i] * (d[i] - c[i] * y[i + 1])

    return y


def inv_iter(y0, a, b, c, n, N, m):
    psi, E = [], []

    for j in range(0, m):
        d2 = y0.copy()
        for k in range(0, j):
            d2 = d2 - psi[k] * (np.inner(y0, psi[k])) / np.linalg.norm(psi[k])
        for i in range(0, N):
            d1 = d2
            d = d1.copy()
            a1 = a.copy()
            b1 = b.copy()
            c1 = c.copy()
            d2 = tridiag_matrix_alg(a1, b1, c1, d, n)
            for k in range(0, j):
                d2 = d2 - psi[k] * (np.inner(d2, psi[k])) / np.linalg.norm(psi[k])

        E.append(np.linalg.norm(d1) / np.linalg.norm(d2))
        psi.append(d2 / np.linalg.norm(d2))
    return [E, psi]


[E, psi] = inv_iter(y0, a, b, c, n, N, m)

for i in range(0, m):
    plt.plot(x, psi[i], label=f"$\psi_{i + 1}$, E = {E[i].round(3)}")

plt.legend()
plt.savefig("lesson_11/schrodinger.png")
