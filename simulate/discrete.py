from typing import Callable, Sequence

import numpy as np


def discrete(
    func: Callable,
    state: Sequence[float],
    params: Sequence[float],
    steps: int,
) -> tuple[np.ndarray, np.ndarray]:
    values = np.zeros(shape=(steps, len(state)))
    values[0] = np.asarray(state)
    timesteps = np.arange(steps)
    for t in timesteps[:-1]:
        values[t + 1] = func(values[t], params)

    return timesteps, values.T


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    def density(n0, params):
        a0, c0 = n0
        alpha, beta, gamma = params
        a_new = (1 - alpha) * a0 + gamma * c0
        c_new = (1 - gamma) * c0 + beta * a0
        return a_new, c_new

    a0 = 500  # initial adults
    c0 = 1000  # initial children
    alpha = 0.05  # adults death rate
    beta = 0.1  # children birth rate
    gamma = 1 / 18  # children to adults rate
    years = 50

    timesteps, (adults, children) = discrete(
        density, [a0, c0], [alpha, beta, gamma], years
    )
    total = adults + children

    print(f"adults final density: {adults[-1]:.2f}")
    print(f"children final density: {children[-1]:.2f}")
    print(f"total density: {total[-1]:.2f}")

    plt.figure(dpi=150)
    plt.title("Adults and Children Densities")
    plt.plot(timesteps, adults, marker="o", mfc="none", label="adults")
    plt.plot(timesteps, children, marker="o", mfc="none", label="children")
    plt.plot(timesteps, total, marker="o", mfc="none", label="total")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
