import numpy as np
import numpy.random as rnd
from scipy.special import binom


class Reaction:
    def __init__(self, r, rc, p, pc, k) -> None:
        self.reactants = r
        self.react_coeffs = rc
        self.products = p
        self.prod_coeff = pc
        self.kinetic_constant = k

    def species(self) -> set:
        return set(self.reactants.extend(self.products))

    def __repr__(self) -> str:
        formula = ""
        for i, r in enumerate(self.reactants):
            char = (
                f" ->{self.kinetic_constant} "
                if i == (len(self.reactants) - 1)
                else " + "
            )
            coeff = "" if self.react_coeffs[i] == 1 else str(self.react_coeffs[i])
            formula += coeff + r + char

        for i, p in enumerate(self.products):
            coeff = "" if self.prod_coeff[i] == 1 else str(self.prod_coeff[i])
            formula += coeff + p

        return formula


def gillespie(species, concentrations, reactions, stop=100) -> tuple:
    combinations = [binom(c, r.react_coeff) for c, r in zip(concentrations, reactions)]
    propensities = [c * r.kinetic_constant for c, r in zip(combinations, reactions)]
    exp_var = sum(propensities)

    values = np.zeros(shape=(stop, len(species)))
    timesteps = [0.0]
    values[0] = concentrations

    for i in range(1, stop):
        tau = rnd.exponential(exp_var)
        timesteps.append(tau)

    return timesteps, values


if __name__ == "__main__":
    infection = Reaction(["S", "I"], [1, 1], ["I"], [2], 3)
    recovery = Reaction(["I"], [1], ["R"], [1], 1)

    print(f"infection: {infection}")
    print(f"recovery: {recovery}")

    species = ["S", "I", "R"]
    concentrations = np.array([90, 10, 0])
    reactions = [infection, recovery]
    s, i, r = gillespie(species, concentrations, reactions)
