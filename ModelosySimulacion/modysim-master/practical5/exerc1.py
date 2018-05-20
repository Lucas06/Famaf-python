# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import random
from math import sqrt


def experiment():
    """
    Enunciado: Desarrollar un método para generar una variable aleatoria cuya
    densidad de probabilidad es:(x - 2) / 2, si 2 <= x <= 3 y (2 - x / 3) / 2,
    si 3 <= x <= 6. Desarrollamos con el MÉTODO DE LA INVERSA.
    """
    U = random()

    if U <= 3/4:
        return(6 - 6 * sqrt(U / 3))
    else:
        return(2 + 2 * sqrt(U))


if __name__ == '__main__':
    print("El valor de la va es: X = {}".format(experiment()))
