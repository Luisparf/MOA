# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém o algoritmo genético para o PCV                        #                          
#                                                                                         #      
###########################################################################################
import random
from math import dist, ceil
from copy import deepcopy
from random import seed, randint
import time


# Uma cópia local de funções como essa reduz o tempo de execução

localLen = len
localDist = dist
localDeepcopy = deepcopy


def fitness(graph, route):
    """
    Função objetivo do TSP
    :param graph: grafo completo
    :param route: rota atual no grafo
    :return: fitness(route)
    """
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
    """
    Busca pela rota com pior fitness na população
    :param population: população do algoritmo genético
    :param graph: grafo completo de entrada
    :return: pior fitness da população e seu indice
    """
    worst = 0
    index = 0
    for i in range(localLen(population) - 1):
        atual = fitness(graph, population[i])
        if atual > worst:
            worst = atual
            index = i
    return worst, index


###########################################################################################

def nearest_neighbour(graph, j):
    """

    :param graph: Grafo completo de entrada
    :param j: vértice de inicio
    :return: Rota encontrada
    """
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

                if x == 1 and counter >= 1:  # first improvement
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


def pos(pais):
    """
    Operador de cruzamento Position based crossover
    :param pais:cromossomos pais
    :return:cromossomos filhos
    """
    positions = []
    filhos = [[0], [], []]
    li = range(1, localLen(pais[1]))
    positions.append(random.sample(li, 3))

    filhos[1] = localDeepcopy(pais[1])
    filhos[2] = localDeepcopy(pais[2])

    for i in positions[0]:
        i = int(i)
        filhos[1][i] = pais[2][i]
        filhos[1][pais[1].index(filhos[1][i])] = pais[1][i]
        filhos[2][i] = pais[1][i]
        filhos[2][pais[2].index(filhos[2][i])] = pais[2][i]

    return filhos


###########################################################################################

def cx(pais):
    """
    Operador de cruzamento Cycle crossover
    :param pais: Cromossomos pais
    :return: Cromossomos filhos
    """
    filhos = [[0], [], []]

    for i in range(1, 3):
        filhos[i] = pais[(i % 2) + 1]
        index = 0

        while True:
            # print(f'i:{i} index:{index}\n')
            filhos[i][index] = pais[i][index]
            index = pais[(i % 2) + 1].index(filhos[i][index])
            # print(f'repetidos:{list(duplicates(pais[(i % 2) + 1]))}')
            if index != 0 or pais[1][0] == pais[2][0]:
                break
    return filhos


###########################################################################################

def selection_by_tournament(graph, population, k):  # seleção por torneio
    """
    Faz a seleção por torneio dos cromossomos pais para o cruzamento
    :param graph: grafo de entrada
    :param population: população atual
    :param k:k elementos
    :return:cromossomos pais selecionados
    """
    selections = []
    pais = []
    # seed(s)
    i1 = 1
    i2 = 2

    # Seleciona k individuos aleatoriamente
    for i in range(k):
        # print(f'\nindividuo selecionado:{randint(1, localLen(population) - 1)}')
        selections.append(deepcopy(population[randint(1, localLen(population) - 1)]))

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
    pais.append(deepcopy(selections[i1]))
    pais.append(deepcopy(selections[i2]))

    return pais


###########################################################################################

def selection_by_fit(graph, population, index):
    """
    Faz a seleção elitizada dos cromossomos pais para o cruzamento
    :param graph: grafo de entrada
    :param population: população atual
    :param index:
    :return:
    """
    pais = []

    minor = float('inf')
    for i in range(localLen(population) - 1):
        if fitness(graph, population[i]) < minor and i != index:
            minor = fitness(graph, population[i])
            i2 = i

    pais.append(0)
    pais.append(population[index])
    pais.append(population[i2])
    return pais


###########################################################################################

def mutation(mut, population):
    """
    Faz a mutação da população
    :param mut: taxa de mutação
    :param population: população atual
    :return:
    """
    mut_tax = ceil((mut / 100) * localLen(population))
    # print(f'mut:{mut} mut_tax:{mut_tax} localLen(population):{localLen(population)}')

    i = (randint(1, localLen(population[1])))
    j = (randint(i, localLen(population[1])))

    # if localLen(population) < mut_tax:
    #     mut_tax = localLen(population)

    for k in range(mut_tax):
        index = (randint(1, localLen(population) - 1))
        aux = population[index][j]
        population[index][j] = population[index][i]
        population[index][i] = aux

    return population


###########################################################################################

def steady_stated(graph, population, filhos):
    """
    Faz a manutenção da população
    :param graph: grafo de entrada
    :param population: população atual
    :param filhos: cromossomos filhos
    :return: população atualizada
    """
    worst, worst_index = search_worst_fit(population, graph)

    menor = filhos[0]
    for i in range(1, localLen(filhos)):
        if fitness(graph, filhos[i]) < fitness(graph, menor):
            menor = filhos[i]

    if fitness(graph, menor) < worst:
        population[worst_index] = menor

    return population


###########################################################################################

def genetic(graph, pop, mut, max_i, max_t, s, cross_operator):
    """
    Algoritmo Genético
    :param graph: grafo de entrada
    :param pop: tamanho da população
    :param mut: tava de mutação
    :param max_i: número máximo de iterações
    :param max_t: tempo máximo em minutos
    :param s: semente aleatória
    :param cross_operator: operador de cruzamento (cx ou pos)
    :return: geração, fitness, s*, tempo de execução
    """
    population = []
    plt_opts = []
    plt_counters = []
    k = 4
    it = 0

    if pop > localLen(graph) - 1:
        pop = localLen(graph)

    # gerar população inicial
    print(f'Gerando população inicial...\n')
    for i in range(1, pop):
        # population.append(nearestneighbour(deepcopy(graph), i)) # traz soluções boas mas sem variabilidade
        # população gerada de forma aletória:
        li = range(1, localLen(graph))
        population.append(random.sample(li, localLen(li)))

    start_time = time.time()
    exe_time = 0
    while (exe_time <= max_t) and (it <= max_i):

        random.seed(s)

        ### Avaliação ###
        best_solution = float('inf')
        for i in range(localLen(population) - 1):
            if fitness(graph, population[i]) < best_solution:
                best_solution = fitness(graph, population[i])

        plt_opts.append(best_solution)
        plt_counters.append(it)

        #### Seleção ###
        print(f'\nSeleção:[{it}]')
        pais = selection_by_tournament(graph, localDeepcopy(population), k)  # seleção por torneio
        # pais = selection_by_fit(graph, population.copy(), index)

        ### Cruzamento ###
        print(f'\nCruzamento:[{it}]')
        if cross_operator == 'cx':
            filhos = cx(pais)
        else:
            filhos = pos(pais)

        ### Mutação ###
        print(f'\nMutação:[{it}]')
        population = mutation(mut, localDeepcopy(population))

        ### Busca Local ###
        print(f'\nBusca Local:[{it}]')
        busca = []
        for i in range(1, localLen(filhos)):
            busca.append(localDeepcopy(two_opt(graph, filhos[i].copy(), 1)))

        ### Atualização ###
        print(f'\nAtualização da população:[{it}]')
        population = steady_stated(graph, population, busca)

        it += 1
        exe_time = time.time() - start_time

    print(f'\nMelhor solução:{best_solution}\n')
    return plt_counters, plt_opts, best_solution, round(exe_time, 2)

    # plot_graf(plt_opts, plt_counters, file_name, round(exe_time, 2), best_solution, cross_operator)
