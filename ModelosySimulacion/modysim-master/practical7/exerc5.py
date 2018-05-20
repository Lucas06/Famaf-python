from math import factorial as fac
from random import random
from scipy.special import chdtrc


def binomial_xi(x, n, p):
    return(fac(n) / (fac(n - x) * fac(x)) * p ** x * (1 - p) ** (n - x))


def p_binomial_estimate(sample, n):
    return(sum(sample) / len(sample) / n)


def chi2_stadistical(pi, Ni, n):
    T = sum([(Ni[j] - (n * pi[j])) ** 2 / (n * pi[j]) for j in range(len(pi))])
    return(T)


def ejer5analitico(sample, k, n):
    muestra = len(sample)
    p = p_binomial_estimate(sample, n)
    binomial1 = [binomial_xi(i, n, p) for i in range(k)]
    N = [sample.count(i) for i in range(k)]
    return(chi2_stadistical(binomial1, N, muestra))


def binomial_naive(p, n):
    i, U = 0, random()
    c = p / (1 - p)
    F = prob = (1 - p)**n

    while U >= F:
        prob *= (c * (n - i) / (i + 1))
        F += prob
        i += 1

    return(i)


def ejer5ext1(sample, r, k, n):
    t = ejer5analitico(sample, k, 8) # muestra, obtener el t original, parametro 8
    pMuestra = p_binomial_estimate(sample, 8) # obtener la estimacion de la muestra
    exitos = 0

    for _ in range(r):
        Y = [binomial_naive(pMuestra, 8) for _ in range(n)]
        N = [Y.count(i) for i in range(k)]
        p = p_binomial_estimate(Y, 8)
        binomial1 = [binomial_xi(i, 8, p) for i in range(k)]
        T = chi2_stadistical(binomial1, N, n)

        if T >= t:
            exitos += 1

    return exitos / float(r), t


def ejer5():
    sample = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    n = len(sample)
    simulado, t = ejer5ext1(sample, 1000, 9, n)
    print("simulado es {}".format(simulado))
    # 7 grados de libertad. k = 9 y m = 1
    print("chi-cuadrado {}".format(chdtrc(7, t)))


if __name__ == '__main__':
    ejer5()
