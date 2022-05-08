# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém o algoritmo genético para o PCV                        #                          
#                                                                                         #      
###########################################################################################

from math import dist, floor
from copy import deepcopy
from random import seed, randint
from aux import plot_graf
import time
import sys

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

def search_worst_fit(population, graph):
    worst = 0
    index = 0
    for i in range(localLen(population) - 1):
        atual = fitness(graph, population[i])
        if atual > worst:
            worst = atual
            index = i
    return worst, index


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

def two_opt(graph, route, x):
    """
    2-opt heuristic.
    Algorithm pseudo-code:
    2optSwap(route, i, k) {
         1. take route[1] to route[i-1] and add them in order to new_route
         2. take route[i] to route[k] and add them in reverse order to new_route
         3. take route[k+1] to end and add them in order to new_route
         return new_route;
    }
    repeat until no improvement is made {
       start_again:
       best_distance = calculateTotalDistance(existing_route)
       for (i = 0; i < number of nodes eligible to be swapped - 1; i++) {
           for (k = i + 1; k < number of nodes eligible to be swapped; k++) {
               new_route = 2optSwap(existing_route, i, k)
               new_distance = calculateTotalDistance(new_route)
               if (new_distance < best_distance) {
                   existing_route = new_route
                   goto start_again
                }
            }
        }
     }
    link: https://en.wikipedia.org/wiki/2-opt
    """

    size_route = localLen(route)
    best_route = route
    improved = True

    plt_counter = -1
    plt_counters = []
    plt_opts = []

    counter = 0
    while improved:
        should_break = False

        improved = False
        best_distance = fitness(graph, route)
        for i in range(1, size_route - 2):
            if should_break:
                break
            for j in range(i + 1, size_route):
                # newRoute = two_opt_swap(route.copy(), i, k)
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # o mesmo que two_opt_swap
                # print(newRoute)
                new_distance = fitness(graph, new_route)

                ### trecho para matplot ###
                plt_opts.append(best_distance)
                plt_counter += 1
                plt_counters.append(plt_counter)
                #################

                if new_distance < best_distance:
                    best_route = new_route
                    improved = True
                    best_distance = new_distance
                    counter += 1

                if x == 1 and counter >= 1:  # critério de parada, first improvement
                    should_break = True
                    improved = False
                    break

            route = best_route
            if should_break:
                break
            # print()
    # print(counter)
    # print(route)
    return route  # , plt_counters, plt_opts


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
            # print(f'i:{i} index:{index}\n')
            filhos[i][index] = pais[i][index]
            # print(f'filhos[{i}][{index}]:{filhos[i][index]}')
            # print(f'\nvalue error: {list.index(pais[(i % 2) + 1], filhos[i][index])}\n')
            try:
                index = list.index(pais[(i % 2) + 1], filhos[i][index])
            except ValueError:
                set_of_citys = set(pais[(i % 2) + 1])
                # print(f'set_of_citys:{set_of_citys}')
                pais[(i % 2) + 1] = list(set_of_citys)
                pais[(i % 2) + 1].append(filhos[i][index])
                index = list.index(pais[(i % 2) + 1], filhos[i][index])
                break
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

def mutation(mut, population, pop):
    mut = int(mut)
    mut_tax = floor((mut / 100) * localLen(population[1]))
    # print(f'mut:{mut} mut_tax:{mut_tax}')

    i = (randint(1, localLen(population[1]) - 1))
    j = (randint(i, localLen(population[1]) - 1))

    for i in range(mut_tax):
        index = (randint(0, pop - 2))
        aux = population[index][j]
        population[index][j] = population[index][i]
        population[index][i] = aux

    return population


###########################################################################################

def steady_stated(graph, population, filhos):
    worst, worst_index = search_worst_fit(population, graph)

    menor = filhos[1]
    for i in range(2, localLen(filhos)):
        if fitness(graph, filhos[i]) < fitness(graph, menor):
            menor = filhos[i]

    if fitness(graph, menor) < worst:
        population[worst_index] = menor

    return population


###########################################################################################

def genetic(graph, pop, mut, max_i, max_t, s):
    population = []
    busca = []
    plt_opts = []
    plt_counters = []

    k = 4
    it = 0

    if pop > localLen(graph) - 1:
        pop = localLen(graph)

    # gerar população inicial
    print(f'Gerando população inicial...\n')
    for i in range(1, pop):
        population.append(nearestneighbour(deepcopy(graph), i))

    # for elemento in population:
    #   print(f'elemento:{elemento}')

    start_time = time.time()
    exe_time = 0
    while (exe_time <= max_t) and (it <= max_i):

        ### Avaliação ###
        best_solution = fitness(graph, population[0])
        for i in range(1, localLen(population)):
            if fitness(graph, population[i]) < best_solution:
                best_solution = fitness(graph, population[i])
        plt_opts.append(best_solution)

        #### Seleção ###
        print(f'\nSeleção:[{it}]')
        pais = selection(graph, population, k, s)

        ### Cruzamento ###
        print(f'\nCruzamento:[{it}]')
        filhos = cx(pais)

        ### Mutação ###
        print(f'\nMutação:[{it}]')
        population = mutation(mut, population, pop)

        ### Busca Local ###
        print(f'\nBusca Local:[{it}]')
        for i in range(1, localLen(filhos)):
            busca.append(two_opt(graph, filhos[i], 1))

        ### atualização ###
        print(f'\nAtualização da população:[{it}]')
        population = steady_stated(graph, population, busca)

        it += 1
        exe_time = time.time() - start_time

    # for i in range(localLen(busca)-1):
    #     print(f'local s* in busca = {fitness(graph,busca[i])}')
    #
    # for i in range(localLen(population)-1):
    #     print(f'local s* in population = {fitness(graph,population[i])}')

    print(f'\nMelhor solução:{best_solution}\n')
    file_name = sys.argv[len(sys.argv) - 1]
    plt_counters = range(it)
    plot_graf(plt_opts, plt_counters, file_name, round(exe_time, 2), best_solution)
