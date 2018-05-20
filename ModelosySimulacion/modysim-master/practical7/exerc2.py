from functions import chi2_stadistical, simulation_distribution, reject
from random import random
from scipy.special import chdtrc


def func():
    U = random()

    if U < 1/6:
        return(1)
    elif U <= 2/6:
        return(2)
    elif U <= 3/6:
        return(3)
    elif U <= 4/6:
        return(4)
    elif U <= 5/6:
        return(5)
    else:
        return(6)


if __name__ == '__main__':
    """
    Enunciado: Para verificar que cierto dado no estaba trucado, se registraron
    1000 lanzamientos, resultando que el número de veces que el dado arrojó el
    valor i (i = 1, 2, 3, 4, 5, 6) fue, respectivamente, 158, 172, 164, 181,
    160, 165. Aproximar el p-valor de la prueba: “el dado es honesto”
    a) utilizando un aproximación ji-cuadrada
    b) realizando una simulación
    """
    pi = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
    Ni = [158, 172, 164, 181, 160, 165]
    n, k = sum(Ni), len(pi)
    Iter = 1000
    T = chi2_stadistical(pi, Ni, n)
    chi2 = chdtrc(k - 1, T)
    sim = simulation_distribution(n, Iter, T, k, pi, func)

    print("Estadístico: {}".format(T))
    print("===============================")
    print("P-valor con Chi-cuadrado: {}".format(chi2))
    reject(chi2)
    print("===============================")
    print("P-valor con Simulación: {}".format(sim))
    reject(sim)
