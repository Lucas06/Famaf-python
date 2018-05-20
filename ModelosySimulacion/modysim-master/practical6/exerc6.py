from functions import sample_mean, uniform


def experiment(sample, Iter, A, B):
    success, n, empirical_mean = 0, len(sample), sample_mean(sample)

    for _ in range(Iter):
        mean = sum([sample[uniform(0, n - 1)] for _ in range(n)]) / n
        value = mean - empirical_mean

        if A < value < B:
            success += 1

    return(success / Iter)


if __name__ == '__main__':
    """
    Enunciado: Sean X1, ... Xn va independientes e idénticamente distribuídas
    con media mu desconocida. Para a y b constantes dadas, a < b, nos interesa
    estimar: p = P(a < sum_{i=1}^{n} Xi/n - mu < b). Estimar p asumiendo que
    para n = 10, los valores de las variables Xi resultan 56, 101, 78, 67, 93,
    87, 64, 72, 80 y 69. Sean a = −5 y b = 5.
    """
    sample = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    Iter, A, B = 10000, -5, 5
    print("Estimación de p: {}".format(experiment(sample, Iter, A, B)))
