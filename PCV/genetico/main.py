# -*- coding: utf-8 -*-

from aux import printgraph, plot_graf
from input import fileinput
from genetic import genetic
import sys

"""
    TSP SOLVER
    for help:
    >_ ./main -h   
"""

if __name__ == '__main__':

    file_name = sys.argv[len(sys.argv) - 1]

    ### Input ###
    args, graph = fileinput()

    genetic(graph[:], args.population, args.mutation, args.max_iteration, args.max_time, args.seed)
    
    

