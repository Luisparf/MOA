# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive import closestNeigbourMatriz, closestInsertionMatriz, nodesDistances, insertDistant

if __name__ == '__main__':

    # lines = fileinput()
    nodes = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    distances = nodesDistances(nodes) # distâncias de nó para nó
    

    
    print(int(closestInsertionMatriz(nodes, distances)))
    # print(distances[24]) 
    # print(distances[1][3]) # distancia entre o nó 1 e nó 3
    # Printar resultado da heurística vizinho mais próximo (considerando só a parte inteira)
    # print(int(matrizConstrutive(nodes, distances)))