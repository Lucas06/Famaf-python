from collections import Counter
from math import log, sqrt, exp as e
from random import random
from scipy.special import ndtr


"""
testear:
- simulation_with_binomial
"""

def empirical_function(value, sample):
    """
    Funcion empírica. Se usa para Kolmogorov-Smirnov.
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


"""
============================== FUNCIONES VIEJAS ===============================
"""


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


def binomial(n, p):
    """
    El algoritmo calcula, dada la cantidad de valores n y la probabilidad p de
    cada uno, una va Binomial.
    """
    F = prob = (1 - p) ** n  # Caso base (p0)
    i, U = 0, random()
    c = p / (1 - p)  # Valor constante en todas las iteraciones

    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return(i)


def uniform(a, b):
    """
    Genera una va Uniforme Discreta en el intervalo [a, b].
    """
    return(int(random() * (b - a + 1)) + a)


def permutation(A):
    """
    Calcula una permutación aleatoria de un conjunto A, de cardinalidad N.
    Recordar que la cantidad de permutaciones de A es N!.
    """
    N = len(A)

    for i in range(N - 1, 0, -1):
        index = uniform(0, i)
        tmp = A[i]
        A[i], A[index] = A[index], tmp
    return(A)


"""
================================== DISCRETAS ==================================
"""


def chi2_stadistical(pi, Ni, n):
    """
    Esta función calcula el valor del estadístico para un TEST CHI-CUADRADO.
    Donde:
    - pi = P(X = i)
    - Ni = #{j | Y_j = i, 1 <= j <= n}
    - n = sum(Ni)
    """
    T = sum([(Ni[j] - (n * pi[j])) ** 2 / (n * pi[j]) for j in range(len(pi))])
    return(T)


def simulation_distribution(n, Iter, T, k, pi, func):
    """
    Simula una muestra de va generadas por func.
    """
    sucess = 0

    for _ in range(Iter):
        distribution = [func() for _ in range(n)]
        distribution.sort()

        Ni = [distribution.count(i + 1) for i in range(k)]

        if chi2_stadistical(pi, Ni, n) >= T:
            sucess += 1

    return(sucess / Iter)


def simulation_with_binomial(n, Iter, T, pi):
    # TODO: hacer bien
    sucess, Ni = 0, []

    Ni.append(n, )
    for _ in range(Iter):
        # Ni = [binomial(n - sum(Ni, pi[j] / 1 - sum(pi))) for j in range(n)]
        for j in range(n):
            Ni.append(binomial(n - sum(Ni), pi[j] / 1 - sum(pi[:j])))

        if chi2_stadistical(pi, Ni, n) >= T:
            sucess += 1

    return(sucess / Iter)


"""
================================== CONTINUAS ==================================
"""


def lamda_exponential_estimate(sample):
    """
    Estima el parámetro lamda de una va exponencial.
    """
    return(len(sample) / sum(sample))


def mu_sigma_normal_estimate(sample):
    """
    Estima los valores de mu y sigma de una va normal.
    """
    n = len(sample)
    mu = sum(sample) / n
    sum_xi = sum([(value - mu) ** 2 for value in sample])

    return(mu, sqrt(sum_xi / n))


def d_sample_uniform(sample):
    """
    Calcula el valor del estadístico d para va uniformes, que luego se
    utilizará como cota para la función p_value.
    """
    n, j, D_values = len(sample), 0, []

    for F in sample:
        D_values.append(((j + 1) / n) - F)
        D_values.append(F - (j / n))
        j += 1

    return(max(D_values))


def d_sample_exponential(sample, lamda):
    """
    Calcula el valor del estadístico d para va exponenciales, que luego se
    utilizará como cota para la función p_value.
    """
    n, j, D_values = len(sample), 0, []

    for x in sample:
        F = 1 - e(- lamda * x)
        D_values.append(((j + 1) / n) - F)
        D_values.append(F - (j / n))
        j += 1

    return(max(D_values))


def d_sample_normal(sample, mu, sigma):
    """
    Calcula el valor del estadístico d para va normales, que luego se utilizará
    como cota para la función p_value.
    """
    n, j, D_values = len(sample), 0, []

    for value in sample:
        F = ndtr((value - mu) / sigma)
        D_values.append(((j + 1) / n) - F)
        D_values.append(F - (j / n))
        j += 1

    return(max(D_values))


def p_value(n, Iter, d):
    """
    Calcula el p-valor bajo las hipótesis de saber los parámetros de la
    distribución que quiero aproximar y utilizando el teorema, es decir,
    simulando con uniformes.
    """
    sucess = 0

    for _ in range(Iter):
        F = [random() for _ in range(n)]
        F.sort()

        D_values = []
        for j in range(n):
            # j / n - F(Y(j))
            D_values.append((j + 1) / n - F[j])
            # F(Y(j)) - (j - 1) / n
            D_values.append(F[j] - j / n)

        if max(D_values) >= d:
            sucess += 1

    return(sucess / Iter)


def p_value_exponential(n, lamda, d, Iter):
    """
    Calcula el p_valor cuando la hipótesis me dice que las va son exponeciales
    y desconozco el valor de lamda. Si conozco el parámetro y quiero ser
    exacto, puedo utilizar esta función, obviando el calculo del lamda en cada
    iteración.
    """
    sucess = 0

    for _ in range(Iter):
        distributions = [exponential(lamda) for _ in range(n)]
        distributions.sort()
        new_lamda = lamda_exponential_estimate(distributions)

        if d_sample_exponential(distributions, new_lamda) >= d:
            sucess += 1

    return(sucess / Iter)


def p_value_normal(n, mu, sigma, d, Iter):
    """
    Calcula el p_valor cuando la hipótesis me dice que las va son exponeciales
    y desconozco el valor de lamda. Si conozco los parámetros y quiero ser
    exacto, puedo utilizar esta función, obviando el calculo de mu y sigma en
    cada iteración.
    """
    sucess = 0

    for _ in range(Iter):
        distributions = [normal(mu, sigma) for _ in range(n)]
        distributions.sort()
        new_mu, new_sigma = mu_sigma_normal_estimate(distributions)

        if d_sample_normal(distributions, new_mu, new_sigma) >= d:
            sucess += 1

    return(sucess / Iter)


"""
============================ DISCRETAS Y CONTINUAS ============================
"""


def reject(p_value):
    alphas = [0.1, 0.05, 0.01]  # Coreesponden con la confianza 90, 95, 99

    for alpha in alphas:
        print("\nCon alpha = {}".format(alpha))
        if p_value < alpha:
            print("Conclusión: Se rechaza H0")
        else:
            print("Conclusión: No se rechaza H0")


"""
================================ DOS MUESTRAS =================================
"""


def correct_order(sample_1, sample_2):
    """
    Dadas dos muestras, la función devuelve el arreglo menor y su longitud en
    las variables sample_1 y n y el mayor con su longitud en sample_2, m
    respectivamente.
    """

    if len(sample_1) > len(sample_2):
        tmp = sample_1
        sample_1 = sample_2
        sample_2 = tmp

    return(len(sample_1), len(sample_2), sample_1, sample_2)


def Range(sample_1, sample_2, sample=None):
    """
    Calcula el rango de una muestra aleatoria, para los casos en los que haya
    o no repeticiones.
    """
    R, repetitions_values = 0, []

    if sample is None:
        sample = sample_1 + sample_2
        sample.sort()

    _, _, sample_1, sample_2 = correct_order(sample_1, sample_2)
    repetitions = [(sample.index(value), counter, value) for value, counter in
                   Counter(sample).items() if counter > 1]

    if len(repetitions) > 0:
        for index, count, value in repetitions:
            repetitions_values.append(value)
            R += sum([j for j in range(index + 1, index + count + 1)]) / count

    R += sum([(i + 1) for i in range(len(sample)) if sample[i] in sample_1 and
             sample[i] not in repetitions_values])

    return(R)


def small_ranges(n, m, r):
    """
    Test de suma de rangos para n y m pequeños.
    """

    if n == 1 and m == 0:
        if r <= 0:
            return(0)
        else:
            return(1)
    elif n == 0 and m == 1:
        if r < 0:
            return(0)
        else:
            return(1)
    else:
        if n == 0:
            return(small_ranges(0, m - 1, r))
        elif m == 0:
            return(small_ranges(n - 1, 0, r - n))
        else:
            value_1 = n / (n + m) * small_ranges(n - 1, m, r - n - m)
            value_2 = m / (n + m) * small_ranges(n, m - 1, r)
            return(value_1 + value_2)


def p_value_small(sample_1, sample_2):
    """
    Esta función devuelve el p-valor para el caso de muestras con valores
    de n y m PEQUEÑOS. También llamado p-valor exacto.
    """
    n, m, sample_1, sample_2 = correct_order(sample_1, sample_2)
    R = Range(sample_1, sample_2)

    return(2 * min(1 - small_ranges(n, m, R - 1), small_ranges(n, m, R)))


def p_value_big(sample_1, sample_2):
    """
    Calcula el p-valor con una normal.
    """
    n, m, sample_1, sample_2 = correct_order(sample_1, sample_2)
    R = Range(sample_1, sample_2)
    R_mean, R_std_dev = n * (n + m + 1) / 2, sqrt(n * m * (n + m + 1) / 12)
    r_star = (R - R_mean) / R_std_dev

    if R <= R_mean:
        return(2 * ndtr(r_star))
    else:
        return(2 * (1 - ndtr(r_star)))


def p_value_simulation(sample_1, sample_2, Iter):
    sample = sample_1 + sample_2
    r, r_min, r_max = Range(sample_1, sample_2), 0, 0

    for _ in range(Iter):
        perm = permutation(sample)
        R = Range(sample_1, sample_2, perm)

        if R >= r:
            r_max += 1

        if R <= r:
            r_min += 1

    return(2 * min(r_max / Iter, r_min / Iter))
