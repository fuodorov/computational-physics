import matplotlib.pyplot as plt
import numpy as np

L, n = 15, 1000
h = L / n
k = 10

A = np.zeros((n + 1, n + 1))
psi = np.zeros((k + 1, n + 1))
energy = np.zeros(k + 1)
x = np.linspace(-L / 2, L / 2, n + 1)
exact_solution = np.exp(-0.5 * x**2)

for i in range(n + 1):
    psi[0][i] = i**2


def potential(x):
    return 0.5 * x**2


for i, j in np.ndindex(A.shape):
    if i == j:
        A[i][j] = 1 / h**2 + potential(x[i])
    elif i == j - 1:
        A[i][j] = -1 / (2 * h**2)
    elif i == j + 1:
        A[i][j] = -1 / (2 * h**2)

A[0][0] = 1 / h**2 + potential(x[0])
A[0][1] = -1 / (2 * h**2)
A[n][n - 1] = -1 / (2 * h**2)
A[n][n] = 1 / h**2 + potential(x[n])

A_inv = np.linalg.inv(A)


for i in range(1, k + 1):
    psi[i] = A_inv.dot(psi[i - 1])
    energy[i] = np.linalg.norm(psi[i - 1]) / np.linalg.norm(psi[i])


plt.plot(
    x,
    psi[-1] / np.linalg.norm(psi[-1]),
    linestyle="--",
    color="r",
    alpha=0.5,
    label=f"$\psi_{0}$, $E_{0}$ = {energy[-1]:.1f}",
)
plt.plot(
    x, exact_solution / np.linalg.norm(exact_solution), linestyle="-", color="b", alpha=0.5, label="Exact solution"
)
plt.legend()
plt.grid()

plt.savefig("lesson_11/schrodinger.png")
