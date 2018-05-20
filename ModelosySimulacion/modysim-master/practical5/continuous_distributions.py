from random import random
from math import log, sqrt, pi, exp as e


def maxN(N):
    """
    Calcula el máximo de N va independientes uniformes en (0, 1).
    """
    return(max([random() for _ in range(N)]))


def minN(N):
    """
    Calcula el mínimo de N va independientes uniformes en (0, 1).
    """
    return(min([random() for _ in range(N)]))


def exponential(lamda):
    """
    Genera una va Exponencial, a partir de su único parámentro lamda,
    utilizando el método de la transformada inversa.
    """
    return(- log(random()) / lamda)


def gamma(N, lamda):
    """
    Esta función genera una va Gamma, es decir, el producto de n va
    exponenciales de parámetro lamda.
    """
    U = 1

    for _ in range(N):
        U *= random()
    return(- log(U) / lamda)


def twoExponentials(lamda):
    """
    Genera dos va exponenciales independientes de parámetro lamda, a trevés de
    la generación de una gamma(2, lamda).
    """
    t = gamma(2, lamda)
    X = t * random()
    Y = t - X

    return(X, Y)


def Nexponentials(N, lamda):
    """
    Genera N va exponenciales, mediante la función gamma, de manera óptima.
    """
    Vi, array = [], []
    t = gamma(N, lamda)
    Vi = [random() for _ in range(N)]
    Vi.sort()
    intervals = ([t * Vi[0]] +
                 [t * (Vi[i] - Vi[i - 1]) for i in range(1, N-1)] +
                 [t - t * Vi[N - 1]])

    return(intervals)


def composition(alphas, distributions):
    """
    A partir de la generación de dos va X1, X2, mediante otro método eficiente,
    esta función genera una nueva va X = alpha * X1 + (1 - alpha) * X2, que
    aceptará X1 con probabilidad alpha y X2 con 1 - alpha.
    """
    assert(sum(alphas) == 1)
    assert(len(alphas) == len(distributions))
    tuples = list(zip(alphas, distributions))
    tuples.sort(reverse=True)
    U, F, j = random(), 0, 0

    for alpha, dist in tuples:
        F += alpha
        if U <= F:
            return(dist)


def rejection_example1():
    """
    Ejemplo del método de Aceptación y Rechazo, donde la función es:
    f(x) = 20 * x (1 - x) ** 3, rechazamos con una uniforme(0, 1).
    """
    c = 135 / 64
    U, Y = random(), random()

    while U < 20 * Y * ((1 - Y) ** 3) / c:
        U, Y = random(), random()
    return(Y)


def rejection_example2():
    """
    Ejemplo del método de Aceptación y Rechazo, donde la función es:
    f(x) = 2 / sqrt(pi) * sqrt(x) * e ** (-x), rechazamos con una
    va exponencial(2/3).
    """
    c = sqrt(27 / 2 * pi) * e(- 1 / 2)
    U, Y = random(), exponential(2/3)

    while U < 20 * Y * ((1 - Y) ** 3) / c:
        U, Y = random(), random()
    return(Y)


def normal(mu, sigma):
    """
    Esta función devuelve una va normal, utilizando el método de Aceptación y
    Rechazo mediante 2 va exponenciales.
    """
    Y1, Y2 = exponential(1), exponential(1)

    while Y2 < (Y1 - 1) ** 2 / 2:
        Y1, Y2 = exponential(1), exponential(1)

    if random() < 0.5:
        return(Y1 * sigma + mu)
    else:
        return(-Y1 * sigma + mu)


def normalPolar():
    """
    Este método genera DOS va normales, a través del método de Aceptación y
    Rechazo.
    """
    V1, V2 = 2 * random() - 1, 2 * random() - 1

    # Generamos un punto aleatorio en el círculo unitario.
    while V1 ** 2 + V2 ** 2 > 1:
        V1, V2 = 2 * random() - 1, 2 * random() - 1

    S = V1 ** 2 + V2 ** 2
    const = sqrt(-2 * log(S) / S)
    return (V1 * const, V2 * const)


def PPoissonH(lamda, T):
    """
    El algoritmo calcula un proceso de Poisson Homogéneo, donde I representa el
    número de eventos que ocurren hasta T y S[i] indica el tiempo en el que
    ocurre el evento i-ésimo. Devuelve la lista de la cantidad y los tiempos de
    los eventos. RECORDAR DEVOLVER EL ANTERIOR.
    """
    t, I, S, exp = 0, 0, [0], exponential(lamda)

    while t + exp <= T:
        t += exp
        I += 1
        S.append(t)
        exp = exponential(lamda)
    return(I, S)


