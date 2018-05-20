from random import random

N = [100, 1000, 10000, 100000, 1000000]

for n in N:
    success = 0.0
    for _ in range(n):
        u = random()
        if u < 1/2:
            x = random() + random()
        else:
            x = random() + random() + random()
        if x > 1:
            success += 1
    print("Interaciones: {}, Exitos: {}".format(n, float(success) / float(n)))
