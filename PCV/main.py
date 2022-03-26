# -*- coding: utf-8 -*-

from input import fileinput, runcodesinput
from constructive import matrizConstrutive, getAllDistances, insertMoreDistant, printGraph
from improvement import twooptswap

if __name__ == '__main__':

    ### Input ###
    # graph = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde cada nó i está no indice i da lista e contém suas coordenadas x,y
    # allDistances = getAllDistances(graph) # distâncias de nó para nó

    ### Heurística construtiva Inserção do mais distante
    # print(insertMoreDistant(graph, allDistances))
    
    ### Heurística melhorativa 

    lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


    twooptswap(lista, 3, len(lista))
   

    # Printar resultado da heurística vizinho mais próximo (considerando só a parte inteira)
    # print(int(matrizConstrutive(nodes, distances)))