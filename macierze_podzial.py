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


def funkcja2():
    A = np.arange(0, 100)
    B = A.reshape([10, -1])

    print(B)
    print("")

    print(B[:2, :])
    print(B[:, :2])

    # zad 35-78
    print(B[3:8, 5:9])


if __name__ == "__main__":
    # funkcja1()
    funkcja2()