def PPoissonNH_naive(lamda, lamdaT, T):
    """
    El algoritmo genera las T primeras unidades de tiempo de un proceso de
    Poisson NO Homogéneo, donde I representa el número de eventos que ocurren
    hasta T y S[i] indica el tiempo en el que ocurre el evento i-ésimo.
    Devuelve la lista de la cantidad y los tiempos de los eventos. También
    conocido como algoritmo de adelgazamiento.
    """
    t, I, S, exp = 0, 0, [0], exponential(lamda)

    while t + exp <= T:
        t += exp
        if random() < lamdaT(t) / lamda:
            I += 1
            S.append(t)
        exp = exponential(lamda)
    return(I, S)


def PPoissonNH(lamdas, lamdaT, intervals):
    """
    :param lamdas: es equivalente al lamda del naive, solo que en este caso va
                   haber un lamda_i por cada intervalo.
    :param lamdaT: al igual que antes es la función de intensidad.
    :param intervals: subintervalos en los cuales quedó partido el intervalo
                      total.

    El algoritmo genera las T primeras unidades de tiempo de un proceso de
    Poisson NO Homogéneo, donde I representa el número de eventos que ocurren
    hasta T y S[i] indica el tiempo en el que ocurre el evento i-ésimo.
    Devuelve la lista de la cantidad y los tiempos de los eventos. También
    conocido como algoritmo de ADELGAZAMIENTO.
    """
    t, I, J, S, k = 0, 0, 0, [0], len(intervals) - 1

    while True:
        exp = exponential(lamdas[J])

        if t + exp > intervals[J]:
            if J == k:
                break
            else:
                exp = (exp - intervals[J] + t) * lamdas[J] / lamdas[J + 1]
                t = intervals[J]
                J += 1
        t += exp

        if random() < lamdaT(t) / lamdas[J]:
            I += 1
            S.append(t)
    return(I, S)


if __name__ == '__main__':
    print_text1 = "La variable aleatoria generada es: X = "
    print_text2 = "Las variables aleatorias generadas son: "

    print("Función 'maxN'")
    N = 5
    print("{}{} \n".format(print_text1, maxN(N)))

    print("Función 'minN'")
    print("{}{} \n".format(print_text1, minN(N)))

    print("Función 'exponential'")
    lamda = 2
    print("{}{} \n".format(print_text1, exponential(lamda)))

    print("Función 'gamma'")
    N, lamda = 10, 3
    print("{}{} \n".format(print_text1, gamma(N, lamda)))

    print("Función 'twoExponentials'")
    lamda = 4
    X, Y = twoExponentials(lamda)
    print("{}X = {}, Y = {} \n".format(print_text2, X, Y))

    print("Función 'Nexponentials'")
    N, lamda = 10, 3
    print("{}\n {} \n".format(print_text2, Nexponentials(N, lamda)))

    print("Función 'composition'")
    alpha, dist = [0.5, 0.5], [exponential, exponential]
    print("{}{} \n".format(print_text1, composition(alpha, dist)))

    print("Función 'rejection_example1'")
    print("{}{} \n".format(print_text1, rejection_example1()))

    print("Función 'rejection_example2'")
    print("{}{} \n".format(print_text1, rejection_example2()))

    print("Función 'normal'")
    mu, sigma = 3, 2.3
    print("{}{} \n".format(print_text1, normal(mu, sigma)))

    print("Función 'normalPolar'")
    X, Y = normalPolar()
    print("{}X = {}, Y = {} \n".format(print_text2, X, Y))

    print("Función 'PPoissonH'")
    lamda, T = 2, 100
    I, S = PPoissonH(lamda, T)
    print("Caí en el intervalo: {} \n".format(I))

    print("Función 'PPoissonNH_naive'")
    # Consideramos lamdaT y lamda del ejercicio 12 del práctico 5.

    def lamdaT(t):
        return(3 + (4 / (t + 1)))

    lamda, T = 7, 50
    I, S = PPoissonNH_naive(lamda, lamdaT, T)
    print("Caí en el intervalo: {} \n".format(I))

    print("Función 'PPoissonNH'")
    # Consideramos lamdaT y lamda del ejercicio 12 del práctico 5.

    def lamdaT(t):
        return(3 + (4 / (t + 1)))

    lamdas = [7, 8, 9, 10]
    intervals = [0, 1, 2, 3]
    I, S = PPoissonNH(lamdas, lamdaT, intervals)
    print("Caí en el intervalo: {}".format(I))
