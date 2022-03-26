# -*- coding: utf-8 -*-
###########################################################################################
#                                                                                         #
#                Módulo que contém os algoritmos nelhorativos para o PCV                  #                          
#                                                                                         #      
###########################################################################################

localLen = len


def sumTravel(allDistances, sizeCycle, cycle):
    walkWeight = 0
    for i in range(sizeCycle-1):
        walkWeight += allDistances[cycle[i]][cycle[i+1]]

    return walkWeight

############################################################################################

def twooptswap(cycle, i, k):

	newCycle = []
	sizeCycle = localLen(cycle)


	newCycle.append(cycle[0:i])
	newCycle.append(cycle[k-2:i-1:-1])
	newCycle.append(cycle[k-1:sizeCycle])

	print(newCycle)


def improve(cycle, distances, sizeCycle):

	k = 2
	"""
	while True:

		bestDistance = sumTravel(cycle)

		for i in range(sizeCycle -1):
			for j in range(i+1, sizeCycle):
				cycle = """



	