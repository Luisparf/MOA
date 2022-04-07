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

def dist_between_points(graph, route, p1 ,p2):
    x1 = graph[route[p1]]['x']
    y1 = graph[route[p1]]['y']

    x2 = graph[route[p2]]['x']
    y2 = graph[route[p2]]['y']

    return localDist([x1, y1], [x2, y2])

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
        for a in range(size_route - 1):
            for b in range(a+2, size_route - 1):
                for c in range(b+2, size_route - 1):
                    new_route = route[:]
                    
                    # d1 = distance(A, C) + distance(B, D) + distance(E, F)

                    #new_route1 = route[:]
                    #new_route1[i:j] = route[]
                    #new_route1[] = route[]
                    wRoute0 = sumdistance(graph, route)
                    
                    #                   P(0,A)                                    D(A,B+1)                                              P(B+1,C)                            D(C,B)                                                       R(A+1,B)                               D(A+1,C+1)                                                P(C+1, 0)
                    wRoute1 = sumdistance(graph, route[0:a+1]) + dist_between_points(graph, route, route[a], route[b+1]) + sumdistance(graph, route[b+1:c+1]) + dist_between_points(graph, route, route[c], route[b]) + sumdistance(graph, route[a+1:b+2:-1]) + dist_between_points(graph, route, route[a+1], route[c+1]) + sumdistance(graph, route[c+1:size_route])
                    if wRoute0 > wRoute1:
                        pass
                    
                    #                   P(0,A)                                    D(A,B)                                                P(B,A+1)                            D(A+1,C)                                                     R(B+1,C)                               D(B+1,C+1)                                                P(C+1, 0)
                    wRoute2 = sumdistance(graph, route[0:a+1]) + dist_between_points(graph, route, route[a], route[b]) + sumdistance(graph, route[b:a+2:-1]) + dist_between_points(graph, route, route[a+1], route[c]) + sumdistance(graph, route[b+1:c+1:-1]) + dist_between_points(graph, route, route[b+1], route[c+1]) + sumdistance(graph, route[c+1:size_route])
                    if wRoute0 > wRoute2:
                        pass

                    #                    P(0,A)                                    D(A,C)                                                R(B+1,C)                            D(B+1,A+1)                                                   P(A+1,B)                               D(B,C+1)                                                  P(C+1,0)        
                    wRoute3 = sumdistance(graph, route[0:a+1]) + dist_between_points(graph, route, route[a], route[c]) + sumdistance(graph, route[b+1:c+1:-1]) + dist_between_points(graph, route, route[b+1], route[a+1]) + sumdistance(graph, route[a+1:b+1]) + dist_between_points(graph, route, route[b] + route[c+1]) + sumdistance(graph, route[c+1:size_route])                  
                    if wRoute0 > wRoute3:
                        pass

                    #                    P(0,A)                                    D(A, B+1)                                             P(B+1,C)                            D(C+1,A+1)                                                   P(A+1,B)                               D(B,C+1)                                                  P(C+1,0)                 
                    wRoute4 = sumdistance(graph, route[0:a+1]) + dist_between_points(graph, route, route[a], route[b+1]) + sumdistance(graph, route[b+1:c+1]) + dist_between_points(graph, route, route[c+1], route[a+1]) + sumdistance(graph, route[a+1:b+1]) +  dist_between_points(graph, route, route[b], route[c+1]) + sumdistance(graph, route[c+1, size_route])  
                    if wRoute0 > wRoute4:
                        pass
