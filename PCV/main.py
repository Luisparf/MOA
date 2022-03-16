# from scipy.spatial import distance
from input import fileinput, runcodesinput

if __name__ == '__main__':
    # lines = fileinput()
    nodes = runcodesinput()  # lê o arquivo e armazena cada nó em uma lista, onde nó i está no indice i da lista e armazena suas coordenadas x,y
    print(nodes)
