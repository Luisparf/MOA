# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém o algoritmo genético para o PCV                        #                          
#                                                                                         #      
###########################################################################################

from math import dist, ceil, floor
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
            # walkedPath.append(first)
            break

        walkedPath.append(menor_index)
        graph[menor_index]['used'] = True
        selected = menor_index

    # print(f'\nwalkedPath = {walkedPath}')

    return walkedPath


###########################################################################################

def pmx(f1, f2):
    s1 = []  # filho 1
    s2 = []  # filho 2
    lista = []
    i = randint(1, localLen(f1) - 1)
    j = randint(i + 1, localLen(f2) - 1)

    s1[i:j] = f2[i:j]
    s2[i:j] = f1[i:j]

    for i in range(1, 3):
        lista.append(1)

    print(f'i:{i} j:{j}\n')
    print(f'Filho 1: {s1} - tamanho:{localLen(s1)}\n')
    print(f'Filho 2: {s2} - tamanho:{localLen(s2)}\n')


###########################################################################################

def cx(pais):
    filhos = [[0], [], []]

    for i in range(1, 3):
        filhos[i] = deepcopy(pais[(i % 2) + 1])
        index = 0

        while True:
            filhos[i][index] = pais[i][index]
            index = list.index(pais[(i % 2) + 1], filhos[i][index])
            if index != 0:
                break
    return filhos


###########################################################################################


def selection(graph, population, k, s):  # seleção por torneio
    selections = []
    pais = []
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

    pais.append(0)
    pais.append(selections[i1])
    pais.append(selections[i2])

    return pais


###########################################################################################

def mutation(mut, cromossomos, pop):
    swap_list = []
    mut = int(mut)
    mut_tax = floor((mut / 100) * localLen(cromossomos[1]))
    # print(f'mut_tax:{mut_tax}')

    for i in range(mut_tax):
        swap_list.append(randint(i, pop - 1))

    i = (randint(1, localLen(cromossomos[1]) - 1))
    j = (randint(i, localLen(cromossomos[1]) - 1))

    for index in swap_list:
        aux = cromossomos[index][j]
        cromossomos[index][j] = cromossomos[index][i]
        cromossomos[index][i] = aux

    return cromossomos


###########################################################################################


def genetic(graph, pop, mut, max_i, max_t, s):
    population = []
    k = 4

    if pop > localLen(graph) - 1:
        pop = localLen(graph)

        # gerar população inicial
    for i in range(1, pop):
        population.append(nearestneighbour(deepcopy(graph), i))

    for elemento in population:
        print(f'elemento:{elemento}')

    start_time = time.time()
    # while time.time() - start_time  <= max_t:

    ### Avaliação ###

    #### Seleção ###
    pais = selection(graph, population, k, s)
    print(f'\nSeleção:\n')
    for pai in pais:
        print(f'{pai}\n')

    ### Cruzamento ###
    print(f'\nCruzamento:\n')
    filhos = cx(pais)
    for filho in filhos:
        print(f'{filho} - tamanho:{localLen(filho)}\n')

    ### Mutação ###
    print(f'\nMutação:\n')
    cromossomos = mutation(mut, population, pop)
    for cromossomo in cromossomos:
        print(f'{cromossomo} - tamanho:{localLen(cromossomo)}\n')

    ### Busca Local ###


    ### atualização ###
