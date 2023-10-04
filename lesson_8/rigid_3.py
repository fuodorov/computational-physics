import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import newton_krylov

if __name__ == "__main__":
    print("Solve the rigid system of equations:")
    print("u' = 998u + 1998v")
    print("v' = -999u - 1999v")
    print("with excplicit scheme:")
    print(
        "y_n+4 = y_n+3 + h/24 * (55 * f(x_n+3, y_n+3) - 59 * f(x_n+2, y_n+2) + 37 * f(x_n+1, y_n+1) - 9 * f(x_n, y_n))"
    )
    print("and implicit scheme:")
    print("y_n+3 = y_n+2 + h/24 * (9 * f(x_n+3, y_n+3) + 19 * f(x_n+2, y_n+2) - 5 * f(x_n+1, y_n+1) + f(x_n, y_n))")

    def f(x, y):
        return np.array([998 * x + 1998 * y, -999 * x - 1999 * y])

    u0, v0 = 1, 0
    h = 0.0001
    t0, tn = 0, 5
    n = int((tn - t0) / h)
    t = np.linspace(t0, tn, n + 1)

    u_e = np.zeros(n + 1)
    v_e = np.zeros(n + 1)
    u_e[0], v_e[0] = u0, v0
    u_e[1], v_e[1] = u0, v0
    u_e[2], v_e[2] = u0, v0

    for i in range(n - 3):
        u_e[i + 3] = u_e[i + 2] + h / 12 * (
            23 * f(u_e[i + 2], v_e[i + 2])[0] - 16 * f(u_e[i + 1], v_e[i + 1])[0] + 5 * f(u_e[i], v_e[i])[0]
        )
        v_e[i + 3] = v_e[i + 2] + h / 12 * (
            23 * f(u_e[i + 2], v_e[i + 2])[1] - 16 * f(u_e[i + 1], v_e[i + 1])[1] + 5 * f(u_e[i], v_e[i])[1]
        )

    u_i = np.zeros(n + 1)
    v_i = np.zeros(n + 1)
    u_i[0], v_i[0] = u0, v0
    u_i[1], v_i[1] = u0, v0

    for i in range(n - 2):
        y = newton_krylov(
            lambda y: y
            - np.array([u_i[i + 1], v_i[i + 1]])
            - h / 12 * (5 * f(y[0], y[1]) + 8 * f(u_i[i + 1], v_i[i + 1]) - f(u_i[i], v_i[i])),
            np.array([u_i[i], v_i[i]]),
        )
        u_i[i + 2] = u_i[i + 1] + h / 12 * (
            5 * f(y[0], y[1])[0] + 8 * f(u_i[i + 1], v_i[i + 1])[0] - f(u_i[i], v_i[i])[0]
        )
        v_i[i + 2] = v_i[i + 1] + h / 12 * (
            5 * f(y[0], y[1])[1] + 8 * f(u_i[i + 1], v_i[i + 1])[1] - f(u_i[i], v_i[i])[1]
        )

    plt.figure(figsize=(10, 5), dpi=200)
    plt.plot(t, u_e, label="u explicit", linestyle="dashed")
    plt.plot(t, v_e, label="v explicit", linestyle="dashed")
    plt.plot(t, u_i, label="u implicit", linestyle="dotted")
    plt.plot(t, v_i, label="v implicit", linestyle="dotted")
    plt.xlabel("t")
    plt.ylabel("u, v")
    plt.x_lim = (t0, tn)
    plt.legend()
    plt.grid()
    plt.savefig("lesson_8/rigid_3.png")
