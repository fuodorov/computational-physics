"""Using the run-through method to solve the difference analog of the boundary value problem
y''(x) = sin(x), -pi/2 <= x <= pi/2
y(-pi/2) = a, y'(pi/2) = b

The exact solution is y(x) = -sin(x) - 1 + a + b * x + pi * b / 2

Difference analog:
y''(x) = (y_{i+1} - 2 * y_i + y_{i-1}) / h^2
y_0 = a, y_n = (beta_{n-1} + h * b) / (1 - alpha_{n-1}

Run-through method:
y_i = alpha_i * y_{i+1} + beta_i

substituting y_i into the difference analog, we get:
alpha_i = 1 / (2 - alpha_{i-1})
beta_i = (beta_{i-1} - h^2 * f_i) / (2 - alpha_{i-1})

where f_i = y''(x_i) = sin(x_i)

alpha_1 = 1 / 2
beta_1 = (a - h^2 * f_1) / 2
"""

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    a, b = 0, 1
    h = 0.001
    x = np.arange(-np.pi / 2, np.pi / 2 + h, h)
    n = len(x)
    alpha = np.zeros(n)
    beta = np.zeros(n)
    f = np.sin(x)

    alpha[1] = 1 / 2
    beta[1] = (a - h**2 * f[1]) / 2

    for i in range(2, n - 1):
        alpha[i] = 1 / (2 - alpha[i - 1])
        beta[i] = (beta[i - 1] - h**2 * f[i]) / (2 - alpha[i - 1])

    y = np.zeros(n)
    y[0], y[-1] = a, (beta[-2] + h * b) / (1 - alpha[-2])

    for i in range(n - 2, 0, -1):
        y[i] = alpha[i] * y[i + 1] + beta[i]

    y_exact = -np.sin(x) - 1 + a + b * x + np.pi * b / 2

    plt.plot(x, y, label="Numerical solution", alpha=0.7, linestyle="-.")
    plt.plot(x, y_exact, label="Exact solution", alpha=0.7, linestyle="--")
    plt.legend()
    plt.grid()
    plt.savefig("lesson_9/run2.png")
