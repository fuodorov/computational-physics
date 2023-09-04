from typing import Callable

import numpy as np


def eiler(f: Callable[[float, float], float], x0: float, y0: float, x: float, h: float) -> float:
    """
    Find the root of a function using the Eiler's method.

    Args:
        f (Callable[[float, float], float]): The function to find the root of.
        x0 (float): The initial approximation.
        y0 (float): The initial approximation.
        x (float): The precision of the root.
        h (float): The step of the method.

    Returns:
        float: The root of the function.

    Doctests:
        >>> eiler(lambda x, y: -y, 0, 1, 1, 1e-5) - np.exp(-1) < 1e-5
        True

    Documentation:
        https://en.wikipedia.org/wiki/Euler_method

    """

    while abs(x0 - x) > h:
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h

    return y0


def runge_kutta(f: Callable[[float, float], float], x0: float, y0: float, x: float, h: float, order: int) -> float:
    """
    Find the root of a function using the Runge-Kutta method.

    Args:
        f (Callable[[float, float], float]): The function to find the root of.
        x0 (float): The initial approximation.
        y0 (float): The initial approximation.
        x (float): The precision of the root.
        h (float): The step of the method.
        order (int): The order of the method.

    Returns:
        float: The root of the function.

    Doctests:
        >>> runge_kutta(lambda x, y: -y, 0, 1, 1, 1e-5, 2) - np.exp(-1) < 1e-5
        True
        >>> runge_kutta(lambda x, y: -y, 0, 1, 1, 1e-5, 4) - np.exp(-1) < 1e-5
        True

    Documentation:
        https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods

    """

    while abs(x0 - x) > h:
        if order == 2:
            k1 = h * f(x0, y0)
            k2 = h * f(x0 + h, y0 + k1)
            y0 = y0 + (k1 + k2) / 2.0
        elif order == 4:
            k1 = h * f(x0, y0)
            k2 = h * f(x0 + h / 2.0, y0 + k1 / 2.0)
            k3 = h * f(x0 + h / 2.0, y0 + k2 / 2.0)
            k4 = h * f(x0 + h, y0 + k3)
            y0 = y0 + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        else:
            raise ValueError("The order of the method must be 2 or 4.")
        x0 = x0 + h

    return y0


if __name__ == "__main__":
    print("Solve the Cauchy problem:")
    print("x' = -x, x(0) = 1, 0 < t < 3")
    print()

    for t in np.linspace(0, 3, 10):
        print(f"Eiler's method: x({t}) = {eiler(lambda t, x: -x, 0, 1, t, 1e-5)}")
        print(f"Runge-Kutta method 2: x({t}) = {runge_kutta(lambda t, x: -x, 0, 1, t, 1e-5, 2)}")
        print(f"Runge-Kutta method 4: x({t}) = {runge_kutta(lambda t, x: -x, 0, 1, t, 1e-5, 4)}")
        print(f"Exact solution: x({t}) = {np.exp(-t)}")
        print()
