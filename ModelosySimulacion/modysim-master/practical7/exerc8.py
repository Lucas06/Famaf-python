from functions import mu_sigma_normal_estimate, d_sample_normal, p_value_normal
from functions import p_value, reject


if __name__ == '__main__':
    """
    Enunciado: Decidir si los siguientes datos corresponden a una distribución
    Normal: 91.9 97.8 111.4 122.3 105.4 95.0 103.8 99.6 96.6 119.3 104.8 101.7.
    Calcular una aproximación del p-valor.
    """
    H0 = "H0: Los siguientes datos corresponden a una distribución normal"
    text = "P-valor con Kolmogorov-Smirnov:"

    sample = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3,
              104.8, 101.7]
    sample.sort()

    n, Iter = len(sample), 10000
    mu, sigma = mu_sigma_normal_estimate(sample)
    d = d_sample_normal(sample, mu, sigma)
    p_value_1 = p_value_normal(n, mu, sigma, d, Iter)
    p_value_2 = p_value(n, Iter, d)

    print("Estadístico: {}".format(d))
    print("===============================")
    print("{}\n{}".format(H0, text))
    print("Estimando parámetros en cada iteración: {}".format(p_value_1))
    reject(p_value_1)
    print("===============================")
    print("Sin estimar parámetros: {}".format(p_value_2))
    reject(p_value_2)
