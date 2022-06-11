import tensorflow as tf

import numpy as np
from matplotlib import pyplot as plot


def data() -> (np.ndarray, np.ndarray):
    X = np.linspace(0, 2 * np.pi, 100)
    Y = np.sin(X)

    return X, Y


def noised_data(Y: np.ndarray, noise_lvl=1.0):
    for i in range(100):
        print(np.random.normal(0.0, noise_lvl))

    return Y


def srednia(x=0.0, n=100) -> float:
    srednia = 0

    for i in range(n):
        srednia += np.random.normal(x, 10.0)

    return srednia / n


if __name__ == "__main__":
    X, Y = data()
    plot.plot(X, Y)
    plot.show()

    Y = noised_data(Y)

    #print(f"srednia = {srednia(10.0, 1000_000)}")
