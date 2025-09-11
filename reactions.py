import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def density(n, t, rate):
    return rate * n


if __name__ == "__main__":
    n0 = 5
    rate = np.log(1.5)
    t = np.linspace(0, 10, 10)
    sol = odeint(density, n0, t, args=(rate,))

    plt.figure(figsize=(8, 5), dpi=200)
    plt.title("Scipy odeint")
    plt.plot(t, sol, marker="s", label="density")
    plt.xlabel("Time")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.show()
