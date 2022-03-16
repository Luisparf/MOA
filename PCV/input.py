# -*- coding: utf-8 -*-
############################################# INPUT BY FILE ###############################################

from math import dist


def fileinput():
    """

    Apenas para uma versão futura...

    """
    f = open('1.in', 'r')
    lines = f.readlines()

    del lines[0:5]
    lines.pop()

    for i in range(1, len(lines)):
        line = lines[i].replace('\r', '').replace('.', '').split()
        lines[i] = line

    f.close()
    return lines


############################################ RUN.CODES INPUT ##############################################

def runcodesinput():
    lines = []
    while (line := str(input())) != "EOF":
        line = line.replace('\r', '').replace('.', '').split()
        lines.append(line.copy())

    del lines[0:5]

    lines = formatnode(lines)
    return lines


############################################################################################################

def formatnode(lines):

    dict = {}

    for i in range(1, len(lines)):
        dict["used"] = False
        dict["x"] = float(lines[i][1])
        dict["y"] = float(lines[i][2])

        lines[i] = dict.copy()
        # print('\n'.join("{}: {}".format(k, v) for k, v in lines[i].items()))

        '''
        trecho que será usado para o calculo da distancia euclidiana
        x1 = int(lines[1]['x'])
        y1 = int(lines[1]['y'])

        x2 = int(lines[i]['x'])
        y2 = int(lines[i]['y'])

        a = [x1, y1]
        b = [x2, y2]
        # print("Euclidian distance between node {}{} and node {}{} is {}\n".format(1, a, i, b, distance.euclidean(a, b)))
        # print("Euclidian distance between node {}{} and node {}{} is {}\n".format(1, a, i, b, dist(a, b)))
        '''
    return lines

############################################################################################################

def nodesDistances(nodes):
    distances = {}
    for i in range(1, len(nodes)):
        distances[i] = {}
        for a in range(1, len(nodes)):
            x0 = nodes[i]['x']
            y0 = nodes[i]['y']
            
            x1 = nodes[a]['x']
            y1 = nodes[a]['y']
            
            distances[i][a] = dist([x0, y0], [x1, y1])

    return distances


