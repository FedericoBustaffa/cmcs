from typing import Callable, Sequence

import numpy as np


class Recurrence:
    def __init__(self, func: Callable, *params) -> None:
        self.func = func
        self.params = params

    def __call__(
        self, state: Sequence[float], steps: int
    ) -> tuple[np.ndarray, np.ndarray]:
        values = np.zeros(shape=(steps, len(state)))
        values[0] = np.asarray(state)
        timesteps = np.arange(steps)
        for t in timesteps[:-1]:
            values[t + 1] = self.func(values[t], *self.params)

        return timesteps, values.T
