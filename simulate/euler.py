from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve


def explicit(
    derivative: Callable,
    y0: float,
    args: tuple,
    timesteps,
):
    step = timesteps[1] - timesteps[0]
    results = [y0]

    y = y0
    for _ in timesteps[:-1]:
        y = y + step * derivative(y, _, *args)
        results.append(y)

    return timesteps, np.asarray(results)


def implicit(
    derivative: Callable,
    y0: float,
    args: tuple,
    timesteps,
):
    step = timesteps[1] - timesteps[0]
    results = [y0]

    y = y0
    for _ in timesteps[:-1]:
        func = lambda y1: y1 - y - step * derivative(y1, _, *args)
        y = fsolve(func, y)[0]
        results.append(y)

    return timesteps, np.asarray(results)


if __name__ == "__main__":

    def logistic(n0, t, r, K):
        return K / (1 + (K / n0 - 1) * np.exp(-r * t))

    def derivative(n0, t, r, K):
        return r * n0 * (1 - n0 / K)

    N_0 = 5
    K = 50
    rate = np.log(1.1)
    times = np.linspace(0, 100, 50)
    step = 10

    plt.figure(figsize=(8, 5), dpi=200)
    plt.title(rf"Euler Method ($\tau = {step:.1f}$)")

    # exact solution
    exact_sol = [logistic(N_0, t, rate, K) for t in times]
    plt.plot(times, exact_sol, label="exact")

    # euler
    timesteps = np.arange(0, times.max() + step, step)
    i_times, i_values = explicit(derivative, N_0, (rate, K), timesteps)
    plt.plot(i_times, i_values, marker="o", mfc="none", label="explicit")

    i_times, i_values = implicit(derivative, N_0, (rate, K), timesteps)
    plt.plot(i_times, i_values, marker="o", mfc="none", label="implicit")

    # scipy odeint
    sol = odeint(derivative, N_0, timesteps, args=(rate, K))
    plt.plot(timesteps, sol, marker="s", mfc="none", label="scipy")

    plt.xlabel("Time")
    plt.ylabel("Density")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    # plt.savefig("/home/federico/obsidian/master/files/euler2.png")
    plt.show()
