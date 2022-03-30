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


def getAllDistances(graph):  # armazena todas as distâncias  nó X nó
    allDistances = {}
    for i in range(1, localLen(graph)):
        try:
            allDistances[i]
        except:
            allDistances[i] = {}

        allDistances[i][i] = 0.0
        x0 = graph[i]['x']
        y0 = graph[i]['y']
        for a in range(i + 1, len(graph)):

            try:
                allDistances[a]

            except:
                allDistances[a] = {}

            x1 = graph[a]['x']
            y1 = graph[a]['y']

            calculatedDist = int(dist([x0, y0], [x1, y1]))  # Só considerando parte inteira
            # calculatedDist = dist([x0, y0], [x1, y1]) # Considerando ponto flutuante

            allDistances[i][a] = calculatedDist
            allDistances[a][i] = calculatedDist

    return allDistances


###########################################################################################

def nearestNeighbour(graph, allDistances):

    selected = randint(1, localLen(graph) - 1)
    first = selected

    walkWeight = 0
    walkedPath = []
    walkedPath.append(selected)
    graph[selected]['used'] = True

    while True:
        # Valor da distância entre nó atual e menor vizinho
        menor = float('inf')

        # Indice do menor vizinho encontrado
        menorIndex = -1

        # Conteiro para verificar se todos os vizinho já foram explorados 
        endCounter = 0
        for i in range(1, localLen(graph)):
            # print("selected = {} i = {}".format(selected, i))

            if (i == selected) or (graph[i]['used']):
                endCounter += 1
                continue

            if allDistances[selected][i] < menor:
                menor = allDistances[selected][i]
                menorIndex = i

        if endCounter == (localLen(graph) - 2):
            penultimo = localLen(walkedPath) - 1
            walkWeight += allDistances[walkedPath[penultimo]][first]
            walkedPath.append(first)
            break

        walkWeight += menor
        walkedPath.append(menorIndex)
        graph[menorIndex]['used'] = True
        selected = menorIndex

    print(walkedPath)

    return walkWeight


###########################################################################################

def printgraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))


############################################################################################


def insertmoredistant(graph):
    """

    More distant insertion heuristic.

    Algorithm source:

    Grafos Hamiltonianos e o Problema do Caixeiro Viajante
            Prof. Ademir Constantino
            Departamento de Informática
            Universidade Estadual de Maringá

    link: https://malbarbo.pro.br/arquivos/2012/1747/problema-do-caixeiro-viajante.pdf

    """

    # Iniciar com um ciclo [v1 , v2 , v3] com 3 vértices.
    route = ['', 1, 2, 3]  # no caso, os 3 primeiros vértices, '' na primeira posição apenas para ciclo[i] = i
    for x in range(1, localLen(route)):
        graph[x]['used'] = True

    while True:

        # a) Encontrar um vértice k não pertencente ao ciclo, mais distante de qualquer vértice do ciclo
        sizeroute = localLen(route)
        i = route[sizeroute - 1]  # no caso, pega o ultimo inserido ***
        chosen_edge = i

        xi = graph[i]['x']
        yi = graph[i]['y']

        greater_distance = 0
        for j in range(1, localLen(graph)):
            x1 = graph[j]['x']
            y1 = graph[j]['y']

            if dist([xi, yi], [x1, y1]) > greater_distance and graph[j]['used'] is False:
                greater_distance = dist([xi, yi], [x1, y1])
                k = j

        # b) Encontrar uma aresta (i,j) do ciclo tal que: (Ci,k + Ck,i+1 - Ci,1+1) seja mínimo.
        """
        minimum = alldist[1][k] + alldist[k][2] - alldist[1][2]
        for i in range(2, sizeroute - 1):
            if alldist[i][k] + alldist[k][i + 1] - alldist[i][i + 1] < minimum:
                minimum = alldist[i][k] + alldist[k][i + 1] - alldist[i][i + 1]
                chosen_edge = i
        """

        x1 = graph[1]['x']
        y1 = graph[1]['y']

        x2 = graph[2]['x']
        y2 = graph[2]['y']

        xk = graph[k]['x']
        yk = graph[k]['y']
        minimum = dist([x1, y1], [xk, yk]) + dist([xk, yk], [x2, y2]) - dist([x1, y1], [x2, y2])
        for i in range(2, sizeroute - 1):
            xi = graph[i]['x']
            yi = graph[i]['y']

            x_p = graph[i+1]['x']
            y_p = graph[i+1]['y']

            if dist([xi, yi], [xk, yk]) + dist([xk, yk], [x_p, y_p]) - dist([xi, yi], [x_p, y_p]) < minimum:
                minimum = dist([xi, yi], [xk, yk]) + dist([xk, yk], [x_p, y_p]) - dist([xi, yi], [x_p, y_p])
                chosen_edge = i

        i = chosen_edge

        # c) Inserir o vértice k entre (i , i+1 ). Se todos os vértices já foram inseridos, pare, caso contrário,voltar ao passo “b”. <- "a"
        route.insert(i, k)
        graph[k]['used'] = True

        if sizeroute == localLen(graph) - 1 :
            break

    route = [value for value in route if value != '']

    route.append(route[0])
    # print(route)
    return route
