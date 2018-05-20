from random import random
from discretes_distributions import uniform


def experiment(alpha):
    """
    Enunciado: Desarrollar un método para generar una variable aleatoria X cuya
    distribución de probabilidad está dada por: P(X = j). Aplicamos el método
    de composición, donde alpha y (1 - alpha) son 0.5.
    """
    U, j = random(), 1
    XI = uniform(0, 1)  # Será X1 si entro en el if, y X2 si entro en el else

    if U < alpha:
        F = (1 / 2)
        while XI >= F:
            j += 1
            F += F * (1 / 2)
    else:
        F = (1 / 2) * (2 / 3)
        while XI >= F:
            j += 1
            F += F * (2 / 3)
    return(j)


if __name__ == '__main__':
    alpha = 0.5  # Probabilidad de tomar la primer va
    print("El valor de X es: {}".format(experiment(alpha)))
