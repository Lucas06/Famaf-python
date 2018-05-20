from random import random
from math import log10, log, sqrt, pi as pi_number, exp as e

"""
######################## VARIABLES ALEATORIAS DISCRETAS #######################
"""


def discrete(xi, pi):
    """
    Genera un va Discreta, a partir de la lista de los valores xi y de sus
    respectivas probabilidades pi.
    """
    U, i, F = random(), 0, pi[0]

    while U >= F:
        i += 1
        F += pi[i]
    return(xi[i])


def uniform(a, b):
    """
    Genera una va Uniforme Discreta en el intervalo [a, b].
    """
    return(int(random() * (b - a + 1)) + a)


def permutation(A):
    """
    Calcula una permutación aleatoria de un conjunto A, de cardinalidad N.
    Recordar que la cantidad de permutaciones de A es N!.
    """
    N = len(A)

    for i in range(N - 1, 0, -1):
        index = uniform(0, i)
        tmp = A[i]
        A[i], A[index] = A[index], tmp
    return(A)


def combinatorial(r, A):
    """
    Devuelve un subconjunto aleatorio de r elementos de un conjunto A, de
    cardinalidad N.
    """
    N = len(A)
    assert(r < N)

    if r < N / 2:
        for i in range(N - 1, r, -1):
            index = uniform(0, i)
            tmp = A[i]
            A[i], A[index] = A[index], tmp
        return(A[N - r:])
    else:
        for i in range(N - 1, N - r, -1):
            index = uniform(0, i)
            tmp = A[i]
            A[i], A[index] = A[index], tmp
        return(A[:r])


def average_example():
    """
    Se desea calcular S = sum_{i=1}^{10000} e ** (1 / i). Es decir, N = 10000.
    Otra forma más resumida:
        return(sum([e(1 / uniform(1, N)) for _ in range(100)]) / 100 * N)
    """
    theta = 0

    for i in range(100):
        theta += e(1 / uniform(1, 10000))
    aproximattion = theta / 100 * 10000

    real_value = sum([e(1 / k) for k in range(1, 10001)])

    print("\t Valor real: {}".format(real_value))
    print("\t Aproximación con {} iteraciones: {}".format(100, aproximattion))
    print("\t Absoluto: {}".format(abs(real_value - aproximattion)))

    return(aproximattion)


def geometric(p):
    """
    Dada una probabilidad p, el algoritmo devuelve una va Geométrica, a través
    del método de la trasformada inversa.
    """
    return(int(log10(1 - random()) / log10(1 - p)) + 1)


def bernoulli_naive(p):
    """
    Dada la probabilida de éxito p, el algoritmo calcula una va Bernoulli.
    """
    return(int(random() < p))


def bernoulli(N, p):
    """
    Este algoritmo se utiliza para generar N va Bernoulli, utilizando un código
    optimizado del libro.
    """
    U, result = random(), []

    for i in range(N):
        if U <= p:
            result.append(1)
            U = U / p
        else:
            U = (U - p) / (1 - p)
            result.append(0)
    return(result)


def poisson_naive(lamda):
    """
    Dado un valor de lamda, la función genera una va Poisson, a través del
    método de la transformada inversa.
    """
    i, U = 0, random()
    F = p = e(-lamda)

    while U >= F:
        i += 1
        p *= lamda / i
        F += p
    return(i)


def pi_poisson(lamda, x):
    """
    Calcula el valor px, es decir P(X = x). Cuando X tiene un distribución de
    Poisson.
    """
    p = e(-lamda)

    for i in range(x):
        p *= lamda / (i + 1)
    return(p)


def F_poisson(lamda, k):
    """
    Función acumulada de una va Poisson, hasta el valor k. Es decir,
    p1 + p2 + ... pk.
    """
    return(sum([pi_poisson(lamda, i) for i in range(k + 1)]))


