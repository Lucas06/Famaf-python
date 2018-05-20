import subprocess

numEjer = 3
Ejer = ['a', 'b', 'c', 'd']

for i in range(1, len(Ejer)):
    print("\n Ejercicio {}:\n".format(i))
    subprocess.call('python {}'.format(str(numEjer) + Ejer[i]) + '.py', shell=True)
