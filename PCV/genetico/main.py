# -*- coding: utf-8 -*-


from input import fileinput
from genetic import genetic


"""
    Genetic Algorithm project
    for help:
    >_ ./main -h   
"""

if __name__ == '__main__':

    ### Input ###
    args, graph = fileinput()

    genetic(graph[:], args.population, args.mutation, int(args.max_iteration), int(args.max_time) * 60, args.seed)
