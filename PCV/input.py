# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém as funções para entrada e formatação dos dados         #                          
#                                                                                         #      
###########################################################################################

############################################# INPUT BY FILE ###############################################

from math import dist


def fileinput():
    """

    Apenas para uma possível versão futura...

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
        line = line.replace('\r', '').split() # .replace('.', '').split()
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
        
    return lines

############################################################################################################


