from random import random


def rejection(N):
    Y, U = random(), random()

    while U >= Y ** (N - 1):
        Y, U = random(), random()
    return(Y)


def inverseTransform(N):
    return(random() ** (1 / N))


def maxMethod(N):
    return(max([random() for _ in range(N + 1)]))


if __name__ == '__main__':
    """
    Enunciado: Utilizar el método del rechazo y los resultados del ejercicio
    anterior para desarrollar otros dos métodos, además del método de la
    transformada inversa, para generar una variable aleatoria con distribución
    de probabilidad: F(x) = X ** n para 0 <= x <= 1. Analizar la eficiencia de
    los tres métodos para generar la variable a partir de F.
    """
    print_text = "La va generada por el"
    N = 1000000
    print("{} MÉTODO DE RECHAZO es: X = {}".format(print_text, rejection(N)))
    print("{} MÉTODO DE TRANSFORMADA INVERSA es: X = {}".format(print_text,
          inverseTransform(N)))
    print("{} MÉTODO DEL MÁXIMO es: X = {}".format(print_text, maxMethod(N)))
