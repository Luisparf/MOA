# -*- coding: utf-8 -*-
############################################################################################
#                                                                                          #
# Módulo que contém os algoritmos construtivos para o PCV utilizando matriz das distancias #
#                                                                                          #
############################################################################################

from math import dist
from improvement_matrix import sumdistance_matrix
import matplotlib.pyplot as plt
import numpy as np

# Uma cópia local de funções como essa reduz o tempo de execução
localLen = len
localDist = dist


########################################################################################################################
def getalldistances(graph):  # armazena todas as distâncias  nó X nó
    all_distances = {}
    for i in range(1, localLen(graph)):

        if all_distances.get(i) is None:
            all_distances[i] = {}

        all_distances[i][i] = 0.0
        x0 = graph[i]['x']
        y0 = graph[i]['y']
        for a in range(i + 1, localLen(graph)):
            # print(i, a)

            if all_distances.get(a) is None:
                all_distances[a] = {}

            x1 = graph[a]['x']
            y1 = graph[a]['y']

            calculated_dist = int(localDist([x0, y0], [x1, y1]))  # Só considerando parte inteira
            # calculatedDist = dist([x0, y0], [x1, y1]) # Considerando ponto flutuante

            all_distances[i][a] = calculated_dist
            all_distances[a][i] = calculated_dist
    # print(allDistances)
    return all_distances


########################################################################################################################
def insertdist_matrix(graph, all_dist):  # Heurística construtiva Inserção do mais distante

    """
      More distant insertion heuristic.
      Algorithm source:
      Grafos Hamiltonianos e o Problema do Caixeiro Viajante
              Prof. Ademir Constantino
              Departamento de Informática
              Universidade Estadual de Maringá
      link: https://malbarbo.pro.br/arquivos/2012/1747/problema-do-caixeiro-viajante.pdf
      """
    route = [1, 2, 3]
    sizegraph = localLen(graph)

    opt_value = 0
    opt_values = []
    counter_values = []

    for i in range(1, 4):
        graph[i]['used'] = True

    while localLen(route) < sizegraph - 1:
        maior = 0
        k = 1
        selected_i = 1
        for i in range(localLen(route) - 1):
            for j in range(i + 1, sizegraph):
                if graph[j]['used'] is False and all_dist[route[i]][j] > maior:
                    k = j
                    maior = all_dist[route[i]][j]

        minimum = float('inf')
        for i in range(localLen(route) - 1):
            # print("{},{}({}) = C{},{} + C{},{} - C{},{} = {}".format(i, i + 1, k, i, k, k, i + 1, i, i + 1,all_dist[i][k] + all_dist[k][i + 1] - all_dist[i][ i + 1]))
            disti = all_dist[route[i]][k] + all_dist[k][route[i + 1]] - all_dist[route[i]][route[i + 1]]
            if disti < minimum:
                minimum = disti
                selected_i = route[i]
        # print(route)
        # print()
        route.insert(selected_i - 1, k)
        graph[k]['used'] = True

    route.append(route[0])
    # print(route)
    return route


########################################################################################################################


def nearestneighbour_matrix(graph, all_distances):  # Heurística construtiva vizinho mais próximo
    # selected = randint(1, localLen(graph)-1)
    selected = 1
    first = selected
    walked_path = [selected]
    graph[selected]['used'] = True

    while True:
        # Valor da distância entre nó atual e menor vizinho
        menor = float('inf')

        # Indice do menor vizinho encontrado
        menor_index = -1

        # Conteiro para verificar se todos os vizinho já foram explorados
        end_counter = 0
        for i in range(1, localLen(graph)):
            # print("selected = {} i = {}".format(selected, i))

            if (i == selected) or (graph[i]['used']):
                end_counter += 1
                continue

            if all_distances[selected][i] < menor:
                menor = all_distances[selected][i]
                menor_index = i

        if end_counter == (localLen(graph) - 1):
            # penultimo = localLen(walkedPath) - 1
            # walkWeight += allDistances[walkedPath[penultimo]][first]
            walked_path.append(first)
            break

        # walkWeight += menor
        walked_path.append(menor_index)
        graph[menor_index]['used'] = True
        selected = menor_index


    # print(walkedPath)
    # print('sum menor {}'.format(sum_menor))
    return walked_path


########################################################################################################################

def insertcheap_matrix(graph, all_dist):
    sizegraph = localLen(graph)
    route = [1, 2, 3]
    for i in range(1, 4):
        graph[i]['used'] = True

    while True:
        k = 1
        minimum = float('inf')
        selected_i = 1
        for i in range(localLen(route) - 1):
            for j in range(i + 1, sizegraph):
                disti = all_dist[route[i]][j] + all_dist[j][route[i + 1]] - all_dist[route[i]][route[i + 1]]
                if disti < minimum and graph[j]['used'] is False:
                    minimum = disti
                    selected_i = route[i]
                    k = j
                # print(route)
                # print()
        route.insert(selected_i - 1, k)
        graph[k]['used'] = True
        if localLen(route) == localLen(graph) - 1:
            break
    route.append(route[0])
    # print(sumdistance_matrix(all_dist, route))
    # print(route)
    return route
