from math import log, sqrt
from random import random


"""
============================== FUNCIONES VIEJAS ===============================
"""


def uniform(a, b):
    """
    Genera una va Uniforme Discreta en el intervalo [a, b].
    """
    return(int(random() * (b - a + 1)) + a)


def exponential(lamda):
    """
    Genera una va Exponencial, a partir de su único parámentro lamda.
    """
    return(- log(random()) / lamda)


def normal(mu, sigma):
    """
    Esta función devuelve una va normal.
    """
    Y1, Y2 = exponential(1), exponential(1)

    while Y2 < (Y1 - 1) ** 2 / 2:
        Y1, Y2 = exponential(1), exponential(1)

    if random() < 0.5:
        return(Y1 * sigma + mu)
    else:
        return(-Y1 * sigma + mu)


"""
============================== FUNCIONES NUEVAS ===============================
"""


def empirical_discrete_function(value, sample):
    """
    Funcion empírica
    :param value: valor en el cual evaluar la función
    :param sample: muestra de valores
    """
    sample.sort()
    n = len(sample)

    if value < sample[0]:
        return(0)
    elif value > sample[n - 1]:
        return(1)
    else:
        for i in range(n - 1):
            if (value >= sample[i]) and (value < sample[i + 1]):
                return((i + 1) / n)


def empirical_continuous_function(value, sample):
    """
    Funcion empírica
    :param value: valor en el cual evaluar la función
    :param sample: muestra de valores
    """
    sample.sort()
    n = len(sample)

    if value < sample[0]:
        return(0)
    elif value > sample[n - 1]:
        return(1)
    else:
        for j in range(n - 1):
            if (value >= sample[j]) and (value < sample[j + 1]):
                return(G(sample[j]) + (G(sample[j+1]) - G(sample[j])) /
                       (sample[j] - sample[j+1]) * (value - j))


def sample_mean(sample):
    """
    Calcula la media muestral.
    """
    return(sum(sample) / len(sample))


def sample_var(sample):
    """
    Calcula la varianza muestral.
    """
    mean = sample_mean(sample)
    return(sum([(value - mean) ** 2 for value in sample]) / (len(sample) - 1))


def sample_mean_rec(sample, n, mean):
    """
    :param sample: lista de los valores
    :param mean: promedio de los valores hasta n - 1
    :param n: valor hasta el cual se calculó el promedio
    """
    return(mean + (sample[n] - mean) / (n + 1))


def sample_var_rec(sample):
    var, mean_new, mean_old = 0, 0, sample[0]

    for n in range(1, len(sample)):
        mean_new = mean_old + (sample[n] - mean_old) / (n + 1)
        var = (1 - 1 / n) * var + (n + 1) * ((mean_new - mean_old) ** 2)
        mean_old = mean_new
    return(var)


def general_form(d, Iter, F):
    """
    Calcula en forma general, con una aproximación a la función de probabilidad
    o de densidad F, la media y la varianza muestrales, y devuelve además la
    cantidad de iteraciones que se necesitaron para alcanzar esos valores.
    """
    const, sample, var, n = d ** 2, [F], 0, 1
    mean_old = sample[0]

    while var / n > const or n < Iter:
        sample.append(F)
        mean_new = mean_old + (sample[n] - mean_old) / (n + 1)
        var = (1 - 1 / n) * var + (n + 1) * ((mean_new - mean_old) ** 2)
        mean_old = mean_new
        n += 1
    return(mean_new, var, n)


def interval(avg, S, n):
    """
    A partir los valores de la media y la varianza (muestral o no), la cantidad
    de elementos y la constante Zalpha, la función devuelve un intervalo de
    confianza para la media X.
    """
    Zalphas = [(1.64, 90), (1.96, 95), (2.33, 99)]

    for value, confidence in Zalphas:
        print("Intervalo de confianza del {}% = ({}, {})".format(confidence,
              avg - value * S / sqrt(n), avg + value * S / sqrt(n)))


def bootstrap(sample, Iter):
    """
    :variable: mean: Estimación por boostrap de la media.
    :variable: var: Estimación por boostrap de la varianza.
    """
    empirical_mean = sample_mean(sample)
    empirical_var = sample_var(sample)
    n, mean, var = len(sample), 0, 0

    for _ in range(Iter):
        sum_xi, values = 0, []
        for _ in range(n):
            index = uniform(0, n - 1)
            sum_xi += sample[index]
            values.append(sample[index])
        mean_tmp = sum_xi / n

        var_tmp = 0
        for value in values:
            var_tmp += (value - mean_tmp) ** 2
        var_tmp /= (n - 1)

        mean += (mean_tmp - empirical_mean) ** 2
        var += (var_tmp - empirical_var) ** 2
    return(mean / Iter, var / Iter)
