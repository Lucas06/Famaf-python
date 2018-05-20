from math import exp as e
from discretes_distributions import uniform


def experiment(N, Iter):
    """
    Enunciado: Se desea construir una aproximación de: sum_{k=1}^{N} e(k / N)
    donde N = 10000.
    """
    theta = 0

    for i in range(Iter):
        theta += e(uniform(1, N) / N)
    return(theta / Iter * N)


def real_value(N):
    return(sum([e(k / N) for k in range(1, N + 1)]))


if __name__ == '__main__':
    Iter = 100  # Cantidad de iteraciones
    N = 10000  # Límite de la sumatoria

    real = real_value(N)  # Valor exacto
    estimate = experiment(N, Iter)  # Valor aproximado

    print("Valor real: {}".format(real))
    print("Aproximación con {} iteraciones: {}".format(Iter, estimate))
    print("Absoluto: {}".format(abs(real - estimate)))
