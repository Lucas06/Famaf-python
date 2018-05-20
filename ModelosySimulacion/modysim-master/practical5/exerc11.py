from random import random
from math import exp as e
from continuous_distributions import exponential


def poisson_naive(lamda):
    """
    Dado un valor de lamda, la función genera una va Poisson de manera no
    óptima.
    """
    i, U = 0, random()
    F = p = e(-lamda)

    while U >= F:
        i += 1
        p *= lamda / i
        F += p
    return(i)


def uniformD(a, b):
    return(int(random() * (b - a + 1)) + a)


def experiment(lamda):
    return(sum([uniformD(20, 40) for _ in range(poisson_naive(lamda))]))


if __name__ == '__main__':
    """
    Enunciado: Los autobuses que llevan los aficionados a un encuentro
    deportivo llegan a destino de acuerdo con un proceso de Poisson a razón de
    cinco por hora. La capacidad de los autobuses es una va que toma valores en
    el conjunto: {20, 21, ..., 40} con igual probabilidad. A su vez, las
    capacidades de dos autobuses distintos son va independientes. Escribir un
    algoritmo para simular la llegada de aficionados al encuentro en el
    instante t = 1 hora.
    """
    lamda = 5
    print("El valor generado es: S = {}".format(experiment(lamda)))
