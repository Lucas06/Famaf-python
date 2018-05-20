from random import random
from continuous_distributions import exponential


def experiment():
    return(random() ** (1 / exponential(1)))


if __name__ == '__main__':
    """
    Enunciado: Desarrollar un método para generar la va con función de
    distribución: F(x) = int_{0}^{inf} x ** y e ** (-y) dy, con 0 <= x <= 1
    Pensar en el método de composición del ejercicio anterior. En particular,
    sea F la función de distribución de X y suponga que la distribución
    condicional de X dado Y = y es: P(X <= x | Y = y) = x ** y, con
    0 <= x <= 1.
    """
    print("El valor de la va es: X = {}".format(experiment()))
