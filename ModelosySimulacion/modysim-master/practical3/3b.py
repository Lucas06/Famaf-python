from random import random

print("Seleccione un opcion \n"
      "(0): Correr automatico \n"
      "(1): Ingresar iteraciones manualmente \n")

option = int(input())
theta = 0.0

def function(theta, n):
    for i in range(n):
        mu = random()
        theta += (1. / (mu ** 3) - 1. / (mu ** 2)) / ((1. + (1. / mu - 1.) ** 2) ** 2)
    theta /= n
    print("Interaciones: {}, Resultado: {}".format(n, theta))

if not option:
    N = [100, 1000, 10000, 100000, 1000000]
    for i in N:
        function(theta, i)
else:
    print("Ingrese el numero de iteraciones")
    function(theta, int(input()))
