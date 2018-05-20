from functions import d_sample_uniform, p_value, reject


if __name__ == '__main__':
    """
    Enunciado: Calcular una aproximación del p-valor de la hipótesis: “Los
    siguientes 10 números son aleatorios”: 0:12, 0:18, 0:06, 0:33, 0:72, 0:83,
    0:36, 0:27, 0:77, 0:74.
    """
    H0 = "H0: Los siguiente 10 números son aleatorios"
    text = "P-valor con Kolmogorov-Smirnov:"

    sample = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
    sample.sort()

    n, Iter, d = len(sample), 1000, d_sample_uniform(sample)
    p_value = p_value(n, Iter, d)

    print("Estadístico: {}".format(d))
    print("===============================")
    print("{}\n{} {}".format(H0, text, p_value))
    reject(p_value)
