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

def findMax(graph, allDistances, subRote, i):
    greaterDistance = 0
    for j in range(1, localLen(graph)):
        if allDistances[i][j] > greaterDistance and graph[j]['used'] == False:
            greaterDistance = allDistances[i][j]
            greaterIndex = j

    graph[greaterIndex]['used'] = True
    subRote.append(greaterIndex)

    print("i = {} , j  = {} , Cij = {} ".format(i, greaterIndex, greaterDistance))
    print('Subrote = {}'.format(subRote))
    print()
    # print("All distances from {}: {}".format(i,allDistances[i]))


############################################################################################

def insertMoreDistant(graph, allDistances):

    """
    Algorithm source:

    XXIV Encontro Nac. de Eng. de Produção - Florianópolis, SC, Brasil, 03 a 05 de nov de 2004

    Análise Comparativa de Algoritmos Heurísticos para Resolução do
    Problema do Caixeiro-Viajante em Grafos Não Clusterizados

    link:http://abepro.org.br/biblioteca/ENEGEP2004_Enegep0601_0567.pdf

    """
    

    subRote = []
    
    # 1. Comece com um subgrafo composto apenas pelo i-ésimo vértice;
    i = randint(1, localLen(graph)-1)
    graph[i]['used'] = True
    subRote.append(i)

    # 2. Encontre um vértice j ≠ i tal que cij seja máximo e forme a subrota i − j − i ;
    # distance = localMax(allDistances[i].values())
    findMax(graph,allDistances,subRote,i)


    # 3. Dada uma subrota, encontre um vértice j que não pertence a esta subrota, 
    # mas que seja o mais distante de todos os vértices pertencentes à mesma;
    i = randint(1, localLen(subRote)-1) # escolhe um vértice da subrota para escolher o vértice mais distante
    i = subRote[i]
    print('Chosen vertex to find max distance: {}'.format(i))

    findMax(graph,allDistances,subRote, i)

   
    # print("All distances from {}: {}".format(i,allDistances[i]))



   