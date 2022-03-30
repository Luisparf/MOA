from math import dist
from random import randint


# Uma cópia local de funções como essa reduz o tempo de execução
localLen = len
localDist = dist



###########################################################################################

def nearestNeighbour(graph):
    # selected = randint(1, localLen(graph)-1)
    selected = 1

    first = selected
    
    walkWeight = 0
    walkedPath = []
    walkedPath.append(selected)
    graph[selected]['used'] = True


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



            if dist([graph[selected]['x'],graph[selected]['y']],[graph[i]['x'],graph[i]['y']])  < menor:
                menor = dist([graph[selected]['x'],graph[selected]['y']],[graph[i]['x'],graph[i]['y']])
                menorIndex = i
        
        if endCounter == (localLen(graph) - 1):
            penultimo = localLen(walkedPath) - 1
            walkWeight +=  int(dist( [ graph[walkedPath[penultimo]]['x'], graph[walkedPath[penultimo]]['y'] ], [ graph[first]['x'], graph[first]['y'] ] ) )
            walkedPath.append(first)
            break


        walkWeight += menor
        walkedPath.append(menorIndex)
        graph[menorIndex]['used'] = True
        selected = menorIndex

    
    # print(walkedPath)

    return walkedPath

###########################################################################################


def insertmoredistant(graph):
    """
    More distant insertion heuristic.
    Algorithm source:
    Grafos Hamiltonianos e o Problema do Caixeiro Viajante
            Prof. Ademir Constantino
            Departamento de Informática
            Universidade Estadual de Maringá
    link: https://malbarbo.pro.br/arquivos/2012/1747/problema-do-caixeiro-viajante.pdf
    """

    # Iniciar com um ciclo [v1 , v2 , v3] com 3 vértices.
    route = [0, 1, 2, 3]  # no caso, os 3 primeiros vértices, 0 na primeira posição apenas para ciclo[i] = i
    for x in range(1, localLen(route)):
        graph[x]['used'] = True

    while True:

        # a) Encontrar um vértice k não pertencente ao ciclo, mais distante de qualquer vértice do ciclo
        sizeroute = localLen(route)
        i = route[sizeroute - 1]  # no caso, pega o ultimo inserido ***
        chosen_edge = i

        xi = graph[i]['x']
        yi = graph[i]['y']

        greater_distance = 0
        for j in range(1, localLen(graph)):
            x1 = graph[j]['x']
            y1 = graph[j]['y']

            if dist([xi, yi], [x1, y1]) > greater_distance and graph[j]['used'] is False:
                greater_distance = dist([xi, yi], [x1, y1])
                k = j

        # b) Encontrar uma aresta (i,j) do ciclo tal que: (Ci,k + Ck,i+1 - Ci,1+1) seja mínimo.
        """
        minimum = alldist[1][k] + alldist[k][2] - alldist[1][2]
        for i in range(2, sizeroute - 1):
            if alldist[i][k] + alldist[k][i + 1] - alldist[i][i + 1] < minimum:
                minimum = alldist[i][k] + alldist[k][i + 1] - alldist[i][i + 1]
                chosen_edge = i
        """

        x1 = graph[1]['x']
        y1 = graph[1]['y']

        x2 = graph[2]['x']
        y2 = graph[2]['y']

        xk = graph[k]['x']
        yk = graph[k]['y']
        minimum = localDist([x1, y1], [xk, yk]) + localDist([xk, yk], [x2, y2]) - localDist([x1, y1], [x2, y2])
        for i in range(2, sizeroute - 1):
            xi = graph[i]['x']
            yi = graph[i]['y']

            x_p = graph[i + 1]['x']
            y_p = graph[i + 1]['y']

            if localDist([xi, yi], [xk, yk]) + localDist([xk, yk], [x_p, y_p]) - localDist([xi, yi],
                                                                                           [x_p, y_p]) < minimum:
                minimum = localDist([xi, yi], [xk, yk]) + localDist([xk, yk], [x_p, y_p]) - localDist([xi, yi],[x_p, y_p])
                chosen_edge = i

        i = chosen_edge

        # c) Inserir o vértice k entre (i , i+1 ). Se todos os vértices já foram inseridos, pare, caso contrário,voltar ao passo “b”. <- "a"
        route.insert(i, k)
        graph[k]['used'] = True

        if sizeroute == localLen(graph) - 1:
            break

    route = [value for value in route if value != 0]

    route.append(route[0])
    print(route)
    return route


###########################################################################################

def runcodesinput():
    lines = []
    d = {}
    
    while True:
        try:
            line = str(input())
            if line == "EOF":
                break
        except EOFError : 
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
def sumdistance(graph, route):

    sizeroute = localLen(route)-1
    walkWeight = 0
    for i in range(sizeroute):
        x0 = graph[route[i]]['x']
        y0 = graph[route[i]]['y']

        x1 = graph[route[i+1]]['x']
        y1 = graph[route[i+1]]['y']

        walkWeight += int(dist([x0,y0],[x1,y1]))
        

    return walkWeight


###########################################################################################


def two_opt(graph, route):
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

        if counter >= 20:
           break

        improved = False

        for i in range(1, size_route - 2):
            best_distance = sumdistance(graph, route)

            for j in range(i + 1, size_route):
                # newRoute = two_opt_swap(route.copy(), i, k)
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # o mesmo que two_opt_swap
                # print(newRoute)
                new_distance = sumdistance(graph, new_route)

                if new_distance < best_distance:
                    best_route = new_route
                    improved = True
                    best_distance = new_distance
                    counter += 1

            route = best_route
            # print()
    print(route)
    return best_distance

##########################################################################################################

if __name__ == '__main__':

    ### Input ###
    graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    # allDistances = getAllDistances(graph) # distâncias de nó para nó
    #print(allDistances)

    ### Heurística construtiva vizinho mais próximo
    # graph = insertmoredistant(graph, allDistances)
    
    ### Heurística construtiva Inserção do mais distante
    route = nearestNeighbour(graph)


    ### Heurística melhorativa 2-opt
    print(int(two_opt(graph, route)))

   

