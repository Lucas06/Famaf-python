from random import random
from math import log10, exp as e

# TO DO: binomial optima


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


if __name__ == '__main__':
    print_text = "La variable aleatoria generada es: "

    print("Función 'discrete'")
    xi, pi = [4, 3, 1, 2], [0.40, 0.25, 0.20, 0.15]
    print("{}{} \n".format(print_text, discrete(xi, pi)))

    print("Función 'uniform'")
    a, b = 0, 5
    print("{}{} \n".format(print_text, uniform(a, b)))

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
    print("{}{} \n".format(print_text, average_example()))

    print("Función 'geometric'")
    p = 0.6
    print("{}{} \n".format(print_text, geometric(p)))

    print("Función 'bernoulli_naive'")
    p = 0.7
    print("{}{} \n".format(print_text, bernoulli_naive(p)))

    print("Función 'bernoulli'")
    N, p = 10, 0.5
    print_bernoulli = "Las variables aleatorias generadas son: "
    print("{}{} \n".format(print_bernoulli, bernoulli(N, p)))

    print("Función 'poisson_naive'")
    lamda = 5
    print("{}{} \n".format(print_text, poisson_naive(lamda)))

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
    print("{}{} \n".format(print_text, poisson(lamda)))

    print("Función 'binomial_naive'")
    n, p = 10, 0.8
    print("{}{} \n".format(print_text, binomial_naive(n, p)))

    print("Función 'pi_binomial'")
    text_binomial = "La probabilidad pi = P(X = {}) es: "
    n, p, x = 20, 0.5, 6
    print("{}{} \n".format(text_binomial.format(x), pi_binomial(n, p, x)))

    print("Función 'F_binomial'")
    text_binomial = "El valor de la función acumulada hasta X = {} es: "
    n, p, x = 20, 0.5, 6
    print("{}{} \n".format(text_binomial.format(x), F_binomial(n, p, x)))

    # print("Función 'binomial'")
    # # n, p = 20, 0.5
    # n, p = 5, 0.3
    # print("{}{} \n".format(print_text, binomial(n, p)))

    print("Función 'rejection_example'")
    print("{}{} \n".format(print_text, rejection_example()))

    print("Función 'composition_example'")
    alpha, dist = [0.5, 0.5], [geometric, geometric]
    print("{}{} \n".format(print_text, composition_example(alpha, dist)))

    print("Función 'alias_example'")
    N = 3
    print("{}{} \n".format(print_text, alias_example(N)))

    print("Función 'urn'")
    pi = [0.24, 0.46, 0.30]
    print("{}{} \n".format(print_text, urn(pi)))
