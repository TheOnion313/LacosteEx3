import math
from math import sin, pi

import matplotlib.pyplot as plt
import numpy as np

analytical_solution = -1 / pi


def sinc(x):
    return sin(x) / x


def dsinc_classic(x, dx):
    return (sinc(x + dx) - sinc(x)) / dx


def dsinc_midpoint(x, dx):
    return (sinc(x + dx) - sinc(x - dx)) / (2 * dx)


def dsinc_stencil(x, dx):
    return (-sinc(x + 2 * dx) + 8 * sinc(x + dx) - 8 * sinc(x - dx) + sinc(x - 2 * dx)) / (12 * dx)


def sim():
    classic_archive = []
    midpoint_archive = []
    stencil_archive = []
    dx_archive = []
    x = pi
    for dx in np.logspace(math.log10(pi), math.log10(1e-16), 1000):
        classic_archive.append(abs(dsinc_classic(x, dx) - analytical_solution))
        midpoint_archive.append(abs(dsinc_midpoint(x, dx) - analytical_solution))
        stencil_archive.append(abs(dsinc_stencil(x, dx) - analytical_solution))
        dx_archive.append(dx)

    fig, plot = plt.subplots(1, 1)

    plt.plot(dx_archive, classic_archive, color="black")
    plt.plot(dx_archive, midpoint_archive, color="blue")
    plt.plot(dx_archive, stencil_archive, color="green")
    plt.plot(dx_archive, np.ones(len(dx_archive))*1e-16, linestyle="dashed", color="red")

    plt.legend(["classic derivative", "midpoint derivative", "Five-stencil drivative"])

    plot.invert_xaxis()
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("dx")
    plt.ylabel("error")

    plt.show()


if __name__ == '__main__':
    sim()
