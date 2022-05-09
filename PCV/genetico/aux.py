# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

localLen = len


def printgraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))


########################################################################################################################

def plot_graf(opt_values, counter_values, file_name, exe_time, cost, cross_operator):
    # print("otimos locais {}".format(opt_values))

    # print("i {}".format(counter_values))

    # plt.axis('auto')
    name = 'Algoritmo genético'
    plt.title(
        f'{file_name} - {name} - tempo total:{exe_time}s',
        loc='center',
        bbox=dict(facecolor='none', edgecolor='purple'),
        color='purple',
        fontsize=10
    )
    plt.annotate(
        f'melhor solução: {cost}',
        xytext=(400, 300),
        textcoords='figure pixels',
        xy=(counter_values[localLen(counter_values) - 1], opt_values[localLen(opt_values) - 1]),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3")
    )

    if opt_values[0] > 10000:
        plt.ticklabel_format(useOffset=True)
        plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
        plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

    plt.grid(True)
    plt.xlabel("Iterações", fontsize=9)
    plt.ylabel("Ótimos locais", fontsize=9)
    plt.plot(counter_values, opt_values, label=f'{cross_operator}',  color='red')
    # plt.scatter(counter_values, opt_values, marker="+", color='red')
    plt.legend(loc='best')
    plt.savefig(
        f'{name.replace(" ", "-") + "_" + cross_operator + "_" +  file_name.replace(" ", "_").replace(".tsp", ".png")}')
    plt.show()
    # print(route)
