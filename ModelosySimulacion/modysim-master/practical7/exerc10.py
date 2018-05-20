from functions import p_value_small, p_value_big, p_value_simulation, reject


if __name__ == '__main__':
    """
    Enunciado: Catorce ciudades, aproximadamente del mismo tamaño, se eligen
    para un estudio de seguridad vial. Siete de ellas se eligen al azar y
    durante un mes aparecen en los periódicos locales artículos relativos a la
    seguridad vial. Los números de accidentes de tránsito del mes posterior a
    la campaña son los siguientes:
    Grupo de tratamiento: 19 31 39 45 47 66 75
    Grupo de control: 28 36 44 49 52 72 72

    a) Calcular el p-valor exacto de este conjunto de datos, correspondiente a
    la hipótesis de que en ambos grupos se tienen resultados idénticos (es
    decir, los artículos no tuvieron ningún efecto)
    b) Calcular el p-valor aproximado en base a una aproximación normal
    c) Calcular el p-valor aproximado en base a una simulación
    """

    sample_1 = [19, 31, 39, 45, 47, 66, 75]
    sample_2 = [28, 36, 44, 49, 52, 72, 72]
    Iter = 10000

    # Inciso a
    p_value_exact = p_value_small(sample_1, sample_2)
    print("P-valor exacto: {}".format(p_value_exact))
    # reject(p_value_exact)
    print("===============================")

    # Inciso b
    p_value_normal = p_value_big(sample_1, sample_2)
    print("P-valor normal: {}".format(p_value_normal))
    # reject(p_value_normal)
    print("===============================")

    # Inciso c
    p_value_simulated = p_value_simulation(sample_1, sample_2, Iter)
    print("P-valor simulado: {}".format(p_value_simulated))
    # reject(p_value_simulated)
