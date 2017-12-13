#-------------------------------------------------------------------------------
# File name: functions.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This program generates random coordinates, and plots the floor map with grid.
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from houseclasses import *

#-------------------------------------------------------------------------------

bestScore = 0

#-------------------------------------------------------------------------------

# Plots grid and graph.
def PlotMap():

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
    plt.title('Score: {:,.2f} euro'.format(sumScore), fontsize=12)
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

        housePlotDetached = patches.Rectangle(((house.x - house.detached), \
            (house.y - house.detached)), (house.width + house.detached * 2), \
            (house.height + house.detached * 2), facecolor=house.color, alpha = 0.4)
        ax.add_patch(housePlotDetached)

        housePlot = patches.Rectangle((house.x,house.y), house.width, house.height,\
            facecolor=house.color, edgecolor='black')
        ax.add_patch(housePlot)

    if sumScore > bestScore:
        bestScore = sumScore
        PlotMap()
    print("Score: {:,.2f} euro".format(bestScore))
    plt.close()

    plt.grid()
    plt.savefig('map.png', bbox_inches='tight')
    plt.cla()
    # plt.show()
