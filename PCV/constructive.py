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
localMax = max
localMin = min

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

def get_key(allDistances,val):
    """
    função que recupera o indide do vértice com a maior distancia para o vértice selecionado
    """
    for key, value in allDistances.items():
        if val == value:
             return key
 
    return "key doesn't exist"

############################################################################################

def printGraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))
   
############################################################################################

def findMaxDistance(graph, allDistances, i):
    """
    a) Encontrar um vértice vk não pertencente ao ciclo, mais distante de qualquer vértice do ciclo
    """
    greaterDistance = 0
    for j in range(1, localLen(graph)):
        if allDistances[i][j] > greaterDistance and graph[j]['used'] == False:
            greaterDistance = allDistances[i][j]
            greaterIndex = j

    return greaterIndex
   
    # print("All distances from {}: {}".format(i,allDistances[i]))


############################################################################################

def findEdge(c, cycle, k): # c = cost or distance
    """
    b) Encontrar uma aresta (i,j) do ciclo tal que: (Ci,k + Ck,j - Ci,j) seja mínimo.
    """
    minimum = float('inf')
    for i in range(1,localLen(cycle)):
        if c[i][k] + c[k][i+1] - c[i][i+1] < minimum:
            minimum = c[i][k] + c[k][i+1] - c[i][i+1]
            chosenEdge = i

    return chosenEdge

############################################################################################

def insertMoreDistant(graph, allDistances):

    # Iniciar com um ciclo [v1 , v2 , v3] com 3 vértices.
    cycle = [1, 2, 3]
    for x in cycle:
        graph[x]['used'] = True

    # a) Encontrar um vértice vk não pertencente ao ciclo, mais distante de qualquer vértice do ciclo
    k = findMaxDistance(graph, allDistances, 3)
    

    # b) Encontrar uma aresta (i,j) do ciclo tal que: (Ci,k + Ck,j - Ci,j) seja mínimo.
    i = findEdge(allDistances, cycle, k)
    print("(i,j) = ({},{})".format(i, i+1))

    # c) Inserir o vértice vk entre (vi , vi+1 ). Se todos os vértices já foram inseridos, pare, 
    # caso contrário,voltar ao passo “b”.

    




   