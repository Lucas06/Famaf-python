from functions import p_value_small, p_value_big, p_value_simulation, reject


if __name__ == '__main__':
    """
    Enunciado: Un experimento diseñado para comparar dos tratamientos contra la
    corrosión arrojó los siguientes datos (los cuales representan la máxima
    profundidad de los agujeros en unidades de milésima de pulgada) en pedazos
    de alambre sujetos a cada uno de los tratamientos por separado:
    Tratamiento 1: 65.2 67.1 69.4 78.4 74.0 80.3
    Tratamiento 2: 59.4 72.1 68.0 66.2 58.5

    a) Calcular el p-valor exacto de este conjunto de datos, correspondiente a
    la hipótesis de que ambos tratamientos tienen resultados idénticos
    b) Calcular el p-valor aproximado en base a una aproximación normal
    c) Calcular el p-valor aproximado en base a una simulación
    """

    sample_1 = [65.2, 67.1, 69.4, 78.4, 74.0, 80.3]
    sample_2 = [59.4, 72.1, 68.0, 66.2, 58.5]
    Iter = 10000

    # Inciso a
    p_value_exact = p_value_small(sample_1, sample_2)
    print("P-valor exacto: {}".format(p_value_exact))
    reject(p_value_exact)
    print("===============================")

    # Inciso b
    p_value_normal = p_value_big(sample_1, sample_2)
    print("P-valor normal: {}".format(p_value_normal))
    reject(p_value_normal)
    print("===============================")

    # Inciso c
    p_value_simulated = p_value_simulation(sample_1, sample_2, Iter)
    print("P-valor simulado: {}".format(p_value_simulated))
    reject(p_value_simulated)
