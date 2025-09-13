from functools import partial

import matplotlib.pyplot as plt

recurrences = []
initials = []
labels = []


def add_recurrence(func, n0, *args, label=None):
    recurrences.append(partial(func, *args))
    initials.append(n0)
    labels.append(label)


def run_simulation(times, title=None):
    values = []
    for r in recurrences:
        values.append([r(t) for t in times])

    plt.figure(dpi=200)
    if title is not None:
        plt.title(title)
    for v, l in zip(values, labels):
        plt.plot(times, v, label=l)

    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    def adults(n0, gamma, death_rate, t):
        if t == 0:
            return n0

        At = adults(n0, gamma, death_rate, t - 1)
        Ct = children(0)
        return (1 - death_rate) * At + gamma * Ct

    def children(n0, beta, gamma, t):
        if t == 0:
            return n0

    initial_values = [1, 2, 3]
    rates = [0.9, 1, 1.1]
    times = [i for i in range(10)]

    for n0 in initial_values:
        for r in rates:
            add_recurrence(density, n0, r, label=rf"$n_0 = {n0}, r = {r}$")
    run_simulation(times, "Linear Growth")
