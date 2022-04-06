# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

localLen = len


def printgraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))


def plot_graph(opt_values, counter_values):
    opt_values.reverse()
    # print("otimos locais {}".format(opt_values))
    # print("i {}".format(counter_values))
    opt_values.reverse()
    plt.axis('auto')
    plt.title("TSP", fontsize=13)
    plt.xlabel("Iterações", fontsize=11)
    plt.ylabel("Ótimos locais", fontsize=11)
    plt.plot(counter_values, opt_values)
    # plt.legend()
    plt.show()
    # print(route)
