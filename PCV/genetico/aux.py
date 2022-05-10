# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import time
localLen = len


def printgraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))


########################################################################################################################

def plot_graf(x_values1, y_values1, x_values2, y_values2, file_name, cost1, cost2, cross_operator1, cross_operator2, time1, time2):

    name = 'Genetic Algorithm'
    plt.title(
        f'{file_name} - {name}',
        loc='center',
        bbox=dict(facecolor='none', edgecolor='purple'),
        color='purple',
        fontsize=10
    )

    plt.annotate(
        f'fitness:{cost1} - time:{str(time.strftime("%H:%M:%S", time.gmtime(time1)))}',
        xytext=(300, 150),
        textcoords='figure pixels',
        xy=(x_values1[localLen(x_values1) - 1], y_values1[localLen(y_values1) - 1]),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3")
    )

    plt.annotate(
        f'fitness:{cost2} - time:{str(time.strftime("%H:%M:%S", time.gmtime(time2)))}',
        xytext=(300, 300),
        textcoords='figure pixels',
        xy=(x_values2[localLen(x_values2) - 1], y_values2[localLen(y_values2) - 1]),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3")
    )

    if y_values1[0] > 10000 or y_values2[0] > 10000:
        plt.ticklabel_format(useOffset=True)
        plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
        plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

    plt.grid(True)
    plt.xlabel("Generation", fontsize=9)
    plt.ylabel("Fitness(Mean best)", fontsize=9)
    plt.plot(x_values1, y_values1, label=f'{cross_operator1}', color='red')
    plt.plot(x_values2, y_values2, label=f'{cross_operator2}', color='green')
    # plt.scatter(counter_values, opt_values, marker="+", color='red')
    plt.legend(loc='best')
    plt.savefig(
        f'{name.replace(" ", "-") + "_" + file_name.replace(" ", "_").replace(".tsp", ".png")}')
    plt.show()
    # print(route)
