from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def window_fourier(
    f: Callable[[float], float],
    h: Callable[[float], float],
    T: np.array,
) -> Callable[[float], float]:
    return lambda w: sum(f(t) * h(t, T) * np.exp(-1j * w * t) for t in T) / len(T)


if __name__ == "__main__":
    print("f(t) = a_0 * sin(w_0 * t) + a_1 * sin(w_1 * t) for t in [0, T]")
    print("a_0 = 1,  a_1 = 0.002,  w_0 = 5.1,  w_1 = 25.5,  T = 2 * pi")
    print("for rectangle window h(t) = 1")
    print("for hann window h(t) = 0.5 * (1 - cos(2 * pi * t))")

    def f(t: float) -> float:
        return np.sin(5.1 * t) + 0.002 * np.sin(25.5 * t) + np.random.uniform(-0.1, 0.1)

    def rectangle(t: float, T: np.array) -> float:  # pylint: disable=unused-argument
        return 1 if t in T else 0

    def hann(t: float, T: np.array) -> float:
        return 0.5 * (1 - 2 * np.cos(2 * np.pi * t / len(T)))

    a, b, n = -10, 10, 100
    T = np.linspace(a, b, n)
    w = np.linspace(0, 30, 1000)

    plt.plot(w, np.abs(window_fourier(f, rectangle, T)(w)), label="rectangle")
    plt.plot(w, np.abs(window_fourier(f, hann, T)(w)), label="hann")
    plt.legend()
    plt.savefig("lesson_12/fourier.png")
