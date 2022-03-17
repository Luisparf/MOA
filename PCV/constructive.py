# -*- coding: utf-8 -*-
from math import dist
from random import randint

# Uma cópia local de funções como essa reduz o tempo de execução
localLen = len

def matrizConstrutive(nodes, distances):
    selected = randint(1, localLen(nodes)-1)
    first = selected

    walkWeigh = 0
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

        walkWeigh += menor
        walkedPath.append(menorIndex)
        nodes[menorIndex]['used'] = True
        selected = menorIndex

    return walkWeigh