def poisson(lamda):
    """
    Dado un valor de razón lamda, el algoritmo calcula de forma óptima,
    partiendo desde lamda, una va de Poisson, a través del método de la
    transformada inversa.
    """
    i, U = int(lamda), random()  # Inicializa en el valor más probable
    F = p = F_poisson(lamda, i)

    if U >= F:
        # Búsqueda ascendente
        while U >= F:
            i += 1
            p *= lamda / i
            F += p
        i -= 1
    else:
        # Búsqueda descendente
        while U < F:
            p *= i / lamda
            F -= p
            i -= 1
        i += 1
    return(i)


def binomial_naive(n, p):
    """
    El algoritmo calcula, dada la cantidad de valores n y la probabilidad p de
    cada uno, una va Binomial, utilizando una fórmula recursiva, a través de
    el método de la transformada inversa.
    """
    F = prob = (1 - p) ** n  # Caso base (p0)
    i, U = 0, random()
    c = p / (1 - p)  # Valor constante en todas las iteraciones

    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return(i)


def pi_binomial(n, p, x):
    """
    Calcula el valor px, es decir P(X = x). Cuando X tiene un distribución
    Binomial.
    """
    prob = (1 - p) ** n
    c = p / (1 - p)

    for i in range(x):
        prob *= c * (n - i) / (i + 1)
    return(prob)


def F_binomial(n, p, k):
    """
    Función acumulada de una va Binomial, hasta el valor k.
    """
    return(sum([pi_binomial(n, p, i) for i in range(k + 1)]))


def binomial(n, p):
    """
    Dado los valores de probabilidad p y la cantidad n, el algoritmo calcula de
    forma óptima, partiendo desde el valor más probable (np), una va Binomial,
    a través del método de la transformada inversa.
    """
    i, U = int(n * p), random()  # Inicializa en el valor más probable
    F = prob = F_binomial(n, p, i)
    c = p / (1 - p)

    if U >= F:
        # Búsqueda ascendente
        while U >= F:
            i += 1
            prob *= c * (n - i) / i
            F += prob
        i -= 1
    else:
        # Búsqueda descendente
        while U < F:
            prob *= (1 / c) * i / (n - i)
            F -= prob
            i -= 1
        i += 1
    return(i)


def rejection_example(xi=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pi=[0.11, 0.12, 0.09,
                      0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10]):
    """
    Ejemplo del método de Aceptación y Rechazo, donde pi, son los valores de
    aplicar la función de masa de X. Tomamos q(Y) = 1 / 10, puesto que la
    función de masa de Y es q(Y) = 1 / (b - a). Además tomamos c = 1.2 ya que
    es el máximo valor resultante de la ecuación P(Xi) / Q(Yi).
    """
    c = 1.2
    den = c * 10
    U, Y = random(), uniform(0, 9)

    while U < pi[Y] / den:
        U, Y = random(), uniform(1, 10)
    return(Y)


def composition_example(alphas, distributions):
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


def alias_example(N):
    # Dibujo del ejercicio.
    from texttable import Texttable

    t = Texttable()
    t.add_rows([['j', '1', '2', '3', '4', 'sum'],
                ['pj * 3', 21/16, 3/4, 3/8, 9/16, 3],
                ['', 11/16, 3/4, '', 9/16, 2],
                ['', 11/16, 5/16, '', '', 1]])
    print(t.draw())

    # Código.
    I = int((N - 1) * random()) + 1
    V = uniform(0, 1)

    if I == 1:
        if V < 3/8:
            return(1)
        else:
            return(3)
    elif I == 2:
        if V < 9/16:
            return(4)
        else:
            return(2)
    else:
        if V < 11/16:
            return(1)
        else:
            return(2)


def urn(pi):
    """
    Por medio de una lista con las probabilidades de los valores xi, la función
    calcula el algoritmo de la urna.
    """
    tmp, digits, result = pi, [], []
    k = '1'

    # Calculo cual es el pi que posee más digitos después de la coma.
    for i in tmp:
        _, digit = str(i).split('.')
        digits.append(len(digit))
    max_digit = max(digits)

    # Creo un múltiplo de 10, de acuerdo a la cantidad de dígitos después de la
    # coma del pi con más digitos.
    for _ in range(max_digit):
        k += '0'
    k = int(k)

    # Convierto todas las probabilidades en números enteros.
    tmp = [int(i * k) for i in pi]

    for i in range(len(pi)):
        for j in range(tmp[i]):
            result.append(i + 1)
    return(result[int(len(result) * random()) + 1])


