# -*- coding: utf-8 -*-

from aux import printgraph, plot_graf
from input import fileinput
from genetic import genetic, nearestneighbour, nearest
import time
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
    start_time = time.time()

    genetic(graph[:], start_time, args.population, args.mutation, args.max_iteration, args.max_time, args.seed)
    
    

