#-------------------------------------------------------------------------------
# File name: algorithms.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This file contains the different algorithms RandomAlgorithm, HillClimber and
# SimulatedAnnealing. The HillClimber algorithm uses different functions:
# moveHouse, swap and randomPlacement. The different functions are randomly
# called in the HillClimber algorithm. TODO SimulatedAnnealing!!
#-------------------------------------------------------------------------------

from Data_structure.plotmap import *
import random
from copy import deepcopy
from tqdm import tqdm

#-------------------------------------------------------------------------------

# Algorithm Random: gets a generated map and only plots the floor plan with the
# highest score of all random algorithm runs.
def RandomAlgorithm(total_houses, runs_algorithm):
    bestScore = 0
    bestObjectList = 0

    for run in tqdm(range(runs_algorithm):
        objects = generateMap(total_houses)
        sumScore = objects.getScore(objects)

        if sumScore > bestScore:
            bestScore = sumScore
            print('{}'.format(int(bestScore)))
            bestObjectList = objects

    plotMap(bestObjectList, 'map.png')

#-------------------------------------------------------------------------------
# Algorithm HillClimber: gets a generated map and plots a floor plan of this map
# for every run of the algorithm. For the amount of iterations in such run,
# different random methods will be chosen and run. The floor plan with the
# highest score of all the iterations will be plotted for every algorithm run.
def HillClimber(total_houses, runs_algorithm, amount_iterations):
    for run in tqdm(range(runs_algorithm)):
        objects = generateMap(total_houses)
        plotMap(objects, 'before.png' + repr(run) + '.png')
        bestScore = objects.getScore(objects)

        for amount in range(amount_iterations):
            old_list = deepcopy(objects)
            moveType = ["swapObject", "moveObject", "randomPlacement"]
            randomMethod = random.choice(moveType)

            if randomMethod == "moveHouse":
                if moveObject(objects) == True:
                    sumScore = objects.getScore(objects)
                    if sumScore > bestScore:
                        bestScore = sumScore
                    else:
                        objects = old_list

            elif randomMethod == "swap":
                if swapObject(objects)  == True:
                    sumScore = objects.getScore(objects)
                    if sumScore > bestScore:
                        bestScore = sumScore
                    else:
                        objects = old_list

            elif randomMethod == "randomPlacement":
                if randomPlacement(objects) == True:
                    sumScore = objects.getScore(objects)
                    if sumScore > bestScore:
                        bestScore = sumScore
                    else:
                        objects = old_list

        plotMap(objects, 'after.png' + repr(run) + '.png')

# Moves a randomly selected house by one step on the X or Y axis.
def moveObject(objects):
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
def swapObject(objects):
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

# Places a randomly selected house on a new random location.
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

#-------------------------------------------------------------------------------
# Algorithm Simulated Annealing: gets a generated map and plots a floor plan of
# this map for every run of the algorithm. For the amount of iterations in such
# run,  different random methods will be chosen and run. The floor plan with the
# highest score of all the iterations will be plotted for every algorithm run.
def SimulatedAnnealing(total_houses, runs_algorithm, amount_iterations):
    temperature = 1000000
    coolingRate = 0.03

    for i in tqdm(range(runs_algorithm)):
        currentList = GenerateMap(total_houses)
        bestScore = currentList.getScore(currentList)
        PlotMap(currentList, 'before.png' + repr(i) + '.png')

        for j in range(amount_iterations):
            currentScore = currentList.getScore(currentList)
            newList = deepcopy(currentList)
            moveType = ["swap", "moveHouse", "randomPlacement"]
            randomMethod = random.choice(moveType)

            if randomMethod == "moveHouse":
                if moveHouse(newList) == True:
                    newScore = newList.getScore(newList)
                    print("newScore: " + str(newScore))
                    if newScore > bestScore:
                        currentList = newList
                        bestList = newList
                        bestScore = newScore
                    elif acceptanceProbability(currentScore, newScore,\
                        temperature) > random.uniform(0, 1):
                        currentList = newList
                    else:
                        currentList = currentList

            elif randomMethod == "swap":
                if swap(newList) == True:
                    newScore = newList.getScore(newList)

                    if newScore > bestScore:
                        currentList = newList
                        bestList = newList
                        bestScore = newScore
                    elif acceptanceProbability(currentScore, newScore, temperature) > random.uniform(0, 1):
                        currentList = newList
                    else:
                        currentList = currentList

            elif randomMethod == "randomPlacement":
                if randomPlacement(newList) == True:
                    newScore = newList.getScore(newList)

                    if newScore > bestScore:
                        currentList = newList
                        bestList = newList
                        bestScore = newScore
                    elif acceptanceProbability(currentScore, newScore, temperature) > random.uniform(0, 1):
                        currentList = newList
                    else:
                        currentList = currentList

            temperature *= 1 - coolingRate
        PlotMap(bestList, 'after.png' + repr(i) + '.png')

def acceptanceProbability(currentScore, newScore, temperature):
    if newScore > currentScore:
        return 1.0
    return math.exp((newScore - currentScore) / temperature)
