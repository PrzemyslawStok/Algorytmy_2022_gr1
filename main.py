import numpy as np


def zajecia1():
    a = np.array([10, 10, 10], dtype=float)
    b = np.array([1.0, 1.0, 1.0], dtype=float)

    print(f"Przemysław Stokłosa: {a}")
    print(f"a :{a}, b: {b}")
    print("")

    print(f"{a}+{b}={a + b}")
    print(f"{a}-{b}={a - b}")
    print(f"{a}*{b}={a * b}")
    print(f"{a}/{b}={a / b}")

    A = 7 * np.ones([1000, 1000])
    print(A)
    print(np.shape(A))
    B = np.arange(1, 100)
    print(B)
    print(np.shape(B))


def instrukcjeWarunkowe(a: int):
    if a > 5:
        print(f"{a}>5")
    else:
        print(f"{a}<=5")


def funkcja1():
    for i in range(10):
        print(f"i={i}")


def wyswietlLinie(dodatkowe_spacje="", dlugosc=10):
    linia: str = ""
    for i in range(dlugosc):
        linia = dodatkowe_spacje + linia + "*  "
    print(linia)


def prostokat(szerokosc_prostokata=10, wysokosc_prostokata=10):
    for i in range(wysokosc_prostokata):
        wyswietlLinie(dlugosc=szerokosc_prostokata)


def trojkat_prostokatny(dlugosc_podstawy=10, wysokosc=5):
    for i in range(wysokosc):
        wyswietlLinie(dlugosc=i)


if __name__ == "__main__":
    # zajecia1()
    # instrukcjeWarunkowe(2)

    # funkcja1()

    # prostokat(5, 5)
    trojkat_prostokatny(10, 5)
