from functions import interval
from random import random


def M():
    """
    Esta función calcula la primer va uniforme que satisface Un > Un+1.
    """
    n, U_old, U_new = 2, random(), random()

    while U_old <= U_new:
        U_old = U_new
        U_new = random()
        n += 1
    return(n)


def experiment(Iter):
    sample, var = [M()], 0
    mean_old = sample[0]

    for n in range(1, Iter + 1):
        sample.append(M())
        mean_new = mean_old + (sample[n] - mean_old) / (n + 1)
        var = (1 - 1 / n) * var + (n + 1) * ((mean_new - mean_old) ** 2)
        mean_old = mean_new
    return(mean_new, var, n)


if __name__ == '__main__':
    """
    Enunciado: Utilizando la función 'M' para estimar e mediante 1000
    ejecuciones de una simulación. Calcular la varianza del estimador y dar una
    estimación de e mediante un intervalo de confianza de 95%.
    """
    Iter = 1000
    mean, var, n = experiment(Iter)

    print("Varianza del estimador es: {}".format(var / n))
    print("Varianza muestral es: {}".format(var))

    print("\nEstimación de 'e': {}".format(mean))
    interval(mean, var, n)
