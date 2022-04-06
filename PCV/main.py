# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive_matrix import nearestneighbour_matrix, insertdist_matrix, getalldistances, insertcheap_matrix
from constructive import nearestneighbour, insertdist, insertcheap
from improvement_matrix import two_opt_matrix, sumdistance_matrix
from improvement import two_opt
from aux import printgraph
import time

"""
    TSP SOLVER
    >_ python3 main.py -h       for help.
"""

if __name__ == '__main__':

    start_time = time.time()
    ### Input ###
    # graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    args, graph = fileinput()

    ### Utiliza matriz de distâncias
    x = -1
    if args.mode == 'm':
        all_dist = getalldistances(graph)  # matriz de distâncias

        ### Heurística construtiva Inserção do mais distante
        if args.algoritmo_construtivo == 'id':
            x = 0
            route = insertdist_matrix(graph, all_dist)  # usando matriz de distâncias

        ### Heurística construtiva Vizinho mais próximo
        elif args.algoritmo_construtivo == 'vp':
            x = 1
            route = nearestneighbour_matrix(graph, all_dist)  # usando matriz de distâncias

        ### Heurística construtiva Inserção do mais barato
        elif args.algoritmo_construtivo == 'ic':
            x = 0
            route = insertcheap_matrix(graph, all_dist)  # usando matriz de distâncias
        else:
            print("{} não é um argumento válido!\n".format(args.algoritmo_construtivo))
            exit(0)

        ### Heurística melhorativa 2-opt
        if args.algoritmo_melhorativo == 'opt2':
            print(int(two_opt_matrix(all_dist, route, x)))  # com matriz

        ### Sem Heurística melhorativa
        elif args.algoritmo_melhorativo == 'none':
            print(int(sumdistance_matrix(all_dist, route)))
        else:
            print("{} não é um argumento válido!\n".format(args.algoritmo_melhorativo))

    ### Não utiliza matriz de distâncias
    elif args.mode == 'n':
        ### Heurística construtiva Vizinho mais próximo
        if args.algoritmo_construtivo == 'vp':
            x = 1
            route = nearestneighbour(graph)

        ### Heurística construtiva Inserção do mais distante
        elif args.algoritmo_construtivo == 'id':
            x = 0
            route = insertdist(graph)

        ### Heurística construtiva Inserção do mais barato

        elif args.algoritmo_construtivo == 'ic':
            x = 0
            route = insertcheap(graph)
        else:
            print("{} não é um argumento válido!\n".format(args.algoritmo_construtivo))
            exit(0)

        ### Heurística melhorativa 2-opt
        if args.algoritmo_melhorativo == 'opt2':
            print(int(two_opt(graph, route, x)))  # com matriz
        else:
            print("{} não é um argumento válido!\n".format(args.algoritmo_melhorativo))
    else:
        print("{} não é um argumento válido!\n".format(args.mode))

    # print("--- %s  ---" % (time.time() - start_time))
    # print("{}".format('=' * 80))


