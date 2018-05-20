import numpy as np
from math import log, sqrt
from matplotlib import pyplot as plt
from random import random
from texttable import Texttable


def exponential(lamda):
    """
    Generate exponential random variable with a uniform variable.
    """
    return(- log(random()) / lamda)


def experiment(N, S, Tf, Tr, Op):
    """
    :param N: Number of machines in service.
    :param S: Number of backup machines.
    :param Tf: Mean time of fail.
    :param Tr: Mean time of of repair.
    :param Op: Number of operators.
    """
    # time: Time variable.
    # machines_down_number: Number of machines that are broken at current time.
    time = machines_down_number = 0

    # Define infinite constant.
    INF = float("inf")

    # repair_time: Time at which the machine presently in repair will become
    # operational, or infinite.
    repair_time = [INF for _ in range(Op)]

    # life_times: list of life time of N machines.
    life_times = [exponential(1 / Tf) for _ in range(N)]
    life_times.sort()

    while True:
        if life_times[0] < repair_time[0]:
            time = life_times.pop(0)
            machines_down_number += 1

            # More broken machines than replacement machines, abort.
            if machines_down_number == S + 1:
                return(time)

            # There are replacement machines.
            if machines_down_number < S + 1:
                life_times.append(time + exponential(1 / Tf))
                life_times.sort()

            # There is a free operator than repair broken machine.
            if INF in repair_time:
                index = repair_time.index(INF)
                repair_time[index] = time + exponential(1 / Tr)
                repair_time.sort()

        else:
            time = repair_time.pop(0)
            # First operator is free.
            repair_time.append(INF)
            # Number of free operators.
            free_op = repair_time.count(INF)

            # Assign one machine to each free operator.
            if machines_down_number >= free_op:
                for _ in range(free_op):
                    index = repair_time.index(INF)
                    repair_time[index] = time + exponential(1 / Tr)
                machines_down_number -= free_op
                free_op = 0

            elif machines_down_number == 0:
                repair_time = [INF for _ in range(Op)]

            if machines_down_number < free_op and machines_down_number != 0:
                for _ in range(machines_down_number):
                    index = repair_time.index(INF)
                    repair_time[index] = time + exponential(1 / Tr)
                machines_down_number = 0


def simulation(F, N, S, Tf, Tr, Op):
    """
    """
    d, Iter, n, sample = 0.01 ** 2, 1000, 1, [F(N, S, Tf, Tr, Op)]
    mean_old, var = sample[0], 0

    while var / n > d or n < Iter:
        sample.append(F(N, S, Tf, Tr, Op))
        mean_new = mean_old + (sample[n] - mean_old) / (n + 1)
        var = (1 - 1 / n) * var + (n + 1) * ((mean_new - mean_old) ** 2)
        mean_old = mean_new
        n += 1
    return(sample, mean_new, var, n)


def histogram(values, mu, sigma, color, number):
    """
    Draws a histogram of values.
    """
    plt.figure("Figure {}".format(number))
    plt.title("Histogram of experiment {}".format(number))
    plt.xlabel("Time (month)")
    plt.ylabel("Relative Frecuency (%)")

    bins = np.linspace(0, 20, 100)
    mu, sigma = round(mu, 3), round(sigma, 3)

    plt.hist(values, bins, normed=1, color=color, edgecolor="w",
             label="$\mu={},\ \sigma={}$".format(mu, sigma))
    plt.legend(loc='upper right')
    plt.xlim(0, 10)
    plt.ylim(0, .6)
    plt.show()
    return(values)


def comparative(args_1, args_2, number):
    """
    """
    exp_1, op_1, mu_1, sigma_1, color_1, graphic_1 = args_1
    exp_2, op_2, mu_2, sigma_2, color_2, graphic_2 = args_2

    plt.figure("Comparative graphic {}".format(number))
    plt.title("Histogram of comparative between simulation {} and {}".format(
              graphic_1, graphic_2))
    plt.xlabel("Time (month)")
    plt.ylabel("Relative Frecuency (%)")

    bins = np.linspace(0, 20, 100)

    mu_1, mu_2 = round(mu_1, 3), round(mu_2, 3)
    sigma_1, sigma_2 = round(sigma_1, 3), round(sigma_2, 3)

    text = "Experiment {}: $\mu_{}={},\ \sigma_{}={}$"
    plt.hist(exp_1, bins, normed=1, color=color_1,
             label=text.format(graphic_1, graphic_1, mu_1, graphic_1, sigma_1))
    plt.hist(exp_2, bins, normed=1, alpha=0.5, color=color_2,
             label=text.format(graphic_2, graphic_2, mu_2, graphic_2, sigma_2))
    plt.legend(loc="upper right")
    plt.axvline(mu_1, color=color_1, linestyle="dashed", linewidth=2,
                label="$\mu_{}$".format(graphic_1))
    plt.axvline(mu_2, color=color_2, linestyle="dashed", linewidth=2,
                label="$\mu_{}$".format(graphic_2))
    plt.xlim(0, 10)
    plt.ylim(0, .6)
    plt.legend(loc=0, prop={'size': 10})
    plt.show()


if __name__ == '__main__':
    N, Tf, Tr = 5, 1, 1/8
    S_1, S_2 = 2, 3
    op_1, op_2 = 1, 2
    Iter = 10000
    table_1, table_2, table_3 = Texttable(), Texttable(), Texttable()
    color_1, color_2, color_3 = '#0A4D6D', '#FF0000', '#6272A4'
    title = ['Iter', 'mu', 'sigma^2', 'sigma']

    # Configure tables
    table_1.set_chars(['', '&', '', '='])
    table_2.set_chars(['', '&', '', '='])
    table_3.set_chars(['', '&', '', '='])
    table_1.add_row(title)
    table_2.add_row(title)
    table_3.add_row(title)

    # Exercice 1
    values_1, mean_1, variance_1, Iter_1 = simulation(experiment, N, S_1, Tf,
                                                      Tr, op_1)
    std_dev_1 = sqrt(variance_1)
    table_1.add_row([str(Iter_1), str(mean_1), str(variance_1),
                    str(std_dev_1)])

    # Exercice 2
    values_2, mean_2, variance_2, Iter_2 = simulation(experiment, N, S_1, Tf,
                                                      Tr, op_2)
    std_dev_2 = sqrt(variance_2)
    table_2.add_row([str(Iter_2), str(mean_2), str(variance_2),
                    str(std_dev_2)])

    # Exercice 3
    values_3, mean_3, variance_3, Iter_3 = simulation(experiment, N, S_2, Tf,
                                                      Tr, op_1)
    std_dev_3 = sqrt(variance_3)
    table_3.add_row([str(Iter_3), str(mean_3), str(variance_3),
                    str(std_dev_3)])

    # Comparative graphic
    args_1 = [values_1, op_1, mean_1, std_dev_1, color_1, 1]
    args_2 = [values_2, op_2, mean_2, std_dev_2, color_2, 2]
    args_3 = [values_3, op_1, mean_3, std_dev_3, color_3, 3]

    comparative(args_1, args_2, 1)
    comparative(args_1, args_3, 2)
    comparative(args_2, args_3, 3)

    print(table_1.draw())
    print("\n")
    print(table_2.draw())
    print("\n")
    print(table_3.draw())
