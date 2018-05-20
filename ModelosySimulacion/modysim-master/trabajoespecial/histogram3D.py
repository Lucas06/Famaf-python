"""Print 3D histogram

Usage:
  train.py [-t]
  train.py -h | --help

Options:
  -t            Train
  -h --help     Show this screen.
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pickle
from docopt import docopt
from experiment import experiment, simulation


def histogram3D():
    opts = docopt(__doc__)

    machines = 6
    Op = 6

    F = experiment
    N, Tf, Tr = 5, 1, 1/8

    if opts['-t']:
        matrix = np.zeros((machines - 1, Op - 1))
        for i in range(1, machines):
            for j in range(1, Op):
                print("Progres: {}".format(machines*(i-1) + (j-1)))
                _, matrix[i-1][j-1], _, _ = simulation(F, N, i, Tf, Tr, j)

        # Para guardar
        f = open("output", 'wb')
        pickle.dump(matrix, f)
        f.close()

    # Para leer
    f = open("output", 'rb')
    matrix = pickle.load(f)
    f.close()

    x = list(range(1, machines))
    y = list(range(1, Op))

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel('Machines')
    ax.set_ylabel('Operators')
    ax.set_zlabel('Mean lifetime')

    # Make data.
    X = x
    Y = y
    X, Y = np.meshgrid(X, Y)
    Z = matrix

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, antialiased=True)

    # Customize the z axis.
    ax.set_zlim(0, 500)
    ax.zaxis.set_major_locator(LinearLocator(6))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    plt.show()

if __name__ == '__main__':
    histogram3D()
