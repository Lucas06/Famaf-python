from functions import interval
from random import random


def N():
    """
    Esta función calcula la mínima va uniforme que satisface
    sum_{i=1}^{n} U_{i} > 1.
    """
    i, U = 1, random()

    while U <= 1:
        U += random()
        i += 1
    return(i)


def experiment(Iter):
    sample, var = [N()], 0
    mean_old = sample[0]

    for n in range(1, Iter + 1):
        sample.append(N())
        mean_new = mean_old + (sample[n] - mean_old) / (n + 1)
        var = (1 - 1 / n) * var + (n + 1) * ((mean_new - mean_old) ** 2)
        mean_old = mean_new
    return(mean_new, var, n)


if __name__ == '__main__':
    """
    Enunciado: Para U1, U2, ... va uniformemente distribuídas en el intervalo
    (0,1), se define la funcion 'N'. Calcular la varianza del estimador N(mean)
    correspondiente a 1000 ejecuciones de la simulación y dar una estimación
    de e mediante un intervalo de confianza de 95%.
    """
    Iter = 1000
    mean, var, n = experiment(Iter)

    print("Varianza del estimador es: {}".format(var / n))
    print("Varianza muestral es: {}".format(var))

    print("\nEstimación de 'e': {}".format(mean))
    interval(mean, var, n)
