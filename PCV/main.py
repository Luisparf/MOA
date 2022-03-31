# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive import nearestneighbour, insertmoredistant, printgraph, getalldistances
from improvement import two_opt
from math import dist
if __name__ == '__main__':
    ### Input ###
    graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y

    ### Heurística construtiva vizinho mais próximo
    route = nearestneighbour(graph)

    ### Heurística construtiva Inserção do mais distante
    # route = insertmoredistant(graph)

    ### Heurística melhorativa 2-opt
    print(int(two_opt(route, graph)))
