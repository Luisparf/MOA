# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive_matrix import nearestneighbour_matrix, insertdist_matrix, getalldistances
from constructive import nearestneighbour, insertprox
from improvement_matrix import two_opt_matrix
from improvement import two_opt
from aux import printgraph

if __name__ == '__main__':
    ### Input ###
    graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    all_dist = getalldistances(graph)  # matriz de distâncias
    # printgraph(graph)
    ### Heurística construtiva vizinho mais próximo
    # route = nearestneighbour_matrix(graph, all_dist) # usando matriz de distâncias
    # route = nearestneighbour(graph)

    ### Heurística construtiva Inserção do mais próximo
    route = insertdist_matrix(graph, all_dist)  # usando matriz de distâncias
    # route = insertprox(graph)  # calculando distâncias

    ### Heurística melhorativa 2-opt
    print(int(two_opt_matrix(all_dist, route))) # com matriz
    # print(int(two_opt(graph, route)))
