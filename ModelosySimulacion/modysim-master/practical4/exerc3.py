from math import sqrt
from discretes_distributions import uniform


def experiment():
    """
    Enunciado: Se lanzan simultáneamente un par de dados legales y se anota el
    resultado de la suma de ambos. El proceso se repite hasta que todos los
    resultados posibles: 2, ... 12 hayan aparecido al menos una vez. Estudiar
    mediante una simulación el número de lanzamientos necesarios para cumplir
    el proceso. Cada lanzamiento implica arrojar el par de dados.
    Mediante una implementación en computadora, calcular el valor medio y la
    desviación estándar del número de lanzamientos, repitiendo el algoritmo:
    100, 1000, 10000 y 100000 veces.
    """
    success = 0
    results = list([x for x in range(2, 13)])  # Lista de resultados

    while results:
        result = uniform(1, 6) + uniform(1, 6)  # Dado_1 + Dado_2
        success += 1
        if result in results:
            results.remove(result)
    return(success)


if __name__ == '__main__':
    N = [100, 1000, 10000, 100000]  # Número de iteraciones
    success = []  # Éxitos de la esperanza x
    success2 = []  # Éxitos de la esperanza de x**2

    for n in N:
        for _ in range(n):
            estimate = experiment()
            success.append(estimate)
            success2.append(estimate ** 2)
            # success.append(experiment())
            # success2.append(experiment() ** 2)
        mean = sum(success) / n
        mean2 = sum(success2) / n
        variance = mean2 - (mean ** 2)

        print("Aproximación con {} iteraciones".format(n))
        print("Esperanza: {}".format(mean))
        print("Desviación Estándar: {} \n".format(sqrt(variance)))
