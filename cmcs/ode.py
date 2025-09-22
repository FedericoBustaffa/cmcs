from typing import Callable, Sequence

import numpy as np
from scipy.optimize import fsolve


def euler(
    f: Callable,
    y0: np.ndarray,
    args: Sequence,
    timesteps: np.ndarray,
    explicit: bool = False,
) -> np.ndarray:
    step = timesteps[1] - timesteps[0]
    values = np.zeros(shape=(len(timesteps), len(y0)))
    values[0] = np.asarray(y0)

    y = np.asarray(y0, dtype=float)
    for i, t in enumerate(timesteps[1:], start=1):
        if explicit:
            y = y + step * np.asarray(f(y, t, *args))
        else:
            y = fsolve(lambda y1: y1 - y - step * np.asarray(f(y1, t, *args)), y)

        values[i] = np.asarray(y)

    return values.T
