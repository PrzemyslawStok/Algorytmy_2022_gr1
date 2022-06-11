import tensorflow as tf

import numpy as np
from matplotlib import pyplot as plot


def data() -> (np.ndarray, np.ndarray):
    X = np.linspace(0, 2 * np.pi, 100)
    Y = np.sin(X)

    return X, Y


def noised_data(Y: np.ndarray, noise_lvl=1.0):
    noise = np.random.normal(0.0, noise_lvl, np.shape(Y))

    return Y + noise


def srednia(x=0.0, n=100) -> float:
    srednia = 0

    for i in range(n):
        srednia += np.random.normal(x, 10.0)

    return srednia / n


def createModel() -> tf.keras.Model:
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=(1,)))
    model.add(tf.keras.layers.Dense(3))
    return model


if __name__ == "__main__":
    X, Y = data()
    noiseY = noised_data(Y, noise_lvl=0.5)

    plot.plot(X, Y)
    plot.scatter(X, noiseY)
    plot.scatter(X, noiseY)
    plot.show()

    model = createModel()
    model.summary()

    # print(f"srednia = {srednia(10.0, 1000_000)}")
