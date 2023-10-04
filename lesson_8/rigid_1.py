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

    u0, v0 = 1, 0
    h = 0.001
    t0, tn = 0, 5
    n = int((tn - t0) / h)
    t = np.linspace(t0, tn, n + 1)

    u_e = np.zeros(n + 1)
    v_e = np.zeros(n + 1)
    u_e[0], v_e[0] = u0, v0

    for i in range(n):
        u_e[i + 1] = u_e[i] + h * f(u_e[i], v_e[i])[0]
        v_e[i + 1] = v_e[i] + h * f(u_e[i], v_e[i])[1]
        print(f'Explicit: {i/(n-1)*100:.2f}%', end='\r')

    u_i = np.zeros(n + 1)
    v_i = np.zeros(n + 1)
    u_i[0], v_i[0] = u0, v0

    for i in range(n):
        # use newton method with one iteration
        # df = np.array([[998, 1998], [-999, -1999]])
        # y = np.array([u_i[i], v_i[i]])
        # y = y - np.linalg.solve(df, f(u_i[i], v_i[i]))
        # u_i[i + 1] = u_i[i] + h * (f(u_i[i], v_i[i])[0] + f(y[0], y[1])[0]) / 2
        # v_i[i + 1] = v_i[i] + h * (f(u_i[i], v_i[i])[1] + f(y[0], y[1])[1]) / 2

        # use newton method with scipy library

        y = newton_krylov(
            lambda y: y - np.array([u_i[i], v_i[i]]) - h * (f(u_i[i], v_i[i]) + f(y[0], y[1])) / 2,
            np.array([u_i[i], v_i[i]]),
        )
        u_i[i + 1] = u_i[i] + h * (f(u_i[i], v_i[i])[0] + f(y[0], y[1])[0]) / 2
        v_i[i + 1] = v_i[i] + h * (f(u_i[i], v_i[i])[1] + f(y[0], y[1])[1]) / 2
        print(f'Implicit: {i/(n-1)*100:.2f}%', end='\r')

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
    plt.savefig("lesson_8/rigid_1.png")
