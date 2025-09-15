import matplotlib.pyplot as plt


def plot_simulation(times: list[int], results: list):
    plt.figure(figsize=(6, 4), dpi=200)
    for r in results:
        plt.plot(
            times,
            r,
            marker="o",
            mfc="none",
        )
    plt.grid()
    plt.tight_layout()
    plt.show()


def discrete_simulation(
    func, initial_values: list, parameters: list, timesteps: int, step: int = 1, start=0
):
    values = [initial_values]
    times = [t for t in range(start, timesteps + 1, step)]
    for _ in times[1:]:
        values.append(func(initial_values, parameters))
        initial_values = values[-1]

    results = [list(i) for i in list(zip(*values))]
    plot_simulation(times, results)

    return results


if __name__ == "__main__":

    def density(n0, params):
        a0, c0 = n0
        alpha, beta, gamma = params
        a_new = (1 - alpha) * a0 + gamma * c0
        c_new = (1 - gamma) * c0 + beta * a0
        return a_new, c_new

    a0 = 50  # initial adults
    c0 = 50  # initial children
    alpha = 0.01  # adults death rate
    beta = 0.01  # children birth rate
    gamma = 0.18  # children to adults rate
    years = 100

    adults, children = discrete_simulation(
        density, [a0, c0], [alpha, beta, gamma], years, 3
    )
