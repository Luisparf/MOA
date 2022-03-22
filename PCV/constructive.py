# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém os algoritmos construtivos para o PCV                  #                          
#                                                                                         #      
###########################################################################################

from math import dist
from random import randint
from functools import reduce

# Uma cópia local de funções como essa reduz o tempo de execução
localLen = len


def getAllDistances(graph): # armazena todas as distâncias  nó X nó
    allDistances = {}
    for i in range(1, len(graph)):
        try:
            allDistances[i]
        except:
            allDistances[i] = {}

        allDistances[i][i] = 0.0
        for a in range(i+1, len(graph)):            
            try:
                allDistances[a]
            except:
                allDistances[a] = {}

            
            x0 = graph[i]['x']
            y0 = graph[i]['y']
            
            x1 = graph[a]['x']
            y1 = graph[a]['y']
            

            calculatedDist = int(dist([x0, y0], [x1, y1])) # Só considerando parte inteira
            #calculatedDist = dist([x0, y0], [x1, y1]) # Considerando ponto flutuante

            allDistances[i][a] = calculatedDist
            allDistances[a][i] = calculatedDist

    return allDistances

###########################################################################################

def matrizConstrutive(graph, allDistances):
    selected = randint(1, localLen(graph)-1)
    first = selected

    walkWeight = 0
    walkedPath = []
    walkedPath.append(graph[selected])

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
            walkedPath.append(first)
            break

        walkWeight += menor
        walkedPath.append(menorIndex)
        graph[menorIndex]['used'] = True
        selected = menorIndex

    
    # print(walkedPath)

    return walkWeight

###########################################################################################

def printGraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))
   
############################################################################################

"""
def get_key(allDistances,val):
    
    for key, value in allDistances.items():
        if val == value:
             return key
 
    return "key doesn't exist"

############################################################################################

def findMaxDistance(graph, allDistances, i):
    
    greaterDistance = 0
    for j in range(1, localLen(graph)):
        if allDistances[i][j] > greaterDistance and graph[j]['used'] == False:
            greaterDistance = allDistances[i][j]
            greaterIndex = j

    return greaterIndex
   
    # print("All distances from {}: {}".format(i,allDistances[i]))


############################################################################################

def findEdge(c, cycle, k): # c = cost or distance
    
    minimum = float('inf')
    for i in range(1,localLen(cycle)):
        if c[i][k] + c[k][i+1] - c[i][i+1] < minimum:
            minimum = c[i][k] + c[k][i+1] - c[i][i+1]
            chosenEdge = i

    return chosenEdge

############################################################################################
"""

def insertMoreDistant(graph, allDistances): 
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
    cycle = ['',1, 2, 3] # no caso, os 3 primeiros vértices, '' no primeiro elemento apenas para ciclo[i] = i
    for x in range(1,localLen(cycle)):
        graph[x]['used'] = True

    while True:

        # a) Encontrar um vértice k não pertencente ao ciclo, mais distante de qualquer vértice do ciclo
        sizeCycle = localLen(cycle)
        i = cycle[sizeCycle-1] # no caso, pega o ultimo inseridos ***
        greaterDistance = 0
        for j in range(1, localLen(graph)):
            if allDistances[i][j] > greaterDistance and graph[j]['used'] == False:
                greaterDistance = allDistances[i][j]
                k = j


        # b) Encontrar uma aresta (i,j) do ciclo tal que: (Ci,k + Ck,j - Ci,j) seja mínimo.
        
        minimum = float('inf')
        for i in range(1,sizeCycle):
            if allDistances[i][k] + allDistances[k][i+1] - allDistances[i][i+1] < minimum : 
                minimum = allDistances[i][k] + allDistances[k][i+1] - allDistances[i][i+1]
                chosenEdge = i
        """
        ***
        # compara primeiro e ultimo elemento do ciclo para de fato considerar a lista(grafo) como um ciclo
        if allDistances[1][k] + allDistances[k][sizeCycle] - allDistances[1][sizeCycle] < minimum: 
            minimum = allDistances[1][k] + allDistances[k][sizeCycle] - allDistances[1][sizeCycle]
            chosenEdge = 1
            """

        i = chosenEdge
        # print("(i,j) = ({},{})".format(i, i+1))

        # c) Inserir o vértice k entre (i , i+1 ). Se todos os vértices já foram inseridos, pare, caso contrário,voltar ao passo “b”. <- "a"
        cycle.insert(i,k)
        graph[k]['used'] = True

        if sizeCycle == localLen(graph)-1:
            break

    del(cycle[0])

    walkWeight = 0
    for i in range(sizeCycle-1):
        walkWeight += allDistances[cycle[i]][cycle[i+1]]

    print(cycle)
    return walkWeight
    


    

    




   