#-------------------------------------------------------------------------------
# File name: main.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This program creates a floor plan in which 20, 40 or 60 houses are placed.
# Uses other files names 'houseclasses.py' and 'functions.py' to generate the
# necessary data.
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from houseclasses import *
from functions import *

#-------------------------------------------------------------------------------

bestScore = 0
n = 3

#-------------------------------------------------------------------------------

# Asks which type of floor plan should be displayed.
total_houses = int(input("How many houses should be on the floor plan? (20, 40, 60)\n"))
if not total_houses in [20, 40, 60]:
    print("The amount of houses has to be 20, 40 or 60.")
    # exit()

def randAlgorithm():

    # Size of window.
    plt.figure(figsize=(7,7), dpi=100)

    # Represents subplot and length of axes.
    ax = plt.subplot(111, aspect='equal')
    ax.plot()
    ax.axis([0,180,0,160])

    # Calls HouseList with its values.
    houses = HouseList(total_houses)
    sumScore = houses.getScore(houses)

    # Sets titles of labels.
    plt.suptitle('Amstelhaege - De Planeauleaugen', fontsize=16)
    plt.title('Score: €{:,.2f}'.format(sumScore), fontsize=12)
    plt.xlabel('180 meter')
    plt.ylabel('160 meter')

    # Intervals of grid lines of x and y axes.
    major_ticksy = np.arange(0, 170, 10)
    major_ticksx = np.arange(0, 190, 10)
    ax.set_axisbelow(True)
    ax.set_yticks(major_ticksy)
    ax.set_xticks(major_ticksx)

    # Iterates over all houses in house list and creates every house in list.
    for house in houses.houseList:

        housePlot = patches.Rectangle((house.x,house.y), house.width, house.height,\
            facecolor=house.color, edgecolor='black')
        ax.add_patch(housePlot)

    global bestScore
    if sumScore > bestScore:
        bestScore = sumScore
    print("Score: €{:,.2f}".format(bestScore))

    # Calls function to plot map.
    PlotMap()

for i in range(n):
    randAlgorithm()
