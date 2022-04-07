# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

localLen = len


def printgraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))


########################################################################################################################

def plot_graf(opt_values, counter_values, constr_name, imp_name, file_name):
    # print("otimos locais {}".format(opt_values))
    # print("i {}".format(counter_values))
    plt.axis('auto')
    plt.title("TSP", fontsize=13)
    # plt.text(1000, 60000, 'oi')
    plt.xlabel("Iterações", fontsize=11)
    plt.ylabel("Ótimos locais", fontsize=11)
    plt.plot(counter_values, opt_values, label=f'Construtivo = {constr_name}')
    # plt.scatter(counter_values, opt_values, marker="+", color='red')
    plt.legend(loc='best')
    plt.savefig(f'{constr_name.replace(" ", "_") + "_" + imp_name.replace(" ", "_") + "_" + file_name.replace(" ", "_").replace(".tsp", ".png")}')
    # plt.show()
    # print(route)
