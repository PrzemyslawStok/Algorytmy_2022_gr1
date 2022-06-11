import tensorflow as tf

import numpy as np
from matplotlib import pyplot as plot


def data() -> (np.ndarray, np.ndarray):
    X = np.linspace(0, 2 * np.pi, 100)
    Y = np.sin(X)

    return X, Y


if __name__ == "__main__":
    X, Y = data()
    plot.plot(X, Y)
    plot.show()
