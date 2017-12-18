#-------------------------------------------------------------------------------
# File name: algorithms.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This file contains the different algorithms RandomAlgorithm, Hill Climber and
# Simulated Annealing. The Hill Climber and Simulated Annealing algorithm use
# different functions: moveObject, swapObject and randomPlacement. The different
# functions are randomly called in the these algorithms. All three algorithms
# will save an image of the highest score generated in the run.
# Note: 'tqdm' will keep track of the total runs and time the algorithm takes
# during the run.
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

    # Iterates over list with houses, checks if a better score is found, saves
    # (new) sumScore as bestScore, and updates list.
    for run in tqdm(range(runs_algorithm)):
        objects = generateMap(total_houses)
        sumScore = objects.getScore(objects)

        if sumScore > bestScore:
            bestScore = sumScore
            print('{}'.format(int(bestScore)))
            bestObjectList = objects

    plotMap(bestObjectList, 'randomMap.png')

#-------------------------------------------------------------------------------
# Algorithm Hill Climber: gets a generated map and plots a floor plan of this
# map for every run of the algorithm. For the amount of iterations in such run,
# different random methods will be chosen and run. The floor plan with the
# highest score of all the iterations will be plotted for every algorithm run.
def HillClimber(total_houses, runs_algorithm, amount_iterations):

    for run in tqdm(range(runs_algorithm)):
        objects = generateMap(total_houses)
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

            elif randomMethod == "swapObject":
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

        plotMap(objects, 'hillClimberMap' + repr(run) + '.png')

# Moves a randomly selected object by one step on the X or Y axis.
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

# Swaps the coordinates of two randomly selected objects.
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

    if not objects.mapBounds(randomHouse1):
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
        return False
    elif not objects.mapBounds(randomHouse2):
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
        return False
    elif objects.overlap(randomHouse1):
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
        return False
    elif objects.overlap(randomHouse2):
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
# run, different random methods will be chosen and run. The floor plan with the
# highest score of all the iterations will be plotted for every algorithm run.
# Seems the same as Hill Climber, but will escape local maxima early in the
# process, when a possible better solution is nearby.
def SimulatedAnnealing(total_houses, runs_algorithm, amount_iterations):

    # Sets temperature and coolingRate, required for Simulated Annealing.
    temperature = 1000000
    coolingRate = 0.03

    for run in tqdm(range(runs_algorithm)):
        currentList = generateMap(total_houses)
        bestList = currentList
        bestScore = currentList.getScore(currentList)

        for amount in range(amount_iterations):
            currentScore = currentList.getScore(currentList)
            print(currentScore)
            newList = deepcopy(currentList)
            moveType = ["swapObject", "moveObject", "randomPlacement"]
            randomMethod = random.choice(moveType)

            if randomMethod == "moveObject":
                if moveObject(newList) == True:
                    newScore = newList.getScore(newList)
                    if newScore > bestScore:
                        currentList = newList
                        bestList = newList
                        bestScore = newScore
                    elif acceptanceProbability(currentScore, newScore,\
                        temperature) > random.uniform(0, 1):
                        currentList = newList
                    else:
                        currentList = currentList

            elif randomMethod == "swapObject":
                if swapObject(newList) == True:
                    newScore = newList.getScore(newList)

                    if newScore > bestScore:
                        currentList = newList
                        bestList = newList
                        bestScore = newScore
                    elif acceptanceProbability(currentScore, newScore,\
                        temperature) > random.uniform(0, 1):
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
                    elif acceptanceProbability(currentScore, newScore,\
                        temperature) > random.uniform(0, 1):
                        currentList = newList
                    else:
                        currentList = currentList

            # Updates temperature.
            temperature *= 1 - coolingRate
        plotMap(bestList, 'simulatedAnnealingMap' + repr(run) + '.png')

# Calculates probability if score should be accepted or not. 1.0 means the new
# score is better, 0.0 means the new score is worse. math.exp is used to
# calculate the acceptance probability.
def acceptanceProbability(currentScore, newScore, temperature):
    if newScore > currentScore:
        return 1.0
    return math.exp((newScore - currentScore) / temperature)
