import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def advance_particle(x, y, z, vx, vy, vz, dt, box_length, box_height, g=0):
    # given as it is

    deltav = np.array([0, 0, 0, 0, 0, 0])

    return newx, newy, newz, newvx, newvy, newvz, deltav


def advance_particles(arr, dt, box_length, box_height, g=0):
    nextarr = np.array(arr)
    deltavs = np.array([0, 0, 0, 0, 0, 0])

    # insert your code here

    return nextarr, deltavs


def run_particles(initparticles, dt, box_length, box_height, particle_mass, T, plot=False, g=0):
    #     given as it is
    """

    :param initparticles: the initial state
    :param dt: the time step
    :param box_length: box dimensions
    :param box_height: box dimensions
    :param particle_mass:
    :param T: the Total time of the simulation
    :param plot: if True plot the first 20 steps of all particles
    :param g: gravity
    :return: an 6xN np array with the momentum change of each wall at time t
    """

    Nstep = int(T // dt) + 1
    total_momentum = np.zeros((6, Nstep))
    new_particles = initparticles

    if (plot == True):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    if plot == True:
        plt.show()
    return total_momentum


def get_uniform_particles(Np, l, vrms):
    pass


if __name__ == '__main__':
    pass