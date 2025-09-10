import matplotlib.pyplot as plt
import numpy as np


def c_birth(n0, rate, t):
    return n0 * np.exp(rate * t)


def euler(y0: float, rate: float, start: float, step: float, stop: float):
    timesteps = np.arange(start, stop + step, step)
    results = [y0]

    y = y0
    for t in timesteps[:-1]:
        y = y + step * rate * y
        results.append(y)

    return timesteps, np.asarray(results)


if __name__ == "__main__":
    N_0 = 5
    rate = np.log(1.5)
    times = np.linspace(0, 10, 50)

    plt.figure(figsize=(8, 5), dpi=200)
    plt.plot(times, [c_birth(N_0, rate, t) for t in times], label="Exact")
    for step in np.logspace(-1, 0, 2):
        e_times, e_values = euler(N_0, rate, 0, step, 10)
        plt.plot(e_times, e_values, label=rf"$\tau = {step:.2f}$")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
