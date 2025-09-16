def discrete_simulation(
    func,
    state: list,
    parameters: list,
    timesteps: int,
    step: int = 1,
    start=0,
):
    values = [state]
    times = [t for t in range(start, timesteps + 1, step)]
    for _ in times[1:]:
        values.append(func(state, parameters))
        state = values[-1]

    return [list(i) for i in list(zip(*values))]


if __name__ == "__main__":
    import matplotlib.pyplot as plt

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
    step = 3

    adults, children = discrete_simulation(
        density, [a0, c0], [alpha, beta, gamma], years, step
    )
    print(f"adults final density: {adults[-1]:.2f}")
    print(f"children final density: {children[-1]:.2f}")

    times = [t for t in range(0, years + 1, 3)]
    plt.figure(dpi=150)
    plt.title("Adults and Children Densities")
    plt.plot(times, adults, marker="o", mfc="none", label="adults")
    plt.plot(times, children, marker="o", mfc="none", label="children")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
