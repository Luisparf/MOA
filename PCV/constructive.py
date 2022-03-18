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

def nodesDistances(nodes): # armazena todas as distâncias  nó X nó
    distances = {}
    for i in range(1, len(nodes)):
        try:
            distances[i]
        except:
            distances[i] = {}

        distances[i][i] = 0.0
        for a in range(i+1, len(nodes)):            
            try:
                distances[a]
            except:
                distances[a] = {}

            
            x0 = nodes[i]['x']
            y0 = nodes[i]['y']
            
            x1 = nodes[a]['x']
            y1 = nodes[a]['y']
            

            calculatedDist = int(dist([x0, y0], [x1, y1])) # Só considerando parte inteira
            #calculatedDist = dist([x0, y0], [x1, y1]) # Considerando ponto flutuante

            distances[i][a] = calculatedDist
            distances[a][i] = calculatedDist

    return distances

###########################################################################################

def matrizConstrutive(nodes, distances):
    selected = randint(1, localLen(nodes)-1)
    first = selected

    walkWeight = 0
    walkedPath = []
    walkedPath.append(nodes[selected])

    while True:
        # Valor da distância entre nó atual e menor vizinho
        menor = float('inf')
        
        # Indice do menor vizinho encontrado
        menorIndex = -1
        
        # Conteiro para verificar se todos os vizinho já foram explorados 
        endCounter = 0
        for i in range(1, localLen(nodes)):
            #print(selected, i)

            if (i == selected) or (nodes[i]['used']):
                endCounter += 1
                continue

            if distances[selected][i] < menor:
                menor = distances[selected][i]
                menorIndex = i
        
        if endCounter == (localLen(nodes) - 2):
            walkedPath.append(first)
            break

        walkWeight += menor
        walkedPath.append(menorIndex)
        nodes[menorIndex]['used'] = True
        selected = menorIndex

    
    # print(walkedPath)

    return walkWeight

###########################################################################################

