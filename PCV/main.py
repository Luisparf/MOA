# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive import matrizConstrutive, getAllDistances, insertMoreDistant, printGraph

if __name__ == '__main__':

    # lines = fileinput()
    graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    allDistances = getAllDistances(graph) # distâncias de nó para nó

    insertMoreDistant(graph, allDistances)
    
    # printGraph(graph)
    

    # Printar resultado da heurística vizinho mais próximo (considerando só a parte inteira)
    # print(int(matrizConstrutive(nodes, distances)))