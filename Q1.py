import numpy as np
from matplotlib import pyplot as plt


def q1():
    dx = np.linspace(0, 20, 2000)
    Odx = 10 ** (-dx)

    plt.plot(dx, Odx)
    plt.xlabel("n")
    plt.ylabel("O(dx)")
    plt.show()


def q2():
    print(0.1 + 0.2 - 0.3)


if __name__ == '__main__':
    q2()
