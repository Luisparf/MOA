# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém as funções para entrada e formatação dos dados         #                          
#                                                                                         #      
###########################################################################################

################################### INPUT BY FILE #########################################

from math import dist


def fileinput():
    """

    Apenas para uma possível versão futura...

    """
    f = open('1.in', 'r')
    d = {}
    lines = f.readlines()

    del lines[0:5]
    lines.pop()

    for i in range(1, len(lines)):
        line = lines[i].replace('\r', '').replace('.', '').split()
        lines[i] = line

    

    for i in range(1, len(lines)):
        d["used"] = False
        d["x"] = float(lines[i][1])
        d["y"] = float(lines[i][2])


        lines[i] = d.copy()

    f.close()
    return lines


################################## RUN.CODES INPUT ########################################

def runcodesinput():
    lines = []
    d = {}
    
    while True:
        try:
            line = str(input())
            if line == "EOF":
                break
        except EOFError as e: 
            break
        
        line = line.replace('\r', '').split() # .replace('.', '').split()
        lines.append(line.copy())

    del lines[0:5]

    for i in range(1, len(lines)):

        try:
            d["used"] = False
            d["x"] = float(lines[i][1])
            d["y"] = float(lines[i][2])
            
        except IndexError:
            lines[i] = d.copy()
            return lines


        lines[i] = d.copy()

    return lines

