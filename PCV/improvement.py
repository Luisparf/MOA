# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém os algoritmos nelhorativos para o PCV                  #                          
#                                                                                         #      
###########################################################################################

localLen = len


def sumdistance(dist, route):
    sizeroute = localLen(route) - 1
    walk_weight = 0
    for i in range(sizeroute):
        walk_weight += dist[route[i]][route[i + 1]]
        # 	print("route[{}] = {}".format(i,route[i]))

    return walk_weight


############################################################################################

def two_opt_swap(route, i, k):
    newroute = []
    sizeroute = localLen(route)

    newroute.append(route[0:i])
    newroute.append(route[k - 2:i - 1:-1])
    newroute.append(route[k - 1:sizeroute])

    flatroute = [item for sublist in newroute for item in sublist]
    # print("\nflatroute = {} i = {} k = {}".format(flatroute, i, k))
    return flatroute


############################################################################################

def two_opt(dist, route):
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

    while improved:

        improved = False

        for i in range(1, size_route - 2):
            best_distance = sumdistance(dist, route)

            for j in range(i + 1, size_route):
                # newRoute = two_opt_swap(route.copy(), i, k)
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # o mesmo que two_opt_swap
                # print(newRoute)
                new_distance = sumdistance(dist, new_route)

                if new_distance < best_distance:
                    best_route = new_route
                    improved = True
                    best_distance = new_distance

            route = best_route
    # print()
    # print(route)
    return best_distance
