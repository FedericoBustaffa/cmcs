import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def c_birth(n0, rate, t):
    return n0 * np.exp(rate * t)


def density(n, t, rate):
    return rate * n


def euler(y0: float, rate: float, start: float, step: float, stop: float):
    timesteps = np.arange(start, stop + step, step)
    results = [y0]

    y = y0
    for _ in timesteps[:-1]:
        y = y + step * rate * y
        results.append(y)

    return timesteps, np.asarray(results)


if __name__ == "__main__":
    N_0 = 5
    rate = np.log(1.5)
    times = np.linspace(0, 10, 50)

    plt.figure(figsize=(8, 5), dpi=200)
    plt.title("Euler Method")

    # exact solution
    plt.plot(times, [c_birth(N_0, rate, t) for t in times], label="exact")

    # euler
    for step in [0.2, 1.0]:
        e_times, e_values = euler(N_0, rate, 0, step, 10)
        plt.plot(e_times, e_values, marker="s", label=rf"$\tau = {step:.2f}$")

    # scipy odeint
    times = np.linspace(0, 10, 10)
    sol = odeint(density, N_0, times, args=(rate,))
    plt.plot(times, sol, marker="s", label="scipy")

    plt.xlabel("Time")
    plt.ylabel("Density")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    # plt.savefig("/home/federico/obsidian/master/files/euler.png")
    plt.show()