"""
######################## VARIABLES ALEATORIAS CONTINUAS #######################
"""


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
    c = sqrt(27 / 2 * pi_number) * e(- 1 / 2)
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

    """
    ###################### VARIABLES ALEATORIAS DISCRETAS #####################
    """

    print("\n\n VARIABLES ALEATORIAS DISCRETAS \n\n")

    print("Función 'discrete'")
    xi, pi = [4, 3, 1, 2], [0.40, 0.25, 0.20, 0.15]
    print("{}{} \n".format(print_text1, discrete(xi, pi)))

    print("Función 'uniform'")
    a, b = 0, 5
    print("{}{} \n".format(print_text1, uniform(a, b)))

    print("Función 'permutation'")
    print_permutation = "La permutación generada es: "
    A = [1, 2, 3, 4, 5, 6]
    print("{}{} \n".format(print_permutation, permutation(A)))

    print("Función 'combinatorial'")
    print_combinatorial = "El combinatorio generado es: "
    A = [1, 2, 3, 4, 5, 6]
    r = len(A) - 2
    print("{}{} \n".format(print_combinatorial, combinatorial(r, A)))

    print("Función 'average_example'")
    print("{}{} \n".format(print_text1, average_example()))

    print("Función 'geometric'")
    p = 0.6
    print("{}{} \n".format(print_text1, geometric(p)))

    print("Función 'bernoulli_naive'")
    p = 0.7
    print("{}{} \n".format(print_text1, bernoulli_naive(p)))

    print("Función 'bernoulli'")
    N, p = 10, 0.5
    print_bernoulli = "Las variables aleatorias generadas son: "
    print("{}{} \n".format(print_bernoulli, bernoulli(N, p)))

    print("Función 'poisson_naive'")
    lamda = 5
    print("{}{} \n".format(print_text1, poisson_naive(lamda)))

    print("Función 'pi_poisson'")
    text_poisson = "La probabilidad pi = P(X = {}) es: "
    lamda, x = 2, 4
    print("{}{} \n".format(text_poisson.format(x), pi_poisson(lamda, x)))

    print("Función 'F_poisson'")
    text_poisson = "El valor de la función acumulada hasta X = {} es: "
    lamda, x = 2, 4
    print("{}{} \n".format(text_poisson.format(x), F_poisson(lamda, x)))

    print("Función 'poisson'")
    lamda = 15
    print("{}{} \n".format(print_text1, poisson(lamda)))

    print("Función 'binomial_naive'")
    n, p = 10, 0.8
    print("{}{} \n".format(print_text1, binomial_naive(n, p)))

    print("Función 'pi_binomial'")
    text_binomial = "La probabilidad pi = P(X = {}) es: "
    n, p, x = 20, 0.5, 6
    print("{}{} \n".format(text_binomial.format(x), pi_binomial(n, p, x)))

    print("Función 'F_binomial'")
    text_binomial = "El valor de la función acumulada hasta X = {} es: "
    n, p, x = 20, 0.5, 6
    print("{}{} \n".format(text_binomial.format(x), F_binomial(n, p, x)))

    print("Función 'rejection_example'")
    print("{}{} \n".format(print_text1, rejection_example()))

    print("Función 'composition_example'")
    alpha, dist = [0.5, 0.5], [geometric, geometric]
    print("{}{} \n".format(print_text1, composition_example(alpha, dist)))

    print("Función 'alias_example'")
    N = 3
    print("{}{} \n".format(print_text1, alias_example(N)))

    print("Función 'urn'")
    pi = [0.24, 0.46, 0.30]
    print("{}{} \n".format(print_text1, urn(pi)))

    """
    ###################### VARIABLES ALEATORIAS CONTINUAS #####################
    """
    print("\n\n VARIABLES ALEATORIAS CONTINUAS \n\n")

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
