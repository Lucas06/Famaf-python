from continuous_distributions import normal, normalPolar


if __name__ == '__main__':
    """
    Enunciado: Escribir dos programas para generar un va normal mediante:
        a) la generación de variables exponenciales según el ejemplo 5f del
           libro Simulación de S. M. Ross
        b) el método polar
    """
    mu, sigma = 0, 1
    N = 10000  # Cantidad de corridas del experimento
    success_normal = []  # Éxitos de la esperanza x
    success_normal2 = []  # Éxitos de la esperanza de x**2
    success_polar = []
    success_polar2 = []

    for _ in range(N):
        result = normal(mu, sigma)
        result_polar, _ = normalPolar()
        success_normal.append(result)
        success_normal2.append(result ** 2)
        success_polar.append(result_polar)
        success_polar2.append(result_polar ** 2)

    mean_normal = sum(success_normal) / N
    mean_normal2 = sum(success_normal2) / N
    variance_normal = mean_normal2 - (mean_normal ** 2)

    mean_polar = sum(success_polar) / N
    mean_polar2 = sum(success_polar2) / N
    variance_polar = mean_polar2 - (mean_polar ** 2)

    print("MÉTODO NORMAL")
    print("Valor real: Esperanza = {}, Varianza = {}".format(mu, sigma))
    print("Aproximaciones: Esperanza = {}, Varianza = {}".format(mean_normal,
          variance_normal))
    print("Absoluto: Esperanza = {}, Varianza = {} \n".format(
          abs(mu - mean_normal), abs(sigma - variance_normal)))

    print("MÉTODO POLAR")
    print("Valor real: Esperanza = {}, Varianza = {}".format(mu, sigma))
    print("Aproximaciones: Esperanza = {}, Varianza = {}".format(mean_polar,
          variance_polar))
    print("Absoluto: Esperanza = {}, Varianza = {}".format(
          abs(mu - mean_polar), abs(sigma - variance_polar)))
