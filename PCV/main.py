# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive import nearestNeighbour, getAllDistances, insertMoreDistant, printGraph
from improvement import two_opt

if __name__ == '__main__':

    ### Input ###
    graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    allDistances = getAllDistances(graph) # distâncias de nó para nó
    #printGraph(graph)

    ### Heurística construtiva Inserção do mais distante
    graph = insertMoreDistant(graph, allDistances)
    #print(graph)
    
    ### Heurística melhorativa 2-opt
    print(int(two_opt(allDistances, graph)))

   

    # Printar resultado da heurística vizinho mais próximo (considerando só a parte inteira)
    # print(int(nearestNeighbour(graph, allDistances)))