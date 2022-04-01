from math import dist
from random import randint

# Uma cópia local de funções como essa reduz o tempo de execução
localLen = len
localDist = dist


############################################################################################

def printgraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))


############################################################################################


def getalldistances(graph):  # armazena todas as distâncias  nó X nó
    all_distances = {}
    for i in range(1, localLen(graph)):

        if all_distances.get(i) is None:
            all_distances[i] = {}

        all_distances[i][i] = 0.0
        x0 = graph[i]['x']
        y0 = graph[i]['y']
        for a in range(i + 1, localLen(graph)):
            # print(i, a)

            if all_distances.get(a) is None:
                all_distances[a] = {}

            x1 = graph[a]['x']
            y1 = graph[a]['y']

            calculated_dist = int(localDist([x0, y0], [x1, y1]))  # Só considerando parte inteira
            # calculated_dist = dist([x0, y0], [x1, y1])  # Considerando ponto flutuante

            all_distances[i][a] = calculated_dist
            all_distances[a][i] = calculated_dist
    # print(allDistances)
    return all_distances


###########################################################################################

def nearestneighbour(graph, all_distances):
    # selected = randint(1, localLen(graph)-1)
    selected = 1

    first = selected

    walked_path = [selected]
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

            if all_distances[selected][i] < menor:
                menor = all_distances[selected][i]
                menor_index = i

        if end_counter == (localLen(graph) - 1):
            # penultimo = localLen(walkedPath) - 1
            # walkWeight += allDistances[walkedPath[penultimo]][first]
            walked_path.append(first)
            break

        # walkWeight += menor
        walked_path.append(menor_index)
        graph[menor_index]['used'] = True
        selected = menor_index

    print(walked_path)
    return walked_path


###########################################################################################



def insertprox(graph, dist):
    route = [1, 2, 3]

    for i in range(1, 4):
        graph[i]['used'] = True

    while True:
        menor = float('inf')
        k = 1
        selected_i = 1
        for i in range(1, len(route)):
            for j in range(4, len(graph)):
                if all_dist[i][j] < menor and graph[j]['used'] is False:
                    k = j
                    menor = all_dist[i][j]

        minimum = all_dist[1][k] + all_dist[k][2] - all_dist[1][2]
        for i in range(2, len(route) + 1):
            # print("{},{}({}) = C{},{} + C{},{} - C{},{} = {}".format(i, i + 1, k, i, k, k, i + 1, i, i + 1,all_dist[i][k] + all_dist[k][i + 1] - all_dist[i][ i + 1]))
            if all_dist[i][k] + all_dist[k][i + 1] - all_dist[i][i + 1] < minimum:
                minimum = all_dist[i][k] + all_dist[k][i + 1] - all_dist[i][i + 1]
                selected_i = i

        route.insert(selected_i, k)
        graph[k]['used'] = True

        if localLen(route) == localLen(graph) - 1:
            break
    route.append(route[0])
    # print(sumdistance_matrix(all_dist, route))
    # print(route)
    return route


###########################################################################################

def runcodesinput():
    lines = []
    d = {}

    while True:
        try:
            line = str(input())
            # if line == "EOF":
            #    break
        except EOFError:
            break

        line = line.replace('\r', '').split()
        lines.append(line.copy())

    del lines[0:5]

    for i in range(1, len(lines)):

        try:
            d["used"] = False
            d["x"] = float(lines[i][1])
            d["y"] = float(lines[i][2])

        except IndexError:
            lines[i] = d.copy()
            break

        lines[i] = d.copy()

    # lines.append(lines[1])  
    # print(lines)  

    return lines


###########################################################################################

def sumdistance(dist, route):
    sizeroute = localLen(route) - 1
    walkWeight = 0
    for i in range(sizeroute):
        walkWeight += dist[route[i]][route[i + 1]]

    return walkWeight


###########################################################################################
def two_opt(route, dist):
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

    counter = 0
    while improved:

        improved = False
        # if counter >= 20:
        #    break
        for i in range(1, size_route - 2):
            best_distance = sumdistance(dist, route)

            for j in range(i + 1, size_route):
                # new_route = two_opt_swap(route.copy(), i, j)
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # o mesmo que two_opt_swap
                new_distance = sumdistance(dist, new_route)

                if new_distance < best_distance:
                    # print("counter = {} best_distance = {}".format(counter, best_distance))
                    best_route = new_route
                    improved = True
                    best_distance = new_distance
                    counter += 1
                    # print(new_route)

            route = best_route
            # print()
    # print(route)
    return best_distance


##########################################################################################################

if __name__ == '__main__':
    ### Input ###
    graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    all_distances = getalldistances(graph)  # distâncias de nó para nó
    # print(allDistances)

    ### Heurística construtiva vizinho mais próximo

    graph = nearestneighbour(graph, all_distances)

    ### Heurística construtiva Inserção do mais próximo
    # graph = insertprox(graph, all_distances)

    ### Heurísica melhorativa 2-opt
    print(two_opt(graph, all_distances))
