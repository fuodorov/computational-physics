import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import newton_krylov

if __name__ == "__main__":
    print("Solve the rigid system of equations:")
    print("u' = 998u + 1998v")
    print("v' = -999u - 1999v")
    print("with excplicit scheme:")
    print("y_n+1 = y_n + h * f(x_n, y_n)")
    print("and implicit scheme:")
    print("y_n+1 = y_n + h * (f(x_n, y_n) + f(x_n+1, y_n+1)) / 2")

    def f(x, y):
        return np.array([998 * x + 1998 * y, -999 * x - 1999 * y])

    def u_exact(t):
        return 2 * np.exp(-t) - np.exp(-1000 * t)

    def v_exact(t):
        return -np.exp(-t) + np.exp(-1000 * t)

    plt.figure(figsize=(10, 5), dpi=200)

    for h in [0.0001, 0.00005]:
        u0, v0 = 1, 0
        t0, tn = 0, 0.1
        n = int((tn - t0) / h)
        t = np.linspace(t0, tn, n + 1)

        u_e = np.zeros(n + 1)
        v_e = np.zeros(n + 1)
        u_e[0], v_e[0] = u0, v0

        for i in range(n):
            u_e[i + 1] = u_e[i] + h * f(u_e[i], v_e[i])[0]
            v_e[i + 1] = v_e[i] + h * f(u_e[i], v_e[i])[1]
            print(f"Explicit: {i/(n-1)*100:.2f}%", end="\r")

        u_i = np.zeros(n + 1)
        v_i = np.zeros(n + 1)
        u_i[0], v_i[0] = u0, v0

        for i in range(n):
            y = newton_krylov(
                lambda y: y - np.array([u_i[i], v_i[i]]) - h * (f(u_i[i], v_i[i]) + f(y[0], y[1])) / 2,
                np.array([u_i[i], v_i[i]]),
            )
            u_i[i + 1] = u_i[i] + h * (f(u_i[i], v_i[i])[0] + f(y[0], y[1])[0]) / 2
            v_i[i + 1] = v_i[i] + h * (f(u_i[i], v_i[i])[1] + f(y[0], y[1])[1]) / 2
            print(f"Implicit: {i/(n-1)*100:.2f}%", end="\r")

        plt.subplot(1, 2, 1)
        plt.plot(t, u_exact(t) - u_e, label=f"delta u with {h=}", linestyle="dashed")
        plt.plot(t, v_exact(t) - v_e, label=f"delta v with {h=}", linestyle="dashed")
        plt.ylim(-0.02, 0.02)
        plt.xlim(0, 0.01)
        plt.title("Explicit scheme 1")
        plt.legend()
        plt.grid()

        plt.subplot(1, 2, 2)
        plt.plot(t, u_exact(t) - u_i, label=f"delta u with {h=}", linestyle="dotted")
        plt.plot(t, v_exact(t) - v_i, label=f"delta v with {h=}", linestyle="dotted")
        plt.ylim(-0.002, 0.002)
        plt.xlim(0, 0.01)
        plt.title("Implicit scheme 1")
        plt.legend()
        plt.grid()

    plt.savefig("lesson_8/rigid_1.png")
