from functions import sample_var, uniform


def experiment(sample, Iter):
    empirical_var = sample_var(sample)
    n, var = len(sample), 0

    for _ in range(Iter):
        values = [sample[uniform(0, n - 1)] for _ in range(n)]
        mean_tmp = sum(values) / n

        var_tmp = 0
        for value in values:
            var_tmp += (value - mean_tmp) ** 2
        var_tmp /= (n - 1)

        var += (var_tmp - empirical_var) ** 2
    return(var / Iter)


if __name__ == '__main__':
    """
    Enunciado: Sean X1, ... Xn va independientes e idénticamente distribuías
    con varianza sigma ** 2 desconocida. Se planea estimar sigma ** 2 mediante
    la varianza muestral: sum_{i=1}^{n} (Xi - X(mean)) ** 2 / (n - 1).
    """
    sample = [1, 3]
    Iter = 10000
    print("Estimación de varianza: {}".format(experiment(sample, Iter)))
