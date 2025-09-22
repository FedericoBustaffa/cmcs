from typing import Callable

import numpy as np


class Recurrence:
    def __init__(self, func: Callable, *params) -> None:
        self.func = func
        self.params = params

    def run(self, state: np.ndarray, time: np.ndarray) -> np.ndarray:
        values = np.zeros(shape=(len(time), len(state)))
        values[0] = np.asarray(state)
        for i, _ in enumerate(time[:-1]):
            values[i + 1] = self.func(values[i], *self.params)

        return values.T
