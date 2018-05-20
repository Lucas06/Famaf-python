from functions import lamda_exponential_estimate, d_sample_exponential
from functions import p_value_exponential, reject, p_value


if __name__ == '__main__':
    """
    Enunciado: En un estudio de vibraciones, una muestra aleatoria de 15
    componentes de un avión fueron sometidos a fuertes vibraciones, hasta que
    se evidenciaron fallas estructurales. Los datos proporcionados son los
    minutos transcurridos hasta que se evidenciaron dichas fallas, 1.6 10.3 3.5
    13.5 18.4 7.7 24.3 10.7 8.4 4.9 7.9 12 16.2 6.8 14.7.
    Pruebe la hipótesis nula de que estas observaciones pueden ser consideradas
    como una muestra de la población exponencial.
    """
    H0 = "H0: Los siguientes datos corresponden a una distribución exponencial"
    text = "P-valor con Kolmogorov-Smirnov:"

    sample = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12,
              16.2, 6.8, 14.7]
    sample.sort()

    n, Iter = len(sample), 10000
    lamda = lamda_exponential_estimate(sample)
    d = d_sample_exponential(sample, lamda)
    p_value_1 = p_value_exponential(n, lamda, d, Iter)
    p_value_2 = p_value(n, Iter, d)

    print("Estadístico: {}".format(d))
    print("===============================")
    print("{}\n{}".format(H0, text))
    print("Estimando parámetros en cada iteración: {}".format(p_value_1))
    reject(p_value_1)
    print("===============================")
    print("Sin estimar parámetros: {}".format(p_value_2))
    reject(p_value_2)
