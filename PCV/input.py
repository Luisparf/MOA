# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém as funções para entrada e formatação dos dados         #                          
#                                                                                         #      
###########################################################################################

################################### INPUT BY FILE #########################################
import os

from argparse import ArgumentParser

localLen = len


def is_valid_file(parser, arg):
    if not os.path.exists(arg):  # se o caminho passado é inválido:
        parser.error("The file '%s' does not exist!" % arg)  # printa que o arquivo não existe
    else:
        return open(arg, 'r')  # senão retorna referencia para o arquivo aberto


def fileinput():
    # algumas definições para --help
    parser = ArgumentParser(description='Solver to PCV ',
                            epilog="(Try 'python3 main.py att48.tsp')")

    parser.add_argument(dest="filename", help='.tsp file with graph coordinates',
                        type=lambda x: is_valid_file(parser, x))

    parser.add_argument('--mode', action='store', dest='mode', default='n',
                        required=False,
                        help="m para execução com matriz de distâncias, n para execução sem matriz de distâncias (padrão: m )")

    parser.add_argument('-c', action='store', dest='algoritmo_construtivo', default='vp',
                        required=False,
                        help="vp para algoritmo 'Vizinho mais próximo', id para algoritmo 'Inserção do mais distante', ic para algoritmo 'Inserção mais barata' (padrão: vp )")

    parser.add_argument('-i', action='store', dest='algoritmo_melhorativo', default='opt2',
                        required=False, help="opt2 para algoritmo '2-opt', n para não executar algoritmo melhorativo")

    args = parser.parse_args()

    d = {}
    lines = []
    i = 0
    while (line := args.filename.readline()) and line != "EOF":

        if i > 5:
            line = line.replace('\r', '').replace('\n', '').split()  # .replace('.', '')
            d["used"] = False
            # d["i"] = i
            d["x"] = float(line[1])
            d["y"] = float(line[2])
            lines.append(d.copy())
            i += 1
        else:
            lines.append(line)
            i += 1

    args.filename.close()

    print(f'{lines[0]}{lines[1]}{lines[2]}{lines[3]}{lines[4]}')

    del lines[0:5]
    return args, lines


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
