from functions import normal


def experiment(d, Iter):
    const, sample, var, n = d ** 2, [normal(0, 1)], 0, 1
    mean_old = sample[0]

    while var / n > const or n < Iter:
        sample.append(normal(0, 1))
        mean_new = mean_old + (sample[n] - mean_old) / (n + 1)
        var = (1 - 1 / n) * var + (n + 1) * ((mean_new - mean_old) ** 2)
        mean_old = mean_new
        n += 1
    return(mean_new, var, n)


if __name__ == '__main__':
    """
    Enunciado: Generar n valores de una va normal estándar de manera tal que se
    cumplan las condiciones: n >= 30 y S / sqrt(n) < 0.1, siendo S la
    desviación estándar muestral de los n datos generados. Dar la media
    muestral, varianza muestral y el número de iteraciones.
    Observación: primero se hacen 30 corridas para satisfacer la primera
    condición del ejercicio.
    """
    d, Iter = 0.1, 30
    mean, var, n = experiment(d, Iter)
    print("Media muestral es: {}\nVarianza muestral es: {}".format(mean, var))
    print("Cantidad de iteraciones: {}".format(n))
