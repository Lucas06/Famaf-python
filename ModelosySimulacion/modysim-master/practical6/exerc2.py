from math import exp as e, sqrt
from random import random


def experiment(d, Iter):
    const, sample, var, n = d ** 2, [e(random() ** 2)], 0, 1
    mean_old = sample[0]

    while var / n > const or n < Iter:
        sample.append(e(random() ** 2))
        mean_new = mean_old + (sample[n] - mean_old) / (n + 1)
        var = (1 - 1 / n) * var + (n + 1) * ((mean_new - mean_old) ** 2)
        mean_old = mean_new
        n += 1
    return(mean_new, var, n)


if __name__ == '__main__':
    """
    Enunciado: Estimar mediante el método de Monte Carlo la integral
    int_{0}^{1} e(x ** 2). Generar al menos 100 valores y detenerse cuando la
    desviación estándar del estimador sea menor que 0.01.
    """
    d, Iter = 0.01, 100
    mean, var, n = experiment(d, Iter)
    print("Media muestral es: {}".format(mean))
    print("Desviación estándar es: {}".format(sqrt(var)))
    print("Cantidad de iteraciones: {}".format(n))
