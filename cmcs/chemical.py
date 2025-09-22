class Reaction:
    def __init__(self, r, p, k):
        self.r = r
        self.p = p
        self.k = k


def to_ode(r: Reaction):
    pass


if __name__ == "__main__":
    reactants = {"s": 1, "i": 1}
    products = {"i": 2}
    kinetic_constant = 3
    r = Reaction(reactants, products, kinetic_constant)
