import numpy as np


def funkcja1():
    A = np.arange(1, 10)
    print(A)
    print(A[0])

    for i in range(5, 9):
        print(A[i])


if __name__ == "__main__":
    funkcja1()
