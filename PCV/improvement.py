# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém os algoritmos nelhorativos para o PCV                  #
#                                                                                         #
###########################################################################################
from math import dist

localLen = len
localDist = dist

########################################################################################################################


def sumdistance(graph, route):
    sizeroute = localLen(route) - 1
    walk_weight = 0
    for i in range(sizeroute):
        xi = graph[route[i]]['x']
        yi = graph[route[i]]['y']

        x_p = graph[route[i + 1]]['x']
        y_p = graph[route[i + 1]]['y']

        walk_weight += localDist([xi, yi], [x_p, y_p])

    return walk_weight
########################################################################################################################


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
        best_distance = sumdistance(graph, route)
        for i in range(1, size_route - 2):
            for j in range(i + 1, size_route):
                # newRoute = two_opt_swap(route.copy(), i, k)
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # o mesmo que two_opt_swap
                # print(newRoute)
                new_distance = sumdistance(graph, new_route)
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

                    ### trecho para matplot ###
                    plt_opts.append(best_distance)
                    plt_counter += 1
                    plt_counters.append(plt_counter)
                    #################

                if x == 1 and counter >= 20:
                    should_break = True
                    improved = False
                    break

            route = best_route
            if should_break:
                break
            # print()
    print(counter)
    # print(route)
    return best_distance, plt_counters, plt_opts

def three_opt(graph, route):
    size_route = localLen(route)
    best_route = route

    improved = True

    while improved:
        for i in range(size_route):
            for j in range(i+2, size_route):
                for k in range(j+2, size_route):
                    new_route0 = route[:]
                    
                    new_route1 = route[:]
                    new_route1[i:j] = route[]
                    new_route1[] = route[]

                    wRoute0 = sumdistance(graph, route)
