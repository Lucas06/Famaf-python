from discretes_distributions import permutation


def experiment(mallet):
    """
    Enunciado: Se baraja un conjunto de N = 100 cartas (numeradas
    consecutivamente del 1 al 100) y se extrae del mazo una carta por vez.
    Consideramos que ocurre un “éxito” si la i-ésima carta extraída es aquella
    cuyo número es i, con i = 1, ..., N.
    """
    success = 0  # Cantidad de éxitos
    mallet_tmp = permutation(mallet)
    for i in range(len(mallet_tmp)):
        if i + 1 == mallet_tmp[i]:  # Evento exitoso
            success += 1
    return(success)


if __name__ == '__main__':
    N = 1000  # Cantidad de corridas del experimento
    mallet = list(range(1, 101))  # Mazo de 100 cartas
    success = []  # Éxitos de la esperanza x
    success2 = []  # Éxitos de la esperanza de x**2

    for _ in range(N):
        result = experiment(mallet)
        success.append(result)
        success2.append(result ** 2)
        # success.append(experiment(mallet))
        # success2.append(experiment(mallet) ** 2)
    mean = sum(success) / N
    mean2 = sum(success2) / N
    variance = mean2 - (mean ** 2)

    print("Esperanza: {}".format(mean))
    print("Varianza: {}".format(variance))
