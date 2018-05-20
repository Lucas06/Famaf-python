from functions import chi2_stadistical, simulation_distribution, reject
from random import random
from scipy.special import chdtrc


def func():
    U = random()

    if U <= 1/2:
        return(2)
    elif U <= 3/4:
        return(1)
    else:
        return(3)


if __name__ == '__main__':
    """
    Enunciado: De acuerdo con la teoría genética de Mendel, cierta planta de
    guisantes debe producir flores blancas, rosas o rojas con probabilidad 1/4,
    1/2 y 1/4, respectivamente. Para verificar experimentalmente la teoría, se
    estudió una muestra de 564 guisantes, donde se encontró que 141 produjeron
    flores blancas, 291 flores rosas y 132 flores rojas. Aproximar el p-valor
    de esta muestra:
    a) utilizando un aproximación ji-cuadrada
    b) realizando una simulación
    """
    pi = [1/4, 1/2, 1/4]
    Ni = [141, 291, 132]
    n, k = sum(Ni), len(pi)
    Iter = 10000
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
