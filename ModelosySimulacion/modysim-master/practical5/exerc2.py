from random import random
from math import log as ln


def experiment(alpha, beta):
    """
    Enunciado: Desarrollar un método para generar una va con distribución de
    probabilidad: F(x) = 1 - e(- alpha * (x ** beta)).
    Una variable aleatoria con esta distribución se conoce como va de Weibull.
    Calculamos beta va y nos quedamos con la mayor, utilizando la función
    inversa de F(x).
    """
    return((- ln(random()) / alpha) ** (1 / beta))


if __name__ == '__main__':
    alpha, beta = 5, 3
    print("El valor de la va es: X = {}".format(experiment(alpha, beta)))
