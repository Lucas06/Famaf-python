from math import sqrt
from random import random


def point():
    """
    Genera un punto aleatorio en el cuadrado comprendido entre los puntos
    (-1, 1), (1,1), (1,-1), (-1,-1) y luego chequea si el punto cayó dentro del
    círculo unitario.
    """
    x, y = 2 * random() - 1, 2 * random() - 1
    return(int(x ** 2 + y ** 2 <= 1))


def interval(avg, Zalpha, S, n):
    return(avg - Zalpha * S / sqrt(n), avg + Zalpha * S / sqrt(n))


def experiment(d, const, Iter):
    d, sample, var, n = (d / const) ** 2, [point()], 0, 1
    mean_old = sample[0]

    while var / n > d or n < Iter:
        sample.append(point())
        mean_new = mean_old + (sample[n] - mean_old) / (n + 1)
        var = (1 - 1 / n) * var + (n + 1) * ((mean_new - mean_old) ** 2)
        mean_old = mean_new
        n += 1
    return(mean_new, var, n)


if __name__ == '__main__':
    """
    Enunciado: Utilizando la función 'point' obtener un intervalo de ancho
    menor que 0.1, el cual contenga a p con el 95% de confianza. ¿Cuántas
    ejecuciones son necesarias?
    """
    d, const, Iter = 0.1, (2 * 1.96), 100
    mean, var, n = experiment(d, const, Iter)
    print("Estimación de PI: {}".format(4 * mean))
    print("Cantidad de iteraciones: {}".format(n))
    const = 1.96
    a, b = interval(mean, const, var, n)
    print("Intervalo de confianza: ({}, {})".format(4 * a, 4 * b))
