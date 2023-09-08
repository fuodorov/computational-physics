"""
Documentation: https://en.wikipedia.org/wiki/Root-finding_algorithm
"""

import timeit
from typing import Callable

import numpy as np


class DifferentSignsError(Exception):
    message: str = "The function must have different signs at the bounds of the interval."

    def __init__(self, message: str = message):
        super().__init__(message)


def dihotomy(f: Callable[[float], float], a: float, b: float, eps: float) -> float:
    """
    Find the root of a function using the dihotomy method.

    Args:
        f (Callable[[float], float]): The function to find the root of.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        eps (float): The precision of the root.

    Returns:
        float: The root of the function.

    Raises:
        ValueError: The function must have different signs at the bounds of the interval.

    Doctests:
        >>> dihotomy(lambda x: x, -1.0, 1.0, 1e-10) < 1e-10
        True

    Documentation:
        https://en.wikipedia.org/wiki/Bisection_method

    """

    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the bounds of the interval.")

    while abs(b - a) > eps:
        c = (a + b) / 2.0

        if f(c) == 0.0:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2.0


def simple_iteration(f: Callable[[float], float], x0: float, delta: float, eps: float) -> float:
    """
    Find the root of a function using the simple iteration method.

    Args:
        f (Callable[[float], float]): The function to find the root of.
        x0 (float): The initial approximation.
        delta (float): The step of the method.
        eps (float): The precision of the root.

    Returns:
        float: The root of the function.

    Documentation:
        https://en.wikipedia.org/wiki/Fixed-point_iteration

    """

    x1 = x0 - delta * f(x0)

    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - delta * f(x0)

    return x1


def newton(f: Callable[[float], float], df: Callable[[float], float], x0: float, eps: float) -> float:
    """
    Find the root of a function using the Newton's method.

    Args:
        f (Callable[[float], float]): The function to find the root of.
        df (Callable[[float], float]): The derivative of the function.
        x0 (float): The initial approximation.
        eps (float): The precision of the root.

    Returns:
        float: The root of the function.

    Doctests:
        >>> newton(lambda x: x**2, lambda x: 2*x, 0.5, 1e-10) < 1e-10
        True

    Documentation:
        https://en.wikipedia.org/wiki/Newton%27s_method

    """

    x1 = x0 - f(x0) / df(x0)

    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - f(x0) / df(x0)
        print

    return x1


if __name__ == "__main__":
    print(
        "Find energy of 1/2*Psi(x)'' + U(x)*Psi(x) = E*Psi(x) for the potential U(x) = -U_0, x < a and U(x) = 0, x > a."
    )
    print("Solution - https://infopedia.su/10x31a7.html")
    print("Solve tan(x) = x for x in [pi/2, 3*pi/2]:")
    print(
        f"Dihotomy method: {dihotomy(lambda x: np.tan(x) - x, np.pi / 2.0 + 1e-10, 3 * np.pi / 2.0 - 1e-10, 1e-10):.10f}",  # noqa: E501
        f"Time: {timeit.timeit('dihotomy(lambda x: np.tan(x) - x, np.pi / 2.0 + 1e-10, 3 * np.pi / 2.0 - 1e-10, 1e-10)', number=10, globals=globals()):.10f}",  # noqa: E501
    )
    print(
        f"Newton's method: {newton(lambda x: np.tan(x) - x, lambda x: 1.0 / np.cos(x) ** 2 - 1.0, 4.5, 1e-10):.10f}",
        f"Time: {timeit.timeit('newton(lambda x: np.tan(x) - x, lambda x: 1.0 / np.cos(x) ** 2 - 1.0, 4.5, 1e-10)', number=10, globals=globals()):.10f}",  # noqa: E501
    )
    print(
        f"Simple iteration method: {simple_iteration(lambda x: np.tan(x) - x, 4.5, 1e-3, 1e-10):.10f}",
        f"Time: {timeit.timeit('simple_iteration(lambda x: np.tan(x) - x, 4.5, 1e-3, 1e-10)', number=10, globals=globals()):.10f}",  # noqa: E501
    )
