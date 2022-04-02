# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém as funções para entrada e formatação dos dados         #                          
#                                                                                         #      
###########################################################################################

################################### INPUT BY FILE #########################################
import os
from argparse import ArgumentParser
from math import dist

localLen = len


def is_valid_file(parser, arg):
    if not os.path.exists(arg):  # se o caminho passado é inválido:
        parser.error("The file '%s' does not exist!" % arg)  # printa que o arquivo não existe
    else:
        return open(arg, 'r')  # senão retorna referencia para o arquivo aberto


def fileinput():
    """

    Apenas para uma possível versão futura...

    """

    # algumas definições para --help
    parser = ArgumentParser(description='Solver to PCV ',
                            epilog="(Try 'python3 main.py <file_name>.tsp')")
    parser.add_argument(dest="filename", help='.tsp file with graph ',
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()

    d = {}
    lines = args.filename.readlines()
    args.filename.readlines()

    print("COMMENT : {} TYPE : {} TSP DIMENSION: {} EDGE_WEIGHT_TYPE : EUC_2D".format(lines[0], lines[1], lines[2],
                                                                                      lines[3], lines[4]))

    del lines[0:5]
    lines.pop()

    for i in range(1, localLen(lines)):
        line = lines[i].replace('\r', '').split()  # .replace('.', '')

        d["used"] = False
        # d["i"] = i
        d["x"] = float(line[1])
        d["y"] = float(line[2])
        lines[i] = d.copy()

    return lines


################################## RUN.CODES INPUT ########################################

def runcodesinput():
    lines = []
    d = {}

    while True:
        try:
            line = str(input())
        except EOFError:
            break

        line = line.replace('\r', '').split()
        lines.append(line.copy())

    del lines[0:5]
    lines.pop()

    for i in range(1, localLen(lines)):
        # print(lines[i])
        d["used"] = False
        # d["i"] = i
        d["x"] = float(lines[i][1])
        d["y"] = float(lines[i][2])

        lines[i] = d.copy()

    # lines.append(lines[1])
    # print(lines)  

    return lines
