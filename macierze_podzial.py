import numpy as np


def funkcja1():
    A = np.arange(1, 10)
    print(A)
    print(A[0])

    for i in range(5, 9):
        print(A[i])

    print(A[:7])
    print(A[2:])
    print(A[2:5])


def funckja2():
    A = np.arange(0, 10)
    B = A.reshape([2, 5])

    print(B)


if __name__ == "__main__":
    # funkcja1()
    funckja2()
