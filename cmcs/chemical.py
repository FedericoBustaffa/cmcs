import numpy as np
from scipy.special import binom


class Reaction:
    def __init__(self, reactants, products, kinetic_constant) -> None:
        self.reactants = reactants
        self.products = products
        self.kinetic_constant = kinetic_constant


def gillespie(concentrations, reactions, stop=100):
    rng = np.random.default_rng()

    values = [concentrations.copy()]
    timesteps = [0.0]

    t = 0.0
    while t < stop:
        combinations = np.array(
            [np.prod(binom(concentrations, r.reactants)) for r in reactions]
        )

        propensities = np.array(
            [c * r.kinetic_constant for c, r in zip(combinations, reactions)]
        )

        propensity_sum = np.sum(propensities)
        if propensity_sum <= 0:
            break

        probabilities = propensities / propensity_sum
        step = rng.exponential(1.0 / propensity_sum)
        t += step
        timesteps.append(t)

        index = rng.choice(len(reactions), p=probabilities)
        r = reactions[index]
        concentrations += r.products - r.reactants
        values.append(concentrations.copy())

    return np.array(timesteps), np.array(values)
