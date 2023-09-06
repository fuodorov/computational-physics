import matplotlib.pyplot as plt
import numpy as np

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
    h = 0.0001
    t0, tn = 0, 10
    n = int((tn - t0) / h)
    t = np.linspace(t0, tn, n + 1)
    u_e = np.zeros(n + 1)
    v_e = np.zeros(n + 1)
    u_e[0], v_e[0] = u0, v0
    u_i = np.zeros(n + 1)
    v_i = np.zeros(n + 1)
    u_i[0], v_i[0] = u0, v0

    for i in range(n):
        u_e[i + 1] = u_e[i] + h * f(u_e[i], v_e[i])[0]
        v_e[i + 1] = v_e[i] + h * f(u_e[i], v_e[i])[1]
        u_i[i + 1] = u_i[i] + h * (f(u_i[i], v_i[i])[0] + f(u_i[i + 1], v_i[i + 1])[0]) / 2
        v_i[i + 1] = v_i[i] + h * (f(u_i[i], v_i[i])[1] + f(u_i[i + 1], v_i[i + 1])[1]) / 2

    plt.subplot(2, 2, 1)
    plt.title("Explicit scheme")
    plt.plot(t, u_e, "b", label="u")
    plt.plot(t, v_e, "g", label="v")
    plt.xlim(-0.1, 5)
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.title("Implicit scheme")
    plt.plot(t, u_i, "b", label="u")
    plt.plot(t, v_i, "g", label="v")
    plt.xlim(-0.001, 0.05)
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(u_e, v_e, "b")
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(u_i, v_i, "b")
    plt.grid(True)

    plt.savefig("lesson_8/rigid.png")
