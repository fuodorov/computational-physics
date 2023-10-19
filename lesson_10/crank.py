import numpy as np
import matplotlib.pyplot as plt

L = 1
n = 100
delta = 1
T = 1000

h = L / n
tau = delta / T

a, b, c, d, q = np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n)
p, u, f = np.zeros((n + 1, T + 1)), np.zeros((n + 1, T + 1)), np.zeros((n, T))

for i in range(0, n + 1):
    p[i][0] = h * i * (1 - i * h / L) ** 2

for j in range(0, T + 1):
    p[0][j] = 0

for m in range(1, T):
    for i in range(1, n):
        a[i] = -1 * tau / (2 * h**2)
        b[i] = 1 + tau / h**2
        c[i] = -1 * tau / (2 * h**2)
        d[i] = p[i][m - 1] + tau / 2 * (
            (p[i + 1][m - 1] - 2 * p[i][m - 1] + p[i - 1][m - 1]) / h**2 + f[i][m - 1] + f[i][m]
        )

    a[1] = 0
    c[n - 1] = 0

    for i in range(2, n):
        dzeta = a[i] / b[i - 1]
        a[i] = 0
        b[i] -= dzeta * c[i - 1]
        d[i] -= dzeta * d[i - 1]

    p[n - 1][m] = d[n - 1] / b[n - 1]

    for i in range(n - 2, 0, -1):
        p[i][m] = (d[i] - c[i] * p[i + 1][m]) / b[i]

y, x = np.meshgrid(
    np.linspace(0, delta, T + 1),
    np.linspace(0, 1, n + 1),
)

fig = plt.figure()
ax = plt.axes(projection="3d")
surf = ax.plot_surface(x, y, p, cmap=plt.cm.cividis)
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.xlabel("x, [cm]")
plt.ylabel("t, [c]")
plt.show()
