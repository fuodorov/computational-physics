from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def window_fourier(
    f: Callable[[float], float], h: Callable[[float], float], a: float, b: float, n: int
) -> Callable[[float], float]:
    """
    Returns a function that is the windowed Fourier series of f with window h and n terms.

    Args:
        f (Callable[[float], float]): The function to approximate.
        h (Callable[[float], float]): The window function.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        n (int): The number of terms in the Fourier series.

    Returns:
        Callable[[float], float]: The windowed Fourier series of f with window h and n terms.

    """
    return lambda w: sum(f(t) * h(t) * np.exp(-1j * w * t) for t in np.linspace(a, b, n))


if __name__ == "__main__":
    print("f(t) = a_0 * sin(w_0 * t) + a_1 * sin(w_1 * t) for t in [0, T]")
    print("a_0 = 1,  a_1 = 0.002,  w_0 = 5.1,  w_1 = 25.5,  T = 2 * pi")
    print("for rectangle window h(t) = 1")
    print("for hann window h(t) = 0.5 * (1 - cos(2 * pi * t))")

    def f(t: float) -> float:
        return np.sin(5.1 * t) + 0.002 * np.sin(25.5 * t) + np.random.uniform(-5, 5)

    def rectangle(t: float) -> float:  # pylint: disable=unused-argument
        return 1

    def hann(t: float) -> float:
        return 0.5 * (1 - np.cos(2 * np.pi * t))

    a = 0
    b = 100 * np.pi
    n = 1000

    w = np.linspace(0, 30, 1000)

    plt.plot(w, np.abs(window_fourier(f, rectangle, a, b, n)(w)), label="rectangle")
    plt.plot(w, np.abs(window_fourier(f, hann, a, b, n)(w)), label="hann")
    plt.legend()
    plt.savefig("lesson_12/fourier.png")
