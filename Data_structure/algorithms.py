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
from houseclasses import *
from copy import deepcopy
from main import *

#-------------------------------------------------------------------------------

# global variable
bestScore = 0

#-------------------------------------------------------------------------------

# TODO
def algoritms(total_houses, runs_algorithm, amount_iterations):
    objects = ObjectList(total_houses)
    PlotMap(total_houses)
    bestScore = objects.getScore(objects)

    moveType = ["moveHouse", "swap", "randomPlacement"]
    randomMethod = random.choice(moveType)
    print("hillClimber_type: " + str(randomMethod))

    for i in range(amount_iterations):
        old_list = deepcopy(objects)

        if randomMethod == "moveHouse":
            if moveHouse(total_houses) == True:
                sumScore = objects.getScore(objects)
                if sumScore > bestScore:
                    bestScore = sumScore
                    print("Best: " + str(bestScore))
                else:
                    objects = old_list

        elif randomMethod == "swap":
            if swap(total_houses)  == True:
                sumScore = objects.getScore(objects)
                if sumScore > bestScore:
                    bestScore = sumScore
                    print("Best: " + str(bestScore))
                else:
                    objects = old_list

        elif randomMethod == "randomPlacement":
            if randomPlacement(total_houses) == True:
                sumScore = objects.getScore(objects)
                if sumScore > bestScore:
                    bestScore = sumScore
                    print("Best: " + str(bestScore))
                else:
                    objects = old_list

# Moves a randomly selected house by one step on the X or Y axis.
def moveHouse(total_houses):
    objects = ObjectList(total_houses)
    randomHouse = random.choice(objects.objectList)
    steps = [1, -1]
    randomStep = random.choice(steps)
    shafts = ["x", "y"]
    randomXY = random.choice(shafts)

    if randomXY == "x":
        randomHouse.x = randomHouse.x + randomStep
    elif randomXY == "y":
        randomHouse.y = randomHouse.y + randomStep

    if objects.MapBounds(randomHouse) and not objects.overlap(randomHouse):
        return True
    else:
        if randomXY == "x":
            randomHouse.x = randomHouse.x - randomStep
        elif randomXY == "y":
            randomHouse.y = randomHouse.y - randomStep
        return False

# Swaps the coördinates of two randomly selected houses.
def swap(total_houses):
    objects = ObjectList(total_houses)
    randomHouse1 = random.choice(objects.objectList)
    randomHouse2 = random.choice(objects.objectList)

    if randomHouse1 == randomHouse2:
        return False
    elif randomHouse1.base_sale_price != randomHouse2.base_sale_price:
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
    else:
        return False

    if not objects.MapBounds(randomHouse1) and objects.MapBounds(randomHouse2):
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
        return False
    elif objects.overlap(randomHouse1) and objects.overlap(randomHouse2):
        randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
        randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
        return False
    return True

# Places a randomly selected house on a new location.
def randomPlacement(total_houses):
    objects = ObjectList(total_houses)
    randomHouse = random.choice(objects.objectList)
    x,y = objects.getRandom_coordinates()
    oldx = deepcopy(randomHouse.x)
    oldy = deepcopy(randomHouse.y)
    randomHouse.x = x
    randomHouse.y = y

    if objects.MapBounds(randomHouse) and not objects.overlap(randomHouse):
        return True
    else:
        randomHouse.x = oldx
        randomHouse.y = oldy
        return False










#
#
# # Hillclimber algorithm which, if it betters the score, moves houses by one
# # step on the axis, by swapping or by relocating it randomly.
# def hillClimber():
#     global objects
#     PlotMap()
#     bestScore = objects.getScore(objects)
#
#     moveType = ["moveHouse", "swap", "randomPlacement"]
#     randomMethod = random.choice(moveType)
#     print("hillClimber_type: " + str(randomMethod))
#
#     for i in range(20000):
#         old_list = deepcopy(objects)
#
#         if randomMethod == "moveHouse":
#             if objects.moveHouse() == True:
#                 sumScore = objects.getScore(objects)
#                 if sumScore > bestScore:
#                     bestScore = sumScore
#                     print("Best: " + str(bestScore))
#                 else:
#                     objects = old_list
#
#         elif randomMethod == "swap":
#             if objects.swap()  == True:
#                 sumScore = objects.getScore(objects)
#                 if sumScore > bestScore:
#                     bestScore = sumScore
#                     print("Best: " + str(bestScore))
#                 else:
#                     objects = old_list
#
#         elif randomMethod == "randomPlacement":
#             if objects.randomPlacement() == True:
#                 sumScore = objects.getScore(objects)
#                 if sumScore > bestScore:
#                     bestScore = sumScore
#                     print("Best: " + str(bestScore))
#                 else:
#                     objects = old_list
#
# # Moves a randomly selected house by one step on the X or Y axis.
# def moveHouse(self):
#     randomHouse = random.choice(self.objectList)
#     steps = [1, -1]
#     randomStep = random.choice(steps)
#     shafts = ["x", "y"]
#     randomXY = random.choice(shafts)
#
#     if randomXY == "x":
#         randomHouse.x = randomHouse.x + randomStep
#     elif randomXY == "y":
#         randomHouse.y = randomHouse.y + randomStep
#
#     if self.MapBounds(randomHouse) and not self.overlap(randomHouse):
#         return True
#     else:
#         if randomXY == "x":
#             randomHouse.x = randomHouse.x - randomStep
#         elif randomXY == "y":
#             randomHouse.y = randomHouse.y - randomStep
#         return False
#
# # Swaps the coördinates of two randomly selected houses.
# def swap(self):
#     randomHouse1 = random.choice(self.objectList)
#     randomHouse2 = random.choice(self.objectList)
#
#     if randomHouse1 == randomHouse2:
#         return False
#     elif randomHouse1.base_sale_price != randomHouse2.base_sale_price:
#         randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
#         randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
#     else:
#         return False
#
#     if not self.MapBounds(randomHouse1) and self.MapBounds(randomHouse2):
#         randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
#         randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
#         return False
#     elif self.overlap(randomHouse1) and self.overlap(randomHouse2):
#         randomHouse1.x, randomHouse2.x = randomHouse2.x, randomHouse1.x
#         randomHouse1.y, randomHouse2.y = randomHouse2.y, randomHouse1.y
#         return False
#     return True
#
# # Places a randomly selected house on a new location.
# def randomPlacement(self):
#     randomHouse = random.choice(self.objectList)
#     x,y = self.getRandom_coordinates()
#     oldx = deepcopy(randomHouse.x)
#     oldy = deepcopy(randomHouse.y)
#     randomHouse.x = x
#     randomHouse.y = y
#
#     if self.MapBounds(randomHouse) and not self.overlap(randomHouse):
#         return True
#     else:
#         randomHouse.x = oldx
#         randomHouse.y = oldy
#         return False
#
# # Simulated annealing algorithm which also accepts moves which lower the score.
# def simulatedAnnealer():
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
