from typing import Callable

import numpy as np

from lesson_3.int import trapezoid_integrate  # pylint: disable=import-error


def finite_difference(f: Callable[[float], float], x: float, h: float) -> float:
    """Compute the finite difference of a function at a point.

    Args:
        f (Callable[[float], float]): The function to differentiate.
        x (float): The point at which to differentiate.
        h (float): The step size.

    Returns:
        float: The derivative of the function at the point.

    Raises:
        ValueError: The step size must be greater than zero.

    Doctests:
        >>> finite_difference(lambda x: 1, 1.0, 1e-3) == 0
        True
        >>> finite_difference(lambda x: x, 1.0, 1e-3) - 1.0 < 1e-10
        True

    Documentation:
        https://en.wikipedia.org/wiki/Finite_difference
    """

    if h <= 0.0:
        raise ValueError("The step size must be greater than zero.")

    return (f(x + h) - f(x)) / h


def bessel_j(n: int, x: float, h: float) -> float:
    """Compute the Bessel function of the first kind.

    Args:
        n (int): The order of the Bessel function.
        x (float): The point at which to evaluate the Bessel function.
        h (float): The step size.

    Returns:
        float: The Bessel function at the point.

    Raises:
        ValueError: The order of the Bessel function must be a non-negative integer.

    Doctests:
        >>> bessel_j(0, 1.0, 1e-3) - 0.7651976865579666 < 1e-10
        True

    Documentation:
        https://en.wikipedia.org/wiki/Bessel_function
    """

    if n < 0:
        raise ValueError("The order of the Bessel function must be a non-negative integer.")

    def f(theta: float) -> float:
        return np.cos(x * np.sin(theta) - n * theta)

    return 1.0 / np.pi * trapezoid_integrate(f, 0.0, np.pi, int(np.pi / h))


def bessel_j_prime(n: int, x: float, h: float) -> float:
    """Compute the derivative of the Bessel function of the first kind.

    Args:
        n (int): The order of the Bessel function.
        x (float): The point at which to evaluate the Bessel function.
        h (float): The step size.

    Returns:
        float: The derivative of the Bessel function at the point.

    Doctests:
        >>> bessel_j_prime(0, 1.0, 1e-3) - (-0.4400505857449335) < 1e-10
        True

    Documentation:
        https://en.wikipedia.org/wiki/Bessel_function
    """

    return finite_difference(lambda x: bessel_j(n, x, h), x, h)


if __name__ == "__main__":
    print("Demonstrate the fulfillment of equality J'0(x) + J1(x) = 0 with precision 1e-10 for x = [0, 2*np.pi]:")
    for h in [1e-7, 1e-8, 1e-9]:
        print(f"h = {h}")
        for x in np.linspace(0.0, 2 * np.pi, 10):
            print(
                f"bessel_j_prime(0, {x}, {h}) + bessel_j(1, {x}, {h}) = {bessel_j_prime(0, x, h) + bessel_j(1, x, h)}"
            )
        print()
