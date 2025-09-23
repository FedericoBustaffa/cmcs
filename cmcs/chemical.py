class Reaction:
    def __init__(self, r, rc, p, pc, k) -> None:
        self.reactants = r
        self.react_coeffs = rc
        self.products = p
        self.prod_coeff = pc
        self.kinetic_constant = k

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


if __name__ == "__main__":
    infection = Reaction(["S", "I"], [1, 1], ["I"], [2], 3)
    print(infection)
