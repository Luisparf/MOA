# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém o algoritmo genético para o PCV                        #                          
#                                                                                         #      
###########################################################################################

from math import dist
from copy import deepcopy
from random import seed, randint
import time

# Uma cópia local de funções como essa reduz o tempo de execução

localLen = len
localDist = dist


def fitness(graph, route):
    sizeroute = localLen(route) - 1
    walk_weight = 0
    for i in range(sizeroute):
        xi = graph[route[i]]['x']
        yi = graph[route[i]]['y']

        x_p = graph[route[i + 1]]['x']
        y_p = graph[route[i + 1]]['y']

        walk_weight += int(localDist([xi, yi], [x_p, y_p]))

    return walk_weight


###########################################################################################

def nearestneighbour(graph, j):
    # selected = randint(1, localLen(graph)-1)
    selected = j
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
            #walkedPath.append(first)
            break

        walkedPath.append(menor_index)
        graph[menor_index]['used'] = True
        selected = menor_index

    # print(f'\nwalkedPath = {walkedPath}')

    return walkedPath


###########################################################################################

def selection(graph, population,k, s):

    selections = []
    costs = []
    seed(s)
    i1 = 1
    i2 = 2


    # Seleciona k individuos aleatoriamente 
    for i in range(k):
        selections.append(population[randint(1, localLen(population) - 1)])



    # Escolhe os dois mais adaptados (2 melhores fitness)
    minor = float('inf')
    for i in range(k): 
        fit = fitness(graph, selections[i]) 
        if fit < minor:
            minor = fitness(graph, selections[i])
            i1 = i
        
    minor = float('inf')
    for i in range(k):
        if fitness(graph, selections[i]) < minor and i != i1:
            minor = fitness(graph, selections[i])
            i2 = i



    cromossomo1 = selections[i1]
    cromossomo2 = selections[i2]
    
    print(f'Pai1:{cromossomo1} - tamanho:{localLen(cromossomo1)}\n')
    print(f'Pai2:{cromossomo2} - tamanho:{localLen(cromossomo2)}\n')

    return cromossomo1, cromossomo2


###########################################################################################

def pmx(f1, f2):

    s1 = [] # filho 1
    s2 = [] # filho 2

    i = randint(1, localLen(f1) - 1)
    j = randint(1, localLen(f2) - 1)

    s1[i:j] = f2[i:j]
    s2[i:j] = f1[i:j]

    print(f'i:{i} j:{j}\n')
    print(f'Filho 1: {s1} - tamanho:{localLen(s1)}\n')
    print(f'Filho 2: {s2} - tamanho:{localLen(s2)}\n')

###########################################################################################


def genetic(graph, pop, mut, max_i, max_t, s):

    population = []
    k = 4

    if pop > localLen(graph)-1:
        pop = localLen(graph) 

    # gerar população inicial 
    for i in range(1, pop ):
        population.append(nearestneighbour(deepcopy(graph),i))

    start_time = time.time()
    # while start_time - time.time() <= max_t:

    ### Avaliação ###


    #### Seleção ###
    f1, f2 = selection(graph, population, k, s) # pai1, pai2

    ### Cruzamento ###

    pmx(f1, f2)






