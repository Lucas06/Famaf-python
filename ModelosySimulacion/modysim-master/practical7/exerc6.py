from functions import exponential, d_sample_exponential, p_value, reject


if __name__ == '__main__':
    """
    Enunciado: Generar los valores correspondientes a 10 va exponenciales
    independientes, cada una con media 1. Luego, en base al estadístico de
    prueba de Kolmogorov-Smirnov, aproxime el p-valor de la prueba de que los
    datos realmente provienen de una distribución exponencial con media 1.
    """
    H0 = "H0: Los siguientes valores provienen de una distribución exponencial"
    H0 += " con media 1"
    text = "P-valor con Kolmogorov-Smirnov:"

    sample = [exponential(1) for _ in range(10)]
    sample.sort()

    n, Iter, d = len(sample), 10000, d_sample_exponential(sample, 1)
    p_value = p_value(n, Iter, d)

    print("Estadístico: {}".format(d))
    print("===============================")
    print("{}\n{} {}".format(H0, text, p_value))
    reject(p_value)
