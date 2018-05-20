from continuous_distributions import PPoissonNH_naive


def lamdaT(t):
    return(3 + (4 / (t + 1)))


if __name__ == '__main__':
    """
    Enunciado: Escribir un programa que utilice el algoritmo del adelgazamiento
    para generar las primeras diez unidades de tiempo de un proceso de Poisson
    no homogéneo con función de intensidad: lambda(t) = 3 + (4 / (t + 1)).
    Indicar una forma de mejorar el algoritmo de adelgazamiento para este
    ejemplo particular.
    """
    lamda, T = 2, 5
    I, S = PPoissonNH_naive(lamda, lamdaT, T)
    print("Las valores generados son: I = {}, \n S = {}".format(I, S))
