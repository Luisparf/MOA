# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém os algoritmos construtivos para o PCV                  #                          
#                                                                                         #      
###########################################################################################

from math import dist

# Uma cópia local de funções como essa reduz o tempo de execução
from improvement import sumdistance

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
            disti = localDist([graph[selected]['x'], graph[selected]['y']], [graph[i]['x'], graph[i]['y']])
            if disti < menor:
                menor = disti
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

def insertdist(graph):
    route = [1, 2, 3]
    sizegraph = localLen(graph)
    for i in range(1, 4):
        graph[i]['used'] = True

    while localLen(route) < sizegraph - 1:
        maior = 0
        k = 1
        selected_i = 1
        for i in range(localLen(route) - 1):
            for j in range(i + 1, sizegraph ):
                disti = localDist([graph[route[i]]['x'], graph[route[i]]['y']], [graph[j]['x'], graph[j]['y']])
                if graph[j]['used'] is False and disti > maior:
                    k = j
                    maior = disti

        minimum = float('inf')
        for i in range(localLen(route) - 2):
            # print("{},{}({}) = C{},{} + C{},{} - C{},{} = {}".format(i, i + 1, k, i, k, k, i + 1, i, i + 1,all_dist[i][k] + all_dist[k][i + 1] - all_dist[i][ i + 1]))
            # all_dist[route[i]][k] + all_dist[k][route[i + 1]] - all_dist[route[i]][route[i + 1]]
            dista = int(localDist([graph[route[i]]['x'], graph[route[i]]['y']], [graph[k]['x'], graph[k]['y']]) +
                        localDist([graph[route[i + 1]]['x'], graph[route[i + 1]]['y']],
                                  [graph[k]['x'], graph[k]['y']]) -
                        localDist([graph[route[i]]['x'], graph[route[i]]['y']],
                                  [graph[route[i + 1]]['x'], graph[route[i + 1]]['y']]))
            if dista < minimum:
                minimum = dista
                selected_i = route[i]
        # print(route)
        # print()
        route.insert(selected_i, k)
        graph[k]['used'] = True

    route.append(route[0])
    # print(sumdistance_matrix(all_dist, route))
    # print(route)
    return route


###########################################################################################
def insertcheap(graph):
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
                disti = int(localDist([graph[route[i]]['x'], graph[route[i]]['y']], [graph[k]['x'], graph[k]['y']]) +
                            localDist([graph[route[i + 1]]['x'], graph[route[i + 1]]['y']],
                                      [graph[k]['x'], graph[k]['y']]) -
                            localDist([graph[route[i]]['x'], graph[route[i]]['y']],
                                      [graph[route[i + 1]]['x'], graph[route[i + 1]]['y']]))
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
