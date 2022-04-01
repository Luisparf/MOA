# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém os algoritmos construtivos para o PCV                  #                          
#                                                                                         #      
###########################################################################################

from math import dist
from random import randint

# Uma cópia local de funções como essa reduz o tempo de execução
localLen = len
localDist = dist


###########################################################################################

def nearestneighbour(graph):
    # selected = randint(1, localLen(graph)-1)
    selected = 1
    first = selected

    walkedPath = [selected]
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

            if localDist([graph[selected]['x'], graph[selected]['y']], [graph[i]['x'], graph[i]['y']]) < menor:
                menor = localDist([graph[selected]['x'], graph[selected]['y']], [graph[i]['x'], graph[i]['y']])
                menor_index = i

        if end_counter == (localLen(graph) - 1):
            walkedPath.append(first)
            break

        walkedPath.append(menor_index)
        graph[menor_index]['used'] = True
        selected = menor_index

    # print(walkedPath)

    return walkedPath


###########################################################################################

def insertprox(graph):
    route = [1, 2, 3]

    for i in range(1, 4):
        graph[i]['used'] = True

    while True:
        menor = float('inf')
        k = 1
        selected_i = 1
        for i in range(1, len(route)):
            for j in range(4, len(graph)):
                distj = localDist([graph[i]['x'], graph[i]['y']], [graph[j]['x'], graph[j]['x']])
                if distj < menor and graph[j]['used'] is False:
                    k = j
                    menor = distj

        minimum = float('inf')
        for i in range(1, len(route) + 1):
            # print("{},{}({}) = C{},{} + C{},{} - C{},{} = {}".format(i, i + 1, k, i, k, k, i + 1, i, i + 1,all_dist[i][k] + all_dist[k][i + 1] - all_dist[i][ i + 1]))
            disti = localDist([graph[i]['x'], graph[i]['y']], [graph[k]['x'], graph[k]['y']]) + \
                    localDist([graph[k]['x'], graph[k]['y']], [graph[i + 1]['x'], graph[i + 1]['y']]) - \
                    localDist([graph[i]['x'], graph[i]['y']], [graph[i + 1]['x'], graph[i + 1]['y']])
            if disti < minimum:
                minimum = disti
                selected_i = i

        route.insert(selected_i, k)
        graph[k]['used'] = True

        if localLen(route) == localLen(graph) - 1:
            break
    route.append(route[0])
    # print(sumdistance_matrix(all_dist, route))
    # print(route)
    return route

###########################################################################################
