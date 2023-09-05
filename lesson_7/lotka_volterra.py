
from lesson_6.cauchy import runge_kutta
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("Solve the Lotka-Volterra equations:")
    print("    dx/dt = a * x - b * x * y")
    print("    dy/dt = c * x * y - d * y")
    print("with: a = 10, b = 2, c = 2, d = 10")
    print("and plot the solution in the phase space.")

    a, b, c, d = 10, 2, 2, 10

    plt.figure(figsize=(10, 10), dpi=100)
    plt.grid()
    
    for x0, y0, color in [(1, 1, 'red'), (2, 2, 'blue'), (3, 3, 'green'), (4, 4, 'orange')]:
        for t in np.linspace(0, 50, 500):
            x = runge_kutta(
                f=lambda t, x: np.array([a * x[0] - b * x[0] * x[1], c * x[0] * x[1] - d * x[1]]), 
                x0=0, 
                y0=np.array([x0, y0]),
                x=t, 
                h=1e-2, 
                order=4
            )
            plt.scatter(x[0], x[1], color=color, s=1)
            print(f"t = {t}, x = {x[0]}, y = {x[1]}", end='\r')

        plt.scatter(x0, y0, color=color, s=10, marker='*', label=f'x0 = {x0}, y0 = {y0}')
    
    plt.legend()
    plt.xlabel('Preys')
    plt.ylabel('Predators')
    plt.title('Lotka-Volterra equations')
    plt.savefig('lesson_7/lotka_volterra.png')