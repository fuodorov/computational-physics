"""
Documentation: https://en.wikipedia.org/wiki/Newton_polynomial
"""

import matplotlib.pyplot as plt
import numpy as np


def divided_diff(x: list, y: list) -> list:
    """
    Compute the divided differences table
    and return the coefficients of the interpolating polynomial.

    Args:
        x (list): The list of x values.
        y (list): The list of y values.

    Returns:
        list: The list of coefficients.

    Doctests:
        >>> divided_diff([0, 1, 2], [1, 2, 3])
        [1.0, 1.0, 0.0]

    Documentation:
        https://en.wikipedia.org/wiki/Divided_differences

    """

    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return list(coef[0])


def newton_poly(coef, x_data, x):
    """
    Compute the value of the Newton's polynomial at the point x.

    Args:
        coef (list): The list of coefficients.
        x_data (list): The list of x values.
        x (float): The point at which the value of the polynomial is computed.

    Returns:
        float: The value of the polynomial at the point x.

    Doctests:
        >>> newton_poly([1, 1, 0], [0, 1, 2], 0.5)
        1.5

    Documentation:
        https://en.wikipedia.org/wiki/Newton_polynomial

    """

    n = len(x_data) - 1
    p = coef[n]

    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p

    return p


if __name__ == "__main__":
    print("Find the coefficients of the Newton's polynom and plot it.")
    print("x_k = -5 + k * 10 / n, y_k = 1 / (1 + x_k^2), k = 0, 1, 2, 3, ..., n, n = 4, 5, ..., 15")
    print()

    plt.figure(figsize=(10, 10), dpi=200)
    plt.title("Newton's polynom")

    for n in range(4, 16, 1):
        x = [-5 + k * 10 / n for k in range(n + 1)]
        y = [1 / (1 + x_k**2) for x_k in x]
        coefficients = divided_diff(x, y)
        print(f"n = {n}, coef = {coefficients}")
        plt.subplot(4, 3, n - 3)
        plt.ylim(-0.5, 1.5)
        plt.grid()
        plt.scatter(x, y, label=f"n = {n}")
        plt.plot(np.linspace(-5, 5, 100), newton_poly(coefficients, x, np.linspace(-5, 5, 100)))

    plt.savefig("lesson_5/polynom.png")
