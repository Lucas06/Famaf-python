from random import random
from math import exp as e
from discretes_distributions import F_poisson, poisson_naive


"""
Enunciado: Desarrollar dos métodos para generar una va X cuya distribución de
probabilidad está dada por: P(X = i) =
(lambda ** i / i! * e(-lambda)) / (sum_{j=0}^{k} lambda ** j / j! * e(-lambda))
"""


def ITexperiment(lamda, k):
    """
    El experimento es igual a la funcion Poisson, con la diferencia de que en
    este caso el p0 esta dividido por la constante den.
    """
    i, U, den = 0, random(), F_poisson(lamda, k)
    F = p = e(-lamda) / den

    while U >= F:
        i += 1
        p *= (lamda / i) / den
        F += p
    return(i)


def RAexperiment(lamda, k):
    """
    Rechazo usando una Poisson.
    """
    X = poisson_naive(lamda)

    while X > k:
        X = poisson_naive(lamda)
    return(X)


if __name__ == '__main__':
    # k, lamda = 100, 3
    k, lamda = 5, 10

    print("La va generada por el MÉTODO DE LA TRANFORMADA INVERSA es: X = {}".
          format(ITexperiment(lamda, k)))

    print("La va generada por el MÉTODO DE ACEPTACIÓN Y RECHAZO es: X = {}".
          format(RAexperiment(lamda, k)))
