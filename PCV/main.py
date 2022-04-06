# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive_matrix import nearestneighbour_matrix, insertdist_matrix, getalldistances, insertcheap_matrix
from constructive import nearestneighbour, insertdist, insertcheap
from improvement_matrix import two_opt_matrix, sumdistance_matrix
from improvement import two_opt, sumdistance
from aux import printgraph, plot_graf
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
        print("### Executando com matriz de distâncias...")
        all_dist = getalldistances(graph)  # matriz de distâncias

        ### Heurística construtiva Inserção do mais distante
        if args.algoritmo_construtivo == 'id':
            x = 0
            route = insertdist_matrix(graph, all_dist)  # usando matriz de distâncias
            name = 'Inserção do mais distante'
            print(f'### Heurística construtiva {name}')


        ### Heurística construtiva Vizinho mais próximo
        elif args.algoritmo_construtivo == 'vp':
            x = 1
            route = nearestneighbour_matrix(graph, all_dist)  # usando matriz de distâncias
            name = 'Vizinho mais próximo'
            print(f'### Heurística construtiva {name}')

        ### Heurística construtiva Inserção mais barata
        elif args.algoritmo_construtivo == 'ic':
            x = 0
            route = insertcheap_matrix(graph, all_dist)  # usando matriz de distâncias
            name = 'Inserção mais barata'
            print(f'### Heurística construtiva {name}')

        else:
            print("{} não é um argumento válido!\n".format(args.algoritmo_construtivo))
            exit(0)

        ### Heurística melhorativa 2-opt
        if args.algoritmo_melhorativo == 'opt2':
            cost, plt_counters, plt_opts = two_opt_matrix(all_dist, route, x)
            print(f'Custo = {cost}')
            plot_graf(plt_opts, plt_counters, name)

        ### Sem Heurística melhorativa
        elif args.algoritmo_melhorativo == 'none':
            print(int(sumdistance_matrix(all_dist, route)))
        else:
            print("{} não é um argumento válido!\n".format(args.algoritmo_melhorativo))

    ### Não utiliza matriz de distâncias
    elif args.mode == 'n':
        print("### Executando sem matriz de distâncias...")

        ### Heurística construtiva Vizinho mais próximo
        if args.algoritmo_construtivo == 'vp':
            x = 1
            route = nearestneighbour(graph)
            name = 'Vizinho mais próximo'
            print(f'### Heurística construtiva {name}')

        ### Heurística construtiva Inserção do mais distante
        elif args.algoritmo_construtivo == 'id':
            x = 0
            route = insertdist(graph)
            name = 'Inserção do mais distante'
            print(f'### Heurística construtiva {name}')

        ### Heurística construtiva Inserção do mais barato
        elif args.algoritmo_construtivo == 'ic':
            x = 0
            route = insertcheap(graph)
            name = 'Inserção mais barata'
            print(f'### Heurística construtiva {name}')

        else:
            print("{} não é um argumento válido!\n".format(args.algoritmo_construtivo))
            exit(0)

        ### Heurística melhorativa 2-opt
        if args.algoritmo_melhorativo == 'opt2':
            print("### Heurística melhorativa 2opt")
            cost, plt_counters, plt_opts = two_opt(graph, route, x)
            print(int(cost))
            plot_graf(plt_opts, plt_counters, name)


        elif args.algoritmo_melhorativo == 'none':
            sumdistance(graph, route)
        else:
            print("{} não é um argumento válido!\n".format(args.algoritmo_melhorativo))
    else:
        print("{} não é um argumento válido!\n".format(args.mode))

    # print("--- %s  ---" % (time.time() - start_time))
    # print("{}".format('=' * 80))
