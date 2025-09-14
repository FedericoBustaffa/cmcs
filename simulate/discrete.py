import matplotlib.pyplot as plt


class Simulator:
    def __init__(self, func, *params):
        self.update = func
        self.params = params

    def run(self, initial_values, steps):
        values = [initial_values]
        for _ in range(steps):
            values.append(self.update(initial_values, *self.params))
            initial_values = values[-1]

        return [list(i) for i in list(zip(*values))]


if __name__ == "__main__":

    def density(n0, alpha, beta, gamma):
        a0, c0 = n0
        a_new = (1 - alpha) * a0 + gamma * c0
        c_new = (1 - gamma) * c0 + beta * a0
        return a_new, c_new

    a0 = 50  # initial adults
    c0 = 50  # initial children
    alpha = 0.01  # adults death rate
    beta = 0.05  # children birth rate
    gamma = 0.18  # children to adults rate
    years = 50

    sim = Simulator(density, alpha, beta, gamma)
    adults, children = sim.run((a0, c0), years)
    times = [t for t in range(years + 1)]

    plt.figure(dpi=200)
    plt.title(
        f"Adults and Children Density\n $a_0 = {a0}, c_0 = {c0}, \\alpha = {alpha}, \\beta={beta}, \\gamma = {gamma}$"
    )
    plt.plot(times, adults, label="adults")
    plt.plot(times, children, label="children")
    plt.plot(times, [a + c for a, c in zip(adults, children)], label="total")
    plt.legend()
    plt.grid()
    plt.show()
