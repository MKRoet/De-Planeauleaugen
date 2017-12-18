#-------------------------------------------------------------------------------
# File name: algortihms.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# TODO
#-------------------------------------------------------------------------------

import random
from tqdm import tqdm
from copy import deepcopy
from Data_structure.plotmap import *

#-------------------------------------------------------------------------------

# global variable
bestScore = 0

#-------------------------------------------------------------------------------

# TODO

# Moves a randomly selected house by one step on the X or Y axis.
def moveHouse(objects):
    randomHouse = random.choice(objects.objectList)
    steps = [1, -1]
    randomStep = random.choice(steps)
    shafts = ["x", "y"]
    randomXY = random.choice(shafts)

    if randomXY == "x":
        randomHouse.x = randomHouse.x + randomStep
    elif randomXY == "y":
        randomHouse.y = randomHouse.y + randomStep

    if objects.mapBounds(randomHouse) and not objects.overlap(randomHouse):
        return True
    else:
        if randomXY == "x":
            randomHouse.x = randomHouse.x - randomStep
        elif randomXY == "y":
            randomHouse.y = randomHouse.y - randomStep
        return False

# Swaps the coordinates of two randomly selected houses.
def swapHouse(objects):
    randomHouse1 = random.choice(objects.objectList)
    randomHouse2 = random.choice(objects.objectList)

    if randomHouse1 == randomHouse2:
        return False
    elif randomHouse1.base_sale_price != randomHouse2.base_sale_price:
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
    else:
        return False

    if not objects.mapBounds(randomHouse1) and not objects.mapBounds(randomHouse2):
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
        return False
    elif objects.overlap(randomHouse1) and objects.overlap(randomHouse2):
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
        return False
    return True

# Places a randomly selected house on a new location.
def randomPlacement(objects):
    randomHouse = random.choice(objects.objectList)
    x,y = objects.getRandom_coordinates()
    oldx = deepcopy(randomHouse.x)
    oldy = deepcopy(randomHouse.y)
    randomHouse.x = x
    randomHouse.y = y

    if objects.mapBounds(randomHouse) and not objects.overlap(randomHouse):
        return True
    else:
        randomHouse.x = oldx
        randomHouse.y = oldy
        return False

def HillClimber(total_houses, runs_algorithm, amount_iterations):

    objects = GenerateMap(total_houses)
    # PlotMap(objects, 'before.png' + repr(i) + '.png')
    bestScore = objects.getScore(objects)

    for i in range(runs_algorithm):

        for j in range(amount_iterations):
            old_list = deepcopy(objects)

            moveType = ["moveHouse", "swapHouse", "randomPlacement"]
            randomMethod = random.choice(moveType)
            print("hillClimber_type: " + str(randomMethod))

            if randomMethod == "moveHouse":
                if moveHouse(objects) == True:
                    sumScore = objects.getScore(objects)
                    if sumScore > bestScore:
                        bestScore = sumScore
                        print("move        " + str(bestScore))
                    else:
                        objects = old_list

            elif randomMethod == "swapHouse":
                if swapHouse(objects)  == True:
                    sumScore = objects.getScore(objects)
                    if sumScore > bestScore:
                        bestScore = sumScore
                        print("swap        " + str(bestScore))
                    else:
                        objects = old_list

            elif randomMethod == "randomPlacement":
                if randomPlacement(objects) == True:
                    sumScore = objects.getScore(objects)
                    if sumScore > bestScore:
                        bestScore = sumScore
                        print("random        " + str(bestScore))
                    else:
                        objects = old_list

            # ??? return ??? dat weer opnieuw gebruiken
            PlotMap(objects, 'after.png')

def RandomAlgorithm(total_houses, runs_algorithm):

    bestScore = 0
    bestObjectList = 0

    for i in range(runs_algorithm):
        A = GenerateMap(total_houses)
        sumScore = A.getScore(A)

        if sumScore > bestScore:
            bestScore = sumScore
            bestObjectList = A

            PlotMap(bestObjectList, 'map.png')

# # Simulated annealing algorithm which also accepts moves which lower the score.
# def SimulatedAnnealing():
#     PlotMap()
#     firstScore = objects.getScore(objects)
#     bestScore = objects.getScore(objects)
#     for i in range(20000):
#         old_list = deepcopy(objects)
#         if objects.moveHouse() == True:
#             sumScore = objects.getScore(objects)
#             if sumScore > bestScore:
#                 bestScore = sumScore
#             print(sumScore)
#     print("Best: " + str(bestScore))
#     print("First: " + str(firstScore))
