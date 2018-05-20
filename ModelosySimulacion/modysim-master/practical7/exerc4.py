from functions import d_sample_exponential, p_value, reject


if __name__ == '__main__':
    """
    Enunciado: Calcular una aproximación del p-valor de la hipótesis: “Los
    siguientes 13 valores provienen de una distribución exponencial con media
    50”: 86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99.
    """
    H0 = "H0: Los siguientes 13 valores provienen de una distribución "
    H0 += "exponencial con media 50"
    text = "P-valor con Kolmogorov-Smirnov:"

    sample = [86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99]
    sample.sort()

    n, Iter, d = len(sample), 10000, d_sample_exponential(sample, 1/50)
    p_value = p_value(n, Iter, d)

    print("Estadístico: {}".format(d))
    print("===============================")
    print("{}\n{} {}".format(H0, text, p_value))
    reject(p_value)
