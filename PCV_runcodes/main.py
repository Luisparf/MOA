from math import dist
from random import randint


# Uma cópia local de funções como essa reduz o tempo de execução
localLen = len

############################################################################################

def printGraph(graph):
    for i in range(1, localLen(graph)):
        print(f"\n{i}")
        print('\n'.join("{}: {}".format(k, v) for k, v in graph[i].items()))
   
############################################################################################


def getAllDistances(graph): # armazena todas as distâncias  nó X nó
    allDistances = {}
    for i in range(1, localLen(graph)-1):
        try:
            allDistances[i]
        except:
            allDistances[i] = {}


        allDistances[i][i] = 0.0

        x0 = graph[i]['x']
        y0 = graph[i]['y']

        for a in range(i+1, len(graph)):  

            try:
                allDistances[a]
                
            except:
                allDistances[a] = {}
        
            x1 = graph[a]['x']
            y1 = graph[a]['y']
            

            calculatedDist = int(dist([x0, y0], [x1, y1])) # Só considerando parte inteira
            #calculatedDist = dist([x0, y0], [x1, y1]) # Considerando ponto flutuante

            allDistances[i][a] = calculatedDist
            allDistances[a][i] = calculatedDist
         
    return allDistances

###########################################################################################

def nearestNeighbour(graph, allDistances):
    selected = randint(1, localLen(graph)-1)
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

            if allDistances[selected][i] < menor:
                menor = allDistances[selected][i]
                menorIndex = i
        
        if endCounter == (localLen(graph) - 1):
            penultimo = localLen(walkedPath) - 1
            walkWeight += allDistances[walkedPath[penultimo]][first]
            walkedPath.append(first)
            break

        walkWeight += menor
        walkedPath.append(menorIndex)
        graph[menorIndex]['used'] = True
        selected = menorIndex

    
    # print(walkedPath)

    return walkedPath

###########################################################################################


def insertMoreDistant(graph, dist): 
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
    route = ['',1,2,3] # no caso, os 3 primeiros vértices, '' na primeira posição apenas para ciclo[i] = i
    for x in range(1,localLen(route)):
        graph[x]['used'] = True
    
   
    while True:

        # a) Encontrar um vértice k não pertencente ao ciclo, mais distante de qualquer vértice do ciclo
        sizeroute = localLen(route)
        i = route[sizeroute-1]# no caso, pega o ultimo inserido ***
            
        chosenEdge = i
        
        greaterDistance = 0
        for j in range(1, localLen(graph)):
            if dist[i][j] > greaterDistance and graph[j]['used'] == False:
                greaterDistance = dist[i][j]
                k = j
            
        # b) Encontrar uma aresta (i,j) do ciclo tal que: (Ci,k + Ck,i+1 - Ci,1+1) seja mínimo.  
        minimum = dist[1][k] + dist[k][2] - dist[1][2]
        for i in range(2,sizeroute-1):
            if dist[i][k] + dist[k][i+1] - dist[i][i+1] < minimum : 
                minimum = dist[i][k] + dist[k][i+1] - dist[i][i+1]
                chosenEdge = i

        i = chosenEdge

        # c) Inserir o vértice k entre (i , i+1 ). Se todos os vértices já foram inseridos, pare, caso contrário,voltar ao passo “b”. <- "a"
        route.insert(i,k)
        graph[k]['used'] = True

        if sizeroute == localLen(graph)-1:
            break

    route = [value for value in route if value != '']

    route.append(route[0]) 
    # print(route)
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

def sumDistance(dist, route):

    sizeroute = localLen(route)-1
    walkWeight = 0
    for i in range(sizeroute):
        walkWeight += dist[route[i]][route[i+1]]
        #   print("route[{}] = {}".format(i,route[i]))

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

    sizeRoute = localLen(route)
    bestRoute = route
    improved = True

    while improved:

        improved = False

        for i in range(1, sizeRoute - 2):
            bestDistance = sumDistance(dist, route)

            for j in range(i+1, sizeRoute):
                # newRoute = two_opt_swap(route.copy(), i, k)
                newRoute = route[:]
                newRoute[i:j] = route[j-1:i-1:-1] # o mesmo que two_opt_swap
                # print(newRoute)
                newDistance = sumDistance(dist, newRoute)

                if newDistance < bestDistance:
                    bestRoute = newRoute
                    improved = True
                    bestDistance = newDistance

            route = bestRoute   
    #print()
    #print(route)
    return bestDistance

##########################################################################################################

if __name__ == '__main__':

    ### Input ###
    graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    allDistances = getAllDistances(graph) # distâncias de nó para nó
    #print(allDistances)

    ### Heurística construtiva vizinho mais próximo
    graph = insertMoreDistant(graph, allDistances)
    
    ### Heurística construtiva Inserção do mais distante
    # graph = nearestNeighbour(graph, allDistances)

    ### Heurística melhorativa 2-opt
    print(int(two_opt(graph, allDistances)))

   

