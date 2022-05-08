# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém as funções para entrada e formatação dos dados         #                          
#                                                                                         #      
###########################################################################################

import os

from argparse import ArgumentParser

localLen = len


def is_valid_file(parser, arg):
    if not os.path.exists(arg):  # se o caminho passado é inválido:
        parser.error("The file '%s' does not exist!" % arg)  # printa que o arquivo não existe
    else:
        return open(arg, 'r')  # senão retorna referencia para o arquivo aberto


def fileinput():

    parser = ArgumentParser(description='Algoritmo genético aplicado ao problema do caixeiro viajante; ',
                            epilog="Tente:  ./main att48.tsp")

    parser.add_argument(dest="filename", help='arquivo .tsp',
                        type=lambda x: is_valid_file(parser, x))

    parser.add_argument('-pop', action='store', type=int, dest='population', default=25,
                        required=False,
                        help="Tamanho da população inicial (padrão: 25)")

    parser.add_argument('-mut', action='store', dest='mutation', default=5,
                        required=False, help="Porcentagem de mutação (padrão: 5 )")

    parser.add_argument('-max_i', action='store', dest='max_iteration', default=2000,
                        required=False, help="Máximo de iterações (padrão: 2000)")

    parser.add_argument('-max_t', action='store', dest='max_time', default=60,
                        required=False, help="Máximo de tempo de execução(minutos) (padrão: 60)")

    parser.add_argument('-s', action='store', dest='seed', default=1,
                        required=False, help="Semente randômica (padrão: 1)")

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
