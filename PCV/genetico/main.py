# -*- coding: utf-8 -*-

from input import fileinput
from genetic import genetic
from aux import plot_graf
import sys

"""
    Genetic Algorithm project
    for help:
    >_ ./main -h   
"""

if __name__ == '__main__':
    file_name = sys.argv[len(sys.argv) - 1]

    ### Input ###
    args, graph = fileinput()

    x2, y2, best_solution2, time2 = genetic(graph[:], int(args.population), int(args.mutation), int(args.max_iteration),
                                            int(args.max_time) * 60, int(args.seed), 'pos')
    x1, y1, best_solution1, time1 = genetic(graph[:], int(args.population), int(args.mutation), int(args.max_iteration),
                                            int(args.max_time) * 60, int(args.seed), 'cx')

    plot_graf(x1, y1, x2, y2, file_name, best_solution1, best_solution2, 'cx', 'pos', time1, time2)
