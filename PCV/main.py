# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive import nearestNeighbour, insertmoredistant, printgraph, getAllDistances
from improvement import two_opt
from math import dist
if __name__ == '__main__':
    ### Input ###
    graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    allDistances = getAllDistances(graph)  # distâncias de nó para nó
    # print(allDistances)

    ### Heurística construtiva vizinho mais próximo
    graph = insertmoredistant(graph, allDistances)

    ### Heurística construtiva Inserção do mais distante
    # graph = nearestNeighbour(graph, allDistances)

    ### Heurística melhorativa 2-opt
    print(int(two_opt(graph, allDistances)))
