# -*- coding: utf-8 -*-
# from scipy.spatial import distance
from input import fileinput, runcodesinput, nodesDistances
from constructive import matrizConstrutive

if __name__ == '__main__':
    # lines = fileinput()
    nodes = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    #print(nodes)
    distances = nodesDistances(nodes)
    #print(distances[24]) 
    
    # Printar resultado da heurística vizinho mais próximo (considerando só a parte inteira)
    print(int(matrizConstrutive(nodes, distances)))