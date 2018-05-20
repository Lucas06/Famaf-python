from continuous_distributions import Nexponentials


if __name__ == '__main__':
    """
    Enunciado: Escribir un programa para generar las primeras T unidades de
    tiempo de un proceso de Poisson con parámetro lambda.
    El ejercicio en sí es escribir la función Nexponentials pero escribo un
    ejemplo particular para probarlo.
    """
    T, lamda = 10, 2
    print("Las Variables Aleatorias generadas son: \n {}".format(
          Nexponentials(T, lamda)))
