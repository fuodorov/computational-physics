"""
Documentation: https://en.wikipedia.org/wiki/Root-finding_algorithm
"""

from typing import Callable

import numpy as np


class DifferentSignsError(Exception):
    message: str = "The function must have different signs at the bounds of the interval."

    def __init__(self, message: str = message):
        super().__init__(message)


def dihotomy(f: Callable[[float], float], a: float, b: float, eps: float) -> (float, int):
    """
    Find the root of a function using the dihotomy method.

    Args:
        f (Callable[[float], float]): The function to find the root of.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        eps (float): The precision of the root.

    Returns:
        float: The root of the function.
        int: The number of iterations.

    Raises:
        ValueError: The function must have different signs at the bounds of the interval.

    Doctests:
        >>> dihotomy(lambda x: x, -1.0, 1.0, 1e-10)[0] < 1e-10
        True

    Documentation:
        https://en.wikipedia.org/wiki/Bisection_method

    """

    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the bounds of the interval.")

    n = 0

    while abs(b - a) > eps:
        c = (a + b) / 2.0

        if f(c) == 0.0:
            return c, n

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        n += 1

    return (a + b) / 2.0, n


def simple_iteration(f: Callable[[float], float], x0: float, delta: float, eps: float) -> (float, int):
    """
    Find the root of a function using the simple iteration method.

    Args:
        f (Callable[[float], float]): The function to find the root of.
        x0 (float): The initial approximation.
        delta (float): The step of the method.
        eps (float): The precision of the root.

    Returns:
        float: The root of the function.
        int: The number of iterations.

    Documentation:
        https://en.wikipedia.org/wiki/Fixed-point_iteration

    """

    x1 = x0 - delta * f(x0)

    n = 0
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - delta * f(x0)
        n += 1

    return x1, n


def newton(f: Callable[[float], float], df: Callable[[float], float], x0: float, eps: float) -> (float, int):
    """
    Find the root of a function using the Newton's method.

    Args:
        f (Callable[[float], float]): The function to find the root of.
        df (Callable[[float], float]): The derivative of the function.
        x0 (float): The initial approximation.
        eps (float): The precision of the root.

    Returns:
        float: The root of the function.
        int: The number of iterations.

    Doctests:
        >>> newton(lambda x: x**2, lambda x: 2*x, 0.5, 1e-10)[0] < 1e-10
        True

    Documentation:
        https://en.wikipedia.org/wiki/Newton%27s_method

    """

    x1 = x0 - f(x0) / df(x0)

    n = 0
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - f(x0) / df(x0)
        n += 1

    return x1, n


if __name__ == "__main__":
    print(
        "Find energy of 1/2*Psi(x)'' + U(x)*Psi(x) = E*Psi(x) for the potential U(x) = -U_0, x < a and U(x) = 0, x > a."
    )
    print("Solve ctg(sqrt(1 - x)) = sqrt(1/x - 1):")
    dihotomy_answer = dihotomy(
        lambda x: 1.0 / np.tan(np.sqrt(1.0 - x)) - np.sqrt(1.0 / x - 1.0),
        0.0 + 1e-5,
        1.0 - 1e-5,
        1e-5,
    )
    newton_answer = newton(
        lambda x: 1.0 / np.tan(np.sqrt(1.0 - x)) - np.sqrt(1.0 / x - 1.0),
        lambda x: 1.0 / (2.0 * np.tan(np.sqrt(1.0 - x)) ** 2 * np.sqrt(1.0 - x))
        + 1.0 / (2.0 * np.sqrt(x**3) * (1.0 - x)),
        0.5,
        1e-10,
    )
    simple_iteration_answer = simple_iteration(
        lambda x: 1.0 / np.tan(np.sqrt(1.0 - x)) - np.sqrt(1.0 / x - 1.0),
        0.7,
        1e-1,
        1e-5,
    )
    print(f"Dihotomy method: {dihotomy_answer[0]}", f"Number of iterations: {dihotomy_answer[1]}")
    print(f"Newton's method: {newton_answer[0]}", f"Number of iterations: {newton_answer[1]}")
    print(
        f"Simple iteration method: {simple_iteration_answer[0]}", f"Number of iterations: {simple_iteration_answer[1]}"
    )
