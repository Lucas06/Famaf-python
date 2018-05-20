from continuous_distributions import composition


if __name__ == '__main__':
    """
    Enunciado: Método de la composición: Suponer que es relativamente fácil
    generar n va a partir de sus distribuciones de probabilidad Fi, con
    i = 1, ..., n. Implementar un método para generar una va cuya distribución
    de probabilidad es: F(x) = sum_{i=1}^{n} pi * Fi(x), donde pi con
    i = 1, ..., n son números no negativos cuya suma es 1.
    En lugar de pasar las funciones Fi, pasamos los valores de dicha va.
    """
    pi = [0.40, 0.25, 0.20, 0.15]
    Fi = [4.2, 3.12, 1.7, 2.55]
    print("El valor de la va es: X = {}".format(composition(pi, Fi)))
