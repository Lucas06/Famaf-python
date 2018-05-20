from random import random
from math import exp as e
from continuous_distributions import exponential


def rejection():
    c, Y, U = 2/e(1), exponential(1/2), random()

    while U >= c * Y * e(- Y / 2):
        Y, U = exponential(1/2), random()
    return(Y)


if __name__ == '__main__':
    """
    Enunciado: Desarrollar un método para generar una va con densidad de
    probabilidad: f(x) = x e ** (-x), con x > 0.
    """
    print("El valor de la va es: X = {}".format(rejection()))
