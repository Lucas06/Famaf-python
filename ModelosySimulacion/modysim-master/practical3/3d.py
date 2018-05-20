from random import random
from math import exp as e

print("Seleccione un opcion \n"
      "(0): Correr automatico \n"
      "(1): Ingresar iteraciones manualmente \n")

option = int(input())
theta = 0.0

def function(theta, n):
    for i in range(n):
        mu_1 = random()
        mu_2 = random()
        theta += e((mu_1 + mu_2) ** 2)
    theta /= n
    print("Interaciones: {}, Resultado: {}".format(n, theta))

if not option:
    N = [1000, 10000, 100000, 1000000]
    for i in N:
        function(theta, i)
else:
    print("Ingrese el numero de iteraciones")
    function(theta, int(input()))
