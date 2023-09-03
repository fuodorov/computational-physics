"""
Documenation: https://en.wikipedia.org/wiki/Numerical_integration
"""

from typing import Callable

import numpy as np


def trapezoid_integrate(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """Integrate a function using the trapezoid rule.

    Args:
        f (Callable[[float], float]): The function to integrate.
        a (float): The lower bound of the integral.
        b (float): The upper bound of the integral.
        n (int): The number of trapezoids to use.

    Returns:
        float: The integral of the function from a to b.

    Raises:
        ValueError: The number of trapezoids must be greater than zero.

    Doctests:
        >>> trapezoid_integrate(lambda x: 1.0, 0.0, 1.0, 100) - 1.0 < 1e-10
        True
        >>> trapezoid_integrate(lambda x: 1.0, 0.0, 1.0, 1000) - 1.0 < 1e-10
        True
        >>> trapezoid_integrate(lambda x: 1.0, 0.0, 1.0, 10000) - 1.0 < 1e-10
        True

    Documenation:
        https://en.wikipedia.org/wiki/Trapezoidal_rule

    """

    if n <= 0:
        raise ValueError("The number of trapezoids must be greater than zero.")

    h = (b - a) / n

    integral = 0.0

    for i in range(n):
        integral += (f(a + i * h) + f(a + (i + 1) * h)) * h / 2.0

    return integral


def simpson_integrate(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """Integrate a function using Simpson's rule.

    Args:
        f (Callable[[float], float]): The function to integrate.
        a (float): The lower bound of the integral.
        b (float): The upper bound of the integral.
        n (int): The number of trapezoids to use.

    Returns:
        float: The integral of the function from a to b.

    Raises:
        ValueError: The number of trapezoids must be greater than zero and even.

    Doctests:
        >>> simpson_integrate(lambda x: 1.0, 0.0, 1.0, 100) - 1.0 < 1e-10
        True
        >>> simpson_integrate(lambda x: 1.0, 0.0, 1.0, 1000) - 1.0 < 1e-10
        True
        >>> simpson_integrate(lambda x: 1.0, 0.0, 1.0, 10000) - 1.0 < 1e-10
        True

    Documenation:
        https://en.wikipedia.org/wiki/Simpson%27s_rule

    """

    if n <= 0 or n % 2 != 0:
        raise ValueError("The number of trapezoids must be greater than zero and even.")

    h = (b - a) / n

    integral = 0.0

    for i in range(n):
        integral += (f(a + i * h) + 4.0 * f(a + (i + 0.5) * h) + f(a + (i + 1) * h)) * h / 6.0

    return integral


if __name__ == "__main__":
    print("Integrating 1/(1+x**2) from -1 to 1:")
    for n in [4, 8, 16, 32, 64]:
        print(f"n = {n}")
        print(
            f"trapezoid_integrate(lambda x: 1/(1+x**2), -1.0, 1.0, {n}) = {trapezoid_integrate(lambda x: 1/(1+x**2), -1.0, 1.0, n):.5}"  # noqa: E501
        )
        print(f"Error: {np.abs(np.pi/2 - trapezoid_integrate(lambda x: 1/(1+x**2), -1.0, 1.0, n)):.5}")
        print(
            f"simpson_integrate(lambda x: 1/(1+x**2), -1.0, 1.0, {n}) = {simpson_integrate(lambda x: 1/(1+x**2), -1.0, 1.0, n):.5}"  # noqa: E501
        )
        print(f"Error: {np.abs(np.pi/2 - simpson_integrate(lambda x: 1/(1+x**2), -1.0, 1.0, n)):.5}")
        print()

    print("Integrating x**(1/3)*np.exp(np.sin(x)) from 0 to 1:")
    for n in [4, 8, 16, 32, 64]:
        print(f"n = {n}")
        print(
            f"trapezoid_integrate(lambda x: x**(1/3)*np.exp(np.sin(x)), 0.0, 1.0, {n}) = {trapezoid_integrate(lambda x: x**(1/3)*np.exp(np.sin(x)), 0.0, 1.0, n):.5}"  # noqa: E501
        )
        print(f"Error: {np.abs(1.29587 - trapezoid_integrate(lambda x: x**(1/3)*np.exp(np.sin(x)), 0.0, 1.0, n)):.5}")
        print(
            f"simpson_integrate(lambda x: x**(1/3)*np.exp(np.sin(x)), 0.0, 1.0, {n}) = {simpson_integrate(lambda x: x**(1/3)*np.exp(np.sin(x)), 0.0, 1.0, n):.5}"  # noqa: E501
        )
        print(f"Error: {np.abs(1.29587 - simpson_integrate(lambda x: x**(1/3)*np.exp(np.sin(x)), 0.0, 1.0, n)):.5}")
        print()
