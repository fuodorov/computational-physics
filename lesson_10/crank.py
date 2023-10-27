import matplotlib.pyplot as plt
import numpy as np

L, T = 1, 1
n, k = 100, 100

h = L / n
tau = T / k

a, b, c, d, q = np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n)
p = np.zeros((n + 1, k + 1))


for i, j in np.ndindex(p.shape):
    if i == 0:
        p[i][j] = 0
    elif j == 0:
        p[i][j] = h * i * (1 - i * h / L) ** 2


for m in range(1, k):
    for i in range(1, n):
        a[i] = -1 * tau / (2 * h**2)
        b[i] = 1 + tau / h**2
        c[i] = -1 * tau / (2 * h**2)
        d[i] = p[i][m - 1] + tau / 2 * ((p[i + 1][m - 1] - 2 * p[i][m - 1] + p[i - 1][m - 1]) / h**2)

    a[1], c[n - 1] = 0, 0

    for i in range(2, n):
        dzeta = a[i] / b[i - 1]
        a[i] = 0
        b[i] -= dzeta * c[i - 1]
        d[i] -= dzeta * d[i - 1]

    p[n - 1][m] = d[n - 1] / b[n - 1]

    for i in range(n - 2, 0, -1):
        p[i][m] = (d[i] - c[i] * p[i + 1][m]) / b[i]


y, x = np.meshgrid(
    np.linspace(0, T, k + 1),
    np.linspace(0, L, n + 1),
)

fig = plt.figure()
ax = plt.axes(projection="3d")
surf = ax.plot_surface(x, y, p, cmap=plt.cm.cividis)
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.xlabel("x, [cm]")
plt.ylabel("t, [c]")
plt.savefig("lesson_10/crank.png")
